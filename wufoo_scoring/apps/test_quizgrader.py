import datetime
import Pyfoo *

from django.test import TestCase
from wufoo_responder.models import Entry, Item

class EntryTestCase(TestCase):
    def setUp(self):
    


# todo: testCase for scoring methods

# todo: testCase for sending emails        
        
        
"""

class BlogPostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(id=1, 
            title='Starting a Django 1.6 Project the Right Way', 
            date=datetime.datetime.now(),
            category='Django')
        Post.objects.create(id=2, 
            title='Python\'s Hardest Problem', 
            date=datetime.datetime.now(),
            category='Python')

    def test_posts_have_category(self):
        """Animals that can speak are correctly identified"""
        first_post = Post.objects.get(id=1)
        second_post = Post.objects.get(id=2)
        self.assertEqual(first_post.category, 'Django')
        self.assertEqual(second_post.category, 'Python')
"""