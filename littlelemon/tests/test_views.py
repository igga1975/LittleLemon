from django.test import TestCase
from restaurant.views import *

class MenuViewTest(TestCase):
    def setup(self):
        menu_item1 = Menu.objects.create(Title = 'Cherry bomb', Price = 100.00)
        menu_item2 = Menu.objects.create(Title = 'Tiramisu', Price = 50)

    def test_getall(self):
        self.setup()
        item1 = Menu.objects.get(Title = "Cherry bomb")
        self.assertEqual(str(item1), 'Cherry bomb:100.00')
