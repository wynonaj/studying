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

- **Learn:** ten-item quick reviews and full-chapter sessions mixing original guide questions, relevant vocabulary and abbreviations, ordering exercises, and highlighted number drills where applicable.
- **Check understanding:** 54 additional applied questions in their own bank, each mapped to an original guide prompt through `sourceId`. These are guide-based practice, not actual or predicted exam questions.
- **Flashcards, Terms & definitions, Abbreviations, Put it in order, Numbers lab, Practice exam, Full study guide:** separate dedicated sections remain available.
- Multiple-choice alternatives are authored for each prompt/term. They are not answers sampled from unrelated questions.
- Missed practice items return after up to three intervening items, with shuffled choices or sorting order. Practice finishes only after every selected item has been answered correctly. Exams retain first-answer scoring.
- Correct and incorrect answers receive spaced explanations; broader vocabulary comparisons are expandable. Layer-job matching is available in Put it in order. No exercise requires a typed answer.

The full guide retains all 54 original prompts. Clarifications correct inconsistencies in the provided notes. The dictionary has 154 terms, including supplemental vocabulary; Learn uses an explicit list of guide-relevant terms. The new understanding bank is excluded from the original-question and exam banks.

## Files and editing

- `dist/index.html`: page shell and script loading.
- `dist/style.css`: responsive styling (Google Fonts with system fallbacks).
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

Progress, XP, and review dates are stored in the current browser under localStorage key `cis320-v1`. Export/import buttons provide a JSON backup. There is no account synchronization or server-side progress database. Changing the site origin uses a different browser storage area; export a backup before moving to a new domain. Retained status estimates practice performance and does not guarantee exam results.
