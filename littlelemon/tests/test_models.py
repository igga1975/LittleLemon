from django.test import TestCase
from restaurant.models import *

class MenuTest(TestCase):

    def test_instance(self):
        item = Menu.objects.create(Title = 'IceCream', Price = 80.000)
        self.assertEqual(str(item), 'IceCream:80.0')
