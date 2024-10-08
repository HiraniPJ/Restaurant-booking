from django.test import TestCase # type: ignore
from .models import Table, Reservation
from django.urls import reverse, resolve # type: ignore
from django.contrib.auth.models import User # type: ignore
from datetime import date, time
from .forms import ReservationForm



# Base Test Case
class BaseTestCase(TestCase):
    def setUp(self):
        # Clear previous data
        User.objects.all().delete()
        Table.objects.all().delete()
        Reservation.objects.all().delete()

        # Create a test user and log in
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'password')
        self.client.login(username='testuser', password='password')

        # Create a test table
        self.table = Table.objects.create(number=1, capacity=4)

        # Create a test reservation
        self.reservation = Reservation.objects.create(
            user=self.user, 
            table=self.table, 
            date="2024-10-10", 
            time="18:00", 
            guests=2
        )
   
# Model Tests
class ModelTests(BaseTestCase):
    
    def test_reservation_creation(self):
        # Test reservation model creation
        self.assertEqual(str(self.reservation), f"Reservation for {self.user} on 2024-10-10 at 18:00")

    def test_table_creation(self):
        # Test table model creation
        table = Table.objects.create(number=2, capacity=6)
        self.assertEqual(str(table), "Table 2 (Seats 6)")

# View Tests
class ViewTests(BaseTestCase):

    def test_home_page(self):
        # Test the home page loads correctly
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mint Restaurant")

    def test_make_reservation(self):
        # Test making a reservation
        response = self.client.post(reverse('make_reservation'), {
            'table': self.table.id, 'date': '2024-10-12', 'time': '19:00', 'guests': 4
        })
        self.assertEqual(response.status_code, 302)
        
        # Verify reservation was created
        new_reservation = Reservation.objects.last()
        self.assertEqual(new_reservation.table, self.table)
        self.assertEqual(new_reservation.date, date(2024, 10, 12))
        self.assertEqual(new_reservation.time, time(19, 0))
        self.assertEqual(new_reservation.guests, 4)    

    def test_make_reservation_invalid(self):
        # Test form submission with missing fields (invalid form)
        response = self.client.post(reverse('make_reservation'), {
            'date': '2024-10-12', 'time': '19:00', 'guests': 4      # Missing 'table'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")  
            
    def test_my_reservations(self):
        # Test viewing a user's reservations
        response = self.client.get(reverse('my_reservations'))
        self.assertEqual(response.status_code, 200)

        #Print only the reservation part
        reservations = response.context['reservations']
       # for reservation in reservations:
        #    print({
        #        'Table': reservation.table.number,
        #        'Date': reservation.date,
        #        'Time': reservation.time,
        #        'Guests': reservation.guests
        #    })

        self.assertEqual(len(reservations), 1)
        reservation = reservations[0]
        self.assertEqual(reservation.table.number, 1)
        self.assertEqual(reservation.date, date(2024, 10, 10))
        self.assertEqual(reservation.time, time(18, 0))
        self.assertEqual(reservation.guests, 2)

        # Specific reservation details
        self.assertContains(response, "Table 1")
        self.assertContains(response, "2024-10-10")
        self.assertContains(response, "18:00")
        self.assertContains(response, "Guests")
        self.assertContains(response, "2")
        
    def test_edit_reservation(self):
        # Test Editing and existing reservation
        response = self.client.post(reverse('edit_reservation', args=[self.reservation.id]), {
            'table': self.table.id,
            'date': '2024-10-15',
            'time': '20:00',
            'guests': 2
        })
        self.assertEqual(response.status_code, 302)
        self.reservation.refresh_from_db()
        self.assertEqual(self.reservation.date, date(2024, 10, 15))
        self.assertEqual(self.reservation.time, time(20, 0))

    def test_edit_reservation_get(self):
        # Test GET request for edit reservation page
        response = self.client.get(reverse('edit_reservation', args=[self.reservation.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/edit_reservation.html')
        self.assertContains(response, "value=\"2024-10-10\"")  # Date of reservation in form

    def test_edit_reservation_invalid(self):
        # Test form submission with invalid guests (invalid form)
        response = self.client.post(reverse('edit_reservation', args=[self.reservation.id]), {
            'table': self.table.id,
            'date': '2024-10-15',
            'time': '20:00',
            'guests': ''    # Missing Guests
        })    
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")  

    def test_delete_reservation(self):
        # Test deleting a reservation
        response = self.client.post(reverse('delete_reservation', args=[self.reservation.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.count(), 0)

# Signup View Tests
class SignupViewTests(BaseTestCase):
    
    def test_signup_view_get(self):
        #Test rendering the signup form (GET request)
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/signup.html')

    def test_signup_view_post(self):
        #username is unique
        unique_username = 'testuser' + str(User.objects.count())

        #Test rendering the signup form (POST request)
        response = self.client.post(reverse('signup'), {
            'username': unique_username, 
            'password1': 'Testpassword123', 
            'password2': 'Testpassword123'
        })
        self.assertEqual(response.status_code, 302)

        # Check user is created
        new_user = User.objects.get(username=unique_username)
        self.assertIsNotNone(new_user)

        # Check if user is logged in
        response = self.client.get(reverse('home'))
        self.assertContains(response, f"Welcome, {unique_username}")

    def test_signup_view_post_invalid(self):
        #Test form with non-matching passwords (invalid form)
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password1': 'Testpassword123', 
            'password2': 'Testpassword456'  # Non-matching passwords
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The two password fields didn’t match.")   
        
# Form Tests
class FormTests(BaseTestCase):

    def test_reservation_form_valid(self):
        #Test if valid form is accepted
        form_data = {
            'table': self.table.id,
            'date': '2024-10-10',
            'time': '18:00',
            'guests': 2
        }
        form = ReservationForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_reservation_form_invalid(self):
        #Test if invalid form is rejected
        form_data = {
            'table': '',
            'date': '',
            'time': '18:00',
            'guests': 2
        }
        form = ReservationForm(data=form_data)
        self.assertFalse(form.is_valid())
    
    def test_reservation_form_invalid_guests(self):
        #Test if form rejects invalid number of guests
        form_data = {
            'table': self.table.id,
            'date': '2024-10-10',
            'time': '18:00',
            'guests': 0
        }
        form = ReservationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('guests', form.errors)
    
# URL Tests
class URLTests(BaseTestCase):

    def test_home_url_resolves(self):
        #Test home page URL resolves
        url = reverse('home')
        self.assertEqual(resolve(url).func.__name__, 'home')
    
    def test_make_reservation_url_resolves(self):
        #Test reservation URL resolves
        url = reverse('make_reservation')
        self.assertEqual(resolve(url).func.__name__, 'make_reservation')

    def test_my_reservation_url_resolves(self):
        #Test my reservation URL resolves
        url = reverse('my_reservations')
        self.assertEqual(resolve(url).func.__name__, 'my_reservations')

    def test_edit_reservation_url_resolves(self):
        #Test edit reservation URL resolves
        url = reverse('edit_reservation', args=[1])
        self.assertEqual(resolve(url).func.__name__, 'edit_reservation')

    def test_delete_reservation_url_resolves(self):
        #Test delete reservation URL resolves
        url = reverse('delete_reservation', args=[1])
        self.assertEqual(resolve(url).func.__name__, 'delete_reservation')