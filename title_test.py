import unittest
from title import convert

class TestConvert(unittest.TestCase):

    def test_convert(self):
        str = convert("hello world")
        self.assertEqual(str, "Hello World")

if __name__ == '__main__':
    unittest.main()