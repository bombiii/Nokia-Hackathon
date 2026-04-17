from pathlib import Path

def next_magic_num(n: int) -> int:
    if n < 1:
        return 1
    
    s = str(n)
    length = len(s)
    half = (length + 1) // 2
    left_half = s[:half]

    if length % 2 == 0:
        candiate_str = left_half + left_half[::-1]
    else:
        candiate_str = left_half + left_half[:-1][::-1]

    if int (candiate_str) > n:
        return int(candiate_str)
    
    new_left = str(int(left_half) + 1)

    if len(new_left) > half:
        return int("1" + "0" * (length - 1) + "1")
    
    if length % 2 == 0:
        return int(new_left + new_left[::-1])
    return int(new_left + new_left[:-1][::-1])


def parse_input(data: str) -> int:
    data = data.strip()
    if '^' in data:
        base, exp = data.split('^')
        return int(base) ** int(exp)
    return int(data)

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            n = parse_input(line)
            print(next_magic_num(n))
        except (ValueError, ZeroDivisionError):
            print(f"HIBA: érvénytelen bemenet: {line}")
        


if __name__ == "__main__":
    main()