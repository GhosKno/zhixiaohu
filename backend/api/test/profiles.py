from rest_framework import status
from rest_framework.test import APITestCase

from api.models import User
from . import createTestUser


class ProfileTestCase(APITestCase):
    def test_retrieve(self):
        user = createTestUser()
        profile = user.profile
        url = f'/api/profiles/{profile.id}/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)

        url = f'/api/profiles/{profile.id+1}/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], False)

    def test_update_info(self):
        createTestUser()
        url = f'/api/profiles/update_info/'
        data = {'nickname': 'test-nick'}
        res = self.client.post(url, data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(username='test-user', password='123456')
        res = self.client.post(url, data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)

        user = User.objects.get(username='test-user')
        self.assertEqual(user.profile.nickname, 'test-nick')

    def test_favorites(self):
        id = createTestUser().id
        url = f'/api/profiles/{id}/favorites/'
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)

    def test_questions(self):
        id = createTestUser().id
        url = f'/api/profiles/{id}/questions/'
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)

    def test_answers(self):
        id = createTestUser().id
        url = f'/api/profiles/{id}/answers/'
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)

    def test_history(self):
        id = createTestUser().id
        url = f'/api/profiles/{id}/history/'
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)

    def test_activities(self):
        id = createTestUser().id
        url = f'/api/profiles/{id}/activities/'
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)

    def test_watched_questions(self):
        id = createTestUser().id
        url = f'/api/profiles/{id}/watched_questions/'
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)

    def test_watched_users(self):
        id = createTestUser().id
        url = f'/api/profiles/{id}/watched_users/'
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)

    def test_be_watched(self):
        id = createTestUser().id
        url = f'/api/profiles/{id}/be_watched/'
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['success'], True)
