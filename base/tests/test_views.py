from django.test import TestCase
from base.models import Comic, Character, Creator, Story
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class ComicTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""

    def test_create_comic(self):
        """
        Ensure we can create a new comic object.
        """
        url = ('api/comics')
        data = {'title': 'Deadpool'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comic.objects.count(), 1)
        self.assertEqual(Comic.objects.get().title, 'Deadpool')
