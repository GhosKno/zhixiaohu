from api.models import User


def createTestUser():
    user = User.objects.create(username='test-user',
                               password='123456',
                               email='example@test.com')
    user.save()
    return user