from django.core.urlresolvers import resolve
from django.test import TestCase
from .views import IndexView


class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, IndexView.as_view())
