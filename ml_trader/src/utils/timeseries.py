from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from typing import List, Tuple

from src.config import TRAIN_MONTHS


def generate_train_test_periods(
    start_date: str,
    end_date: str,
    train_months: int,
    test_months: int
) -> Tuple[List[Tuple[str, str]], List[Tuple[str, str]]]:
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    train_periods = []
    test_periods = []

    current_train_start = start_date

    while True:
        train_end = current_train_start + relativedelta(months=train_months) - timedelta(days=1)
        test_start = train_end + timedelta(days=1)
        test_end = test_start + relativedelta(months=test_months) - timedelta(days=1)

        if test_end > end_date:
            break  # Stop when test period exceeds the end date

        train_periods.append([current_train_start.strftime("%Y-%m-%d"), train_end.strftime("%Y-%m-%d")])
        test_periods.append([test_start.strftime("%Y-%m-%d"), test_end.strftime("%Y-%m-%d")])

        # Move train period start forward
        current_train_start += relativedelta(months=TRAIN_MONTHS)

    return train_periods, test_periods