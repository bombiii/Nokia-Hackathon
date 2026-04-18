from pathlib import Path



def main():
    for path in sorted(Path(".").glob("*.txt")):
        print(path.name)
        text = Path(path).read_text(encoding="utf-16")
        print(text)

if __name__ == "__main__":
    main()
