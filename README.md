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

### F1. Modular OCR Toolkits and Specialized Components

<details open>
<summary><strong>Show / hide F1 collection</strong></summary>

Systems that follow or support the detector-recognizer pipeline: OCR engines, open toolkits, text detectors, cropped recognizers, formula recognizers, and structured-object components.

### OCR Engines and Toolkits

| Model / System | Date | Venue / Source | Role | Paper / Project | Code / Stars | Docs / Model |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Tesseract** | 2007 | ICDAR 2007 | OCR engine | [Paper](https://doi.org/10.1109/ICDAR.2007.4376991) | [GitHub 74.6k](https://github.com/tesseract-ocr/tesseract) | [Docs](https://tesseract-ocr.github.io/) |
| **EasyOCR** | 2020 | GitHub release | ready-to-use OCR engine | [GitHub 29.6k project](https://github.com/JaidedAI/EasyOCR) | [GitHub 29.6k](https://github.com/JaidedAI/EasyOCR) | - |
| **PaddleOCR / PP-OCR** | 2020.09 | arXiv / industrial toolkit | OCR toolkit and PP-OCR series | [Paper](https://arxiv.org/abs/2009.09941) | [GitHub 81.5k](https://github.com/PaddlePaddle/PaddleOCR) | [Docs](https://paddlepaddle.github.io/PaddleOCR/) |
| **MMOCR** | 2021.08 | arXiv toolbox paper | OCR research toolkit | [Paper](https://arxiv.org/abs/2108.06543) | [GitHub 4.7k](https://github.com/open-mmlab/mmocr) | [Docs](https://mmocr.readthedocs.io/) |
| **docTR** | 2021 | GitHub / documentation | document OCR toolkit | [GitHub 6.1k project](https://github.com/mindee/doctr) | [GitHub 6.1k](https://github.com/mindee/doctr) | [Docs](https://mindee.github.io/doctr/) |

### Text Detection and Spotting Components

| Model / System | Date | Venue / Source | Role | Paper / Project | Code / Stars | Docs / Model |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **EAST** | 2017 | CVPR 2017 | text detection | [Paper](https://arxiv.org/abs/1704.03155) | - | - |
| **CRAFT** | 2019 | CVPR 2019 | character-region text detection | [Paper](https://arxiv.org/abs/1904.01941) | [GitHub 3.4k](https://github.com/clovaai/CRAFT-pytorch) | - |
| **PSENet** | 2019 | CVPR 2019 | arbitrary-shape text detection | [Paper](https://arxiv.org/abs/1806.02559) | [GitHub 1.2k](https://github.com/whai362/PSENet) | - |
| **DBNet** | 2020 | AAAI 2020 | differentiable-binarization detection | [Paper](https://doi.org/10.1609/aaai.v34i07.6812) | [GitHub 2.3k](https://github.com/MhLiao/DB) | - |
| **DBNet++** | 2023 | TPAMI 2023 | adaptive-scale DB text detection | [Paper](https://doi.org/10.1109/TPAMI.2022.3155612) | [GitHub 2.3k](https://github.com/MhLiao/DB) | - |
| **FCENet** | 2021 | CVPR 2021 | Fourier-contour text detection | [Paper](https://arxiv.org/abs/2104.10442) | - | - |

### Cropped Text Recognizers

| Model / System | Date | Venue / Source | Role | Paper / Project | Code / Stars | Docs / Model |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **CRNN** | 2017 | TPAMI 2017 | cropped sequence recognition | [Paper](https://doi.org/10.1109/TPAMI.2016.2646371) | [GitHub 2.5k](https://github.com/meijieru/crnn.pytorch) | - |
| **ASTER** | 2019 | TPAMI 2019 | rectified irregular text recognition | [Paper](https://doi.org/10.1109/TPAMI.2018.2848939) | [GitHub 742](https://github.com/bgshih/aster) | - |
| **SRN** | 2020 | CVPR 2020 | semantic reasoning recognizer | [Paper](https://arxiv.org/abs/2003.12294) | - | - |
| **ABINet** | 2021 | CVPR 2021 | language-aware recognizer | [Paper](https://arxiv.org/abs/2103.06495) | - | - |
| **ViTSTR** | 2021 | ICDAR 2021 | ViT recognizer | [Paper](https://arxiv.org/abs/2105.08582) | [GitHub 313](https://github.com/roatienza/deep-text-recognition-benchmark) | - |
| **PARSeq** | 2022 | ECCV 2022 | permuted autoregressive recognizer | [Paper](https://arxiv.org/abs/2207.06966) | [GitHub 721](https://github.com/baudm/parseq) | - |
| **SVTR** | 2022 | IJCAI 2022 | efficient single-visual-model recognizer | [Paper](https://doi.org/10.24963/ijcai.2022/124) | [GitHub 81.5k](https://github.com/PaddlePaddle/PaddleOCR) | - |
| **SVTRv2** | 2024.11 | arXiv preprint | upgraded cropped recognizer | [Paper](https://arxiv.org/abs/2411.15858) | [GitHub 81.5k](https://github.com/PaddlePaddle/PaddleOCR) | - |
| **TrOCR** | 2021.09 / 2023 | arXiv / AAAI 2023 | pretrained encoder-decoder recognizer | [Paper](https://arxiv.org/abs/2109.10282) | - | [HF Docs](https://huggingface.co/docs/transformers/model_doc/trocr) |

### Formula, Table, and Structured-Object Components

| Model / System | Date | Venue / Source | Role | Paper / Project | Code / Stars | Docs / Model |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **UniMERNet** | 2024.04 | arXiv preprint | formula recognition | [Paper](https://arxiv.org/abs/2404.15254) | [GitHub 482](https://github.com/opendatalab/UniMERNet) | - |
| **PP-FormulaNet** | 2025.03 | arXiv preprint | formula recognition | [Paper](https://arxiv.org/abs/2503.18382) | [GitHub 81.5k](https://github.com/PaddlePaddle/PaddleOCR) | - |
| **StructEqTable** | 2025 | project release | equation/table structure parsing | [GitHub 1.8k project](https://github.com/AlibabaResearch/AdvancedLiterateMachinery) | [GitHub 1.8k](https://github.com/AlibabaResearch/AdvancedLiterateMachinery) | - |

</details>

<a id="f2-foundation-model-document-parsers"></a>

### F2. Foundation-Model Document Parsers

<details open>
<summary><strong>Show / hide F2 collection</strong></summary>

End-to-end or near end-to-end models that read page images and generate structured representations such as Markdown, HTML, LaTeX, JSON, or OCR-formatted text.

### OCR-Free and Transitional Encoder-Decoders

| Model / System | Date | Venue / Source | Route | Paper / Project | Code / Stars | Docs / Model |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Donut** | 2022 | ECCV 2022 | OCR-free encoder-decoder | [Paper](https://arxiv.org/abs/2111.15664) | [GitHub 6.9k](https://github.com/clovaai/donut) | - |
| **Pix2Struct** | 2023 | ICML 2023 | screenshot/page-to-sequence pretraining | [Paper](https://arxiv.org/abs/2210.03347) | [GitHub 684](https://github.com/google-research/pix2struct) | - |
| **Nougat** | 2023.08 | arXiv preprint | scholarly PDF-to-Markdown parser | [Paper](https://arxiv.org/abs/2308.13418) | [GitHub 10.0k](https://github.com/facebookresearch/nougat) | - |

### Early Document VLMs

| Model / System | Date | Venue / Source | Route | Paper / Project | Code / Stars | Docs / Model |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **DocOwl** | 2023.07 | arXiv preprint | document-oriented VLM | [Paper](https://arxiv.org/abs/2307.02499) | [GitHub 2.4k](https://github.com/X-PLUG/mPLUG-DocOwl) | - |
| **DocOwl 1.5** | 2024.03 | arXiv preprint | OCR-free structure learning | [Paper](https://arxiv.org/abs/2403.12895) | [GitHub 2.4k](https://github.com/X-PLUG/mPLUG-DocOwl) | - |
| **DocOwl 2** | 2024.09 | arXiv preprint | high-resolution multi-page document VLM | [Paper](https://arxiv.org/abs/2409.03420) | [GitHub 2.4k](https://github.com/X-PLUG/mPLUG-DocOwl) | - |
| **Vary** | 2023.12 | arXiv preprint | document-specialized VLM | [Paper](https://arxiv.org/abs/2312.06109) | [GitHub 1.9k](https://github.com/Ucas-HaoranWei/Vary) | - |
| **GOT-OCR 2.0** | 2024.09 | arXiv preprint | unified OCR-specialized VLM | [Paper](https://arxiv.org/abs/2409.01704) | [GitHub 8.1k](https://github.com/Ucas-HaoranWei/GOT-OCR2.0) | - |
| **Monkey** | 2024 | CVPR 2024 | text-centric MLLM | [Paper](https://arxiv.org/abs/2311.06607) | [GitHub 1.9k](https://github.com/Yuliang-Liu/Monkey) | - |
| **TextMonkey** | 2024.03 | arXiv preprint | OCR-free document MLLM | [Paper](https://arxiv.org/abs/2403.04473) | [GitHub 1.9k](https://github.com/Yuliang-Liu/Monkey) | - |
| **UReader** | 2023.10 | arXiv preprint | OCR-free visually situated language understanding | [Paper](https://arxiv.org/abs/2310.05126) | - | - |
| **TextHawk** | 2024.04 | arXiv preprint | fine-grained text perception in MLLMs | [Paper](https://arxiv.org/abs/2404.09204) | - | [Hugging Face](https://huggingface.co/TencentBAC) |
| **Fox** | 2024.05 | arXiv preprint | multi-page document understanding system | [Paper](https://arxiv.org/abs/2405.14295) | [GitHub 195](https://github.com/ucaslcl/Fox) | - |

### 2025-2026 OCR-Specialized Parsers

| Model / System | Date | Venue / Source | Route | Paper / Project | Code / Stars | Docs / Model |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **SmolDocling** | 2025.03 | arXiv preprint | ultra-compact document conversion VLM | [Paper](https://arxiv.org/abs/2503.11576) | - | [Hugging Face](https://huggingface.co/ds4sd/SmolDocling-256M-preview) |
| **MonkeyOCR** | 2025.06 | arXiv preprint | structure-recognition-relation document parser | [Paper](https://arxiv.org/abs/2506.05218) | [GitHub 6.6k](https://github.com/Yuliang-Liu/MonkeyOCR) | - |
| **DeepSeek-OCR** | 2025 | GitHub / model release | visual token compression for OCR | [GitHub 23.3k project](https://github.com/deepseek-ai/DeepSeek-OCR) | [GitHub 23.3k](https://github.com/deepseek-ai/DeepSeek-OCR) | - |
| **HunyuanOCR** | 2025.11 | arXiv technical report | OCR-specialized document VLM | [Paper](https://arxiv.org/abs/2511.19575) | - | - |
| **dots.ocr** | 2025.12 | arXiv preprint | multilingual document layout parsing VLM | [Paper](https://arxiv.org/abs/2512.02498) | - | - |
| **olmOCR-2** | 2025.10 | arXiv preprint | unit-test reward training for document OCR | [Paper](https://arxiv.org/abs/2510.19817) | [GitHub 17.4k](https://github.com/allenai/olmocr) | - |
| **PaddleOCR-VL-1.5** | 2026.01 | arXiv technical report | compact multi-task document parsing VLM | [Paper](https://arxiv.org/abs/2601.21957) | [GitHub 81.5k](https://github.com/PaddlePaddle/PaddleOCR) | - |
| **GLM-OCR** | 2026.03 | arXiv technical report | OCR-specialized document parser | [Paper](https://arxiv.org/abs/2603.10910) | - | - |
| **Qianfan-OCR** | 2026.03 | arXiv technical report | end-to-end document intelligence model | [Paper](https://arxiv.org/abs/2603.13398) | - | [Website](https://cloud.baidu.com/product/wenxinworkshop) |
| **FireRed-OCR** | 2026.03 | arXiv technical report | OCR-specialized VLM | [Paper](https://arxiv.org/abs/2603.01840) | [GitHub 280](https://github.com/FireRedTeam/FireRed-OCR) | - |

### Emerging Generation and Training Routes

| Model / System | Date | Venue / Source | Route | Paper / Project | Code / Stars | Docs / Model |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **FDRL for Document OCR** | 2026.01 | arXiv preprint | format-decoupled reinforcement learning | [Paper](https://arxiv.org/abs/2601.08834) | - | - |
| **MinerU-Diffusion** | 2026.03 | arXiv preprint | diffusion-style inverse-rendering OCR | [Paper](https://arxiv.org/abs/2603.22458) | - | - |

</details>

<a id="f3-hybrid-document-parsing-workflows"></a>

### F3. Hybrid Document Parsing Workflows

<details open>
<summary><strong>Show / hide F3 collection</strong></summary>

Systems that combine layout detection, OCR, region decomposition, VLM generation, rule-based validators, and document assembly.

### Full Document Parsing Workflows

| Model / System | Date | Venue / Source | Route | Paper / Project | Code / Stars | Docs / Model |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **MinerU** | 2025 | GitHub / OpenDataLab release | layout decomposition + document parsing workflow | [GitHub 66.9k project](https://github.com/opendatalab/MinerU) | [GitHub 66.9k](https://github.com/opendatalab/MinerU) | - |
| **MinerU2.5-Pro** | 2026.04 | arXiv preprint | data-centric document parsing system | [Paper](https://arxiv.org/abs/2604.04771) | [GitHub 66.9k](https://github.com/opendatalab/MinerU) | - |
| **Dolphin-v2** | 2026.02 | arXiv preprint | anchor prompting + document parsing workflow | [Paper](https://arxiv.org/abs/2602.05384) | [GitHub 9.0k](https://github.com/bytedance/Dolphin) | - |
| **Docling** | 2024.08 | arXiv technical report | production document conversion workflow | [Paper](https://arxiv.org/abs/2408.09869) | [GitHub 61.2k](https://github.com/docling-project/docling) | [Docs](https://docling-project.github.io/docling/) |

### PDF-to-Structured-Output Workflows

| Model / System | Date | Venue / Source | Route | Paper / Project | Code / Stars | Docs / Model |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Marker** | 2023 | GitHub release | PDF-to-Markdown workflow | [GitHub 35.9k project](https://github.com/datalab-to/marker) | [GitHub 35.9k](https://github.com/datalab-to/marker) | - |
| **Surya** | 2024 | GitHub release | OCR, layout, reading order, line detection | [GitHub 20.7k project](https://github.com/datalab-to/surya) | [GitHub 20.7k](https://github.com/datalab-to/surya) | - |
| **Pix2Text** | 2024 | GitHub release | layout + formula + OCR workflow | [GitHub 3.1k project](https://github.com/breezedeus/Pix2Text) | [GitHub 3.1k](https://github.com/breezedeus/Pix2Text) | - |

</details>

<a id="f4-general-purpose-vlms-used-as-ocr-interfaces"></a>

### F4. General-Purpose VLMs Used as OCR Interfaces

<details open>
<summary><strong>Show / hide F4 collection</strong></summary>

General multimodal models that can perform OCR-related tasks through prompts, while OCR is only one part of their capability.

### Open General VLMs

| Model / System | Date | Venue / Source | OCR-Relevant Role | Paper / Project | Code / Stars | Demo / Docs |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Qwen-VL** | 2023.08 | arXiv technical report | visual text reading, grounding, document QA | [Paper](https://arxiv.org/abs/2308.12966) | [GitHub 6.7k](https://github.com/QwenLM/Qwen-VL) | - |
| **Qwen2-VL** | 2024.09 | arXiv technical report | dynamic-resolution VLM with OCR ability | [Paper](https://arxiv.org/abs/2409.12191) | [GitHub 19.3k](https://github.com/QwenLM/Qwen2-VL) | - |
| **Qwen2.5-VL** | 2025.02 | arXiv technical report | general VLM OCR and document prompting | [Paper](https://arxiv.org/abs/2502.13923) | [GitHub 19.3k](https://github.com/QwenLM/Qwen2.5-VL) | [Demo](https://chat.qwen.ai/) |
| **InternVL** | 2024 | CVPR 2024 | open general VLM baseline | [Paper](https://arxiv.org/abs/2312.14238) | [GitHub 10.1k](https://github.com/OpenGVLab/InternVL) | [Demo](https://chat.intern-ai.org.cn/) |
| **InternVL 1.5** | 2024.04 | arXiv preprint | open general VLM suite | [Paper](https://arxiv.org/abs/2404.16821) | [GitHub 10.1k](https://github.com/OpenGVLab/InternVL) | [Demo](https://chat.intern-ai.org.cn/) |
| **InternVL3** | 2025.04 | arXiv technical report | open general VLM OCR baseline | [Paper](https://arxiv.org/abs/2504.10479) | [GitHub 10.1k](https://github.com/OpenGVLab/InternVL) | [Demo](https://chat.intern-ai.org.cn/) |
| **LLaVA** | 2024 | NeurIPS 2024 | visual instruction tuning baseline | [Paper](https://arxiv.org/abs/2304.08485) | [GitHub 24.9k](https://github.com/haotian-liu/LLaVA) | - |
| **CogVLM** | 2024 | ICLR 2024 | visual expert for language models | [Paper](https://arxiv.org/abs/2311.03079) | [GitHub 6.7k](https://github.com/THUDM/CogVLM) | - |
| **DeepSeek-VL** | 2024.03 | arXiv technical report | general VLM baseline for text-rich images | [Paper](https://arxiv.org/abs/2403.05525) | [GitHub 4.1k](https://github.com/deepseek-ai/DeepSeek-VL) | - |
| **MiniCPM-V** | 2024.08 | arXiv technical report | mobile-scale general MLLM with OCR ability | [Paper](https://arxiv.org/abs/2408.01800) | [GitHub 25.6k](https://github.com/OpenBMB/MiniCPM-o) | [Demo](https://minicpm-omni.openbmb.cn/) |
| **Florence-2** | 2023.11 | arXiv technical report | fixed-token general vision foundation model | [Paper](https://arxiv.org/abs/2311.06242) | - | [Hugging Face](https://huggingface.co/microsoft/Florence-2-large) |
| **Kimi-VL** | 2025.04 | arXiv technical report | general VLM OCR and document prompting | [Paper](https://arxiv.org/abs/2504.07491) | - | - |

### Closed/API General VLMs

| Model / System | Date | Venue / Source | OCR-Relevant Role | Paper / Project | Code / Stars | Demo / Docs |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **GPT-4V** | 2023 | system card | closed general VLM OCR interface | [System Card](https://cdn.openai.com/papers/GPTV_System_Card.pdf) | - | [Docs](https://platform.openai.com/docs) |
| **GPT-4o** | 2024 | product / API release | closed general VLM OCR interface | [Docs](https://platform.openai.com/docs) | - | [Docs](https://platform.openai.com/docs) |
| **Gemini family** | 2023.12 / 2024 | technical report / API docs | closed general VLM OCR interface | [Report](https://arxiv.org/abs/2312.11805) | - | [Docs](https://ai.google.dev/gemini-api/docs) |
| **Claude 3 / 3.5 / 4** | 2024-2025 | product / API docs | closed general VLM OCR interface | [Docs](https://docs.anthropic.com/) | - | [Docs](https://docs.anthropic.com/) |

</details>

<a id="f5-commercial-ocr-and-document-ai-services"></a>

### F5. Commercial OCR and Document AI Services

<details open>
<summary><strong>Show / hide F5 collection</strong></summary>

Closed-source or managed systems for document conversion, enterprise OCR, scientific document parsing, formula OCR, receipts, forms, invoices, and other vertical workflows.

### Enterprise OCR and Document AI

| System | Date | Venue / Source | Access Mode | Native Input | Output Contract | Docs / Website |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **ABBYY FineReader / ABBYY Vantage** | 1993- | product line / docs | commercial, on-prem / SDK / cloud | scanned document / PDF | searchable PDF, text, export formats, fields | [FineReader](https://www.abbyy.com/finereader/) / [Vantage](https://www.abbyy.com/vantage/) |
| **TextIn** | 2025 | product docs | commercial cloud API | document / receipt / form | JSON, Markdown, key-value fields | [Website](https://www.textin.com/) |

### Scientific OCR and Managed Parsing APIs

| System | Date | Venue / Source | Access Mode | Native Input | Output Contract | Docs / Website |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mathpix** | 2026 | product docs | commercial cloud API | formula / paper / document | LaTeX / Markdown | [Website](https://mathpix.com/) |
| **Mistral OCR** | 2025 | product docs | commercial cloud API | document / PDF / image | Markdown / structured response | [Docs](https://docs.mistral.ai/capabilities/document_ai/basic_ocr/) |
| **Qwen-OCR API** | 2025 | product docs | commercial cloud API | document / image | structured OCR output | [Docs](https://help.aliyun.com/zh/model-studio/) |

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
