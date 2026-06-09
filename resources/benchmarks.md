# Benchmark and Dataset Inventory

OCR benchmarks should not be read as a single leaderboard. Different benchmark families measure different input units, output contracts, metrics, and semantic load.

## Cropped Text Recognition

These benchmarks usually take a cropped word or line image and score the predicted string.

| Benchmark | Typical Input | Output / Metric | Notes |
|---|---|---|---|
| IIIT5K | cropped word | word accuracy / edit distance | classic scene text recognition set |
| SVT | cropped word | word accuracy | street-view text recognition |
| IC13 / IC15 recognition | cropped word | word accuracy | ICDAR recognition subsets |
| SVTP | cropped word | word accuracy | perspective text |
| CUTE80 | cropped word | word accuracy | curved text |
| Union14M-Benchmark | cropped word | accuracy / normalized edit distance | harder modern recognition benchmark |

## Text Detection and Spotting

These benchmarks evaluate localization, detection, multilingual text, curved text, dense text, or end-to-end spotting.

| Benchmark | Typical Input | Output / Metric | Notes |
|---|---|---|---|
| ICDAR 2013 / 2015 | scene image | precision / recall / F1; word accuracy | robust reading series |
| MSRA-TD500 | scene image | text-line detection F1 | multi-oriented long text |
| Total-Text | scene image | polygon detection F1 | curved text |
| CTW1500 | scene image | polygon detection F1 | curved text |
| ICDAR MLT | scene image | multilingual detection / recognition | multilingual robust reading |
| TextOCR | natural image | text recognition / localization | dense text in natural images |
| HierText | natural image | hierarchical text detection / recognition | word-line-paragraph hierarchy |

## Document Structure and Parsing

These benchmarks evaluate page-level or region-level structure, including layout, reading order, tables, and formulas.

| Benchmark | Typical Input | Output / Metric | Notes |
|---|---|---|---|
| PubLayNet | document page | layout detection mAP | scientific document layout |
| DocLayNet | document page | layout detection mAP | diverse document layout |
| DocBank | document page | token-level structure labels | document layout and structure |
| PubTabNet | table crop | HTML tree / TEDS | table structure recognition |
| FinTabNet | table crop | table structure metrics | financial tables |
| TableBank | table image / page | table structure | large table dataset |
| UniMER | formula crop | LaTeX edit distance | mathematical expression recognition |
| HME100K / Im2Markup-style sets | formula image | LaTeX edit distance | handwritten or rendered formula recognition |
| OmniDocBench | PDF / page image | overall and module-level parsing scores | full-page parsing benchmark |
| Real5-OmniDocBench | degraded page image | parsing score and degradation drop | physical capture and degradation robustness |
| MDPBench | document page | multilingual parsing scores | multilingual document parsing |

## Document Understanding and Information Extraction

These benchmarks depend on OCR, but often evaluate semantic extraction or reasoning rather than OCR alone.

| Benchmark | Typical Input | Output / Metric | Notes |
|---|---|---|---|
| FUNSD | form page | entity / relation F1 | noisy scanned forms |
| CORD | receipt image | entity / KIE F1 | receipt understanding |
| SROIE | receipt image | field extraction F1 | receipt OCR and KIE |
| DocVQA | document page + question | ANLS | extractive document QA |
| ChartQA | chart + question | answer accuracy | chart reasoning |
| InfographicVQA | infographic + question | answer accuracy / ANLS | infographic understanding |
| MP-DocVQA | multi-page document + question | ANLS | multi-page document QA |
| DUDE | document + question | document QA metrics | long and diverse document understanding |

## VLM-OCR Benchmarks

These benchmarks evaluate OCR-related abilities through prompting interfaces and are mainly targeted at general-purpose VLMs.

| Benchmark | Typical Input | Output / Metric | Notes |
|---|---|---|---|
| OCRBench | mixed text-rich images | task accuracy / total score | VLM OCR-related tasks |
| OCRBench v2 | mixed text-rich images | scenario scores / total score | expanded VLM OCR evaluation |
| CC-OCR | mixed Chinese-centric images | multi-domain scores | cross-domain OCR literacy |
| OCR-Reasoning | text-rich images | accuracy / reasoning score | text-rich visual reasoning |

