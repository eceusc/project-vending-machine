from django.test import TestCase
from web_server.models import transaction
import datetime

class TransactionTest(TestCase):

    def create_transaction(self, user_id=12345678, user=1, timestamp=datetime.date.today):
        return transaction.objects.create(user_id=user_id, user=user, timestamp=timestamp)

    def test_transaction_creation(self):
        o1 = self.create_transaction()
        o2 = self.create_transaction(user_id=10000000, user=2, timestamp=datetime.date.today)

        self.assertEqual(12345678, o1.user_id)
        self.assertEqual(10000000, o2.user_id)

        self.assertEqual(1, o1.user)
        self.assertEqual(2, o2.user)

        self.assertEqual(datetime.date.today, o1.timestamp)
        self.assertEqual(datetime.date.today, o2.timestamp)
