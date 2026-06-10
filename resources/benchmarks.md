# Benchmark and Dataset Inventory

OCR benchmarks should not be read as a single leaderboard. Different benchmark families measure different input units, output contracts, metrics, semantic load, and deployment assumptions. This file keeps a fuller inventory than the front-page README.

## How to Read This Inventory

| Field | Meaning |
|:---:|:---|
| Date | First public release, paper year, or challenge year. |
| Type | Benchmark, training corpus, challenge, or evaluation suite. |
| Input | Word crop, line image, scene image, document page, table crop, formula crop, PDF page, multi-page document, or QA pair. |
| Target / Metric | Typical target representation and common metrics. |
| Notes | Why the dataset matters for OCR or document parsing. |

## Cropped Text Recognition and Handwriting

| Date | Name | Type | Input | Target / Metric | Notes | Links |
|:---:|:---|:---:|:---|:---|:---|:---:|
| 2023 | Union14M / Union14M-Benchmark | training corpus / benchmark | word crops | word accuracy / NED | modern harder recognition pool and benchmark | [Paper](https://arxiv.org/abs/2303.16968) |
| 2015 | ICDAR 2015 Recognition | benchmark | incidental cropped words | word accuracy | blurred / oriented scene text crops | [Website](https://rrc.cvc.uab.es/?ch=4) |
| 2014 | MJSynth / Synth90k | synthetic training data | rendered word crops | training corpus | classic synthetic data for CRNN-era recognition | [Website](https://www.robots.ox.ac.uk/~vgg/data/text/) |
| 2014 | RIMES | handwriting benchmark | French handwriting lines / pages | CER / WER | handwriting recognition and document analysis | [Website](http://www.a2ialab.com/doku.php?id=rimes_database:start) |
| 2013 | ICDAR 2013 Recognition | benchmark | focused scene word crops | word accuracy | clean focused text recognition | [Website](https://rrc.cvc.uab.es/?ch=2) |
| 2011 | IIIT5K | benchmark | cropped word images | word accuracy | classic STR benchmark | [Website](https://cvit.iiit.ac.in/research/projects/cvit-projects/the-iiit-5k-word-dataset) |
| 2011 | SVT | benchmark | street-view word crops | word accuracy | Google Street View text recognition | [Website](http://www.iapr-tc11.org/mediawiki/index.php/The_Street_View_Text_Dataset) |
| 2011 | SVTP | benchmark | perspective word crops | word accuracy | perspective-distorted cropped words | [Website](http://www.iapr-tc11.org/mediawiki/index.php/SVTP_Dataset) |
| 2011 | CUTE80 | benchmark | curved word crops | word accuracy | curved cropped text | [Website](http://cs-chan.com/downloads_CUTE80_dataset.html) |
| 2002 | IAM | handwriting benchmark | handwritten words / lines | CER / WER | classic offline handwriting recognition benchmark | [Website](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database) |
| 1999 | MNIST | controlled recognition benchmark | digit images | accuracy | controlled character recognition baseline | [Website](http://yann.lecun.com/exdb/mnist/) |
| 1995 | NIST SD19 | handwriting dataset | handwritten digits / characters | accuracy | large handwritten character corpus | [Website](https://www.nist.gov/srd/nist-special-database-19) |
| 1994 | CEDAR | handwriting dataset | words / addresses | recognition metrics | classic postal/address OCR data | [Website](https://cedar.buffalo.edu/Databases/) |
| 1987 | USPS | controlled recognition benchmark | digit images | accuracy | postal digit recognition baseline | [Website](https://www.kaggle.com/datasets/bistaumanga/usps-dataset) |

## Scene Text Detection, Recognition, and Spotting

| Date | Name | Type | Input | Target / Metric | Notes | Links |
|:---:|:---|:---:|:---|:---|:---|:---:|
| 2022 | HierText | benchmark | natural images | word / line / paragraph hierarchy | dense hierarchical text detection and recognition | [Paper](https://arxiv.org/abs/2203.15143), [GitHub](https://github.com/google-research-datasets/hiertext) |
| 2021 | TextOCR | benchmark | natural images | text boxes and transcriptions | dense text in everyday images | [Website](https://textvqa.org/textocr/) |
| 2019 | ReCTS | benchmark | Chinese signboards | detection / recognition / end-to-end | Chinese scene text reading | [Website](https://rrc.cvc.uab.es/?ch=12) |
| 2019 | LSVT | benchmark | large-scale street-view Chinese text | detection / recognition / spotting | large-scale Chinese scene text | [Website](https://rrc.cvc.uab.es/?ch=16) |
| 2019 | ArT | benchmark | arbitrary-shape scene text | polygon detection / spotting | arbitrary-shape text benchmark | [Website](https://rrc.cvc.uab.es/?ch=14) |
| 2017 | ICDAR 2017 MLT | benchmark | multilingual scene images | detection / recognition | multilingual robust reading | [Website](https://rrc.cvc.uab.es/?ch=8) |
| 2017 | CTW1500 | benchmark | curved text-line images | polygon F1 | curved long text lines | [GitHub](https://github.com/Yuliang-Liu/Curve-Text-Detector) |
| 2017 | Total-Text | benchmark | curved / horizontal scene text | polygon detection / spotting | curved text benchmark | [GitHub](https://github.com/cs-chan/Total-Text-Dataset) |
| 2016 | SynthText | synthetic training data | text pasted into natural images | detection / recognition training | classic scene-text synthetic data | [Website](https://www.robots.ox.ac.uk/~vgg/data/scenetext/) |
| 2016 | COCO-Text | benchmark | MS-COCO images with text | detection / recognition | natural image text benchmark | [Website](https://bgshih.github.io/cocotext/) |
| 2015 | ICDAR 2015 Incidental Text | benchmark | camera-captured scene images | detection / spotting Hmean | incidental blurred / oriented text | [Website](https://rrc.cvc.uab.es/?ch=4) |
| 2013 | ICDAR 2013 Robust Reading | benchmark | focused scene images | detection / recognition | focused scene text baseline | [Website](https://rrc.cvc.uab.es/?ch=2) |
| 2012 | MSRA-TD500 | benchmark | scene images with long text lines | text-line detection F1 | multi-oriented long text lines | [GitHub](https://github.com/ut-text-detection/UTD-Text-Detection) |
| 2011 | ICDAR 2011 Robust Reading | benchmark | scene images | detection / recognition | early scene text benchmark | [Website](https://rrc.cvc.uab.es/?ch=1) |
| 2003 | ICDAR 2003 Robust Reading | benchmark | scene images | detection / recognition | early robust reading task | [Website](https://rrc.cvc.uab.es/) |

## Document Layout, Forms, KIE, and Receipts

| Date | Name | Type | Input | Target / Metric | Notes | Links |
|:---:|:---|:---:|:---|:---|:---|:---:|
| 2024 | DocStructBench | benchmark | document pages | fine-grained structure detection | fine-grained document structure | [Paper](https://arxiv.org/abs/2406.10021) |
| 2022 | DocLayNet | benchmark | diverse document pages | layout mAP | 11-class layout detection across document types | [Paper](https://arxiv.org/abs/2206.01062), [HF](https://huggingface.co/datasets/ds4sd/DocLayNet) |
| 2022 | XFUND | multilingual form benchmark | form pages | entity / relation F1 | multilingual form understanding | [Paper](https://arxiv.org/abs/2104.08836), [GitHub](https://github.com/doc-analysis/XFUND) |
| 2021 | Kleister-NDA / Kleister-Charity | KIE benchmark | long business documents | key-value extraction F1 | long document key information extraction | [Paper](https://arxiv.org/abs/2103.10213) |
| 2020 | DocBank | layout / token benchmark | PDF pages | token-level structure labels | large-scale token-level document layout labels | [Paper](https://arxiv.org/abs/2006.01038) |
| 2019 | PubLayNet | layout benchmark | scientific document pages | layout mAP | large document layout benchmark | [Paper](https://arxiv.org/abs/1908.07836) |
| 2019 | SROIE | receipt benchmark | receipt images | OCR + field extraction F1 | receipt information extraction challenge | [Website](https://rrc.cvc.uab.es/?ch=13) |
| 2019 | CORD | receipt KIE benchmark | receipt images | semantic field extraction F1 | receipt understanding | [GitHub](https://github.com/clovaai/cord) |
| 2019 | FUNSD | form understanding benchmark | scanned forms | entity / relation F1 | noisy form understanding | [Website](https://guillaumejaume.github.io/FUNSD/) |
| 2013 | PRImA Layout | layout benchmark | scanned document pages | layout segmentation | early document layout analysis | [Website](https://www.primaresearch.org/dataset/) |

## Tables, Formulas, and Structured Objects

| Date | Name | Type | Input | Target / Metric | Notes | Links |
|:---:|:---|:---:|:---|:---|:---|:---:|
| 2024 | UniMER-1M | formula dataset | formula images | LaTeX edit distance | large-scale formula recognition data | [Paper](https://arxiv.org/abs/2404.15254), [GitHub](https://github.com/opendatalab/UniMERNet) |
| 2021 | PubTables-1M | table benchmark | PDF tables | AP / GriTS / cell structure | large table detection and structure benchmark | [Paper](https://arxiv.org/abs/2110.00061), [GitHub](https://github.com/microsoft/table-transformer) |
| 2021 | WTW | table benchmark | wild tables | table detection / structure | natural-scene and document tables | [GitHub](https://github.com/wangwen-whu/WTW-Dataset) |
| 2020 | FinTabNet | table benchmark | financial report tables | TEDS / structure | complex financial tables | [Website](https://developer.ibm.com/exchanges/data/all/fintabnet/) |
| 2020 | PubTabNet | table benchmark | table images | HTML / TEDS | table image-to-HTML benchmark | [Paper](https://arxiv.org/abs/1911.10683) |
| 2020 | HME100K | formula benchmark | handwritten formula images | LaTeX / expression rate | handwritten mathematical expression recognition | [GitHub](https://github.com/HCIILAB/HME100K-Dataset) |
| 2019 | SciTSR | table benchmark | scientific tables | cell structure F1 | scientific table structure recognition | [Paper](https://arxiv.org/abs/1908.04729) |
| 2019 | TableBank | table benchmark | Word / LaTeX document tables | detection / structure | large table dataset from office and LaTeX documents | [Paper](https://arxiv.org/abs/1903.01949) |
| 2016 | Im2LaTeX-100K | formula dataset | rendered formulas | LaTeX edit distance | image-to-markup formula generation | [Paper](https://arxiv.org/abs/1609.04938) |
| 2014- | CROHME | formula competition | handwritten math expressions | expression recognition rate | handwriting math expression recognition | [Website](https://www.isical.ac.in/~crohme/) |

## Document QA, Chart QA, and OCR-Dependent Understanding

| Date | Name | Type | Input | Target / Metric | Notes | Links |
|:---:|:---|:---:|:---|:---|:---|:---:|
| 2024 | MMLongBench-Doc | benchmark | long documents + questions | answer accuracy / LLM judging | long document VQA / reasoning | [Paper](https://arxiv.org/abs/2407.01523) |
| 2023 | DUDE | document QA benchmark | diverse documents + questions | ANLS / accuracy | diverse document understanding | [Paper](https://arxiv.org/abs/2305.14828) |
| 2023 | MP-DocVQA | multi-page document QA | multi-page documents + questions | ANLS | multi-page document question answering | [Website](https://rrc.cvc.uab.es/?ch=17) |
| 2022 | ChartQA | chart QA benchmark | chart images + questions | relaxed accuracy | visual and logical chart reasoning | [Paper](https://arxiv.org/abs/2203.10244), [GitHub](https://github.com/vis-nlp/ChartQA) |
| 2021 | InfographicVQA | infographic QA benchmark | infographics + questions | ANLS / accuracy | infographic document understanding | [Paper](https://arxiv.org/abs/2104.12756), [Website](https://www.docvqa.org/datasets/infographicvqa) |
| 2020 | DocVQA | document QA benchmark | document image + question | ANLS | classic document visual question answering | [Paper](https://arxiv.org/abs/2007.00398), [Website](https://www.docvqa.org/) |
| 2019 | TextVQA | text-rich VQA benchmark | natural images + questions | VQA accuracy | natural-image QA requiring OCR | [Paper](https://arxiv.org/abs/1904.08920), [Website](https://textvqa.org/) |
| 2019 | ST-VQA | scene-text VQA benchmark | text-rich images + questions | ANLS | scene text visual question answering | [Website](https://rrc.cvc.uab.es/?ch=11) |
| 2018 | FigureQA | chart / figure QA | synthetic figures + questions | accuracy | synthetic chart and figure reasoning | [Paper](https://arxiv.org/abs/1710.07300) |
| 2019 | PlotQA | plot QA benchmark | chart images + questions | accuracy | chart reasoning benchmark | [Paper](https://arxiv.org/abs/1909.00997) |

## Page-Level Parsing and VLM-OCR Evaluation

| Date | Name | Type | Input | Target / Metric | Notes | Links |
|:---:|:---|:---:|:---|:---|:---|:---:|
| 2026 | RealDocBench | real-world parsing benchmark | degraded real documents | parsing robustness | real degraded document parsing | [Paper](https://arxiv.org/abs/2606.07401) |
| 2026 | MPDocBench-Parse | multi-page parsing benchmark | multi-page documents | structured output / consistency | multi-page parsing stress test | [Paper](https://arxiv.org/abs/2605.22100) |
| 2026 | PureDocBench | page parsing benchmark | page images | structure / layout parsing | structural parsing without semantic shortcuts | [Paper](https://arxiv.org/abs/2605.07492) |
| 2026 | CC-OCR v2 | VLM-OCR benchmark | multi-domain text-rich images | OCR capability and reasoning scores | expanded CC-OCR evaluation | [Paper](https://arxiv.org/abs/2605.03903) |
| 2025 | DocPTBench | photographed document parsing | photographed documents | parsing robustness | perspective / lighting / capture degradation | [Paper](https://arxiv.org/abs/2512.15872), [GitHub](https://github.com/Topdu/DocPTBench) |
| 2025 | Real5-OmniDocBench | real-world parsing benchmark | degraded page images | parse score / degradation drop | real degradation robustness for document parsers | [Paper](https://arxiv.org/abs/2508.11236), [HF](https://huggingface.co/datasets/PaddlePaddle/Real5-OmniDocBench) |
| 2025 | OCR-Reasoning | reasoning-heavy OCR benchmark | text-rich images + questions | OCR reasoning accuracy | OCR-centered multimodal reasoning benchmark | [Paper](https://arxiv.org/abs/2505.17163), [GitHub](https://github.com/SCUT-DLVCLab/OCR-Reasoning), [Project](https://ocr-reasoning.github.io/) |
| 2025 | Reasoning-OCR | reasoning-oriented OCR benchmark | text-rich images + reasoning tasks | answer accuracy | OCR reasoning evaluation | [Paper](https://arxiv.org/abs/2505.12766) |
| 2025 | MDPBench | multilingual parsing benchmark | multilingual documents | multilingual parse scores | multilingual document parsing evaluation | [Paper](https://arxiv.org/abs/2505.05438) |
| 2025 | KITAB-Bench | multilingual OCR / document benchmark | Arabic text-rich documents | OCR and document understanding scores | Arabic-centric OCR and document understanding | [Paper](https://arxiv.org/abs/2502.14949) |
| 2025 | olmOCR-Bench | document OCR benchmark | PDF pages | OCR / Markdown quality | document OCR evaluation accompanying olmOCR | [Paper](https://arxiv.org/abs/2502.18411) |
| 2025 | OCRBench v2 | VLM-OCR benchmark | mixed text-rich images | scenario scores / total score | expanded VLM OCR capability evaluation | [Paper](https://arxiv.org/abs/2501.00321) |
| 2024 | OmniDocBench | page-level parsing benchmark | PDF / page images | text / layout / table / formula parse scores | widely used full-page parsing benchmark | [Paper](https://arxiv.org/abs/2412.07626), [GitHub](https://github.com/opendatalab/OmniDocBench) |
| 2024 | CC-OCR | VLM-OCR benchmark | cross-domain text-rich images | OCR literacy scores | Chinese-centric and cross-domain OCR evaluation | [Paper](https://arxiv.org/abs/2412.02210) |
| 2023 | OCRBench | VLM-OCR benchmark | mixed text-rich images | task accuracy / total score | early OCR-oriented MLLM benchmark | [Paper](https://arxiv.org/abs/2305.07895), [GitHub](https://github.com/Yuliang-Liu/MultimodalOCR) |

## Training Corpora and Synthetic Data

| Date | Name | Type | Input | Target / Metric | Notes | Links |
|:---:|:---|:---:|:---|:---|:---|:---:|
| 2023 | Union14M | training corpus | word crops | recognition training | unified large-scale STR training data | [Paper](https://arxiv.org/abs/2303.16968) |
| 2022 | SynthDoG | synthetic document generator | document pages | document images / labels | synthetic data for Donut-style document understanding | [GitHub](https://github.com/clovaai/donut) |
| 2021 | SynthTIGER | synthetic text image generator | cropped and scene text | detection / recognition training | configurable text-image generation | [GitHub](https://github.com/clovaai/synthtiger) |
| 2016 | SynthText | synthetic scene text | natural images with rendered text | detection / recognition labels | detection and spotting pretraining | [Website](https://www.robots.ox.ac.uk/~vgg/data/scenetext/) |
| 2014 | MJSynth / Synth90k | synthetic word crops | rendered words | text labels | recognition pretraining | [Website](https://www.robots.ox.ac.uk/~vgg/data/text/) |

## Adjacent but Useful Evaluation Resources

| Date | Name | Type | Input | Target / Metric | Notes | Links |
|:---:|:---|:---:|:---|:---|:---|:---:|
| 2024 | Needle-in-a-Document / long-document QA suites | stress tests | long PDFs / docs + questions | answer accuracy | useful for downstream document intelligence, not OCR itself | [MMLongBench-Doc](https://arxiv.org/abs/2407.01523) |
| 2023 | MMMU / multimodal exam benchmarks | VLM benchmark | images + questions | accuracy | may contain text-rich questions but mixes OCR with reasoning | [Paper](https://arxiv.org/abs/2311.16502) |
| 2023 | MathVista | VLM benchmark | math diagrams + questions | accuracy | formula/chart-heavy reasoning, not a pure OCR benchmark | [Paper](https://arxiv.org/abs/2310.02255) |
