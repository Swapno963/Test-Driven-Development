from django.test import TestCase
from model_bakery import baker
from django.contrib.auth.models import User
from posts.models import Posts

class PostAuthorTest(TestCase):
    def setUp(self):
        self.user = baker.make(User)
        self.post = Posts.objects.create(
            title="title",
            body="body",
            author= self.user
        )

    def test_author_is_instance_of_user_model(self):
        self.assertTrue(isinstance(self.user, User))

    def test_blogs_belongs_to_user(self):
        self.assertTrue(hasattr(self.post, "author"))
        self.assertEqual(self.post.author, self.user)