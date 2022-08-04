import datetime

import pytest
from pydantic import ValidationError

from deposit import Deposit


def test_get_amount():
    some_json = {"date": "31.01.2021", "periods": 7, "amount": 10000, "rate": 6}
    deposit_object = Deposit(**some_json)
    expected_result = {
        "28.02.2021": 10100.25,
        "30.04.2021": 10201.51,
        "30.06.2021": 10303.78,
        "31.01.2021": 10050.0,
        "31.03.2021": 10150.75,
        "31.05.2021": 10252.51,
        "31.07.2021": 10355.29}
    assert deposit_object.get_amount() == expected_result


@pytest.mark.parametrize("input_json, result", [({"date": "31.01.2021", "periods": 7, "amount": 10000, "rate": 6},
                                                 datetime.datetime(2021, 1, 31, 0, 0)),
                                                ({"date": "01.12.2020", "periods": 7, "amount": 10000, "rate": 6},
                                                 datetime.datetime(2020, 12, 1, 0, 0)),
                                                ])
def test_good_date_format(input_json, result):
    deposit_object = Deposit(**input_json)
    assert deposit_object.date == result


@pytest.mark.parametrize("input_json, result", [({"date": "31-01-2021", "periods": 7, "amount": 10000, "rate": 6},
                                                 datetime.datetime(2021, 1, 31, 0, 0)),
                                                ({"date": "01.12.2020", "periods": 7, "amount": 10000, "rate": -1},
                                                 datetime.datetime(2020, 12, 1, 0, 0)),
                                                ])
def test_json_format(input_json, result):
    with pytest.raises(ValidationError):
        Deposit(**input_json)
