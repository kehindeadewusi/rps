from datetime import datetime
from billups.dates.dateutils import days_to_snake_day


def test_days_to():
    dt = datetime(2022, 7, 15)
    d = days_to_snake_day(dt)

    assert d == 1
