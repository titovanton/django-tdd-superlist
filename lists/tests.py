from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page


class HomePageViewTest(TestCase):
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertIn('<title>To-Do', response.content.decode('utf8'))
        self.assertTrue(response.content.decode('utf8').startsWith('<html>'))
        self.assertTrue(response.content.decode('utf8').endsWith('</html>'))
