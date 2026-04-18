from pathlib import Path
import re
import json

def parse_ipconfig(text: str):
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
            value = re.sub(r"\(.*?\)", "", value).strip()
            
            if key in FIELDS:
                field = FIELDS[key]
            
                if field == "dns_servers":
                    current["dns_servers"].append(value)
                else:
                    current[field] = value
                    last_field = field
        elif current is not None and last_field == "dns_servers":
            v = line.strip()
            if v:
                current["dns_servers"].append(re.sub(r"\(.*?\)", "", v).strip())


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
