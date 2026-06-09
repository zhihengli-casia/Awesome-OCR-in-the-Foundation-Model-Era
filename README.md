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

- [Model collections](#model-collections)
- [Benchmark and dataset inventory](resources/benchmarks.md)
- [Cross-era OCR arena](arena/README.md)
- [Contributing](CONTRIBUTING.md)

## Model Collections

Each category below is expandable. The full model inventory is maintained in [resources/models.md](resources/models.md).

<details>
<summary><strong>F1. Modular OCR Toolkits and Specialized Components</strong></summary>

Systems that follow or support the detector-recognizer pipeline.

- **OCR engines and toolkits:** Tesseract, EasyOCR, PaddleOCR / PP-OCR, MMOCR, docTR.
- **Text detection and spotting components:** EAST, CRAFT, PSENet, DBNet / DBNet++, FCENet.
- **Cropped text recognizers:** CRNN, ASTER, SRN, ABINet, ViTSTR, PARSeq, SVTR / SVTRv2, TrOCR.
- **Structured-object components:** UniMERNet, PP-FormulaNet, StructEqTable.

[Open full F1 list](resources/models.md#f1-modular-ocr-toolkits-and-specialized-components)

</details>

<details>
<summary><strong>F2. Foundation-Model Document Parsers</strong></summary>

End-to-end or near end-to-end models that read page images and generate Markdown, HTML, LaTeX, JSON, or OCR-formatted text.

- **OCR-free and transitional encoder-decoders:** Donut, Pix2Struct, Nougat.
- **Early document VLMs:** DocOwl, Vary, GOT-OCR, Monkey / TextMonkey, UReader, TextHawk, Fox.
- **2025-2026 OCR-specialized parsers:** SmolDocling, MonkeyOCR, DeepSeek-OCR, HunyuanOCR, dots.ocr, olmOCR-2, PaddleOCR-VL-1.5, GLM-OCR, Qianfan-OCR, FireRed-OCR.
- **Emerging generation routes:** MinerU-Diffusion, FDRL for Document OCR.

[Open full F2 list](resources/models.md#f2-foundation-model-document-parsers)

</details>

<details>
<summary><strong>F3. Hybrid Document Parsing Workflows</strong></summary>

Systems that combine layout detection, OCR, region decomposition, VLM generation, rule-based validators, and document assembly.

- **Document parsing workflows:** MinerU / MinerU2.5-Pro, Dolphin-v2, Docling.
- **PDF-to-structured-output workflows:** Marker, Surya, Pix2Text.

[Open full F3 list](resources/models.md#f3-hybrid-document-parsing-workflows)

</details>

<details>
<summary><strong>F4. General-Purpose VLMs as OCR Interfaces</strong></summary>

General multimodal models that can perform OCR-related tasks through prompts, while OCR is only one part of their capability.

- **Open general VLMs:** Qwen-VL, Qwen2-VL, Qwen2.5-VL, InternVL, LLaVA, CogVLM, DeepSeek-VL, MiniCPM-V, Florence-2, Kimi-VL.
- **Closed general VLMs:** GPT-4V / GPT-4o, Gemini, Claude.

[Open full F4 list](resources/models.md#f4-general-purpose-vlms-used-as-ocr-interfaces)

</details>

<details>
<summary><strong>F5. Commercial OCR and Document AI Services</strong></summary>

Closed-source or managed systems for document conversion, enterprise OCR, scientific document parsing, formula OCR, receipts, forms, invoices, and other vertical workflows.

- **Enterprise OCR and document AI:** ABBYY FineReader / Vantage, TextIn.
- **Scientific and formula-heavy OCR:** Mathpix.
- **Managed document parsing APIs:** Mistral OCR, Qwen-OCR API.

[Open full F5 list](resources/models.md#f5-commercial-ocr-and-document-ai-services)

</details>

## Resource Files

- `resources/models.md`: expandable model collections organized by the five-family taxonomy.
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
