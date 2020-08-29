from django.test import TestCase
from django.urls import resolve
from blog.views import resume

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/resume')
        self.assertEqual(found.func, resume)