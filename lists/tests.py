import re

from django.test import TestCase
from django.http import HttpRequest
from django.shortcuts import render

from lists.views import home_page


class HomePageViewTest(TestCase):
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        home_expected = render(request, 'home.html')
        self.assertEqual(
            re.sub(r'\<.+csrf.+\/\>', '', home_expected.content.decode('utf8')),
            re.sub(r'\<.+csrf.+\/\>', '', response.content.decode('utf8')))

    def test_home_page_can_store_post_requests(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'new item'
        response = home_page(request)
        self.assertIn('<td>new item</td>', response.content.decode('utf8'))
