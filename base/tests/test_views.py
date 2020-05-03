from django.test import TestCase
from base.models import Comic, Character, Creator, Story
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class ComicTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        pass

    def test_create_comic(self):
        """
        Ensure we can create a new comic object.
        """
        data = {'title': 'Deadpool', 'issue': '14'}
        response = self.client.post('/api/comic/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comic.objects.count(), 1)
        self.assertEqual(Comic.objects.get().title, 'Deadpool')

    def test_get_comic_list(self):
        Comic.objects.create(title="Test Comic", issue=10)
        response = self.client.get('/api/comic/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class CharacterTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        pass

    def test_create_character(self):
        """
        Ensure we can create a new character object.
        """
        data = {'name': 'Deadpool', 'description': 'hello'}
        response = self.client.post('/api/character/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Character.objects.count(), 1)
        self.assertEqual(Character.objects.get().name, 'Deadpool')

    def test_get_character_list(self):
        Character.objects.create(name="Test Character", description="test")
        response = self.client.get('/api/character/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class CreatorTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        pass

    def test_create_creator(self):
        """
        Ensure we can create a new creator object.
        """
        data = {'name': 'chucknorris', 'description': 'this is my test'}
        response = self.client.post('/api/creator/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Creator.objects.count(), 1)
        self.assertEqual(Creator.objects.get().name, 'chucknorris')

    def test_get_creator_list(self):
        Creator.objects.create(name="Test Creator", description="test test")
        response = self.client.get('/api/creator/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
