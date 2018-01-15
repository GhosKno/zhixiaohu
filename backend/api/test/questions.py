from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, APIClient

from .topics import TopicTestCase
from . import createTestUser


class QuestionTestCase(APITestCase):
    client = APIClient()
    def test_retrieve(self):
        id = self.test_create()
        url = f'/api/questions/{id}/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)

        url = f'/api/questions/{id+5}/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], False)

    def test_create(self):
        url = '/api/topics/'
        data = {'label': 'test',
                'introduction': 'test introduction'}
        createTestUser()
        self.client.login(username='test-user', password='123456')
        res = self.client.post(url, data, format='json')
        id = res.data['data']['id']

        url = '/api/questions/'
        data = {'title': 'test title',
                'detail': 'test detail',
                'topics': [id]}

        self.client.logout()

        res = self.client.post(url, data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(username='test-user', password='123456')
        res = self.client.post(url, data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        res = self.client.post(url, data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        return id

    def test_get_answers(self):
        id = self.test_create()
        self.client.logout()
        url = f'/api/questions/{id}/get_answers/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)
        url = f'/api/questions/{id+5}/get_answers/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], False)

    def test_watch(self):
        id = self.test_create()
        url = f'/api/questions/{id}/watch/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)
        return id

    def test_cancel_watch(self):
        id = self.test_watch()
        url = f'/api/questions/{id}/cancel_watch/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)

