from django.test import TestCase
from django.urls import reverse
from .models import News, Comment

class NewsTests(TestCase):
    def test_create_news(self):
        news = News.objects.create(title="Test News", text="This is a test news.")
        self.assertEqual(News.objects.count(), 1)
        self.assertEqual(news.title, "Test News")

    def test_edit_news(self):
        news = News.objects.create(title="Test News", text="This is a test news.")
        url = reverse("news-detail", args=[news.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test News")

    def test_delete_news(self):
        news = News.objects.create(title="Test News", text="This is a test news.")
        news.delete()
        self.assertEqual(News.objects.count(), 0)

class CommentTests(TestCase):
    def test_create_comment(self):
        news = News.objects.create(title="Test News", text="This is a test news.")
        comment = Comment.objects.create(news=news, text="Test comment")
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(comment.text, "Test comment")

if __name__ == '__main__':
    main()
