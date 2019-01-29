from django.test import TestCase
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserEditForm, UserRegistrationForm, ProfileEditForm


class TestUserLoginForm(TestCase):
    
    def test_can_login(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        form = UserLoginForm({'username': 'testuser', 'password':'12345'})
        self.assertTrue(form.is_valid()) 
