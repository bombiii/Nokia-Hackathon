from pathlib import Path
import re
import json

def parse_ipconfig(text: str) -> list[dict]:
    FIELDS = {
      "description": "description",
      "physical address": "physical_address",
      "dhcp enabled": "dhcp_enabled",
      "ipv4 address": "ipv4_address",
      "autoconfiguration ipv4 address": "ipv4_address",
      "subnet mask": "subnet_mask",
      "default gateway": "default_gateway",
      "dns servers": "dns_servers",
  }

    adapters = []
    current = None
    last_field = None

    for line in text.splitlines():
        if not line.startswith((" ", "\t")) and "adapter" in line.lower() and line.strip().endswith(":"):
            if current is not None:
                adapters.append(current)
            
            current = {
                "adapter_name": line.strip().rstrip(":"),
                "description": "",
                "physical_address": "",
                "dhcp_enabled": "",
                "ipv4_address": "",
                "subnet_mask": "",
                "default_gateway": "",
                "dns_servers": [],
            }

        elif current is not None and ":" in line:
            key, value = line.split(":", 1)
            key = key.replace(".", "").strip()
            key = " ".join(key.split())
            key = key.lower()

            value = value.strip()
            value = re.sub(r"\((Preferred|Deferred|Duplicate|Deprecated|Tentative)\)", "", value, flags=re.IGNORECASE).strip()
            
            indent = len(line) - len(line.lstrip())
            if key in FIELDS:
                field = FIELDS[key]
                if field == "dns_servers":
                    if value:
                        current["dns_servers"].append(value)
                    last_field = field
                else:
                    current[field] = value
                    last_field = field
            elif last_field == "dns_servers" and indent > 20:
                full = line.strip()
                if full:
                    current["dns_servers"].append(re.sub(r"\(.*?\)", "", full).strip())
            else:
                last_field = None


    if current is not None:
        adapters.append(current)

    return adapters

def main():
    results = []
    for path in sorted(Path(".").glob("*.txt")):
        text = Path(path).read_text(encoding="utf-16")
        result = {
            "file_name": path.name,
            "adapters": parse_ipconfig(text),
        }
        results.append(result)
    out = json.dumps(results, indent=2, ensure_ascii=False)
    print(out)
    Path("output.json").write_text(out, encoding="utf-8")

if __name__ == "__main__":
    main()
