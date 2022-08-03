import unittest
import utils


class UtilsTestCase(unittest.TestCase):
    def test_valid_json(self):
        valid_json = {"date": "31.01.2021", "periods": 7, "amount": 10000, "rate": 6}
        self.assertEqual(utils.validate_json(valid_json), True)

    def test_not_valid_json(self):
        valid_json = {"date": "31.01.2021", "periods": 7, "amount": 10000, "rate": 100}
        self.assertEqual(utils.validate_json(valid_json), False)

    def test_empty_json(self):
        valid_json = {}
        self.assertEqual(utils.validate_json(valid_json), False)


if __name__ == '__main__':
    unittest.main()
