import unittest

from failing_calculator import average_ratios


class TestFailingCalculator(unittest.TestCase):
    def test_average_ratios_raises_on_zero(self):
        with self.assertRaises(ValueError) as context:
            average_ratios([10, 5, 0])
        self.assertEqual(str(context.exception), "numbers must not contain zero")


if __name__ == "__main__":
    unittest.main()
