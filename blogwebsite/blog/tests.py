from django.test import TestCase


class BlogModelTests(TestCase):
    def setUp(self):
        from django.contrib.auth.models import User
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_blog_post_creation(self):
        from .models import BlogPost
        post = BlogPost.objects.create(
            title='Test Post',
            slug='test-post',
            content='This is a test post content.',
            author=self.user,
            published=True
        )
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.slug, 'test-post')
        self.assertEqual(post.author, self.user)
        self.assertTrue(post.published)

    def test_blog_post_str_method(self):
        from .models import BlogPost
        post = BlogPost.objects.create(
            title='Another Test Post',
            slug='another-test-post',
            content='Content here.',
            author=self.user
        )
        self.assertEqual(str(post), 'Another Test Post')

    def test_get_excerpt(self):
        from .models import BlogPost
        post = BlogPost.objects.create(
            title='Long Content Post',
            slug='long-content-post',
            content='This is a very long content that should be truncated when getting excerpt.',
            author=self.user
        )
        excerpt = post.get_excerpt(20)
        self.assertEqual(excerpt, 'This is a very lo...')