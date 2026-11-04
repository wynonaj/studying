"""Add CIS 425 to class navigation and refresh static asset cache hashes."""

import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DIST = ROOT / 'dist'

for name in ['index.html', 'cis304.html', 'cis464.html']:
    path = DIST / name
    text = path.read_text()
    link = '<a href="cis425.html">CIS 425 <small>Defensive cybersecurity</small></a>'
    text = text.replace(link, '')
    pattern = r'(<nav class="class-switch"[^>]*>)(.*?)(</nav>)'
    def add_link(match):
        body = match.group(2)
        marker = '<a href="cis464.html"'
        body = body.replace(marker, link + marker, 1)
        return match.group(1) + body + match.group(3)
    text = re.sub(pattern, add_link, text, count=1)
    path.write_text(text)

classes = DIST / 'classes.html'
text = classes.read_text()
if 'href="cis425.html"' not in text:
    marker = '<a class="class-entry" href="cis464.html">'
    card = ('<a class="class-entry" href="cis425.html"><span class="c-tag">DEFENSIVE CYBERSECURITY</span>'
            '<strong>CIS 425</strong><h2>How defenders protect systems</h2>'
            '<span>Secure architecture, attacks, hardening, website analysis, cryptography, protocols and logs.</span>'
            '<span>Open class →</span></a>')
    text = text.replace(marker, card + marker, 1)
    text = text.replace('ONE PLACE · THREE SEPARATE CLASSES', 'ONE PLACE · FOUR SEPARATE CLASSES')
classes.write_text(text)

for path in DIST.glob('*.html'):
    text = path.read_text()
    def hashed(match):
        asset = DIST / match.group(2)
        digest = hashlib.sha256(asset.read_bytes()).hexdigest()[:12]
        return f'{match.group(1)}{match.group(2)}?v={digest}{match.group(3)}'
    text = re.sub(r'((?:href|src)=")([\w.-]+\.(?:css|js))(?:\?v=[a-f0-9]+)?(")', hashed, text)
    path.write_text(text)

print('Wired CIS 425 into the Classes workspace and refreshed asset hashes')
