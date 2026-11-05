import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_rates_at_other_weights(self):
        for zone, expected in (
            ("local", 6.5),
            ("regional", 9.5),
        ):
            with self.subTest(zone=zone, weight_kg=1):
                self.assertEqual(shipping_quote(1, zone), expected)
        self.assertEqual(shipping_quote(0.75, "local"), 6.12)
        self.assertEqual(shipping_quote(0.75, "regional"), 9.12)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")
