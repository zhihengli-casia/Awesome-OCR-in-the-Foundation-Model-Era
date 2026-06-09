# Model and System Inventory

This page lists representative OCR systems by functional family. The goal is not to rank models, but to make clear what each system is, what it consumes, what it outputs, and how it should be evaluated.

## F1. Modular OCR Toolkits and Specialized Components

| System | Year | Route | Access / Scale | Native Input | Output Contract | Link |
|---|---:|---|---|---|---|---|
| Tesseract | 2007 | detector + recognizer | open | scanned page / line | text, hOCR, boxes | [GitHub](https://github.com/tesseract-ocr/tesseract) |
| EasyOCR | 2020 | detector + recognizer | open | scene / document image | text + boxes | [GitHub](https://github.com/JaidedAI/EasyOCR) |
| PaddleOCR / PP-OCR | 2020-2025 | detector + recognizer + structure modules | open, mobile-server | scene / page / vertical domain | text + boxes, optional structure | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| MMOCR | 2021 | detector + recognizer toolkit | open | scene / crop / page | detection and recognition outputs | [GitHub](https://github.com/open-mmlab/mmocr) |
| docTR | 2021-2023 | detector + recognizer | open | document page | words, lines, boxes | [GitHub](https://github.com/mindee/doctr) |
| DBNet / DBNet++ | 2020-2022 | text detector | open | scene / document image | text-region boxes or polygons | [GitHub](https://github.com/MhLiao/DB) |
| CRNN | 2015 | cropped recognizer | open | cropped word / line | string | [GitHub](https://github.com/meijieru/crnn.pytorch) |
| ASTER | 2018 | cropped recognizer | open | irregular cropped word | rectified string | [GitHub](https://github.com/bgshih/aster) |
| ABINet / PARSeq | 2021-2022 | cropped recognizer | open | cropped word | string | [GitHub](https://github.com/baudm/parseq) |
| SVTR / SVTRv2 | 2022-2024 | cropped recognizer | open | cropped word / line | string | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| TrOCR | 2023 | encoder-decoder recognizer | open, 558M | cropped word / line | string | [Hugging Face docs](https://huggingface.co/docs/transformers/model_doc/trocr) |
| UniMERNet / PP-FormulaNet | 2024-2025 | formula recognizer | open | formula image | LaTeX | [GitHub](https://github.com/opendatalab/UniMERNet) |
| StructEqTable | 2025 | structured object recognizer | open | table or equation region | LaTeX / HTML / Markdown | [GitHub](https://github.com/AlibabaResearch/AdvancedLiterateMachinery) |

## F2. Foundation-Model Document Parsers

| System | Year | Route | Access / Scale | Native Input | Output Contract | Link |
|---|---:|---|---|---|---|---|
| Donut | 2022 | OCR-free encoder-decoder | open, 143M | page image | task sequence / JSON-like text | [GitHub](https://github.com/clovaai/donut) |
| Pix2Struct | 2023 | OCR-free encoder-decoder | open, 1.3B | screenshot / page image | structured sequence | [GitHub](https://github.com/google-research/pix2struct) |
| Nougat | 2023 | OCR-free encoder-decoder | open, 350M | academic PDF page | Markdown / LaTeX | [GitHub](https://github.com/facebookresearch/nougat) |
| DocOwl family | 2023-2024 | document-oriented VLM | open, 7-8B | page / document image | text / Markdown / QA answer | [GitHub](https://github.com/X-PLUG/mPLUG-DocOwl) |
| Vary | 2023 | OCR-specialized VLM | open, about 7.5B | page image | Markdown / LaTeX | [GitHub](https://github.com/Ucas-HaoranWei/Vary) |
| GOT-OCR | 2024 | OCR-specialized VLM | open, 580M | page / scene / crop | plain or formatted OCR | [GitHub](https://github.com/Ucas-HaoranWei/GOT-OCR2.0) |
| Monkey / TextMonkey | 2024 | text-centric VLM | open, 9-10B | document or text-rich image | text / structured response | [GitHub](https://github.com/Yuliang-Liu/Monkey) |
| TextHawk | 2024 | OCR-enhanced VLM | open | text-rich image | text / document response | [Hugging Face](https://huggingface.co/TencentBAC) |
| Fox | 2024 | document-specialized VLM | open, about 3B | multi-page document | Markdown | [GitHub](https://github.com/ucaslcl/Fox) |
| MonkeyOCR | 2025 | OCR-specialized VLM | open, 1.2-3B | page image | Markdown / JSON / HTML | [GitHub](https://github.com/Yuliang-Liu/MonkeyOCR) |
| SmolDocling | 2025 | lightweight page parser | open, 256M | page image | DocTags / Markdown | [Hugging Face](https://huggingface.co/ds4sd/SmolDocling-256M-preview) |
| olmOCR-2 | 2025 | OCR-specialized VLM | open, about 8B | page image | Markdown | [GitHub](https://github.com/allenai/olmocr) |
| PaddleOCR-VL-1.5 | 2026 | OCR-specialized VLM | open, 0.9B | high-resolution page | Markdown / layout / objects | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| Qianfan-OCR | 2026 | OCR-specialized VLM | open / service, 4B | page image | Markdown / HTML / structured text | [Website](https://cloud.baidu.com/product/wenxinworkshop) |
| FireRed-OCR | 2026 | OCR-specialized VLM | open, about 2B | page image | Markdown / HTML / LaTeX | [GitHub](https://github.com/FireRedTeam/FireRed-OCR) |

## F3. Hybrid Document Parsing Workflows

| System | Year | Route | Access / Scale | Native Input | Output Contract | Link |
|---|---:|---|---|---|---|---|
| MinerU2.5-Pro | 2025 | layout + VLM | open, 1.2B | PDF / page image | Markdown + layout objects | [GitHub](https://github.com/opendatalab/MinerU) |
| Dolphin-v2 | 2025 | layout + VLM | open | page image | Markdown / JSON / LaTeX | [GitHub](https://github.com/bytedance/Dolphin) |
| Docling | 2024 | layout + OCR workflow | open toolkit | PDF / page image | DocTags / Markdown / JSON | [GitHub](https://github.com/docling-project/docling) |
| Marker / Surya | 2024 | layout + OCR workflow | open toolkit | PDF / page image | Markdown / JSON / HTML | [GitHub](https://github.com/datalab-to/marker) |

## F4. General-Purpose VLMs Used as OCR Interfaces

| System | Year | Route | Access / Scale | Native Input | Output Contract | Link |
|---|---:|---|---|---|---|---|
| Qwen-VL / Qwen2-VL / Qwen2.5-VL | 2023-2025 | general VLM | open, 3-72B | arbitrary image / page | natural language, text, boxes | [GitHub](https://github.com/QwenLM/Qwen2.5-VL) |
| InternVL family | 2024-2025 | general VLM | open, 1-78B | arbitrary image / page | natural language / text | [GitHub](https://github.com/OpenGVLab/InternVL) |
| LLaVA family | 2024 | general VLM | open | arbitrary image | natural language | [GitHub](https://github.com/haotian-liu/LLaVA) |
| CogVLM / DeepSeek-VL / Kimi-VL | 2024-2025 | general VLM | open | arbitrary image / screenshot | natural language / text | [CogVLM GitHub](https://github.com/THUDM/CogVLM) |
| GPT-4V / GPT-4o | 2023-2024 | general VLM | closed API | arbitrary image / document | natural language / structured text | [Docs](https://platform.openai.com/docs) |
| Gemini family | 2024-2025 | general VLM | closed API | arbitrary image / document | natural language / structured text | [Docs](https://ai.google.dev/gemini-api/docs) |
| Claude | 2024-2025 | general VLM | closed API | arbitrary image / document | natural language / structured text | [Docs](https://docs.anthropic.com/) |

## F5. Commercial OCR and Document AI Services

| System | Access | Native Input | Output Contract | Link |
|---|---|---|---|---|
| ABBYY FineReader | on-prem / SDK / commercial | scanned document / PDF | searchable PDF / text / export formats | [Website](https://www.abbyy.com/finereader/) |
| TextIn | cloud API / commercial | document / receipt / form | JSON / Markdown / key-value fields | [Website](https://www.textin.com/) |
| Mathpix | cloud API / commercial | formula / paper / document | LaTeX / Markdown | [Website](https://mathpix.com/) |
| Mistral OCR | cloud API / commercial | document / PDF / image | Markdown / structured response | [Docs](https://docs.mistral.ai/capabilities/document_ai/basic_ocr/) |

