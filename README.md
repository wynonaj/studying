# CIS 320 Recall Lab

A static study app covering Chapters 1, 2, 3, 4, and 12 from the supplied CIS 320 Test 1 guide.

## Run locally

Requires Node.js 20 or newer. There are no npm package dependencies or build step.

```sh
npm start
```

Open `http://127.0.0.1:8765`. You can also serve the app with Python:

```sh
python3 -m http.server 8765 --directory dist
```

Use an HTTP server rather than opening `index.html` directly: the app loads its study material with `fetch('content.json')`. `PORT` and `HOST` may be set for the Node server; the default host is local-only.

## Study modes

- **Learn First:** five-step contextual lessons, plain-language glossary, analogies, worked examples, then practice. Lessons are marked complete after their checkpoint questions are answered correctly.
- **Subnet decoder:** decimal or binary IPv4 input with prefixes /0–/32; clickable network/host bits, live prefix slider, six worked calculation steps, and repeatable randomized practice. /31 and /32 use their special address counts.
- **Practice Quiz:** all existing study sections remain. Optional teaching cards explain the rule before answering. Chapter progress now counts each item answered correctly once, independently of spaced-retention levels and XP.

- **Easy explanations:** 25 chapter reading sections from the added notes (summary checklist excluded), with corrections and 32 separate practice questions. Added-note questions stay outside the original Learn and exam banks. Original guide questions link to relevant reading sections. Wrong-answer feedback starts with a beginner reminder and keeps further detail expandable.

- **Learn:** ten-item quick reviews and full-chapter sessions mixing original guide questions, relevant vocabulary and abbreviations, ordering exercises, and highlighted number drills where applicable.
- **Check understanding:** 54 additional applied questions in their own bank, each mapped to an original guide prompt through `sourceId`. These are guide-based practice, not actual or predicted exam questions.
- **Flashcards, Terms & definitions, Abbreviations, Put it in order, Numbers lab, Practice exam, Full study guide:** separate dedicated sections remain available.
- Multiple-choice alternatives are authored for each prompt/term. They are not answers sampled from unrelated questions.
- Missed practice items return after up to three intervening items, with shuffled choices or sorting order. Practice finishes only after every selected item has been answered correctly. Exams retain first-answer scoring.
- Word-bank abbreviation builders and 25 tap-to-fill sentences supplement the original questions in chapter practice. Abbreviations keeps its original multiple-choice mode alongside word builders and sentence practice.
- All sorting attempts start shuffled, including retries, avoiding the solved order and consecutive identical starting orders where multiple jumbled arrangements exist.
- Correct and incorrect answers receive spaced explanations; broader vocabulary comparisons are expandable. Layer-job matching and a side-by-side OSI/TCP/IP model builder are available in Put it in order. No exercise requires a typed answer.

The full guide retains all 54 original prompts. Clarifications correct inconsistencies in the provided notes. The dictionary has 154 terms, including supplemental vocabulary; Learn uses an explicit list of guide-relevant terms. The new understanding bank is excluded from the original-question and exam banks.

## Files and editing

- `dist/index.html`: page shell and script loading.
- `dist/style.css`: responsive styling (Google Fonts with system fallbacks).
- `dist/teaching.js`: teaching flow, chapter context and jargon translator.
- `dist/subnet.js`: validated subnet calculations, visual decoder and practice generation.
- `dist/app.js`: UI, mixed session selection, ordering/number exercises, grading and progress.
- `dist/vocab.js`: vocabulary and abbreviation definitions.
- `dist/content.json`: original questions, study answers, quiz answers, authored distractors, explanations, and the separate understanding bank.
- `dist/icon.svg`: app icon.
- `.openai/hosting.json`: existing Sites identity and static directory configuration; no secrets.
- `scripts/`: dependency-free local server and deployment archive helper.
- `tests/content.cjs`: study-bank integrity, source mapping and chapter-mixture checks.

`dist` contains the hand-authored source, not disposable generated output. Edit it directly and keep it in Git. The original Word file and temporary content-authoring scripts are not needed to run or deploy this app.

## Verify

```sh
npm run check
npm test
```

Checks validate four unique choices with one correct answer, required explanations, the 54 source mappings, chapter-scoped mixed sessions, separation of question banks, and absence of typed answer fields.

## Deploy

The app is plain static HTML/CSS/JavaScript. Serve the **contents of `dist/`** as the web root on a static host; no backend, API key, runtime package installation or build command is required. Relative asset URLs also support deployment under a subdirectory.

The existing private publication uses Sites. Open this checkout with the Sites integration, reuse the `project_id` in `.openai/hosting.json`, and publish the exact committed source through the Sites workflow. Authentication and publication credentials come from that integration; they are not stored in this repository. Committing to GitHub does not automatically redeploy Sites or enable GitHub Pages.

For a deployment archive containing `dist/` and the Sites manifest:

```sh
npm run package
```

