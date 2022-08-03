import unittest

import deposit


class DepositTestCase(unittest.TestCase):
    def test_get_amount(self):
        some_json = {"date": "31.01.2021", "periods": 7, "amount": 10000, "rate": 6}
        expected_result = {
            "28.02.2021": 10100.25,
            "30.04.2021": 10201.51,
            "30.06.2021": 10303.78,
            "31.01.2021": 10050.0,
            "31.03.2021": 10150.75,
            "31.05.2021": 10252.51,
            "31.07.2021": 10355.29}
        self.assertDictEqual(deposit.get_amount(some_json), expected_result)


if __name__ == '__main__':
    unittest.main()
