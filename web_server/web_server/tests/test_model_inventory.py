from django.test import TestCase
from web_server.models import Inventory

class InventoryTest(TestCase):

	def create_inventory(candy, id=123, machine=456, item=789):
		return Inventory.objects.create(id=id,machine=machine,item=item)

	def test_inventory_creation(candy):
		c1 = candy.create_inventory()
		c2 = candy.create_inventory(id=321)

		candy.assertEqual(123,c1.id)
		candy.assertEqual(321,c2.id)
		
		candy.assertEqual(456,c1.machine)
		candy.assertEqual(456,c2.machine)
