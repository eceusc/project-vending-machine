from django.test import TestCase
from web_server.models import User

class UserTest(TestCase):

    def create_user(self, github_username='Al Gore'):
        return User.objects.create(github_username=github_username)

    def test_user_creation(self):
        o1 = self.create_user()
        o2 = self.create_user(github_username='London Tipton')

        self.assertEqual('Al Gore', o1.github_username)
        self.assertEqual('London Tipton', o2.github_username)
