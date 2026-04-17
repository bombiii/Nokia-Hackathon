from pathlib import Path
import math
from datetime import datetime

FREE_MINUTES = 30
LOW_RATE = 300
LOW_RATE_HOURS = 3
HIGH_RATE = 500
DAY_CAP = 10_000
DAY_MINUTES = 24 * 60


def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    print(data, end="")


if __name__ == "__main__":
    main()
