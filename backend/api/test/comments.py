from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from api.test.questions import QuestionTestCase


class CommentTestCase(APITestCase):

    def test_create(self):
        id = QuestionTestCase().test_create()
        url = '/api/answers/'
        data = {'detail': 'test answer',
                'question': id}
        self.client.login(username='test-user', password='123456')
        res = self.client.post(url, data)
        self.client.logout()
        id = res.data['data']['id']
        url = '/api/comments/'
        data = {'detail': 'test-comment',
                'answer': id}
        res = self.client.post(url, data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(username='test-user', password='123456')
        res =  self.client.post(url, data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)





