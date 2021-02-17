from django.test import TestCase
from django.urls import reverse
from .models import Project


class TestProjects(TestCase):
    """
    Here's the test for django project kickstart project website.
    """
    def setUp(self):
        """
        Set up dummy objects for tests
        """
        # Project.objects.create(
        #     name="Cat Feeder",
        #     category='Pet',
        #     currency='USD',
        #     state='sleeping',
        #     country='cats land',
        #     goal='99999',
        #     )
    def test(self):
        assert True
    # def test_project_name(self):
    #     """
    #     """
    #     one = Project.objects.get(name="Cat Feeder")
    #     self.assertEqual(one.title, "Cat Feeder")
