from django.test import TestCase
from .models import Table, Reservation
from django.contrib.auth.models import User
from django.urls import reverse


# Create your tests here.

class ModelTests(TestCase):
    
    def setUp(self):
        # Create a test user and table
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'password')
        self.table = Table.objects.create(number=1, capacity=4)

    def test_reservation_creation(self):
        # Test reservation model creation
        reservation = Reservation.objects.create(user=self.user, table=self.table, date="2024-10-10", time="18:00", guests=2)
        self.assertEqual(str(reservation), f"Reservation for {self.user} on 2024-10-10 at 18:00")

    def test_table_creation(self):
        # Test table model creation
        table = Table.objects.create(number=2, capacity=6)
        self.assertEqual(str(table), "Table 2 (Seats 6)")
     
    def test_home_page(self):
        url = reverse('home') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mint Restaurant")