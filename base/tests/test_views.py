from django.test import TestCase
from base.models import Comic, Character, Creator, Story
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


# class ComicTests(APITestCase):
#     def test_create_comic(self):
#         """
#         Ensure we can create a new comic object.
#         """
#         url = reverse('comic-list')
#         data = {'title': 'Deadpool'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Comic.objects.count(), 1)
#         self.assertEqual(Comic.objects.get().title, 'Deadpool')


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

    # def test_api_can_create_a_comic(self):
    #     Comic.objects.create(
    #         title='Deadpool',
    #         issue="1 edition",
    #         image='https://m.media-amazon.com/images/I/51vCE8RCEoL.jpg',
    #         price='22.83',
    #         pages=76
    #     )
    #     self.client = APIClient()
    #     comic_data = {'title': 'Deadpool'}
    #     response = self.client.post(
    #         comic_data,
    #         format="json"
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Comic.objects.count(), 1)
    #     self.assertEqual(Comic.objects.get().title, 'Deadpool')

    # def test_api_can_get_a_comic(self):
    #     """Test the api can get a comic."""
    #     comic = Comic.objects.get(id=1)
    #     response = self.client.get(
    #         '/comic/',
    #         kwargs={'pk': comic.id}, format="json")

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertContains(response, comic)

    # def test_api_can_update_comic(self):
    #     """Test the api can update a given comic."""
    #     comic = Comic.objects.get()
    #     change_comic = {'title': 'Superman'}
    #     res = self.client.put(
    #         reverse('details', kwargs={'pk': comic.id}),
    #         change_comic, format='json'
    #     )
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)

    # def test_api_can_delete_comic(self):
    #     """Test the api can delete a comic."""
    #     Comic = Comic.objects.get()
    #     response = self.client.delete(
    #         reverse('details', kwargs={'pk': comic.id}),
    #         format='json',
    #         follow=True)
    #     self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
