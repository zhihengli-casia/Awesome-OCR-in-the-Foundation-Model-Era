# Awesome OCR in the Foundation-Model Era

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/github/stars/zhihengli-casia/Awesome-OCR-in-the-Foundation-Model-Era?style=social)](https://github.com/zhihengli-casia/Awesome-OCR-in-the-Foundation-Model-Era)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A curated list of OCR, document parsing, OCR-specialized vision-language models, hybrid document parsing workflows, commercial OCR services, and benchmarks.

This repository accompanies the survey:

> **OCR in the Foundation Model Era: A Survey**  
> Zhiheng Li et al., in preparation, 2026.

OCR is treated here in a broad but bounded sense: visual text and document images are converted into machine-readable text or structured document representations. Downstream tasks such as document QA, information extraction, RAG, and agent workflows are included only when they shape OCR system design or evaluation.

## Contents

- [Featured modern OCR models](#featured-modern-ocr-models)
- [System taxonomy](#system-taxonomy)
- [Model and system inventory](resources/models.md)
- [Benchmark and dataset inventory](resources/benchmarks.md)
- [Cross-era OCR arena](arena/README.md)
- [Contributing](CONTRIBUTING.md)

## Featured Modern OCR Models

| Model / System | Family | Date | Paper | Code | Model / Demo / Docs |
|---|:---:|:---:|---|---|---|
| **MinerU2.5-Pro** | F3 | 2026 | [arXiv](https://arxiv.org/abs/2604.04771) | [GitHub](https://github.com/opendatalab/MinerU) | - |
| **Qianfan-OCR** | F2 | 2026 | [arXiv](https://arxiv.org/abs/2603.13398) | - | [Website](https://cloud.baidu.com/product/wenxinworkshop) |
| **FireRed-OCR** | F2 | 2026 | [arXiv](https://arxiv.org/abs/2603.01840) | [GitHub](https://github.com/FireRedTeam/FireRed-OCR) | - |
| **GLM-OCR** | F2 | 2026 | [arXiv](https://arxiv.org/abs/2603.10910) | - | - |
| **Dolphin-v2** | F3 | 2026 | [arXiv](https://arxiv.org/abs/2602.05384) | [GitHub](https://github.com/bytedance/Dolphin) | - |
| **PaddleOCR-VL-1.5** | F2 | 2026 | [arXiv](https://arxiv.org/abs/2601.21957) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | - |
| **HunyuanOCR** | F2 | 2025 | [arXiv](https://arxiv.org/abs/2511.19575) | - | - |
| **olmOCR-2** | F2 | 2025 | [arXiv](https://arxiv.org/abs/2510.19817) | [GitHub](https://github.com/allenai/olmocr) | - |
| **DeepSeek-OCR** | F2 | 2025 | - | [GitHub](https://github.com/deepseek-ai/DeepSeek-OCR) | - |
| **MonkeyOCR** | F2 | 2025 | [arXiv](https://arxiv.org/abs/2506.05218) | [GitHub](https://github.com/Yuliang-Liu/MonkeyOCR) | - |
| **SmolDocling** | F2 | 2025 | [arXiv](https://arxiv.org/abs/2503.11576) | - | [Hugging Face](https://huggingface.co/ds4sd/SmolDocling-256M-preview) |
| **Docling** | F3 | 2024 | [arXiv](https://arxiv.org/abs/2408.09869) | [GitHub](https://github.com/docling-project/docling) | [Docs](https://docling-project.github.io/docling/) |
| **GOT-OCR 2.0** | F2 | 2024 | [arXiv](https://arxiv.org/abs/2409.01704) | [GitHub](https://github.com/Ucas-HaoranWei/GOT-OCR2.0) | - |
| **Nougat** | F2 | 2023 | [arXiv](https://arxiv.org/abs/2308.13418) | [GitHub](https://github.com/facebookresearch/nougat) | - |

See the full [model and system inventory](resources/models.md).

## System Taxonomy

The foundation-model era does not collapse OCR into a single technical route. The survey organizes today's OCR ecosystem into five coexisting system families.

### F1. Modular OCR Toolkits and Specialized Components

Systems that follow or support the detector-recognizer pipeline. They include OCR engines, text detectors, cropped text recognizers, formula recognizers, table recognizers, and open toolkits.

Representative systems: Tesseract, EasyOCR, PaddleOCR / PP-OCR, MMOCR, docTR, DBNet, CRNN, ASTER, ABINet, PARSeq, SVTR, TrOCR, UniMERNet, PP-FormulaNet.

### F2. Foundation-Model Document Parsers

End-to-end or near end-to-end models that read page images and generate structured representations such as Markdown, HTML, LaTeX, JSON, or OCR-formatted text.

Representative systems: Donut, Pix2Struct, Nougat, DocOwl, Vary, GOT-OCR, MonkeyOCR, SmolDocling, HunyuanOCR, GLM-OCR, olmOCR, DeepSeek-OCR, PaddleOCR-VL, Qianfan-OCR, FireRed-OCR.

### F3. Hybrid Document Parsing Workflows

Systems that combine layout detection, OCR, region decomposition, VLM generation, rule-based validators, and document assembly.

Representative systems: MinerU, Dolphin, Docling, Marker, Surya, Pix2Text.

### F4. General-Purpose VLMs as OCR Interfaces

General multimodal models that can perform OCR-related tasks through prompts, even though OCR is only one of their capabilities.

Representative systems: Qwen-VL, Qwen2-VL, Qwen2.5-VL, InternVL, LLaVA, CogVLM, DeepSeek-VL, MiniCPM-V, Kimi-VL, GPT-4V, GPT-4o, Gemini, Claude.

### F5. Commercial OCR and Document AI Services

Closed-source or managed systems for document conversion, enterprise OCR, scientific document parsing, formula OCR, receipts, forms, invoices, and other vertical workflows.

Representative services: ABBYY FineReader, TextIn, Mathpix, Mistral OCR.

## Resource Files

- `resources/models.md`: citation-oriented inventory of representative systems.
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
