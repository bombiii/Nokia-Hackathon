from pathlib import Path
import math
from datetime import datetime

FREE_MINS = 30
LOW_RATE = 300
LOW_RATE_HOURS = 3
HIGH_RATE = 500
DAY_CAP = 10_000
DAY_MINS = 24 * 60

DATE_FORMAT = "%Y-%m-%d %H:%M"

def parse_datetime(s: str) -> datetime:
    return datetime.strptime(s, DATE_FORMAT)

def calculate_fee(total_mins: float, per_min: bool = False) -> int:
    if total_mins <= FREE_MINS:
        return 0
    
    full_days = int(total_mins // DAY_MINS)
    remaining = total_mins - full_days * DAY_MINS

    fee = full_days * DAY_CAP

    if full_days == 0:
        billable = remaining - FREE_MINS
    else:
        billable = remaining

    if billable <= 0:
        return fee
    
    hours = math.ceil(billable / 60)

    if hours <= LOW_RATE_HOURS:
        partial = hours * LOW_RATE
    else:
        partial = LOW_RATE_HOURS * LOW_RATE + (hours - LOW_RATE_HOURS) * HIGH_RATE

    fee += min(partial, DAY_CAP)

    return fee


def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    print(data, end="")


if __name__ == "__main__":
    main()