This creates `artifacts/cis320-recall-lab.tar.gz` and requires the standard `tar` command. The host’s upload/deploy step is separate. Sites may generate its own verified archive during publishing.

## Progress

Progress, XP, and review dates are stored in the current browser under localStorage key `cis320-v1`. There is no account synchronization or server-side progress database. Changing the site origin uses a different browser storage area. Retained status estimates practice performance and does not guarantee exam results.

## Vercel publication

The current Vercel deployment is https://studying-gamma.vercel.app/ and uses the GitHub repository `wynonaj/studying`. Publish source changes to `main` with `dist` as the static output directory. The existing Sites manifest is retained for compatibility; Vercel does not require it.

## CIS 304 Module I

The header now switches between CIS 320 (`index.html`) and CIS 304 (`cis304.html`). The new class follows the same visual theme but has its own script, content, activities, and `cis304-module1-v1` browser storage. CIS 320 retains `cis320-v1` unchanged.

CIS 304 includes all **51 original study-guide prompts**, organized into Foundations (10), Business Processes (16), Architecture & Infrastructure (11), and Enterprise Systems (14). Every prompt has a complete answer, three-step teaching flow, concrete example, flashcard, and multiple-choice practice. Additional banks contain 64 terms, 31 focused checks, 11 choice-based cloze cards, 20 abbreviation word banks, and six sorting sequences. The formula lab generates new scenarios and teaches the slide 20 equations: PI/AI, AO/PO, AO/AI. The reading library preserves all 40 assigned/extra links.

- `dist/cis304-content.json`: all authored content and reading/reference links.
- `dist/cis304.js`: lessons, quizzes, retries, exams, flashcards, formula engine, and interactive concept views.
- `dist/classes.css`: class switch and scoped CIS 304 styling.
- `scripts/review/cis304/guide-prompts.json`: exact source prompt checklist.
- `scripts/review/cis304/slides-text.txt`: slide text plus embedded SmartArt text (including formulas).
- `tests/cis304.cjs`: coverage, choice integrity, formulas, retry/scoring, flash flips, rendering, asset hashes, and progress isolation checks.

To regenerate the authored content, run `python3 scripts/review/cis304/build_content.py` followed by `python3 scripts/review/cis304/enrich_content.py`. JSON is fetched without caching. After changing JS or CSS, update the SHA-256 first-12-character version in the HTML pages. `npm test` runs both class suites; `npm run check` checks both class scripts. Static deployment still uses the entire `dist` directory, so both class pages deploy together.

Source notes: questions follow the supplied Fall 2026 study guide, supplemented by the Module I slides and linked references. The EA-properties answer explicitly identifies a synthesis of slides 33–36, because a separate fixed list was not supplied. SOA retains the course’s cloud association while explaining that reusable services need not be cloud-hosted. Linked videos are not represented as verified transcripts. Content is a study aid, not an instructor-issued answer key.

## CIS 464 Project Management

The third class tab opens `cis464.html`, covering Schwalbe Chapters **1, 2, 3, and 10**. Its content and progress are separate from both other classes; storage key: `cis464-chapters-v1`.

Includes 71 three-step lessons with chapter/source labels, 75 vocabulary terms, 30 applied checks, seven cloze checks, seven sorting activities, acronym word banks, flip flashcards, exams, and delayed retries. Interactive views explain project constraints, project/program/portfolio relationships, documents, AI agents, and the stakeholder power–interest grid.

The financial lab teaches PV, NPV, ROI, payback, and weighted scoring. It includes the Chapter 2 slide 28 exercise, slide 29 worked figure, and fresh practice numbers. Timing and discount-factor rounding are explicit; the worked figure's rounded factors reproduce its $272,800 NPV. Financial practice uses its scenario values in saved IDs.

All 183 slides have an entry in the source library, including extracted text, SmartArt text, speaker notes, and supported embedded images. Lessons synthesize the concepts; they are not a claim that each slide is a separate quiz question or that the original PowerPoint layout was reconstructed. Dated forecasts and environmental estimates retain their context. Clarifications link to PMI, Scrum, Agile Manifesto, and IBM sources.

- `dist/cis464-content.json`: authored learning and practice content.
- `dist/cis464-slides.json` and `dist/cis464-media/`: supplied slide reference material.
- `dist/cis464.js`: isolated class UI and activities.
- `scripts/review/cis464/`: extraction and content/app builders.
- `tests/cis464.cjs`: content coverage, 1,500 randomized financial checks, rendering, retries, flashcards, and storage isolation.

Regenerate content with `build_content.py` then `enrich_content.py`; regenerate the UI with `build_app.py` (which reuses the CIS 304 UI structure and replaces class-specific content/activities). Run these with Python from the repository. The extraction script needs the original four decks at their specified Downloads paths; runtime deployment needs only `dist/`. Update HTML asset hashes after changing scripts or styles.

`npm test` and `npm run check` now cover all three classes. Deploy the entire `dist/` directory.
