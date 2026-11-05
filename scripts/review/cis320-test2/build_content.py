"""Build the browser data for the separate CIS 320 Test 2 study space."""

from __future__ import annotations

import json
from pathlib import Path

from guide_content import EXERCISES, GUIDE_TOPICS
from support_content import (
    CHECK_ROWS,
    CLOZE_ROWS,
    CONNECTIONS,
    SECTIONS,
    SORT_ROWS,
    VOCAB_ROWS,
)

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "dist" / "cis320-test2-content.json"


def validate_choices(correct: str, wrong: list[str], label: str) -> None:
    values = [correct, *wrong]
    if len(values) != 4 or len(set(values)) != 4:
        raise ValueError(f"{label} needs four distinct choices: {values}")


def build_vocab() -> list[dict]:
    items = []
    for index, (section, term, expansion, definition, source, wrong) in enumerate(VOCAB_ROWS, 1):
        correct = expansion or term
        validate_choices(correct, wrong, f"vocab {term}")
        if expansion:
            question = f"What does {term} stand for?"
            answer = f"{term} stands for {expansion}. {definition}"
            teach = (
                f"First expand the letters: {expansion}. Then connect the name to its job. "
                f"{definition}"
            )
        else:
            question = f"Which term matches this meaning? {definition}"
            answer = definition
            teach = (
                f"The defining clue is the job or scope in the sentence. {definition} "
                f"That exact idea is called {term}."
            )
        items.append(
            dict(
                id=f"t2-v{index:03}",
                section=section,
                source=source,
                title=term,
                term=term,
                exp=expansion,
                q=question,
                correct=correct,
                distractors=wrong,
                answer=answer,
                teach=teach,
                example=f"If a question describes this exact job, separate it from nearby terms by asking where it acts and what information it changes or carries.",
            )
        )
    return items


def build_checks() -> list[dict]:
    items = []
    for index, (section, source, q, correct, wrong, teach, example) in enumerate(CHECK_ROWS, 1):
        validate_choices(correct, wrong, f"check {index}")
        items.append(
            dict(
                id=f"t2-check-{index:03}",
                section=section,
                source=source,
                title=f"Apply guide topic {source}",
                q=q,
                correct=correct,
                distractors=wrong,
                answer=teach,
                teach=teach,
                example=example,
            )
        )
    return items


def build_cloze() -> list[dict]:
    items = []
    for index, (section, source, q, answers, wrong, teach) in enumerate(CLOZE_ROWS, 1):
        if q.count("____") != len(answers):
            raise ValueError(f"cloze {index} blank/answer mismatch")
        items.append(
            dict(
                id=f"t2-cloze-{index:02}",
                kind="cloze",
                section=section,
                source=source,
                title=f"Build the relationship · {index}",
                q=q,
                correct="; ".join(answers),
                distractors=wrong,
                answer=teach,
                teach=teach,
                example="Read the whole completed sentence aloud once after checking it. The surrounding words explain the role of each blank.",
            )
        )
    return items


def build_sorts() -> list[dict]:
    items = []
    for index, (section, source, title, q, steps, teach) in enumerate(SORT_ROWS, 1):
        if len(steps) < 3 or len(steps) != len(set(steps)):
            raise ValueError(f"sort {index} has invalid steps")
        items.append(
            dict(
                id=f"t2-sort-{index:02}",
                section=section,
                source=source,
                title=title,
                q=q,
                items=steps,
                correct=" → ".join(steps),
                distractors=[],
                answer=teach,
                teach=teach,
                example="Follow the actor at each step: identify who sends or decides first, what the receiver learns, and what can happen only after that result exists.",
            )
        )
    return items


