#!/usr/bin/env python3
"""Extract the supplied CIS 320 Test 2 sources into one review manifest.

The deployed app does not need the original Office/PDF files.  This script is
only for source review and makes the authoring trail reproducible.
"""

from __future__ import annotations

import hashlib
import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


DOWNLOADS = Path.home() / "Downloads"
ATTACHMENTS = Path.home() / ".codex" / "attachments"
HERE = Path(__file__).resolve().parent

PRESENTATIONS = [
    DOWNLOADS / "Ch5_Transport Layer.pptx",
    DOWNLOADS / "Ch6_Application Layer.pptx",
    DOWNLOADS / "Ch7_Support Services.pptx",
    DOWNLOADS / "Ch8_Routing & Subnetting Part 1 (1).pptx",
    DOWNLOADS / "Ch8_Routing_Appendix_Examples.pptx",
    DOWNLOADS / "Ch8_Routing & Subnetting Part 2 (1).pptx",
    DOWNLOADS / "Ch 9_Wireless.pptx",
]

DOCUMENT = DOWNLOADS / "Chapter 8_Subnetting Exercises - Answers Explained (1).docx"
PDFS = [
    DOWNLOADS / "CIS320_Test_2_Completed_Study_Guide.pdf",
    DOWNLOADS / "Subnetting_Network+_Lammle (2).pdf",
]

PASTED = [
    ATTACHMENTS / "507565e3-c500-4b93-a20f-9a0c32239e9c" / "Pasted text.txt",
    ATTACHMENTS / "0ed11232-2b13-45d4-84dd-946153347746" / "Pasted text.txt",
    ATTACHMENTS / "83e08308-1224-4505-93bd-30681f1b742f" / "Pasted text.txt",
    ATTACHMENTS / "62808b63-e2e1-4332-bf2a-d4d33449c633" / "Pasted text.txt",
    ATTACHMENTS / "2379221d-30d4-4935-89f7-272318bfb571" / "Pasted text.txt",
    ATTACHMENTS / "d2f8cfe4-da90-4d47-9fdf-f7b66852ab95" / "Pasted text.txt",
    ATTACHMENTS / "0e80b632-4a1b-4e93-96fa-3dc93157f6b2" / "Pasted text.txt",
    ATTACHMENTS / "9a8908c3-1a07-42c6-9fd8-427436ef4488" / "Pasted text.txt",
    ATTACHMENTS / "02adb1ac-6c5d-430a-a8f7-43fcf891d686" / "Pasted text.txt",
    ATTACHMENTS / "1dc3eb6f-cd49-42e6-917a-52a467d54521" / "Pasted text.txt",
    ATTACHMENTS / "1c547106-ccff-4e87-aeb3-4ccae7aba973" / "Pasted text.txt",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def natural_number(name: str) -> int:
    match = re.search(r"(\d+)", Path(name).stem)
    return int(match.group(1)) if match else 0


def xml_text(blob: bytes) -> list[str]:
    root = ET.fromstring(blob)
    values = []
    for node in root.iter():
        if node.tag.endswith("}t") and node.text and node.text.strip():
            values.append(" ".join(node.text.split()))
    return values


def pptx_record(path: Path) -> dict:
    with zipfile.ZipFile(path) as archive:
        names = set(archive.namelist())
        slide_names = sorted(
            (name for name in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)),
            key=natural_number,
        )
        slides = []
        for slide_name in slide_names:
            number = natural_number(slide_name)
            notes_name = f"ppt/notesSlides/notesSlide{number}.xml"
            slides.append(
                {
                    "number": number,
                    "text": xml_text(archive.read(slide_name)),
                    "notes": xml_text(archive.read(notes_name)) if notes_name in names else [],
                }
            )
        media = [
            {"name": Path(name).name, "bytes": archive.getinfo(name).file_size}
            for name in sorted(names)
            if name.startswith("ppt/media/") and not name.endswith("/")
        ]
    return {
        "path": str(path),
        "sha256": digest(path),
        "slideCount": len(slides),
        "slides": slides,
        "media": media,
    }


def docx_record(path: Path) -> dict:
    with zipfile.ZipFile(path) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    body = next(node for node in root if node.tag.endswith("}body"))
    blocks = []
    for child in body:
        if child.tag.endswith("}p"):
            text = "".join(node.text or "" for node in child.iter() if node.tag.endswith("}t")).strip()
            if text:
                blocks.append({"type": "paragraph", "text": " ".join(text.split())})
        elif child.tag.endswith("}tbl"):
            rows = []
            for row in (node for node in child if node.tag.endswith("}tr")):
                cells = []
                for cell in (node for node in row if node.tag.endswith("}tc")):
                    text = "".join(node.text or "" for node in cell.iter() if node.tag.endswith("}t"))
                    cells.append(" ".join(text.split()))
                rows.append(cells)
            blocks.append({"type": "table", "rows": rows})
    return {"path": str(path), "sha256": digest(path), "blocks": blocks}


def pdf_record(path: Path) -> dict:
    try:
        import pdfplumber
    except ImportError as exc:  # pragma: no cover - authoring dependency
        raise SystemExit("pdfplumber is required to rebuild the source manifest") from exc
    with pdfplumber.open(path) as document:
        pages = [
            {"number": index, "text": (page.extract_text() or "").strip()}
            for index, page in enumerate(document.pages, 1)
        ]
    # Some scanned PDFs expose no pages through pdfminer/pdfplumber even though
    # the PDF page tree is valid.  Keep their true page count in the manifest.
    if not pages:
        from pypdf import PdfReader

        reader = PdfReader(path)
        pages = [
            {"number": index, "text": (page.extract_text() or "").strip()}
            for index, page in enumerate(reader.pages, 1)
        ]
    return {
        "path": str(path),
        "sha256": digest(path),
        "pageCount": len(pages),
        "imageOnly": not any(page["text"] for page in pages),
        "pages": pages,
    }


def pasted_records() -> dict:
    groups: dict[str, dict] = {}
    for path in PASTED:
        value = digest(path)
        record = groups.setdefault(value, {"sha256": value, "copies": [], "text": path.read_text()})
        record["copies"].append(str(path))
    return {"providedCount": len(PASTED), "uniqueCount": len(groups), "unique": list(groups.values())}


def main() -> None:
    for path in [*PRESENTATIONS, DOCUMENT, *PDFS, *PASTED]:
        if not path.exists():
            raise SystemExit(f"Missing source: {path}")
    manifest = {
        "presentations": [pptx_record(path) for path in PRESENTATIONS],
        "document": docx_record(DOCUMENT),
        "pdfs": [pdf_record(path) for path in PDFS],
        "pastedNotes": pasted_records(),
    }
    destination = HERE / "source-manifest.json"
    destination.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(
        json.dumps(
            {
                "output": str(destination),
                "slides": sum(item["slideCount"] for item in manifest["presentations"]),
                "documentBlocks": len(manifest["document"]["blocks"]),
                "pdfPages": sum(item["pageCount"] for item in manifest["pdfs"]),
                "uniquePastedNotes": manifest["pastedNotes"]["uniqueCount"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
