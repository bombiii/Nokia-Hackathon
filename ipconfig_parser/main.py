from pathlib import Path

def parse_ipconfig(text: str):
    adapters = []
    current = None

    for line in text.splitlines():
        if not line.startswith((" ", "\t")) and "adapter" in line.lower() and line.strip().endswith(":"):
            if current is not None:
                adapters.append(current)
            current = {"adapter_name": line.strip().rstrip(":")}
        elif current is not None and ":" in line:
            key, value = line.split(":", 1)
            key = key.replace(".", "").strip()
            key = " ".join(key.split())
            key = key.lower()

            value = value.strip()
            current[key] = value

    if current is not None:
        adapters.append(current)

    return adapters

def main():
    for path in sorted(Path(".").glob("*.txt")):
        text = Path(path).read_text(encoding="utf-16")
        result = parse_ipconfig(text)
        print(result)

if __name__ == "__main__":
    main()
