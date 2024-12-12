from django.test import TestCase

# Create your tests here.
from .models import Posts

class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Posts.objects.count()

        self.assertEqual(posts, 0)