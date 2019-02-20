from django.test import TestCase
from web_server.models.Contributions import Contributions
from web_server.models.Contributions import ContributorType

class ContributionTest(TestCase):

    def create_contribution(self, identification=0, contributionType=ContributorType.AD, 
        contributor="5422f2d2-624c-473e-912a-65e44c468218", approval = 1):
        return Contributions.objects.create(identification=identification, contributionType=contributionType,
            contributor=contributor, approval=approval)

    def test_contribution_creation(self):
        o1 = self.create_contribution()
        
        o2 = self.create_contribution(identification=3, contributionType=ContributorType.ME,
            contributor="e5055ca7-45a6-4156-b300-2ae00af3c055", approval=0)

        self.assertEqual(o1.identification,0)
        self.assertEqual(o1.contributionType, ContributorType.AD)
        self.assertEqual(o1.contributor, "5422f2d2-624c-473e-912a-65e44c468218")
        self.assertEqual(o1.approval, 1)

        self.assertEqual(o2.identification,3)
        self.assertEqual(o2.contributionType, ContributorType.ME)
        self.assertEqual(o2.contributor, "e5055ca7-45a6-4156-b300-2ae00af3c055")
        self.assertEqual(o2.approval, 0)
