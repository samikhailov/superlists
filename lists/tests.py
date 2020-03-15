from django.test import TestCase


class HomePageTest(TestCase):
    """Тест домашней страницы"""
    def test_home_page_returns_corrext_html(self):
        """Тест: используется домашний шаблон"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
