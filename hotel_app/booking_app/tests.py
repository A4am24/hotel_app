from django.test import TestCase
from .models import  Hotel


# Create your tests here.
class HotelTestcase(TestCase):
    def setUp(self):
        self.hotel=Hotel('')