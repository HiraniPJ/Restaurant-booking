from django.test import TestCase
from .models import Table, Reservation
from django.urls import reverse
from django.contrib.auth.models import User
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
        self.assertEqual(str(self.table), "Table 1 (Seats 4)")

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
        self.assertContains(response, "Reservation for testuser")

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
        self.assertEqual(self.reservation.date, "2024-10-15")
        self.assertEqual(self.reservation.time, "20:00")

    def test_delete_reservation(self):
        # Test deleting a reservation
        response = self.client.post(reverse('delete_reservation', args=[self.reservation.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.count(), 0)
        
