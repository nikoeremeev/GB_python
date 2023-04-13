import unittest
from main import func


class TestSample(unittest.TestCase):
    def setUp(self) -> None:
        self.data = {'one': 1, 'two': 2, 'three': 3, 'four': 4}

    def test_step_1(self):
        self.assertEqual(func(self.data), 4)

    def test_step_2(self):
        self.assertEqual(func(self.data, first=False), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
