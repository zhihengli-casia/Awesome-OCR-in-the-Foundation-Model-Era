# Awesome OCR in the Foundation-Model Era

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/github/stars/zhihengli-casia/Awesome-OCR-in-the-Foundation-Model-Era?style=social)](https://github.com/zhihengli-casia/Awesome-OCR-in-the-Foundation-Model-Era)
[![Last Commit](https://img.shields.io/github/last-commit/zhihengli-casia/Awesome-OCR-in-the-Foundation-Model-Era?style=flat-square&color=blue)](https://github.com/zhihengli-casia/Awesome-OCR-in-the-Foundation-Model-Era/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A curated list of OCR, document parsing, OCR-specialized vision-language models, hybrid document parsing workflows, commercial OCR services, and benchmarks.

This repository accompanies the survey:

> **OCR in the Foundation Model Era: A Survey**  
> Zhiheng Li et al., in preparation, 2026.

OCR is treated here in a broad but bounded sense: visual text and document images are converted into machine-readable text or structured document representations. Downstream tasks such as document QA, information extraction, RAG, and agent workflows are included only when they shape OCR system design or evaluation.

## Contents

- [F1. Modular OCR Toolkits and Specialized Components](#f1-modular-ocr-toolkits-and-specialized-components)
- [F2. Foundation-Model Document Parsers](#f2-foundation-model-document-parsers)
- [F3. Hybrid Document Parsing Workflows](#f3-hybrid-document-parsing-workflows)
- [F4. General-Purpose VLMs Used as OCR Interfaces](#f4-general-purpose-vlms-used-as-ocr-interfaces)
- [F5. Commercial OCR and Document AI Services](#f5-commercial-ocr-and-document-ai-services)
- [Benchmarks](resources/benchmarks.md)
- [Cross-era OCR Arena](arena/README.md)

## Model Collections

<a id="f1-modular-ocr-toolkits-and-specialized-components"></a>

## F1. Modular OCR Toolkits and Specialized Components

<details open>
<summary><strong>Show / hide F1 collection</strong></summary>

Systems that follow or support the detector-recognizer pipeline: OCR engines, open toolkits, text detectors, cropped recognizers, formula recognizers, and structured-object components.

### OCR Engines and Toolkits

| Title | Task / Tags | Links |
|:---:|:---:|:---:|
| [![ICDAR 2007](https://img.shields.io/badge/ICDAR-2007-4b4b4b)](https://doi.org/10.1109/ICDAR.2007.4376991) [![GitHub stars](https://img.shields.io/github/stars/tesseract-ocr/tesseract?style=social)](https://github.com/tesseract-ocr/tesseract)<br>**Tesseract** | OCR engine; open-source OCR | [Paper](https://doi.org/10.1109/ICDAR.2007.4376991)<br>[GitHub](https://github.com/tesseract-ocr/tesseract)<br>[Docs](https://tesseract-ocr.github.io/) |
| [![GitHub release](https://img.shields.io/badge/GitHub-release-24292f?logo=github)](https://github.com/JaidedAI/EasyOCR) [![GitHub stars](https://img.shields.io/github/stars/JaidedAI/EasyOCR?style=social)](https://github.com/JaidedAI/EasyOCR)<br>**EasyOCR** | ready-to-use OCR engine; multilingual OCR | [GitHub](https://github.com/JaidedAI/EasyOCR) |
| [![arXiv 2020.09](https://img.shields.io/badge/arXiv-2020.09-b31b1b)](https://arxiv.org/abs/2009.09941) [![GitHub stars](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR?style=social)](https://github.com/PaddlePaddle/PaddleOCR)<br>**PaddleOCR / PP-OCR** | industrial OCR toolkit; PP-OCR series | [Paper](https://arxiv.org/abs/2009.09941)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR)<br>[Docs](https://paddlepaddle.github.io/PaddleOCR/) |
| [![arXiv 2021.08](https://img.shields.io/badge/arXiv-2021.08-b31b1b)](https://arxiv.org/abs/2108.06543) [![GitHub stars](https://img.shields.io/github/stars/open-mmlab/mmocr?style=social)](https://github.com/open-mmlab/mmocr)<br>**MMOCR** | OCR research toolbox; detection/recognition/spotting | [Paper](https://arxiv.org/abs/2108.06543)<br>[GitHub](https://github.com/open-mmlab/mmocr)<br>[Docs](https://mmocr.readthedocs.io/) |
| [![GitHub release](https://img.shields.io/badge/GitHub-release-24292f?logo=github)](https://github.com/mindee/doctr) [![GitHub stars](https://img.shields.io/github/stars/mindee/doctr?style=social)](https://github.com/mindee/doctr)<br>**docTR** | document OCR toolkit; detection + recognition | [GitHub](https://github.com/mindee/doctr)<br>[Docs](https://mindee.github.io/doctr/) |

### Text Detection and Spotting Components

| Title | Task / Tags | Links |
|:---:|:---:|:---:|
| [![CVPR 2017](https://img.shields.io/badge/CVPR-2017-4b4b4b)](https://arxiv.org/abs/1704.03155)<br>**EAST** | text detection; dense prediction | [Paper](https://arxiv.org/abs/1704.03155) |
| [![CVPR 2019](https://img.shields.io/badge/CVPR-2019-4b4b4b)](https://arxiv.org/abs/1904.01941) [![GitHub stars](https://img.shields.io/github/stars/clovaai/CRAFT-pytorch?style=social)](https://github.com/clovaai/CRAFT-pytorch)<br>**CRAFT** | character-region text detection | [Paper](https://arxiv.org/abs/1904.01941)<br>[GitHub](https://github.com/clovaai/CRAFT-pytorch) |
| [![CVPR 2019](https://img.shields.io/badge/CVPR-2019-4b4b4b)](https://arxiv.org/abs/1806.02559) [![GitHub stars](https://img.shields.io/github/stars/whai362/PSENet?style=social)](https://github.com/whai362/PSENet)<br>**PSENet** | arbitrary-shape text detection | [Paper](https://arxiv.org/abs/1806.02559)<br>[GitHub](https://github.com/whai362/PSENet) |
| [![AAAI 2020](https://img.shields.io/badge/AAAI-2020-4b4b4b)](https://doi.org/10.1609/aaai.v34i07.6812) [![GitHub stars](https://img.shields.io/github/stars/MhLiao/DB?style=social)](https://github.com/MhLiao/DB)<br>**DBNet** | differentiable-binarization text detection | [Paper](https://doi.org/10.1609/aaai.v34i07.6812)<br>[GitHub](https://github.com/MhLiao/DB) |
| [![TPAMI 2023](https://img.shields.io/badge/TPAMI-2023-4b4b4b)](https://doi.org/10.1109/TPAMI.2022.3155612) [![GitHub stars](https://img.shields.io/github/stars/MhLiao/DB?style=social)](https://github.com/MhLiao/DB)<br>**DBNet++** | adaptive-scale DB text detection | [Paper](https://doi.org/10.1109/TPAMI.2022.3155612)<br>[GitHub](https://github.com/MhLiao/DB) |
| [![CVPR 2021](https://img.shields.io/badge/CVPR-2021-4b4b4b)](https://arxiv.org/abs/2104.10442)<br>**FCENet** | Fourier-contour text detection | [Paper](https://arxiv.org/abs/2104.10442) |

### Cropped Text Recognizers

| Title | Task / Tags | Links |
|:---:|:---:|:---:|
| [![TPAMI 2017](https://img.shields.io/badge/TPAMI-2017-4b4b4b)](https://doi.org/10.1109/TPAMI.2016.2646371) [![GitHub stars](https://img.shields.io/github/stars/meijieru/crnn.pytorch?style=social)](https://github.com/meijieru/crnn.pytorch)<br>**CRNN** | cropped sequence recognition; CTC | [Paper](https://doi.org/10.1109/TPAMI.2016.2646371)<br>[GitHub](https://github.com/meijieru/crnn.pytorch) |
| [![TPAMI 2019](https://img.shields.io/badge/TPAMI-2019-4b4b4b)](https://doi.org/10.1109/TPAMI.2018.2848939) [![GitHub stars](https://img.shields.io/github/stars/bgshih/aster?style=social)](https://github.com/bgshih/aster)<br>**ASTER** | rectified irregular text recognition | [Paper](https://doi.org/10.1109/TPAMI.2018.2848939)<br>[GitHub](https://github.com/bgshih/aster) |
| [![CVPR 2020](https://img.shields.io/badge/CVPR-2020-4b4b4b)](https://arxiv.org/abs/2003.12294)<br>**SRN** | semantic reasoning recognizer | [Paper](https://arxiv.org/abs/2003.12294) |
| [![CVPR 2021](https://img.shields.io/badge/CVPR-2021-4b4b4b)](https://arxiv.org/abs/2103.06495)<br>**ABINet** | language-aware recognizer | [Paper](https://arxiv.org/abs/2103.06495) |
| [![ICDAR 2021](https://img.shields.io/badge/ICDAR-2021-4b4b4b)](https://arxiv.org/abs/2105.08582) [![GitHub stars](https://img.shields.io/github/stars/roatienza/deep-text-recognition-benchmark?style=social)](https://github.com/roatienza/deep-text-recognition-benchmark)<br>**ViTSTR** | ViT recognizer | [Paper](https://arxiv.org/abs/2105.08582)<br>[GitHub](https://github.com/roatienza/deep-text-recognition-benchmark) |
| [![ECCV 2022](https://img.shields.io/badge/ECCV-2022-4b4b4b)](https://arxiv.org/abs/2207.06966) [![GitHub stars](https://img.shields.io/github/stars/baudm/parseq?style=social)](https://github.com/baudm/parseq)<br>**PARSeq** | permuted autoregressive recognizer | [Paper](https://arxiv.org/abs/2207.06966)<br>[GitHub](https://github.com/baudm/parseq) |
| [![IJCAI 2022](https://img.shields.io/badge/IJCAI-2022-4b4b4b)](https://doi.org/10.24963/ijcai.2022/124) [![GitHub stars](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR?style=social)](https://github.com/PaddlePaddle/PaddleOCR)<br>**SVTR** | efficient single-visual-model recognizer | [Paper](https://doi.org/10.24963/ijcai.2022/124)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| [![arXiv 2024.11](https://img.shields.io/badge/arXiv-2024.11-b31b1b)](https://arxiv.org/abs/2411.15858) [![GitHub stars](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR?style=social)](https://github.com/PaddlePaddle/PaddleOCR)<br>**SVTRv2** | upgraded cropped recognizer | [Paper](https://arxiv.org/abs/2411.15858)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| [![AAAI 2023](https://img.shields.io/badge/AAAI-2023-4b4b4b)](https://arxiv.org/abs/2109.10282)<br>**TrOCR** | pretrained encoder-decoder recognizer | [Paper](https://arxiv.org/abs/2109.10282)<br>[HF Docs](https://huggingface.co/docs/transformers/model_doc/trocr) |

### Formula, Table, and Structured-Object Components

| Title | Task / Tags | Links |
|:---:|:---:|:---:|
| [![arXiv 2024.04](https://img.shields.io/badge/arXiv-2024.04-b31b1b)](https://arxiv.org/abs/2404.15254) [![GitHub stars](https://img.shields.io/github/stars/opendatalab/UniMERNet?style=social)](https://github.com/opendatalab/UniMERNet)<br>**UniMERNet** | formula recognition; LaTeX output | [Paper](https://arxiv.org/abs/2404.15254)<br>[GitHub](https://github.com/opendatalab/UniMERNet) |
| [![arXiv 2025.03](https://img.shields.io/badge/arXiv-2025.03-b31b1b)](https://arxiv.org/abs/2503.18382) [![GitHub stars](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR?style=social)](https://github.com/PaddlePaddle/PaddleOCR)<br>**PP-FormulaNet** | formula recognition; PaddleOCR component | [Paper](https://arxiv.org/abs/2503.18382)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| [![GitHub release](https://img.shields.io/badge/GitHub-release-24292f?logo=github)](https://github.com/AlibabaResearch/AdvancedLiterateMachinery) [![GitHub stars](https://img.shields.io/github/stars/AlibabaResearch/AdvancedLiterateMachinery?style=social)](https://github.com/AlibabaResearch/AdvancedLiterateMachinery)<br>**StructEqTable** | equation/table structure parsing | [GitHub](https://github.com/AlibabaResearch/AdvancedLiterateMachinery) |

</details>

<a id="f2-foundation-model-document-parsers"></a>

## F2. Foundation-Model Document Parsers

<details open>
<summary><strong>Show / hide F2 collection</strong></summary>

End-to-end or near end-to-end models that read page images and generate structured representations such as Markdown, HTML, LaTeX, JSON, or OCR-formatted text.

### OCR-Free and Transitional Encoder-Decoders

| Title | Task / Tags | Links |
|:---:|:---:|:---:|
| [![ECCV 2022](https://img.shields.io/badge/ECCV-2022-4b4b4b)](https://arxiv.org/abs/2111.15664) [![GitHub stars](https://img.shields.io/github/stars/clovaai/donut?style=social)](https://github.com/clovaai/donut)<br>**Donut** | OCR-free encoder-decoder; document understanding | [Paper](https://arxiv.org/abs/2111.15664)<br>[GitHub](https://github.com/clovaai/donut) |
| [![ICML 2023](https://img.shields.io/badge/ICML-2023-4b4b4b)](https://arxiv.org/abs/2210.03347) [![GitHub stars](https://img.shields.io/github/stars/google-research/pix2struct?style=social)](https://github.com/google-research/pix2struct)<br>**Pix2Struct** | screenshot/page-to-sequence pretraining | [Paper](https://arxiv.org/abs/2210.03347)<br>[GitHub](https://github.com/google-research/pix2struct) |
| [![arXiv 2023.08](https://img.shields.io/badge/arXiv-2023.08-b31b1b)](https://arxiv.org/abs/2308.13418) [![GitHub stars](https://img.shields.io/github/stars/facebookresearch/nougat?style=social)](https://github.com/facebookresearch/nougat)<br>**Nougat** | scholarly PDF-to-Markdown parser | [Paper](https://arxiv.org/abs/2308.13418)<br>[GitHub](https://github.com/facebookresearch/nougat) |

### Early Document VLMs

| Title | Task / Tags | Links |
|:---:|:---:|:---:|
| [![arXiv 2023.07](https://img.shields.io/badge/arXiv-2023.07-b31b1b)](https://arxiv.org/abs/2307.02499) [![GitHub stars](https://img.shields.io/github/stars/X-PLUG/mPLUG-DocOwl?style=social)](https://github.com/X-PLUG/mPLUG-DocOwl)<br>**DocOwl** | document-oriented VLM | [Paper](https://arxiv.org/abs/2307.02499)<br>[GitHub](https://github.com/X-PLUG/mPLUG-DocOwl) |
| [![arXiv 2024.03](https://img.shields.io/badge/arXiv-2024.03-b31b1b)](https://arxiv.org/abs/2403.12895) [![GitHub stars](https://img.shields.io/github/stars/X-PLUG/mPLUG-DocOwl?style=social)](https://github.com/X-PLUG/mPLUG-DocOwl)<br>**DocOwl 1.5** | OCR-free structure learning | [Paper](https://arxiv.org/abs/2403.12895)<br>[GitHub](https://github.com/X-PLUG/mPLUG-DocOwl) |
| [![arXiv 2024.09](https://img.shields.io/badge/arXiv-2024.09-b31b1b)](https://arxiv.org/abs/2409.03420) [![GitHub stars](https://img.shields.io/github/stars/X-PLUG/mPLUG-DocOwl?style=social)](https://github.com/X-PLUG/mPLUG-DocOwl)<br>**DocOwl 2** | high-resolution multi-page document VLM | [Paper](https://arxiv.org/abs/2409.03420)<br>[GitHub](https://github.com/X-PLUG/mPLUG-DocOwl) |
| [![arXiv 2023.12](https://img.shields.io/badge/arXiv-2023.12-b31b1b)](https://arxiv.org/abs/2312.06109) [![GitHub stars](https://img.shields.io/github/stars/Ucas-HaoranWei/Vary?style=social)](https://github.com/Ucas-HaoranWei/Vary)<br>**Vary** | document-specialized VLM | [Paper](https://arxiv.org/abs/2312.06109)<br>[GitHub](https://github.com/Ucas-HaoranWei/Vary) |
| [![arXiv 2024.09](https://img.shields.io/badge/arXiv-2024.09-b31b1b)](https://arxiv.org/abs/2409.01704) [![GitHub stars](https://img.shields.io/github/stars/Ucas-HaoranWei/GOT-OCR2.0?style=social)](https://github.com/Ucas-HaoranWei/GOT-OCR2.0)<br>**GOT-OCR 2.0** | unified OCR-specialized VLM | [Paper](https://arxiv.org/abs/2409.01704)<br>[GitHub](https://github.com/Ucas-HaoranWei/GOT-OCR2.0) |
| [![CVPR 2024](https://img.shields.io/badge/CVPR-2024-4b4b4b)](https://arxiv.org/abs/2311.06607) [![GitHub stars](https://img.shields.io/github/stars/Yuliang-Liu/Monkey?style=social)](https://github.com/Yuliang-Liu/Monkey)<br>**Monkey** | text-centric MLLM | [Paper](https://arxiv.org/abs/2311.06607)<br>[GitHub](https://github.com/Yuliang-Liu/Monkey) |
| [![arXiv 2024.03](https://img.shields.io/badge/arXiv-2024.03-b31b1b)](https://arxiv.org/abs/2403.04473) [![GitHub stars](https://img.shields.io/github/stars/Yuliang-Liu/Monkey?style=social)](https://github.com/Yuliang-Liu/Monkey)<br>**TextMonkey** | OCR-free document MLLM | [Paper](https://arxiv.org/abs/2403.04473)<br>[GitHub](https://github.com/Yuliang-Liu/Monkey) |
| [![arXiv 2023.10](https://img.shields.io/badge/arXiv-2023.10-b31b1b)](https://arxiv.org/abs/2310.05126)<br>**UReader** | OCR-free visually situated language understanding | [Paper](https://arxiv.org/abs/2310.05126) |
| [![arXiv 2024.04](https://img.shields.io/badge/arXiv-2024.04-b31b1b)](https://arxiv.org/abs/2404.09204)<br>**TextHawk** | fine-grained text perception in MLLMs | [Paper](https://arxiv.org/abs/2404.09204)<br>[Hugging Face](https://huggingface.co/TencentBAC) |
| [![arXiv 2024.05](https://img.shields.io/badge/arXiv-2024.05-b31b1b)](https://arxiv.org/abs/2405.14295) [![GitHub stars](https://img.shields.io/github/stars/ucaslcl/Fox?style=social)](https://github.com/ucaslcl/Fox)<br>**Fox** | multi-page document understanding system | [Paper](https://arxiv.org/abs/2405.14295)<br>[GitHub](https://github.com/ucaslcl/Fox) |

### 2025-2026 OCR-Specialized Parsers

| Title | Task / Tags | Links |
|:---:|:---:|:---:|
| [![arXiv 2025.03](https://img.shields.io/badge/arXiv-2025.03-b31b1b)](https://arxiv.org/abs/2503.11576)<br>**SmolDocling** | ultra-compact document conversion VLM | [Paper](https://arxiv.org/abs/2503.11576)<br>[Hugging Face](https://huggingface.co/ds4sd/SmolDocling-256M-preview) |
| [![arXiv 2025.06](https://img.shields.io/badge/arXiv-2025.06-b31b1b)](https://arxiv.org/abs/2506.05218) [![GitHub stars](https://img.shields.io/github/stars/Yuliang-Liu/MonkeyOCR?style=social)](https://github.com/Yuliang-Liu/MonkeyOCR)<br>**MonkeyOCR** | structure-recognition-relation document parser | [Paper](https://arxiv.org/abs/2506.05218)<br>[GitHub](https://github.com/Yuliang-Liu/MonkeyOCR) |
| [![GitHub release](https://img.shields.io/badge/GitHub-release-24292f?logo=github)](https://github.com/deepseek-ai/DeepSeek-OCR) [![GitHub stars](https://img.shields.io/github/stars/deepseek-ai/DeepSeek-OCR?style=social)](https://github.com/deepseek-ai/DeepSeek-OCR)<br>**DeepSeek-OCR** | visual token compression for OCR | [GitHub](https://github.com/deepseek-ai/DeepSeek-OCR) |
| [![arXiv 2025.11](https://img.shields.io/badge/arXiv-2025.11-b31b1b)](https://arxiv.org/abs/2511.19575)<br>**HunyuanOCR** | OCR-specialized document VLM | [Paper](https://arxiv.org/abs/2511.19575) |
| [![arXiv 2025.12](https://img.shields.io/badge/arXiv-2025.12-b31b1b)](https://arxiv.org/abs/2512.02498)<br>**dots.ocr** | multilingual document layout parsing VLM | [Paper](https://arxiv.org/abs/2512.02498) |
| [![arXiv 2025.10](https://img.shields.io/badge/arXiv-2025.10-b31b1b)](https://arxiv.org/abs/2510.19817) [![GitHub stars](https://img.shields.io/github/stars/allenai/olmocr?style=social)](https://github.com/allenai/olmocr)<br>**olmOCR-2** | unit-test reward training for document OCR | [Paper](https://arxiv.org/abs/2510.19817)<br>[GitHub](https://github.com/allenai/olmocr) |
| [![arXiv 2026.01](https://img.shields.io/badge/arXiv-2026.01-b31b1b)](https://arxiv.org/abs/2601.21957) [![GitHub stars](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR?style=social)](https://github.com/PaddlePaddle/PaddleOCR)<br>**PaddleOCR-VL-1.5** | compact multi-task document parsing VLM | [Paper](https://arxiv.org/abs/2601.21957)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| [![arXiv 2026.03](https://img.shields.io/badge/arXiv-2026.03-b31b1b)](https://arxiv.org/abs/2603.10910)<br>**GLM-OCR** | OCR-specialized document parser | [Paper](https://arxiv.org/abs/2603.10910) |
| [![arXiv 2026.03](https://img.shields.io/badge/arXiv-2026.03-b31b1b)](https://arxiv.org/abs/2603.13398)<br>**Qianfan-OCR** | end-to-end document intelligence model | [Paper](https://arxiv.org/abs/2603.13398)<br>[Website](https://cloud.baidu.com/product/wenxinworkshop) |
| [![arXiv 2026.03](https://img.shields.io/badge/arXiv-2026.03-b31b1b)](https://arxiv.org/abs/2603.01840) [![GitHub stars](https://img.shields.io/github/stars/FireRedTeam/FireRed-OCR?style=social)](https://github.com/FireRedTeam/FireRed-OCR)<br>**FireRed-OCR** | OCR-specialized VLM | [Paper](https://arxiv.org/abs/2603.01840)<br>[GitHub](https://github.com/FireRedTeam/FireRed-OCR) |

### Emerging Generation and Training Routes

| Title | Task / Tags | Links |
|:---:|:---:|:---:|
| [![arXiv 2026.01](https://img.shields.io/badge/arXiv-2026.01-b31b1b)](https://arxiv.org/abs/2601.08834)<br>**FDRL for Document OCR** | format-decoupled reinforcement learning | [Paper](https://arxiv.org/abs/2601.08834) |
| [![arXiv 2026.03](https://img.shields.io/badge/arXiv-2026.03-b31b1b)](https://arxiv.org/abs/2603.22458)<br>**MinerU-Diffusion** | diffusion-style inverse-rendering OCR | [Paper](https://arxiv.org/abs/2603.22458) |

</details>

<a id="f3-hybrid-document-parsing-workflows"></a>

## F3. Hybrid Document Parsing Workflows

<details open>
<summary><strong>Show / hide F3 collection</strong></summary>

Systems that combine layout detection, OCR, region decomposition, VLM generation, rule-based validators, and document assembly.

### Full Document Parsing Workflows

| Title | Task / Tags | Links |
|:---:|:---:|:---:|
| [![GitHub release](https://img.shields.io/badge/GitHub-release-24292f?logo=github)](https://github.com/opendatalab/MinerU) [![GitHub stars](https://img.shields.io/github/stars/opendatalab/MinerU?style=social)](https://github.com/opendatalab/MinerU)<br>**MinerU** | layout decomposition + document parsing workflow | [GitHub](https://github.com/opendatalab/MinerU) |
| [![arXiv 2026.04](https://img.shields.io/badge/arXiv-2026.04-b31b1b)](https://arxiv.org/abs/2604.04771) [![GitHub stars](https://img.shields.io/github/stars/opendatalab/MinerU?style=social)](https://github.com/opendatalab/MinerU)<br>**MinerU2.5-Pro** | data-centric document parsing system | [Paper](https://arxiv.org/abs/2604.04771)<br>[GitHub](https://github.com/opendatalab/MinerU) |
| [![arXiv 2026.02](https://img.shields.io/badge/arXiv-2026.02-b31b1b)](https://arxiv.org/abs/2602.05384) [![GitHub stars](https://img.shields.io/github/stars/bytedance/Dolphin?style=social)](https://github.com/bytedance/Dolphin)<br>**Dolphin-v2** | anchor prompting + document parsing workflow | [Paper](https://arxiv.org/abs/2602.05384)<br>[GitHub](https://github.com/bytedance/Dolphin) |
| [![arXiv 2024.08](https://img.shields.io/badge/arXiv-2024.08-b31b1b)](https://arxiv.org/abs/2408.09869) [![GitHub stars](https://img.shields.io/github/stars/docling-project/docling?style=social)](https://github.com/docling-project/docling)<br>**Docling** | production document conversion workflow | [Paper](https://arxiv.org/abs/2408.09869)<br>[GitHub](https://github.com/docling-project/docling)<br>[Docs](https://docling-project.github.io/docling/) |

### PDF-to-Structured-Output Workflows

| Title | Task / Tags | Links |
|:---:|:---:|:---:|
| [![GitHub release](https://img.shields.io/badge/GitHub-release-24292f?logo=github)](https://github.com/datalab-to/marker) [![GitHub stars](https://img.shields.io/github/stars/datalab-to/marker?style=social)](https://github.com/datalab-to/marker)<br>**Marker** | PDF-to-Markdown workflow | [GitHub](https://github.com/datalab-to/marker) |
| [![GitHub release](https://img.shields.io/badge/GitHub-release-24292f?logo=github)](https://github.com/datalab-to/surya) [![GitHub stars](https://img.shields.io/github/stars/datalab-to/surya?style=social)](https://github.com/datalab-to/surya)<br>**Surya** | OCR, layout, reading order, line detection | [GitHub](https://github.com/datalab-to/surya) |
| [![GitHub release](https://img.shields.io/badge/GitHub-release-24292f?logo=github)](https://github.com/breezedeus/Pix2Text) [![GitHub stars](https://img.shields.io/github/stars/breezedeus/Pix2Text?style=social)](https://github.com/breezedeus/Pix2Text)<br>**Pix2Text** | layout + formula + OCR workflow | [GitHub](https://github.com/breezedeus/Pix2Text) |

</details>

<a id="f4-general-purpose-vlms-used-as-ocr-interfaces"></a>

## F4. General-Purpose VLMs Used as OCR Interfaces

<details open>
<summary><strong>Show / hide F4 collection</strong></summary>

General multimodal models that can perform OCR-related tasks through prompts, while OCR is only one part of their capability.

### Open General VLMs

| Title | Task / Tags | Links |
|:---:|:---:|:---:|
| [![arXiv 2023.08](https://img.shields.io/badge/arXiv-2023.08-b31b1b)](https://arxiv.org/abs/2308.12966) [![GitHub stars](https://img.shields.io/github/stars/QwenLM/Qwen-VL?style=social)](https://github.com/QwenLM/Qwen-VL)<br>**Qwen-VL** | visual text reading; grounding; document QA | [Paper](https://arxiv.org/abs/2308.12966)<br>[GitHub](https://github.com/QwenLM/Qwen-VL) |
| [![arXiv 2024.09](https://img.shields.io/badge/arXiv-2024.09-b31b1b)](https://arxiv.org/abs/2409.12191) [![GitHub stars](https://img.shields.io/github/stars/QwenLM/Qwen2-VL?style=social)](https://github.com/QwenLM/Qwen2-VL)<br>**Qwen2-VL** | dynamic-resolution VLM with OCR ability | [Paper](https://arxiv.org/abs/2409.12191)<br>[GitHub](https://github.com/QwenLM/Qwen2-VL) |
| [![arXiv 2025.02](https://img.shields.io/badge/arXiv-2025.02-b31b1b)](https://arxiv.org/abs/2502.13923) [![GitHub stars](https://img.shields.io/github/stars/QwenLM/Qwen2.5-VL?style=social)](https://github.com/QwenLM/Qwen2.5-VL)<br>**Qwen2.5-VL** | general VLM OCR and document prompting | [Paper](https://arxiv.org/abs/2502.13923)<br>[GitHub](https://github.com/QwenLM/Qwen2.5-VL)<br>[Demo](https://chat.qwen.ai/) |
| [![CVPR 2024](https://img.shields.io/badge/CVPR-2024-4b4b4b)](https://arxiv.org/abs/2312.14238) [![GitHub stars](https://img.shields.io/github/stars/OpenGVLab/InternVL?style=social)](https://github.com/OpenGVLab/InternVL)<br>**InternVL** | open general VLM baseline | [Paper](https://arxiv.org/abs/2312.14238)<br>[GitHub](https://github.com/OpenGVLab/InternVL)<br>[Demo](https://chat.intern-ai.org.cn/) |
| [![arXiv 2024.04](https://img.shields.io/badge/arXiv-2024.04-b31b1b)](https://arxiv.org/abs/2404.16821) [![GitHub stars](https://img.shields.io/github/stars/OpenGVLab/InternVL?style=social)](https://github.com/OpenGVLab/InternVL)<br>**InternVL 1.5** | open general VLM suite | [Paper](https://arxiv.org/abs/2404.16821)<br>[GitHub](https://github.com/OpenGVLab/InternVL)<br>[Demo](https://chat.intern-ai.org.cn/) |
| [![arXiv 2025.04](https://img.shields.io/badge/arXiv-2025.04-b31b1b)](https://arxiv.org/abs/2504.10479) [![GitHub stars](https://img.shields.io/github/stars/OpenGVLab/InternVL?style=social)](https://github.com/OpenGVLab/InternVL)<br>**InternVL3** | open general VLM OCR baseline | [Paper](https://arxiv.org/abs/2504.10479)<br>[GitHub](https://github.com/OpenGVLab/InternVL)<br>[Demo](https://chat.intern-ai.org.cn/) |
| [![NeurIPS 2024](https://img.shields.io/badge/NeurIPS-2024-4b4b4b)](https://arxiv.org/abs/2304.08485) [![GitHub stars](https://img.shields.io/github/stars/haotian-liu/LLaVA?style=social)](https://github.com/haotian-liu/LLaVA)<br>**LLaVA** | visual instruction tuning baseline | [Paper](https://arxiv.org/abs/2304.08485)<br>[GitHub](https://github.com/haotian-liu/LLaVA) |
| [![ICLR 2024](https://img.shields.io/badge/ICLR-2024-4b4b4b)](https://arxiv.org/abs/2311.03079) [![GitHub stars](https://img.shields.io/github/stars/THUDM/CogVLM?style=social)](https://github.com/THUDM/CogVLM)<br>**CogVLM** | visual expert for language models | [Paper](https://arxiv.org/abs/2311.03079)<br>[GitHub](https://github.com/THUDM/CogVLM) |
| [![arXiv 2024.03](https://img.shields.io/badge/arXiv-2024.03-b31b1b)](https://arxiv.org/abs/2403.05525) [![GitHub stars](https://img.shields.io/github/stars/deepseek-ai/DeepSeek-VL?style=social)](https://github.com/deepseek-ai/DeepSeek-VL)<br>**DeepSeek-VL** | general VLM baseline for text-rich images | [Paper](https://arxiv.org/abs/2403.05525)<br>[GitHub](https://github.com/deepseek-ai/DeepSeek-VL) |
| [![arXiv 2024.08](https://img.shields.io/badge/arXiv-2024.08-b31b1b)](https://arxiv.org/abs/2408.01800) [![GitHub stars](https://img.shields.io/github/stars/OpenBMB/MiniCPM-o?style=social)](https://github.com/OpenBMB/MiniCPM-o)<br>**MiniCPM-V** | mobile-scale general MLLM with OCR ability | [Paper](https://arxiv.org/abs/2408.01800)<br>[GitHub](https://github.com/OpenBMB/MiniCPM-o)<br>[Demo](https://minicpm-omni.openbmb.cn/) |
| [![arXiv 2023.11](https://img.shields.io/badge/arXiv-2023.11-b31b1b)](https://arxiv.org/abs/2311.06242)<br>**Florence-2** | fixed-token general vision foundation model | [Paper](https://arxiv.org/abs/2311.06242)<br>[Hugging Face](https://huggingface.co/microsoft/Florence-2-large) |
| [![arXiv 2025.04](https://img.shields.io/badge/arXiv-2025.04-b31b1b)](https://arxiv.org/abs/2504.07491)<br>**Kimi-VL** | general VLM OCR and document prompting | [Paper](https://arxiv.org/abs/2504.07491) |

### Closed/API General VLMs

| Title | Task / Tags | Links |
|:---:|:---:|:---:|
| [![System Card 2023](https://img.shields.io/badge/System%20Card-2023-6f42c1)](https://cdn.openai.com/papers/GPTV_System_Card.pdf)<br>**GPT-4V** | closed general VLM OCR interface | [System Card](https://cdn.openai.com/papers/GPTV_System_Card.pdf)<br>[Docs](https://platform.openai.com/docs) |
| [![API 2024](https://img.shields.io/badge/API-2024-6f42c1)](https://platform.openai.com/docs)<br>**GPT-4o** | closed general VLM OCR interface | [Docs](https://platform.openai.com/docs) |
| [![Report 2023.12](https://img.shields.io/badge/Report-2023.12-6f42c1)](https://arxiv.org/abs/2312.11805)<br>**Gemini family** | closed general VLM OCR interface | [Report](https://arxiv.org/abs/2312.11805)<br>[Docs](https://ai.google.dev/gemini-api/docs) |
| [![API 2024-2025](https://img.shields.io/badge/API-2024--2025-6f42c1)](https://docs.anthropic.com/)<br>**Claude 3 / 3.5 / 4** | closed general VLM OCR interface | [Docs](https://docs.anthropic.com/) |

</details>

<a id="f5-commercial-ocr-and-document-ai-services"></a>

## F5. Commercial OCR and Document AI Services

<details open>
<summary><strong>Show / hide F5 collection</strong></summary>

Closed-source or managed systems for document conversion, enterprise OCR, scientific document parsing, formula OCR, receipts, forms, invoices, and other vertical workflows.

### Enterprise OCR and Document AI

| Title | Task / Tags | Links |
|:---:|:---:|:---:|
| [![Product line 1993-](https://img.shields.io/badge/Product%20line-1993--6f42c1)](https://www.abbyy.com/finereader/)<br>**ABBYY FineReader / ABBYY Vantage** | commercial OCR; on-prem / SDK / cloud; searchable PDF / fields | [FineReader](https://www.abbyy.com/finereader/)<br>[Vantage](https://www.abbyy.com/vantage/) |
| [![Product docs 2025](https://img.shields.io/badge/Product%20docs-2025-6f42c1)](https://www.textin.com/)<br>**TextIn** | document / receipt / form parsing; JSON / Markdown / fields | [Website](https://www.textin.com/) |

### Scientific OCR and Managed Parsing APIs

| Title | Task / Tags | Links |
|:---:|:---:|:---:|
| [![Product docs 2026](https://img.shields.io/badge/Product%20docs-2026-6f42c1)](https://mathpix.com/)<br>**Mathpix** | formula / paper / document OCR; LaTeX / Markdown | [Website](https://mathpix.com/) |
| [![Product docs 2025](https://img.shields.io/badge/Product%20docs-2025-6f42c1)](https://docs.mistral.ai/capabilities/document_ai/basic_ocr/)<br>**Mistral OCR** | managed OCR API; Markdown / structured response | [Docs](https://docs.mistral.ai/capabilities/document_ai/basic_ocr/) |
| [![Product docs 2025](https://img.shields.io/badge/Product%20docs-2025-6f42c1)](https://help.aliyun.com/zh/model-studio/)<br>**Qwen-OCR API** | managed OCR API; structured OCR output | [Docs](https://help.aliyun.com/zh/model-studio/) |

</details>

## Other Resource Files

- `resources/models.md`: standalone expandable model collections for longer maintenance notes.
- `resources/benchmarks.md`: OCR, document parsing, document understanding, and VLM-OCR benchmarks.
- `arena/README.md`: proposed cross-era evaluation tracks and result-table schema.

## Update Policy

This list prioritizes resources that are useful for a full-history OCR survey:

- historically important OCR methods and benchmarks;
- modern OCR-specialized VLMs and document parsers;
- general VLMs frequently used as OCR interfaces;
- industrial or commercial services with public documentation;
- datasets and benchmarks that define evaluation protocols.

Pull requests should include a stable project page, model card, paper, documentation page, or benchmark page.

## Citation

If this repository or the survey helps your work, please cite the survey once the public version is available.

```bibtex
@article{li2026ocrfoundation,
  title   = {OCR in the Foundation Model Era: A Survey},
  author  = {Li, Zhiheng and Ma, Zongyang and Chen, Jiaxian and Cui, Cheng and Liu, Yi and Zhang, Ziqi and Li, Bing and Hu, Weiming and Yuan, Chunfeng},
  journal = {arXiv preprint},
  year    = {2026}
}
```
