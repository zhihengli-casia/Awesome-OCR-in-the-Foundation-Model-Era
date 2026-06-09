# Model and System Inventory

This page follows an Awesome-MLLM-style format: each entry exposes the paper, code, model page, demo, or documentation when available. The entries are organized by the five-family taxonomy used in the survey.

Legend: **F1** modular OCR toolkit/component; **F2** foundation-model document parser; **F3** hybrid document parsing workflow; **F4** general-purpose VLM used as an OCR interface; **F5** commercial OCR or document AI service.

## Latest OCR / Document Parsing Models

| Model / System | Family | Date | Paper | Code | Model / Demo / Docs |
|---|:---:|:---:|---|---|---|
| **MinerU2.5-Pro** | F3 | 2026 | [arXiv](https://arxiv.org/abs/2604.04771) | [GitHub](https://github.com/opendatalab/MinerU) | - |
| **Qianfan-OCR** | F2 | 2026 | [arXiv](https://arxiv.org/abs/2603.13398) | - | [Website](https://cloud.baidu.com/product/wenxinworkshop) |
| **MinerU-Diffusion** | F2 | 2026 | [arXiv](https://arxiv.org/abs/2603.22458) | - | - |
| **FireRed-OCR** | F2 | 2026 | [arXiv](https://arxiv.org/abs/2603.01840) | [GitHub](https://github.com/FireRedTeam/FireRed-OCR) | - |
| **GLM-OCR** | F2 | 2026 | [arXiv](https://arxiv.org/abs/2603.10910) | - | - |
| **Dolphin-v2** | F3 | 2026 | [arXiv](https://arxiv.org/abs/2602.05384) | [GitHub](https://github.com/bytedance/Dolphin) | - |
| **PaddleOCR-VL-1.5** | F2 | 2026 | [arXiv](https://arxiv.org/abs/2601.21957) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | - |
| **FDRL for Document OCR** | F2 | 2026 | [arXiv](https://arxiv.org/abs/2601.08834) | - | - |
| **dots.ocr** | F2 | 2025 | [arXiv](https://arxiv.org/abs/2512.02498) | - | - |
| **HunyuanOCR** | F2 | 2025 | [arXiv](https://arxiv.org/abs/2511.19575) | - | - |
| **olmOCR-2** | F2 | 2025 | [arXiv](https://arxiv.org/abs/2510.19817) | [GitHub](https://github.com/allenai/olmocr) | - |
| **DeepSeek-OCR** | F2 | 2025 | - | [GitHub](https://github.com/deepseek-ai/DeepSeek-OCR) | - |
| **MonkeyOCR** | F2 | 2025 | [arXiv](https://arxiv.org/abs/2506.05218) | [GitHub](https://github.com/Yuliang-Liu/MonkeyOCR) | - |
| **SmolDocling** | F2 | 2025 | [arXiv](https://arxiv.org/abs/2503.11576) | - | [Hugging Face](https://huggingface.co/ds4sd/SmolDocling-256M-preview) |
| **PP-FormulaNet** | F1 | 2025 | [arXiv](https://arxiv.org/abs/2503.18382) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | - |
| **Docling** | F3 | 2024 | [arXiv](https://arxiv.org/abs/2408.09869) | [GitHub](https://github.com/docling-project/docling) | [Docs](https://docling-project.github.io/docling/) |
| **GOT-OCR 2.0** | F2 | 2024 | [arXiv](https://arxiv.org/abs/2409.01704) | [GitHub](https://github.com/Ucas-HaoranWei/GOT-OCR2.0) | - |
| **DocOwl 2** | F2 | 2024 | [arXiv](https://arxiv.org/abs/2409.03420) | [GitHub](https://github.com/X-PLUG/mPLUG-DocOwl) | - |
| **TextHawk** | F2 | 2024 | [arXiv](https://arxiv.org/abs/2404.09204) | - | [Hugging Face](https://huggingface.co/TencentBAC) |
| **TextMonkey** | F2 | 2024 | [arXiv](https://arxiv.org/abs/2403.04473) | [GitHub](https://github.com/Yuliang-Liu/Monkey) | - |
| **Vary** | F2 | 2023 | [arXiv](https://arxiv.org/abs/2312.06109) | [GitHub](https://github.com/Ucas-HaoranWei/Vary) | - |
| **Nougat** | F2 | 2023 | [arXiv](https://arxiv.org/abs/2308.13418) | [GitHub](https://github.com/facebookresearch/nougat) | - |
| **Pix2Struct** | F2 | 2023 | [arXiv](https://arxiv.org/abs/2210.03347) | [GitHub](https://github.com/google-research/pix2struct) | - |
| **Donut** | F2 | 2022 | [arXiv](https://arxiv.org/abs/2111.15664) | [GitHub](https://github.com/clovaai/donut) | - |

## F1. Modular OCR Toolkits and Specialized Components

| Model / System | Date | Role | Paper | Code | Model / Docs |
|---|:---:|---|---|---|---|
| **Tesseract** | 2007 | OCR engine | [ICDAR](https://doi.org/10.1109/ICDAR.2007.4376991) | [GitHub](https://github.com/tesseract-ocr/tesseract) | [Docs](https://tesseract-ocr.github.io/) |
| **EasyOCR** | 2020 | OCR engine | - | [GitHub](https://github.com/JaidedAI/EasyOCR) | - |
| **PaddleOCR / PP-OCR** | 2020-2025 | industrial OCR toolkit | [arXiv](https://arxiv.org/abs/2009.09941) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | [Docs](https://paddlepaddle.github.io/PaddleOCR/) |
| **MMOCR** | 2021 | OCR research toolkit | - | [GitHub](https://github.com/open-mmlab/mmocr) | [Docs](https://mmocr.readthedocs.io/) |
| **docTR** | 2021-2023 | document OCR toolkit | - | [GitHub](https://github.com/mindee/doctr) | [Docs](https://mindee.github.io/doctr/) |
| **DBNet / DBNet++** | 2020-2023 | text detection | [AAAI](https://doi.org/10.1609/aaai.v34i07.6812) / [TPAMI](https://doi.org/10.1109/TPAMI.2022.3155612) | [GitHub](https://github.com/MhLiao/DB) | - |
| **CRAFT** | 2019 | text detection | [arXiv](https://arxiv.org/abs/1904.01941) | [GitHub](https://github.com/clovaai/CRAFT-pytorch) | - |
| **EAST** | 2017 | text detection | [arXiv](https://arxiv.org/abs/1704.03155) | - | - |
| **PSENet** | 2019 | arbitrary-shape text detection | [arXiv](https://arxiv.org/abs/1806.02559) | [GitHub](https://github.com/whai362/PSENet) | - |
| **FCENet** | 2021 | arbitrary-shape text detection | [arXiv](https://arxiv.org/abs/2104.10442) | - | - |
| **CRNN** | 2015 / 2017 | cropped text recognition | [TPAMI](https://doi.org/10.1109/TPAMI.2016.2646371) | [GitHub](https://github.com/meijieru/crnn.pytorch) | - |
| **ASTER** | 2018 / 2019 | irregular text recognition | [TPAMI](https://doi.org/10.1109/TPAMI.2018.2848939) | [GitHub](https://github.com/bgshih/aster) | - |
| **SRN** | 2020 | semantic reasoning recognizer | [arXiv](https://arxiv.org/abs/2003.12294) | - | - |
| **ABINet** | 2021 | language-aware recognizer | [arXiv](https://arxiv.org/abs/2103.06495) | - | - |
| **ViTSTR** | 2021 | ViT recognizer | [arXiv](https://arxiv.org/abs/2105.08582) | [GitHub](https://github.com/roatienza/deep-text-recognition-benchmark) | - |
| **PARSeq** | 2022 | autoregressive recognizer | [arXiv](https://arxiv.org/abs/2207.06966) | [GitHub](https://github.com/baudm/parseq) | - |
| **SVTR / SVTRv2** | 2022 / 2025 | efficient cropped recognizer | [IJCAI](https://doi.org/10.24963/ijcai.2022/124) / [arXiv](https://arxiv.org/abs/2411.15858) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | - |
| **TrOCR** | 2023 | pretrained encoder-decoder recognizer | [arXiv](https://arxiv.org/abs/2109.10282) | - | [HF Docs](https://huggingface.co/docs/transformers/model_doc/trocr) |
| **UniMERNet** | 2024 | formula recognition | [arXiv](https://arxiv.org/abs/2404.15254) | [GitHub](https://github.com/opendatalab/UniMERNet) | - |
| **PP-FormulaNet** | 2025 | formula recognition | [arXiv](https://arxiv.org/abs/2503.18382) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | - |
| **StructEqTable** | 2025 | equation/table structure parsing | - | [GitHub](https://github.com/AlibabaResearch/AdvancedLiterateMachinery) | - |

## F2. Foundation-Model Document Parsers

| Model / System | Date | Route | Paper | Code | Model / Demo / Docs |
|---|:---:|---|---|---|---|
| **Donut** | 2022 | OCR-free encoder-decoder | [arXiv](https://arxiv.org/abs/2111.15664) | [GitHub](https://github.com/clovaai/donut) | - |
| **Pix2Struct** | 2023 | screenshot/page-to-sequence pretraining | [arXiv](https://arxiv.org/abs/2210.03347) | [GitHub](https://github.com/google-research/pix2struct) | - |
| **Nougat** | 2023 | scholarly PDF-to-Markdown parser | [arXiv](https://arxiv.org/abs/2308.13418) | [GitHub](https://github.com/facebookresearch/nougat) | - |
| **DocOwl / DocOwl 1.5 / DocOwl 2** | 2023-2024 | document-oriented VLM | [DocOwl](https://arxiv.org/abs/2307.02499), [1.5](https://arxiv.org/abs/2403.12895), [2](https://arxiv.org/abs/2409.03420) | [GitHub](https://github.com/X-PLUG/mPLUG-DocOwl) | - |
| **Vary** | 2023 | document-specialized VLM | [arXiv](https://arxiv.org/abs/2312.06109) | [GitHub](https://github.com/Ucas-HaoranWei/Vary) | - |
| **GOT-OCR 2.0** | 2024 | unified OCR-specialized VLM | [arXiv](https://arxiv.org/abs/2409.01704) | [GitHub](https://github.com/Ucas-HaoranWei/GOT-OCR2.0) | - |
| **Monkey / TextMonkey** | 2024 | text-centric OCR-free MLLM | [Monkey](https://arxiv.org/abs/2311.06607), [TextMonkey](https://arxiv.org/abs/2403.04473) | [GitHub](https://github.com/Yuliang-Liu/Monkey) | - |
| **UReader** | 2023 | OCR-free visually situated language understanding | [arXiv](https://arxiv.org/abs/2310.05126) | - | - |
| **TextHawk** | 2024 | fine-grained text perception in MLLMs | [arXiv](https://arxiv.org/abs/2404.09204) | - | [Hugging Face](https://huggingface.co/TencentBAC) |
| **Fox** | 2024 | multi-page document understanding system | [arXiv](https://arxiv.org/abs/2405.14295) | [GitHub](https://github.com/ucaslcl/Fox) | - |
| **SmolDocling** | 2025 | ultra-compact document conversion VLM | [arXiv](https://arxiv.org/abs/2503.11576) | - | [Hugging Face](https://huggingface.co/ds4sd/SmolDocling-256M-preview) |
| **MonkeyOCR** | 2025 | structure-recognition-relation document parser | [arXiv](https://arxiv.org/abs/2506.05218) | [GitHub](https://github.com/Yuliang-Liu/MonkeyOCR) | - |
| **DeepSeek-OCR** | 2025 | visual token compression for OCR | - | [GitHub](https://github.com/deepseek-ai/DeepSeek-OCR) | - |
| **HunyuanOCR** | 2025 | OCR-specialized document VLM | [arXiv](https://arxiv.org/abs/2511.19575) | - | - |
| **dots.ocr** | 2025 | multilingual document layout parsing VLM | [arXiv](https://arxiv.org/abs/2512.02498) | - | - |
| **olmOCR-2** | 2025 | unit-test reward training for document OCR | [arXiv](https://arxiv.org/abs/2510.19817) | [GitHub](https://github.com/allenai/olmocr) | - |
| **PaddleOCR-VL-1.5** | 2026 | compact multi-task document parsing VLM | [arXiv](https://arxiv.org/abs/2601.21957) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | - |
| **GLM-OCR** | 2026 | OCR-specialized document parser | [arXiv](https://arxiv.org/abs/2603.10910) | - | - |
| **Qianfan-OCR** | 2026 | end-to-end document intelligence model | [arXiv](https://arxiv.org/abs/2603.13398) | - | [Website](https://cloud.baidu.com/product/wenxinworkshop) |
| **FireRed-OCR** | 2026 | OCR-specialized VLM | [arXiv](https://arxiv.org/abs/2603.01840) | [GitHub](https://github.com/FireRedTeam/FireRed-OCR) | - |
| **MinerU-Diffusion** | 2026 | diffusion-style inverse-rendering OCR | [arXiv](https://arxiv.org/abs/2603.22458) | - | - |

## F3. Hybrid Document Parsing Workflows

| Model / System | Date | Route | Paper | Code | Model / Demo / Docs |
|---|:---:|---|---|---|---|
| **MinerU / MinerU2.5-Pro** | 2025-2026 | layout decomposition + VLM parsing | [arXiv](https://arxiv.org/abs/2604.04771) | [GitHub](https://github.com/opendatalab/MinerU) | - |
| **Dolphin-v2** | 2026 | anchor prompting + document parsing workflow | [arXiv](https://arxiv.org/abs/2602.05384) | [GitHub](https://github.com/bytedance/Dolphin) | - |
| **Docling** | 2024 | production document conversion workflow | [arXiv](https://arxiv.org/abs/2408.09869) | [GitHub](https://github.com/docling-project/docling) | [Docs](https://docling-project.github.io/docling/) |
| **Marker** | 2023 | PDF-to-Markdown workflow | - | [GitHub](https://github.com/datalab-to/marker) | - |
| **Surya** | 2024 | OCR, layout, reading order, line detection | - | [GitHub](https://github.com/datalab-to/surya) | - |
| **Pix2Text** | 2024 | layout + formula + OCR workflow | - | [GitHub](https://github.com/breezedeus/Pix2Text) | - |

## F4. General-Purpose VLMs Used as OCR Interfaces

| Model / System | Date | OCR-Relevant Role | Paper | Code | Model / Demo / Docs |
|---|:---:|---|---|---|---|
| **Qwen-VL** | 2023 | visual text reading, grounding, document QA | [arXiv](https://arxiv.org/abs/2308.12966) | [GitHub](https://github.com/QwenLM/Qwen-VL) | - |
| **Qwen2-VL** | 2024 | dynamic resolution VLM with OCR ability | [arXiv](https://arxiv.org/abs/2409.12191) | [GitHub](https://github.com/QwenLM/Qwen2-VL) | - |
| **Qwen2.5-VL** | 2025 | general VLM OCR and document prompting | [arXiv](https://arxiv.org/abs/2502.13923) | [GitHub](https://github.com/QwenLM/Qwen2.5-VL) | [Demo](https://chat.qwen.ai/) |
| **InternVL / InternVL 1.5 / InternVL3** | 2024-2025 | open general VLM baseline | [InternVL](https://arxiv.org/abs/2312.14238), [1.5](https://arxiv.org/abs/2404.16821), [3](https://arxiv.org/abs/2504.10479) | [GitHub](https://github.com/OpenGVLab/InternVL) | [Demo](https://chat.intern-ai.org.cn/) |
| **LLaVA** | 2024 | visual instruction tuning baseline | [arXiv](https://arxiv.org/abs/2304.08485) | [GitHub](https://github.com/haotian-liu/LLaVA) | - |
| **CogVLM** | 2024 | visual expert for language models | [arXiv](https://arxiv.org/abs/2311.03079) | [GitHub](https://github.com/THUDM/CogVLM) | - |
| **DeepSeek-VL** | 2024 | general VLM baseline for text-rich images | [arXiv](https://arxiv.org/abs/2403.05525) | [GitHub](https://github.com/deepseek-ai/DeepSeek-VL) | - |
| **MiniCPM-V** | 2024 | mobile-scale general MLLM with OCR ability | [arXiv](https://arxiv.org/abs/2408.01800) | [GitHub](https://github.com/OpenBMB/MiniCPM-o) | [Demo](https://minicpm-omni.openbmb.cn/) |
| **Florence-2** | 2023 | fixed-token general vision foundation model | [arXiv](https://arxiv.org/abs/2311.06242) | - | [Hugging Face](https://huggingface.co/microsoft/Florence-2-large) |
| **Kimi-VL** | 2025 | general VLM OCR and document prompting | [arXiv](https://arxiv.org/abs/2504.07491) | - | - |
| **GPT-4V / GPT-4o** | 2023-2024 | closed general VLM OCR interface | [GPT-4V system card](https://cdn.openai.com/papers/GPTV_System_Card.pdf) | - | [Docs](https://platform.openai.com/docs) |
| **Gemini family** | 2024-2025 | closed general VLM OCR interface | [arXiv](https://arxiv.org/abs/2312.11805) | - | [Docs](https://ai.google.dev/gemini-api/docs) |
| **Claude 3 / 3.5 / 4** | 2024-2025 | closed general VLM OCR interface | - | - | [Docs](https://docs.anthropic.com/) |

## F5. Commercial OCR and Document AI Services

| System | Access Mode | Native Input | Output Contract | Docs / Website |
|---|---|---|---|---|
| **ABBYY FineReader / ABBYY Vantage** | commercial, on-prem / SDK / cloud | scanned document / PDF | searchable PDF, text, export formats, fields | [FineReader](https://www.abbyy.com/finereader/) / [Vantage](https://www.abbyy.com/vantage/) |
| **TextIn** | commercial cloud API | document / receipt / form | JSON, Markdown, key-value fields | [Website](https://www.textin.com/) |
| **Mathpix** | commercial cloud API | formula / paper / document | LaTeX / Markdown | [Website](https://mathpix.com/) |
| **Mistral OCR** | commercial cloud API | document / PDF / image | Markdown / structured response | [Docs](https://docs.mistral.ai/capabilities/document_ai/basic_ocr/) |
| **Qwen-OCR API** | commercial cloud API | document / image | structured OCR output | [Docs](https://help.aliyun.com/zh/model-studio/) |

