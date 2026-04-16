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


def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    print(data, end="")


if __name__ == "__main__":
    main()
