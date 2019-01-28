from django.test import TestCase
from beer.models import Beer, Review
from django.contrib.auth.models import User



class TestViews(TestCase):
    
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
    
    def test_get_index_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')
        
    def test_get_user_profile_page(self):
        page = self.client.get("/users/testuser/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'accounts/user/detail.html')    
        
    def test_get_edit_beer_page(self):
        
        beer = Beer(
            name= 'test-beer',
            brewery= 'test-brewery',
            country_of_origin= 'test-country',
            strength='3.0',
            added_by=self.user
        )
        beer.save()
        page = self.client.get("/edit_beer/{}".format(beer.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'beer/beer_form.html')
            
        
        