from django.test import TestCase

class SmokeTest(TestCase):
    """Тест на токсичность"""

    def test_bad_maths(self):
        """Тест: неправильные математичесие расчеты"""
        self.assertEqual(1 + 1, 3)
