from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from api.test.questions import QuestionTestCase
from . import createTestUser


class AnswerTestCase(APITestCase):
    def test_retrieve(self):
        pass

 # TODO resolve db lock error in thread
    def test_create(self):
        url = '/api/answers/'
        data = {'detail': 'test answer',
                'question': 1}
        res = self.client.post(url, data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        QuestionTestCase().test_create()
        self.client.login(username='test-user', password='123456')
        res = self.client.post(url, data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['success'], True)

    def test_get_comments(self):
        self.test_create()
        url = '/api/answers/1/get_comments/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)

    def test_agree(self):
        pass

    def test_cancel_agree(self):
        pass

    def test_disagree(self):
        pass

    def test_cancel_disagree(self):
        pass

    def test_favorite(self):
        pass

    def test_cancel_favorite(self):
        pass



