from django.test import TestCase
from datetime import datetime, timedelta
from django.utils.timezone import now
from http import HTTPStatus
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

    def test_curd_operations(self):
        # create
        post = Posts.objects.create(title="test title", body="body")
        self.assertEqual(Posts.objects.count(), 1)

        # retrive
        retrived_post = Posts.objects.get(id=post.id)
        self.assertEqual(retrived_post.title, "test title")

        # update
        post.title = "updated title"
        post.save()
        updated_post = Posts.objects.get(id=post.id)
        self.assertEqual(updated_post.title, "updated title")

        # delete
        post.delete()
        self.assertEqual(Posts.objects.count(), 0)

    def test_empty_body_allowed(self):
        post = Posts.objects.create(title="Test Title", body="")
        self.assertEqual(post.body, "")

    def test_query_efficiency(self):
        with self.assertNumQueries(1):
            Posts.objects.create(title="Title 1", body="Body 1")
    
    def test_query_optimization(self):
        for i in range(10):
            Posts.objects.create(title=f"Title {i}", body="Body")
        with self.assertNumQueries(1):
            posts = list(Posts.objects.all())  # Fetch all posts in one query


    def test_invalid_title_length(self):
        with self.assertRaises(Exception): 
            '''Django validates field constraints like max_length only when saving the model or during form validation. The issue here is likely that you are directly calling Posts.objects.create(), which skips certain field validations.''' 
            post = Posts(title="A" * 51, body="Test Body")
            post.full_clean()  # This raises a ValidationError if constraints are violated
            post.save()


class HomePageTest(TestCase):
    def setUp(self):
        Posts.objects.create(
            title="my title",
            body="test body"
        )  
        Posts.objects.create(
            title="my title 2",
            body="test body 2"
        )


    def test_homepage_returns_correct_response(self):
        responce = self.client.get("/")
        
        self.assertTemplateUsed(responce, 'posts/index.html')
        self.assertEqual(responce.status_code, HTTPStatus.OK)