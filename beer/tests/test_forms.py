from django.test import TestCase
from beer.forms import BeerCreateForm, ReviewCreateForm

# create valid beer to use for testing
testbeer = {
            'name': 'test-beer',
            'brewery': 'test-brewery',
            'country_of_origin': 'test-country',
            'strength':'3.0'
        }

class TestBeerCreateForm(TestCase):
    
    def test_can_create_beer(self):
        form = BeerCreateForm(testbeer)
        self.assertTrue(form.is_valid()) 
    
    def test_cannot_create_beer_with_just_name(self):
        form = BeerCreateForm({'name':'Test'})
        self.assertFalse(form.is_valid())
        
    def test_correct_message_for_missing_name(self):
        form = BeerCreateForm({'name':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])
                