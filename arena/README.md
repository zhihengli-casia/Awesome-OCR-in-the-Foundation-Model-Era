# Cross-Era OCR Arena

OCR systems from different eras do not share a single input-output contract. A cropped recognizer, a detector-recognizer toolkit, a document parser, a general VLM, and a commercial API require separate evaluation tracks rather than one undifferentiated OCR score.

## Evaluation Tracks

| Track | Capability Layer | Data Sources | Input Unit | Target Representation | Core Metrics | Families |
|---|---|---|---|---|---|---|
| A | Cropped recognition | IIIT5K, SVT, IC13/15, SVTP, CUTE80, Union14M hard cases | word / line crop | string | word accuracy, CER, NED | F1, F4 |
| B | Page-level parsing | OmniDocBench clean subsets | page image | Markdown / structured page | text, layout, table, formula, reading-order scores | F1-F5 |
| C | Structured objects | PubTabNet, FinTabNet, OmniDocBench tables, UniMER, formula sets | table / formula region | HTML / LaTeX | TEDS, cell F1, formula edit distance | F1-F5 |
| D | Robustness | Real5-OmniDocBench and controlled degradations | degraded page image | structured page | clean score, degraded score, score drop | F1-F5 |
| E | Efficiency and failure audit | shared Track B/C samples | page or region | model output + audit labels | s/page, peak memory, API cost, invalid output rate, error-type counts | F1-F5 |

## Reporting Schema

Result tables report numeric values rather than text-only labels.

Required fields: family, model, version, parameters or access mode, track scores, robustness drop, runtime, peak memory, API cost, invalid-output rate, and notes.

## Configuration Fields

Each experiment records:

- model version and checkpoint;
- inference resolution or page tiling policy;
- prompt or task token, if applicable;
- decoding settings;
- post-processing and output normalization;
- hardware and runtime environment;
- API date and endpoint version for closed models.
