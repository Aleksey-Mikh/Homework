from django.urls import reverse

from rest_framework.test import APITestCase, APIClient
from rest_framework import status


class TestApi(APITestCase):

    def test_get_news_get_method(self):
        url = reverse('news:get_news')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_news_post_method(self):
        url = reverse('news:get_news')
        data = {
            "source": "https://people.onliner.by/feed",
            "pub_date": "",
            "limit": 1,
            "json": False,
            "to-pdf": False,
            "to-html": False
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data, {
                "message": "You see this message because you enter false in JSON value."
            }
        )

    def test_feeds_get_method(self):
        url = reverse('news:feeds')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_feeds_pk_get_method(self):
        url = reverse('news:feeds_pk', kwargs={"pk": 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_news_get_method(self):
        url = reverse('news:news')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_news_pk_get_method(self):
        url = reverse('news:news_pk', kwargs={"pk": 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
