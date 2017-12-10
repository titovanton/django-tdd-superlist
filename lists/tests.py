from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page


class HomePageViewTest(TestCase):
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        home_expected = render_to_string('home.html')
        self.assertEqual(home_expected, response.content.decode('utf8'))
