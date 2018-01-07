from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, APIClient

from .topics import TopicTestCase
from . import createTestUser


class QuestionTestCase(APITestCase):

    def test_retrieve(self):
        self.test_create()
        url = '/api/questions/1/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)

        url = '/api/questions/2/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], False)

    def test_create(self):
        TopicTestCase().test_create()
        url = '/api/questions/'
        data = {'title': 'test title',
                'detail': 'test detail',
                'topics': [1]}
        res = self.client.post(url, data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(username='test-user', password='123456')
        res = self.client.post(url, data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        res = self.client.post(url, data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_answers(self):
        self.test_create()
        url = '/api/questions/1/get_answers/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)
        url = '/api/questions/2/get_answers/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], False)


    def test_watch(self):
        pass

    def test_cancel_watch(self):
        pass
