from pydantic import BaseModel, validator
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Deposit(BaseModel):
    date: str
    periods: int
    amount: int
    rate: float

    @validator('date')
    def validate_date(cls, v):
        try:
            v = datetime.strptime(v, "%d.%m.%Y")
        except Exception as e:
            raise ValueError('wrong date format')
        return v

    @validator('periods')
    def validate_period(cls, v):
        if v < 1 or v > 60:
            raise ValueError('value must be between 1 and 60')
        return v

    @validator('amount')
    def validate_amount(cls, v):
        if v < 10000 or v > 3000000:
            raise ValueError('value must be between 10000 and 3000000')
        return v

    @validator('rate')
    def validate_rate(cls, v):
        if v < 1 or v > 8:
            raise ValueError('value must be between 1 and 8')
        return v

    def get_amount(self):
        count = 1
        self.amount = self.amount * (1 + self.rate / 12 / 100)
        result = {datetime.strftime(self.date, "%d.%m.%Y"): round(self.amount, 2)}
        while count < self.periods:
            self.amount = self.amount * (1 + self.rate / 12 / 100)
            result[datetime.strftime(self.date + relativedelta(months=count), "%d.%m.%Y")] = round(self.amount, 2)
            count += 1
        return result
