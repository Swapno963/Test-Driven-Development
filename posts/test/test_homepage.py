from django.test import TestCase
from http import HTTPStatus
from posts.models import Posts



class HomePageTest(TestCase):
    def setUp(self):
        post1 = Posts.objects.create(title="my title", body="test body")
        post2 = Posts.objects.create(title="my title 2", body="test body 2")

    def test_homepage_returns_correct_response(self):
        responce = self.client.get("/")

        self.assertTemplateUsed(responce, "posts/index.html")
        self.assertEqual(responce.status_code, HTTPStatus.OK)

    def test_homepage_returns_posts_list(self):
        response = self.client.get("/")

        self.assertContains(response, "my title")
        self.assertContains(response, "my title 2")

