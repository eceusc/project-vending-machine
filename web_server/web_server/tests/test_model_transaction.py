from django.test import TestCase
from web_server.models import transaction
#import datetime
from django.utils import timezone

class TransactionTest(TestCase):

    def create_transaction(self, user_id=12345678, user=1):
        return transaction.objects.create(user_id=user_id, user=user)

    def test_transaction_creation(self):
        o1 = self.create_transaction()
        o2 = self.create_transaction(user_id=10000000, user=2)

        self.assertEqual(12345678, o1.user_id)
        self.assertEqual(10000000, o2.user_id)

        self.assertEqual(1, o1.user)
        self.assertEqual(2, o2.user)
