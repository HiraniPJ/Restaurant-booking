from django.test import TestCase
from .models import Table, Reservation
from django.urls import reverse
from django.urls import resolve
from django.contrib.auth.models import User
from datetime import date, time
from .forms import ReservationForm



#Base Test Case
class BaseTestCase(TestCase):
    def setUp(self):
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
   
#Model Tests
class ModelTests(BaseTestCase):
    
    def test_reservation_creation(self):
        # Test reservation model creation
        self.assertEqual(str(self.reservation), f"Reservation for {self.user} on 2024-10-10 at 18:00")

    def test_table_creation(self):
        # Test table model creation
        table = Table.objects.create(number=2, capacity=6)
        self.assertEqual(str(table), "Table 2 (Seats 6)")

#View Tests
class ViewTests(BaseTestCase):

    def test_home_page(self):
        # Test the home page loads correctly
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mint Restaurant")

    def test_make_reservation(self):
        # Test making a reservation
        response = self.client.post(reverse('make_reservation'), {
            'table': self.table.id,
            'date': '2024-10-12',
            'time': '19:00',
            'guests': 4
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.count(), 2)

    def test_my_reservations(self):
        # Test viewing a user's reservations
        response = self.client.get(reverse('my_reservations'))
        
        self.assertEqual(response.status_code, 200)

        #Print only the reservation part
        reservations = response.context['reservations']
        for reservation in reservations:
            print({
                'Table': reservation.table.number,
                'Date': reservation.date,
                'Time': reservation.time,
                'Guests': reservation.guests
            })

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

    def test_delete_reservation(self):
        # Test deleting a reservation
        response = self.client.post(reverse('delete_reservation', args=[self.reservation.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.count(), 0)
        
#Form Tests
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

#URL Tests
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