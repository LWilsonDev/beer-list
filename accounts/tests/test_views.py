from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class TestViews(TestCase):
    
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
    
    def test_get_login_page_if_not_logged_in(self):
        self.client.logout()
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'accounts/login.html')
        
    def test_redirect_if_accessing_login_page_when_logged_in(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 302)
        self.assertRedirects(page, '/')    
        
    def test_get_logout_page(self):
        page = self.client.get("/accounts/logout/")
        self.assertEqual(page.status_code, 302)
        self.assertRedirects(page, '/') 
        
    def test_get_sign_up_page(self):
        self.client.logout()
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'accounts/registration.html')
        
    def test_get_user_list_page(self):
        page = self.client.get("/accounts/users/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'accounts/user/list.html')
        
    
    