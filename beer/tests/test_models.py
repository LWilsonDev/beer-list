from django.test import TestCase
from beer.models import Beer, Review
from django.contrib.auth.models import User

class TestBeerModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        
    def test_beer_as_capitalized_string(self)  :
        beer = Beer(
            name= 'test-beer',
            brewery= 'test-brewery',
            country_of_origin= 'test-country',
            strength='3.0',
            added_by=self.user
        )
        beer.save()
        self.assertEqual('Test-Beer', str(beer))
        
    def test_get_absolute_url(self):
        beer = Beer(
            name= 'test-beer',
            brewery= 'test-brewery',
            country_of_origin= 'test-country',
            strength='3.0',
            added_by=self.user
        )
        beer.save()
        self.assertEqual(beer.get_absolute_url(), '/beer/{}'.format(beer.id))
        
    def test_review_average_rating_with_one_review(self):
        beer = Beer(
            name= 'test-beer',
            brewery= 'test-brewery',
            country_of_origin= 'test-country',
            strength='3.0',
            added_by=self.user
        )
        beer.save()
        review = Review(
            author = self.user,
            beer = beer,
            rating = '3'
            )
        review.save()
        self.assertEqual(beer.average_rating(), 3.0)
        
    def test_review_average_rating_with_multiple_reviews(self):
        beer = Beer(
            name= 'test-beer',
            brewery= 'test-brewery',
            country_of_origin= 'test-country',
            strength='3.0',
            added_by=self.user
        )
        beer.save()
        review = Review(
            author = self.user,
            beer = beer,
            rating = '5'
            )
        review.save()
        review2 = Review(
            author = self.user,
            beer = beer,
            rating = '2'
            )
        review2.save()
        self.assertEqual(beer.average_rating(), 3.5)
    
    def test_beer_rating_no_reviews(self):
        beer = Beer(
            name= 'test-beer',
            brewery= 'test-brewery',
            country_of_origin= 'test-country',
            strength='3.0',
            added_by=self.user
        )
        beer.save()
        self.assertEqual(beer.average_rating(), 'No ratings yet')  
        
    def test_beer_likes_count(self):
        beer = Beer(
            name= 'test-beer',
            brewery= 'test-brewery',
            country_of_origin= 'test-country',
            strength='3.0',
            added_by=self.user,
        )
        beer.save()
        
        beer.likes.add(self.user)
        self.assertEqual(beer.total_likes(), 1)     
            
        


        
        
    