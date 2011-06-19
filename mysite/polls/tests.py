"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test import Client
from polls.models import Poll, Choice


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class PollsDBTest(TestCase):
    fixtures = ["test_data.json"]

    def test_get_poll(self):
        self.assertEqual(Poll.objects.get(pk=1).question,
                "Best football team?")

    def test_count_choices(self):
        self.assertEqual(Choice.objects.all().count(), 3)

class PollsViewsTest(TestCase):
    fixtures = ["test_data.json"]

    def test_vote(self):
        c = Client()
        response = c.post("/polls/1/vote/", {'choice': '1'})
        self.assertEqual(response.status.code, 302)
        self.assertEqual(Choice.objects.get(pk=1).votes, 3)
