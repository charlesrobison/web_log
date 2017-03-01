from django.test import TestCase
from django.contrib.auth.models import User
from myblog.models import Post

# Create your tests here.

class PostTestCase(TestCase):
    fixtures = ['myblog_test_fixture.json', ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        excpected = "This is a title"
        p1 = Post(title=excpected)
        actual = str(p1)
        self.assertEqual(excpected, actual)