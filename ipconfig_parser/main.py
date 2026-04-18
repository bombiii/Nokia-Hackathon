from pathlib import Path

def parse_ipconfig(text: str) -> dict:
    for line in text.splitlines():
        if not line.startswith((" ", "\t")) and "adapter" in line.lower() and line.strip().endswith(":"):
            print(line.strip())


def main():
    for path in sorted(Path(".").glob("*.txt")):
        text = Path(path).read_text(encoding="utf-16")
        parse_ipconfig(text)

if __name__ == "__main__":
    main()
