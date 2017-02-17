import unittest
from main import f


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(f("FOO"), 'FOO')


if __name__ == '__main__':
    unittest.main()
