from django.test import TestCase
from datetime import datetime, timedelta
from django.utils.timezone import now

# Create your tests here.
from .models import Posts

class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Posts.objects.count()
        self.assertEqual(posts, 0)

    def test_post_str(self):
        post = Posts.objects.create(title="Test Title", body="Test Body")
        self.assertEqual(str(post), "Test Title")

    def test_title_max_length(self):
        post = Posts.objects.create(title="a"*50, body="test body")
        self.assertEqual(post.title, "a"*50)

    def test_auto_not_add_and_auto_not(self):
        posts = Posts.objects.create(title="test title", body="test body")
        self.assertIsNotNone(posts.created)
        self.assertIsNotNone(posts.modified)

        # Assert that created and modified timestamps are approximately equal to the current time

        self.assertTrue(now() - posts.created <= timedelta(seconds=1))
        self.assertTrue(now() - posts.modified <= timedelta(seconds=1))