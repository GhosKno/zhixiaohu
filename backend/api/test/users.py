from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, \
    APIRequestFactory, force_authenticate

from api.models import User
from api.serializers import ProfileSerializer


class UserTestCase(APITestCase):
    def test_register(self):
        url = reverse('user-register')
        data = {'username': 'test-user',
                'password': '123456',
                'email': 'example@test.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get().username, 'test-user')

    def test_login(self):
        url = reverse('user-login')
        data = {'username': 'test-user',
                'password': '123456'}
        user = createTestUser()
        response = self.client.post(url, data, format='json')
        profile = user.profile
        profile.is_watch = False
        request = APIRequestFactory().get(url)
        seri = ProfileSerializer(profile, context={'request':request})
        self.assertEqual(response.data['data'], seri.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        url = reverse('user-logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        user = User.objects.create(username='test-user', password='123456', email='example@test.com')
        data = {'username': 'test-user',
                'password': '123456'}
        self.client.post(reverse('user-login'), data=data, format='json')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_message(self):
        url = reverse('user-messages')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        createTestUser()
        data = {'username': 'test-user',
                'password': '123456'}
        self.client.post(reverse('user-login'), data, format='json')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reset_pwd(self):
        url = reverse('user-reset-password')
        data = {'old': '123456',
                'new': '654321'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        createTestUser()
        self.client.post(reverse('user-login'),
                         data={'username': 'test-user',
                            'password': '123456'},
                         format='json')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(username='test-user')
        res = user.check_password('654321')
        self.assertEqual(res, True)

    def test_watch(self):
        user = createTestUser()
        id = user.id
        response = self.client.get(f'/api/users/{id}/watch/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        data = {'username': 'test-user',
                'password': '123456'}
        self.client.post(reverse('user-login'), data, format='json')
        response = self.client.get(f'/api/users/{id}/watch/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user = User.objects.get(username='test-user')
        count = user.watchedBy.count()
        self.assertEqual(1, count)

    def test_cancel_watch(self):
        user = createTestUser()
        id = user.id
        data = {'username': 'test-user',
                'password': '123456'}
        response = self.client.post(reverse('user-login'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(f'/api/users/{id}/watch/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(f'/api/users/{id}/cancel_watch/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(username='test-user')
        count = user.watchedBy.count()
        self.assertEqual(0, count)


def createTestUser():
    user = User.objects.create(username='test-user',
                               password='123456',
                               email='example@test.com')
    user.save()
    return user