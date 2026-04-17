from pathlib import Path

def min_num_of_drops(n: int, h: int) -> int:
    if h <= 0:
        return 0
    if n == 0:
        return h
    
    k = 0
    while True:
        k += 1
        total = 0
        binom = 1
        for i in range(1, n + 1):
            binom = binom * (k - i + 1) // i
            total += binom
            if total >= h:
                return k
            if i >= k:
                break

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split(",")]
        n, h = int(parts[0]), int(parts[1])
        print(min_num_of_drops(n, h))

if __name__ == "__main__":
    main()
