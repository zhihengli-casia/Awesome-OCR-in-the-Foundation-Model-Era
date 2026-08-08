# Contributing

Repository changes follow the survey taxonomy, source-verification standard, and Markdown conventions below.

## Eligibility and Sources

- Each entry includes at least one primary source: the original paper, official project or benchmark page, official repository, or official model/dataset card.
- Search summaries, unattributed mirrors, placeholder links, and unsupported ranking claims are excluded.
- The task and output contract determine scope. Faithful transcription and source-grounded structural reconstruction belong to OCR or document parsing; semantic interpretation is identified as downstream understanding.
- Existing valid records remain intact unless a primary source establishes a correction, replacement, or duplicate.

## Model or System Records

Required fields comprise the system name, public date or year, F1-F5 family, native input, output contract, and primary source. Code, model cards, documentation, access mode, and parameter scale are recorded when public.

## Benchmark or Dataset Records

Required fields comprise the benchmark name, release date, task layer, input unit, target representation, principal metric, scale when reported, and primary source. Training corpora are distinguished from evaluation sets.

## Style and Validation

- Public prose uses neutral, objective, declarative academic language.
- Dates use arXiv `YYYY.MM` when available; otherwise the official release, challenge, project, or publication year is used.
- Commercial systems remain separate from open models when access mode is reported.
- Markdown tables retain a consistent column count. Contents anchors, relative paths, repeated titles, repeated links, and visibly obsolete links are checked before submission.
- Evaluation claims identify the benchmark, protocol, and source. Unqualified state-of-the-art language is excluded.
