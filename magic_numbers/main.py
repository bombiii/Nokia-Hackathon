from pathlib import Path

def next_magic_num(n: int) -> int:
    if n < 1:
        return 1

    s = str(n)
    ln = len(s)
    half = (ln + 1) // 2
    left = s[:half]

    if ln % 2 == 0:
        candidate = left + left[::-1]
    else:
        candidate = left + left[:-1][::-1]

    if int(candidate) > n:
        return int(candidate)

    new_left = str(int(left) + 1)

    if len(new_left) > half:
        return int("1" + "0" * (ln - 1) + "1")

    if ln % 2 == 0:
        return int(new_left + new_left[::-1])
    return int(new_left + new_left[:-1][::-1])


def parse_num(raw: str) -> int:
    raw = raw.strip()
    if "^" in raw:
        b, e = raw.split("^", 1)
        return int(b) ** int(e)
    return int(raw)


def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        n = parse_num(line)
        print(next_magic_num(n))


if __name__ == "__main__":
    main()