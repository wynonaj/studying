"""Extract slide and speaker-note text from the eight CIS 425 lecture decks."""

from __future__ import annotations

import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


DOWNLOADS = Path('/Users/wynonajaner/Downloads')
CONVERTED = Path('/tmp/cis425-decks')
OUTPUT = Path(__file__).with_name('source-slides.json')
FILES = [
    DOWNLOADS / 'Lecture 1_Opening.pptx',
    CONVERTED / 'Lecture 2 Architecture.pptx',
    DOWNLOADS / 'Lecture 3 Overview of Attacks - part I.pptx',
    DOWNLOADS / 'Lecture 4 Overview of Attacks - part II.pptx',
    DOWNLOADS / 'Lecture 5 - OS Hardening.pptx',
    DOWNLOADS / 'Lecture 6 - How to determine if a website is malicious.pptx',
    CONVERTED / 'Lecture 7_Cryptography & Cryptocurrency.pptx',
    CONVERTED / 'Lecture 8 Sec_NWK_Admn.pptx',
]
NS = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}


def number(name: str) -> int:
    match = re.search(r'(\d+)\.xml$', name)
    return int(match.group(1)) if match else 0


def extract_xml(archive: zipfile.ZipFile, name: str) -> list[str]:
    root = ET.fromstring(archive.read(name))
    values = []
    for node in root.findall('.//a:t', NS):
        value = ' '.join((node.text or '').split())
        if value:
            values.append(value)
    return values


def extract(path: Path, lecture: int) -> dict:
    with zipfile.ZipFile(path) as archive:
        slides = sorted(
            (name for name in archive.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml', name)),
            key=number,
        )
        notes_by_number = {
            number(name): extract_xml(archive, name)
            for name in archive.namelist()
            if re.fullmatch(r'ppt/notesSlides/notesSlide\d+\.xml', name)
        }
        return {
            'lecture': lecture,
            'file': path.name,
            'slides': [
                {
                    'number': number(name),
                    'text': extract_xml(archive, name),
                    'notes': notes_by_number.get(number(name), []),
                }
                for name in slides
            ],
        }


def main() -> None:
    decks = [extract(path, lecture) for lecture, path in enumerate(FILES, 1)]
    OUTPUT.write_text(json.dumps(decks, indent=2, ensure_ascii=False) + '\n')
    print('Extracted', sum(len(deck['slides']) for deck in decks), 'slides')
    for deck in decks:
        print(f"Lecture {deck['lecture']}: {len(deck['slides'])} slides")


if __name__ == '__main__':
    main()
