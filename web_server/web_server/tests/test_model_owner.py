from django.test import TestCase
from web_server.models import Owner

class OwnerTest(TestCase):

    def create_owner(self, name='Al Gore'):
        return Owner.objects.create(name=name)

    def test_owner_creation(self):
        o1 = self.create_owner()
        o2 = self.create_owner(name='London Tipton')

        self.assertEqual('Al Gore', o1.name)
        self.assertEqual('London Tipton', o2.name)
