from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, APIClient

from api.models import User


class TopicTestCase(APITestCase):
    client = APIClient()
    def test_list(self):
        url = '/api/topics/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)

# TODO fix test error
    def test_create(self):
        url = '/api/topics/'
        data = {'label':'test',
                'introduction': 'test introduction'}
        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        createTestUser()
        self.client.login(username='test-user', password='123456')
        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['success'], True)
        #print(res.data)

        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_questions(self):
        self.test_create()
        url = '/api/topics/2/get_questions/'
        res = self.client.get(url)
        #print(res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        url = '/api/topics/1/get_questions/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_hot(self):
        url = '/api/topics/hot/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


def createTestUser():
    user = User.objects.create(username='test-user',
                               password='123456',
                               email='example@test.com')
    user.save()
    return user