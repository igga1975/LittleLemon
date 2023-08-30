from django.test import TestCase
from restaurant.views import *

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(Title = 'Cherry bomb', Price = 100.00)
        Menu.objects.create(Title = 'Tiramisu', Price = 50)

    def test_all(self):
        self.setup()
        item1 = Menu.objects.get(Title = "Cherry bomb")
        item2 = Menu.objects.get(Title = 'Tiramisu')
        self.assertEqual(str(item1), 'Cherry bomb:100.00')
        self.assertEqual(str(item2), 'Tiramisu:50.00')
