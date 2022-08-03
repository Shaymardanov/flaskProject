from dateutil.relativedelta import relativedelta
from datetime import datetime


def get_amount(input_json):
    count = 1
    amount = input_json['amount'] * (1 + input_json['rate'] / 12 / 100)
    date = datetime.strptime(input_json['date'], "%d.%m.%Y")
    result = {datetime.strftime(date, "%d.%m.%Y"): round(amount, 2)}
    while count < input_json['periods']:
        amount = amount * (1 + input_json['rate'] / 12 / 100)
        result[datetime.strftime(date + relativedelta(months=count), "%d.%m.%Y")] = round(amount, 2)
        count += 1
    return result
