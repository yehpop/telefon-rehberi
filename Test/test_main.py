from telefon_rehberi.main import func1
import unittest


class TestMain(unittest.TestCase):
    def test_func1(self):
        result = func1()
        correct_result = True

        self.assertEqual(result, correct_result)
