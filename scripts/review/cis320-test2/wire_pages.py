"""Wire the separate CIS 320 Test 2 page into the existing Classes workspace."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DIST = ROOT / "dist"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    if text.count(old) != 1:
        raise ValueError(f"Could not find one insertion point for {label}")
    return text.replace(old, new, 1)


index = DIST / "index.html"
text = index.read_text(encoding="utf-8")
class_nav = '<nav class="class-switch" aria-label="Choose class"><a href="index.html" aria-current="page">CIS 320 <small>Networking</small></a><a href="cis304.html">CIS 304 <small>Enterprise architecture</small></a><a href="cis464.html">CIS 464 <small>Project management</small></a><a href="cis425.html">CIS 425 <small>Defensive cybersecurity</small></a></nav>'
test_nav = '<nav class="test-switch" aria-label="Choose CIS 320 exam"><a href="index.html" aria-current="page">Test 1 <small>Ch. 1–4, 12</small></a><a href="cis320-test2.html">Test 2 <small>Ch. 5–9</small></a></nav>'
text = replace_once(text, class_nav, class_nav + test_nav, "Test 1/Test 2 navigation")
index.write_text(text, encoding="utf-8")

classes = DIST / "classes.html"
text = classes.read_text(encoding="utf-8")
text = text.replace(
    "Layers, cables, IP addresses, subnet math and network design.",
    "Test 1 and Test 2: layers, transport, applications, routing, subnetting, wireless and network design.",
)
classes.write_text(text, encoding="utf-8")


asset_pattern = re.compile(r'(?P<prefix>(?:src|href)=")(?P<asset>[^"?]+\.(?:js|css))\?v=(?P<version>[^"&]+)(?P<suffix>")')


def refresh(page: Path) -> None:
    source = page.read_text(encoding="utf-8")

    def hashed(match: re.Match[str]) -> str:
        asset = DIST / match.group("asset")
        if not asset.exists():
            return match.group(0)
        digest = hashlib.sha256(asset.read_bytes()).hexdigest()[:12]
        return f'{match.group("prefix")}{match.group("asset")}?v={digest}{match.group("suffix")}'

    page.write_text(asset_pattern.sub(hashed, source), encoding="utf-8")


for page in DIST.glob("*.html"):
    refresh(page)

print("Wired CIS 320 Test 2 and refreshed static asset hashes.")

