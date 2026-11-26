
from pathlib import Path

ENTRY = "The fridge locked at midnight and texted me 'hydration is enough.' I pay its Wi-Fi bill and it still talks to me like a disappointed gym coach."

Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(ENTRY, encoding="utf-8")
