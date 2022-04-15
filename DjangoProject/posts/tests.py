from django.test import TestCase
from .models import Post
from django.urls import reverse


class PostsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("posts_home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("posts_home"))
        self.assertTemplateUsed(response, "posts_home.html")

    def test_template_content(self):
        response = self.client.get(reverse("posts_home"))
        self.assertContains(response, "This is a test!")