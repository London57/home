from django.test import TestCase
from forms import LoginForm
from models import AbstractUser



class RedirectAfterLoginTest(TestCase):
    def setUp(self):
        AbstractUser.objects.create(username='user', last_name='test')
        