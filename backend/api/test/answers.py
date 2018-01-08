from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from api.test.questions import QuestionTestCase
from . import createTestUser


class AnswerTestCase(APITestCase):
    def test_retrieve(self):
        pass

    def test_create(self):
        id = QuestionTestCase().test_create()
        url = '/api/answers/'
        data = {'detail': 'test answer',
                'question': id}
        res = self.client.post(url, data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.client.login(username='test-user', password='123456')
        res = self.client.post(url, data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['success'], True)
        return id

    def test_get_comments(self):
        id = self.test_create()
        url = f'/api/answers/{id}/get_comments/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)
        return id

    def test_agree(self):
        id = self.test_create()
        url = f'/api/answers/{id}/agree/'

        self.client.logout()
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(username='test-user', password='123456')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)
        return id

    def test_cancel_agree(self):
        id = self.test_agree()
        url = f'/api/answers/{id}/cancel_agree/'

        self.client.logout()
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(username='test-user', password='123456')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)
        return id

    def test_disagree(self):
        id = self.test_create()
        url = f'/api/answers/{id}/disagree/'

        self.client.logout()
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(username='test-user', password='123456')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)
        return id

    def test_cancel_disagree(self):
        id = self.test_agree()
        url = f'/api/answers/{id}/cancel_disagree/'

        self.client.logout()
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(username='test-user', password='123456')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)
        return id

    def test_favorite(self):
        id = self.test_create()
        url = f'/api/answers/{id}/favorite/'

        self.client.logout()
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(username='test-user', password='123456')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)
        return id

    def test_cancel_favorite(self):
        id = self.test_favorite()
        url = f'/api/answers/{id}/cancel_favorite/'

        self.client.logout()
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(username='test-user', password='123456')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)