SOURCES = [
    dict(id="guide", kind="pdf", title="CIS320 Test 2 Completed Study Guide", detail="5 pages · 57 answered guide topics · the scope authority for the new Test 2 learning path."),
    dict(id="ch5", kind="slides", count=21, title="Chapter 5 · Transport Layer", detail="21 lecture slides · TCP, UDP, ports, sockets, states, flow control, and handshakes."),
    dict(id="ch6", kind="slides", count=26, title="Chapter 6 · Application Layer", detail="26 lecture slides · HTTP, URLs, APIs, email, FTP, BitTorrent, QUIC, and HTTP/3."),
    dict(id="ch7", kind="slides", count=26, title="Chapter 7 · Support Services", detail="26 lecture slides · private addressing, NAT/PAT, DHCP, ARP, and DNS."),
    dict(id="ch8a", kind="slides", count=40, title="Chapter 8 · Routing and Subnetting Part 1", detail="40 lecture slides · switching and routing, tables, route protocols, aggregation, MPLS, and SDN."),
    dict(id="ch8examples", kind="slides", count=20, title="Chapter 8 · Routing Appendix Examples", detail="20 lecture slides · route-table and forwarding examples used to make the routing process concrete."),
    dict(id="ch8b", kind="slides", count=28, title="Chapter 8 · Routing and Subnetting Part 2", detail="28 lecture slides · masks, prefixes, address blocks, host ranges, and subnet design."),
    dict(id="ch9", kind="slides", count=28, title="Chapter 9 · Wireless", detail="28 lecture slides · channels, standards, MIMO, Wi-Fi security, medium access, cells, and 802.15."),
    dict(id="lammle", kind="pdf", title="Subnetting Network+ reading", detail="24-page scanned subnetting reading · used as additional calculation reference without expanding beyond the supplied exam topics."),
    dict(id="exercises", kind="document", title="Chapter 8 Subnetting Exercises · Answers Explained", detail="15 pages · all 20 original multiple-choice problems, diagrams, answers, and worked explanations are preserved in their own practice bank."),
    dict(id="notes-a", kind="notes", title="Pasted subnetting lesson set", detail="Eight supplied files were exact byte-for-byte copies of one 29-lesson beginner guide; represented once to avoid duplicate questions."),
    dict(id="notes-b", kind="notes", title="Formatted subnetting guide variant", detail="Two supplied files were exact copies of one expanded Markdown version; represented once."),
    dict(id="notes-c", kind="notes", title="Pasted worked-problem companion", detail="One unique set with 31 foundation problems plus the 20 review problems and explanations."),
]


def normalize_guide() -> list[dict]:
    if len(GUIDE_TOPICS) != 57:
        raise ValueError(f"Expected 57 guide topics, found {len(GUIDE_TOPICS)}")
    items = []
    for number, raw in enumerate(GUIDE_TOPICS, 1):
        item = dict(raw)
        item.setdefault("number", number)
        item.setdefault("id", f"t2-q{number:02}")
        item.setdefault("sourceLabel", "CIS320 Test 2 Completed Study Guide")
        item.setdefault("slides", [])
        item.setdefault("distractors", [])
        validate_choices(item["correct"], item["distractors"], f"guide topic {number}")
        required = ["section", "title", "q", "correct", "answer", "teach", "example"]
        for key in required:
            if not item.get(key):
                raise ValueError(f"Guide topic {number} is missing {key}")
        items.append(item)
    if [item["number"] for item in items] != list(range(1, 58)):
        raise ValueError("Guide numbering is not continuous")
    return items


def normalize_exercises() -> list[dict]:
    if len(EXERCISES) != 20:
        raise ValueError(f"Expected 20 exercises, found {len(EXERCISES)}")
    items = []
    for number, raw in enumerate(EXERCISES, 1):
        item = dict(raw)
        item.setdefault("exerciseNumber", number)
        item.setdefault("id", f"t2-ex{number:02}")
        item.setdefault("section", 5)
        item.setdefault("source", 57)
        item.setdefault("title", f"Provided subnetting exercise {number}")
        item.setdefault("skill", "Apply the reusable subnet worksheet")
        item.setdefault("sourceLabel", "Chapter 8 Subnetting Exercises · Answers Explained")
        item.setdefault("slides", [])
        validate_choices(item["correct"], item["distractors"], f"exercise {number}")
        for key in ["q", "correct", "answer", "teach", "example", "skill"]:
            if not item.get(key):
                raise ValueError(f"Exercise {number} is missing {key}")
        items.append(item)
    if [item["exerciseNumber"] for item in items] != list(range(1, 21)):
        raise ValueError("Exercise numbering is not continuous")
    return items


def main() -> None:
    data = dict(
        title="CIS 320 Test 2 Recall Lab",
        module="Chapters 5–9 and Subnetting",
        sections=SECTIONS,
        questions=normalize_guide(),
        vocab=build_vocab(),
        checks=build_checks(),
        cloze=build_cloze(),
        sorts=build_sorts(),
        exercises=normalize_exercises(),
        connections=CONNECTIONS,
        sources=SOURCES,
        sourceSummary=dict(
            lectureSlides=189,
            guideTopics=57,
            exactExercises=20,
            providedPastedNotes=11,
            uniquePastedNotes=3,
        ),
    )
    ids = []
    for key in ["questions", "vocab", "checks", "cloze", "sorts", "exercises", "connections"]:
        ids.extend(item["id"] for item in data[key])
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate content IDs")
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"Wrote {OUT}: {len(data['questions'])} guide topics, "
        f"{len(data['exercises'])} exact exercises, {len(data['vocab'])} terms, "
        f"{len(data['checks'])} checks, {len(data['cloze'])} blanks, "
        f"and {len(data['sorts'])} sorts."
    )


if __name__ == "__main__":
    main()

