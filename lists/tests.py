from cv2 import exp
from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase
from lists.views import home_page
from django.template.loader import render_to_string


class SomkeTest(TestCase):

    """
    This method tests the two things the following methods test.
    """

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

    # def test_root_url_resolve_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)

    # def test_home_page_returns_correct_html(self):
    #     response = self.client.get('/')

    #     # Use Django Test Client to test
    #     self.assertTemplateUsed(response, 'wrong.html')

    #     # Use render_to_string() to test
    #     # html = response.content.decode('utf8')
    #     # expected_html = render_to_string('home.html')
    #     # self.assertEqual(html, expected_html)

    #     # Deprecated hand-writtem asserts
    #     # self.assertTrue(html.startswith('<html>'))
    #     # self.assertIn('<title>To-Do Lists</title>', html)
    #     # self.assertTrue(html.endswith('</html>'))

    # Smoke test
    # def test_bad_maths(self):
    #     self.assertEqual(1 + 1, 3)
