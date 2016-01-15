from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase

from .views import IndexView


class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, IndexView.as_view())
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = IndexView.as_view(request)
        self.assertTrue(response.content.startwith(b'<html>'))
        self.assertIn(b'<title>扇贝</title>', response.content)
        self.assertTrue(response.content.endwith(b'</html>'))
