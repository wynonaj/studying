# Explanation review — 2026-09-24

Reviewed the 54 guide items, 154 vocabulary entries, 54 understanding questions,
44 added-notes/conversion questions, 25 cloze exercises, layer matching,
sorting explanations, static number exercises and generated number feedback.
Retained useful original explanations; this is not a claim that every item needed rewriting.

Changes:
- Authored specific mechanism/example feedback and a distinct memory cue for every vocabulary term.
- Replaced all 32 original added-notes explanations and all 25 cloze explanations.
- Corrected spine–leaf feedback that previously described campus tiers.
- Improved applied-question reasoning and targeted guide explanations for subnet counts,
  registries, campus layers and management information.
- Removed definition-as-explanation and source-question reminder fallbacks. Those could
  repeat the answer or show the original /17 example during a different subnet question.
- Show reasoning directly for either result. Render a memory cue only when it differs
  from both the answer and explanation. Do not repeat identical easy/detail blocks.
- Preserve original questions, options, scoring, retry behavior and saved progress IDs.
- Add unscored reminders after three numeric attempts in practice, and every three
  Address Detective or conversion questions. No interstitials are inserted into exams.

Research links are recorded in content.json feedbackSources. The review used IEEE's
802 overview, IANA number-resource coordination, IETF working-group guidance,
RFC 3416 for SNMP, RFC 4291 for IPv6 compression, RFC 3021 for /31 links, and
Cisco's ACI design guide for the basic leaf-to-spine relationship. Existing Ethernet,
OSI, cabling and optical references remain available elsewhere in the app.

The vocabulary-feedback.txt and cloze-feedback.json files are authored review inputs.
Run python3 scripts/review/apply-feedback-review.py from the project root to apply
these inputs and the question-specific corrections to content.json.

Validation includes full content/regression tests, 300 generated number rounds,
all vocabulary feedback paths (including word banks), duplicate-feedback checks,
spine–leaf and subnet-example regressions, unscored-reminder callbacks and browser
verification of the first reminder appearing after three Address Detective questions.
