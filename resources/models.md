# Model and System Collections

This page organizes representative OCR systems as expandable collections. Each family corresponds to a system role in the survey taxonomy, and each family contains concrete model collections.

Legend: **F1** modular OCR toolkit/component; **F2** foundation-model document parser; **F3** hybrid document parsing workflow; **F4** general-purpose VLM used as an OCR interface; **F5** commercial OCR or document AI service.

For entries with arXiv versions, the Date column uses the arXiv `YYYY.MM` month, with multiple releases listed slash-separated when a row groups several papers. Accepted venues should be shown in the paper/source label when tracked; entries without arXiv keep the available public source or project date.

## Category Directory

<details>
<summary><strong>F1. Modular OCR Toolkits and Specialized Components</strong></summary>

- OCR engines and toolkits
- Text detection and spotting components
- Cropped text recognizers
- Formula, table, and structured-object components

</details>

<details>
<summary><strong>F2. Foundation-Model Document Parsers</strong></summary>

- OCR-free and transitional encoder-decoders
- Early document VLMs
- 2025-2026 OCR-specialized parsers
- Emerging generation and training routes

</details>

<details>
<summary><strong>F3. Hybrid Document Parsing Workflows</strong></summary>

- Full document parsing workflows
- PDF-to-Markdown and document conversion workflows

</details>

<details>
<summary><strong>F4. General-Purpose VLMs Used as OCR Interfaces</strong></summary>

- Open general VLMs
- Closed/API general VLMs

</details>

<details>
<summary><strong>F5. Commercial OCR and Document AI Services</strong></summary>

- Enterprise OCR and document AI
- Scientific OCR and formula-heavy services
- Managed document parsing APIs

</details>

## Detailed Collections

<a id="f1-modular-ocr-toolkits-and-specialized-components"></a>

<details>
<summary><strong>F1. Modular OCR Toolkits and Specialized Components</strong></summary>

### OCR Engines and Toolkits

| Model / System | Date | Role | Paper | Code | Docs / Model |
|---|:---:|---|---|---|---|
| **Tesseract** | 2007 | OCR engine | [ICDAR](https://doi.org/10.1109/ICDAR.2007.4376991) | [GitHub](https://github.com/tesseract-ocr/tesseract) | [Docs](https://tesseract-ocr.github.io/) |
| **EasyOCR** | 2020 | OCR engine | - | [GitHub](https://github.com/JaidedAI/EasyOCR) | - |
| **PaddleOCR / PP-OCR** | 2020.09 | industrial OCR toolkit | [arXiv](https://arxiv.org/abs/2009.09941) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | [Docs](https://paddlepaddle.github.io/PaddleOCR/) |
| **MMOCR** | 2021.08 | OCR research toolkit | [arXiv](https://arxiv.org/abs/2108.06543) | [GitHub](https://github.com/open-mmlab/mmocr) | [Docs](https://mmocr.readthedocs.io/) |
| **docTR** | 2021-2023 | document OCR toolkit | - | [GitHub](https://github.com/mindee/doctr) | [Docs](https://mindee.github.io/doctr/) |

### Text Detection and Spotting Components

| Model / System | Date | Role | Paper | Code | Docs / Model |
|---|:---:|---|---|---|---|
| **EAST** | 2017.04 | text detection | [arXiv](https://arxiv.org/abs/1704.03155) | [GitHub](https://github.com/argman/EAST) | - |
| **CRAFT** | 2019.04 | text detection | [arXiv](https://arxiv.org/abs/1904.01941) | [GitHub](https://github.com/clovaai/CRAFT-pytorch) | - |
| **PSENet** | 2018.06 | arbitrary-shape text detection | [arXiv](https://arxiv.org/abs/1806.02559) | [GitHub](https://github.com/whai362/PSENet) | - |
| **DBNet / DBNet++** | 2019.11 / 2022.02 | text detection | [AAAI](https://arxiv.org/abs/1911.08947) / [TPAMI](https://arxiv.org/abs/2202.10304) | [GitHub](https://github.com/MhLiao/DB) | - |
| **FCENet** | 2021.04 | arbitrary-shape text detection | [arXiv](https://arxiv.org/abs/2104.10442) | [GitHub](https://github.com/yuchenwang815/FCENet) | - |

### Cropped Text Recognizers

| Model / System | Date | Role | Paper | Code | Docs / Model |
|---|:---:|---|---|---|---|
| **CRNN** | 2015.07 | cropped text recognition | [TPAMI](https://arxiv.org/abs/1507.05717) | [GitHub](https://github.com/meijieru/crnn.pytorch) | - |
| **ASTER** | 2018 / 2019 | irregular text recognition | [TPAMI](https://doi.org/10.1109/TPAMI.2018.2848939) | [GitHub](https://github.com/bgshih/aster) | - |
| **SRN** | 2020.03 | semantic reasoning recognizer | [arXiv](https://arxiv.org/abs/2003.12294) | - | - |
| **ABINet** | 2021.03 | language-aware recognizer | [arXiv](https://arxiv.org/abs/2103.06495) | [GitHub](https://github.com/FangShancheng/ABINet) | - |
| **ViTSTR** | 2021.05 | ViT recognizer | [arXiv](https://arxiv.org/abs/2105.08582) | [GitHub](https://github.com/roatienza/deep-text-recognition-benchmark) | - |
| **PARSeq** | 2022.07 | autoregressive recognizer | [arXiv](https://arxiv.org/abs/2207.06966) | [GitHub](https://github.com/baudm/parseq) | - |
| **SVTR / SVTRv2** | 2022.05 / 2024.11 | efficient cropped recognizer | [IJCAI](https://arxiv.org/abs/2205.00159) / [arXiv](https://arxiv.org/abs/2411.15858) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | - |
| **TrOCR** | 2021.09 | pretrained encoder-decoder recognizer | [arXiv](https://arxiv.org/abs/2109.10282) | [GitHub](https://github.com/microsoft/unilm/tree/master/trocr) | [HF Docs](https://huggingface.co/docs/transformers/model_doc/trocr) |

### Formula, Table, and Structured-Object Components

| Model / System | Date | Role | Paper | Code | Docs / Model |
|---|:---:|---|---|---|---|
| **IMPO / From Pixel to Precision** | 2026 | HMER with image-level reward | [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_From_Pixel_to_Precision_Enhancing_Handwritten_Mathematical_Expression_Recognition_with_CVPR_2026_paper.html) | - | - |
| **Texo** | 2026.02 | compact formula recognizer | [arXiv](https://arxiv.org/abs/2602.17189) | - | - |
| **TexTeller / Tex80M** | 2025.08 | scalable handwritten formula recognition | [arXiv](https://arxiv.org/abs/2508.09220) | [GitHub](https://github.com/OleehyO/TexTeller) | [HF](https://huggingface.co/OleehyO/TexTeller) |
| **PP-FormulaNet** | 2025.03 | formula recognition | [arXiv](https://arxiv.org/abs/2503.18382) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | - |
| **StructEqTable** | 2025 | equation/table structure parsing | - | [GitHub](https://github.com/AlibabaResearch/AdvancedLiterateMachinery) | - |
| **SemiHMER** | 2025.02 | semi-supervised HMER | [arXiv](https://arxiv.org/abs/2502.07172) | - | - |
| **TAMER** | 2024.08 | tree-aware transformer for HMER | [arXiv](https://arxiv.org/abs/2408.08578) | [GitHub](https://github.com/qingzhenduyu/TAMER) | - |
| **PosFormer** | 2024.07 | position-aware HMER | [arXiv](https://arxiv.org/abs/2407.07764) | [GitHub](https://github.com/SJTU-DeepVisionLab/PosFormer) | - |
| **UniMERNet** | 2024.04 | formula recognition | [arXiv](https://arxiv.org/abs/2404.15254) | [GitHub](https://github.com/opendatalab/UniMERNet) | - |
| **GAP** | 2024 | grammar- and position-aware multi-line formula recognition | [DOI](https://doi.org/10.1145/3616855.3635776) | - | - |
| **LAST** | 2023 | line-aware semi-autoregressive HMER | [DOI](https://doi.org/10.1145/3581783.3612499) | [GitHub](https://github.com/HCIILAB/LAST) | - |
| **SGRL** | 2023.08 | semantic graph representation learning for HMER | [arXiv](https://arxiv.org/abs/2308.10493) | - | - |
| **CoMER** | 2022.07 | coverage modeling for transformer-based HMER | [arXiv](https://arxiv.org/abs/2207.04410) | [GitHub](https://github.com/Green-Wood/CoMER) | - |
| **CAN** | 2022.07 | counting-aware HMER | [arXiv](https://arxiv.org/abs/2207.11463) | [GitHub](https://github.com/LBH1024/CAN) | - |
| **SAN** | 2022.03 | syntax-aware HMER | [arXiv](https://arxiv.org/abs/2203.01601) | [GitHub](https://github.com/tal-tech/san) | - |
| **BTTR** | 2021.05 | bidirectionally trained transformer for HMER | [arXiv](https://arxiv.org/abs/2105.02412) | [GitHub](https://github.com/Green-Wood/BTTR) | - |
| **WAP** | 2017 | handwritten mathematical expression recognition | [DOI](https://doi.org/10.1016/j.patcog.2017.06.017) | - | - |
| **Im2Markup** | 2016.09 | image-to-LaTeX generation | [arXiv](https://arxiv.org/abs/1609.04938) | [GitHub](https://github.com/harvardnlp/im2markup) | - |

</details>

<a id="f2-foundation-model-document-parsers"></a>

<details>
<summary><strong>F2. Foundation-Model Document Parsers</strong></summary>

### OCR-Free and Transitional Encoder-Decoders

| Model / System | Date | Route | Paper | Code | Docs / Model |
|---|:---:|---|---|---|---|
| **KOSMOS-2.5** | 2023.09 | multimodal literate model for text-intensive images | [arXiv](https://arxiv.org/abs/2309.11419) | [GitHub](https://github.com/microsoft/unilm/tree/master/kosmos-2.5) | [HF](https://huggingface.co/microsoft/kosmos-2.5) |
| **Nougat** | 2023.08 | scholarly PDF-to-Markdown parser | [arXiv](https://arxiv.org/abs/2308.13418) | [GitHub](https://github.com/facebookresearch/nougat) | - |
| **UDOP** | 2022.12 | unified vision-text-layout generation | [arXiv](https://arxiv.org/abs/2212.02623) | [GitHub](https://github.com/microsoft/UDOP) | - |
| **Pix2Struct** | 2022.10 | screenshot/page-to-sequence pretraining | [arXiv](https://arxiv.org/abs/2210.03347) | [GitHub](https://github.com/google-research/pix2struct) | - |
| **Dessurt** | 2022.03 | end-to-end document recognition and understanding | [arXiv](https://arxiv.org/abs/2203.16618) | [GitHub](https://github.com/herobd/dessurt) | - |
| **Donut** | 2021.11 | OCR-free encoder-decoder | [arXiv](https://arxiv.org/abs/2111.15664) | [GitHub](https://github.com/clovaai/donut) | - |

### Document-VLM Precursors and Adaptations

| Model / System | Date | Route | Paper | Code | Docs / Model |
|---|:---:|---|---|---|---|
| **DocOwl / DocOwl 1.5 / DocOwl 2** | 2023.07 / 2024.03 / 2024.09 | document-oriented VLM | [DocOwl](https://arxiv.org/abs/2307.02499), [1.5](https://arxiv.org/abs/2403.12895), [2](https://arxiv.org/abs/2409.03420) | [GitHub](https://github.com/X-PLUG/mPLUG-DocOwl) | - |
| **Vary** | 2023.12 | document-specialized VLM | [arXiv](https://arxiv.org/abs/2312.06109) | [GitHub](https://github.com/Ucas-HaoranWei/Vary) | - |
| **GOT-OCR 2.0** | 2024.09 | unified OCR-specialized VLM | [arXiv](https://arxiv.org/abs/2409.01704) | [GitHub](https://github.com/Ucas-HaoranWei/GOT-OCR2.0) | - |
| **Monkey / TextMonkey** | 2023.11 / 2024.03 | text-centric OCR-free MLLM | [Monkey](https://arxiv.org/abs/2311.06607), [TextMonkey](https://arxiv.org/abs/2403.04473) | [GitHub](https://github.com/Yuliang-Liu/Monkey) | - |
| **UReader** | 2023.10 | OCR-free visually situated language understanding | [arXiv](https://arxiv.org/abs/2310.05126) | [GitHub](https://github.com/LukeForeverYoung/UReader) | - |
| **TextHawk** | 2024.04 | fine-grained text perception in MLLMs | [arXiv](https://arxiv.org/abs/2404.09204) | [GitHub](https://github.com/yuyq96/TextHawk) | [Hugging Face](https://huggingface.co/TencentBAC) |
| **Fox** | 2024.05 | multi-page document understanding system | [arXiv](https://arxiv.org/abs/2405.14295) | [GitHub](https://github.com/ucaslcl/Fox) | - |

### OCR-Specialized Page Parsers

| Model / System | Date | Route | Paper | Code | Docs / Model |
|---|:---:|---|---|---|---|
| **PaddleOCR-VL-1.6** | 2026.06 | latest compact document parsing VLM in the PaddleOCR-VL line | [arXiv](https://arxiv.org/abs/2606.03264) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | [Docs](https://paddlepaddle.github.io/PaddleOCR/) |
| **ABot-OCR** | 2026.05 | AMap end-to-end OCR VLM | [arXiv](https://arxiv.org/abs/2605.27978) | [GitHub](https://github.com/amap-cvlab/ABot-OCR) | - |
| **Qianfan-OCR** | 2026.03 | end-to-end document intelligence model | [arXiv](https://arxiv.org/abs/2603.13398) | - | [Website](https://cloud.baidu.com/product/wenxinworkshop) |
| **GLM-OCR** | 2026.03 | OCR-specialized document parser | [arXiv](https://arxiv.org/abs/2603.10910) | [GitHub](https://github.com/zai-org/GLM-OCR) | [HF](https://huggingface.co/zai-org/GLM-OCR) |
| **FireRed-OCR** | 2026.03 | OCR-specialized VLM | [arXiv](https://arxiv.org/abs/2603.01840) | [GitHub](https://github.com/FireRedTeam/FireRed-OCR) | - |
| **GutenOCR** | 2026.01 | grounded OCR front-end fine-tuned from Qwen2.5-VL | [arXiv](https://arxiv.org/abs/2601.14490) | [GitHub](https://github.com/Roots-Automation/GutenOCR) | - |
| **LightOnOCR-2-1B** | 2026.01 | 1B multilingual end-to-end OCR VLM | [arXiv](https://arxiv.org/abs/2601.14251) | - | [HF](https://huggingface.co/lightonai/LightOnOCR-2-1B) |
| **OCRVerse** | 2026.01 | holistic OCR VLM for text-centric and vision-centric OCR | [arXiv](https://arxiv.org/abs/2601.21639) | [GitHub](https://github.com/DocTron-hub/OCRVerse) | - |
| **PaddleOCR-VL-1.5** | 2026.01 | compact multi-task document parsing VLM | [arXiv](https://arxiv.org/abs/2601.21957) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | - |
| **DeepSeek-OCR / DeepSeek-OCR 2** | 2026.01 / 2025.10 | visual token compression and causal-flow document parsing | [arXiv](https://arxiv.org/abs/2601.20552) / [arXiv](https://arxiv.org/abs/2510.18234) | [GitHub](https://github.com/deepseek-ai/DeepSeek-OCR) | - |
| **dots.ocr** | 2025.12 | multilingual document layout parsing VLM | [arXiv](https://arxiv.org/abs/2512.02498) | [GitHub](https://github.com/rednote-hilab/dots.ocr) | [HF](https://huggingface.co/rednote-hilab/dots.ocr) |
| **HunyuanOCR** | 2025.11 | OCR-specialized document VLM | [arXiv](https://arxiv.org/abs/2511.19575) | [GitHub](https://github.com/Tencent-Hunyuan/HunyuanOCR) | [HF](https://huggingface.co/tencent/HunyuanOCR) |
| **olmOCR / olmOCR-2** | 2025.10 / 2025.02 | open PDF-to-Markdown OCR and unit-test reward training | [arXiv](https://arxiv.org/abs/2510.19817) / [arXiv](https://arxiv.org/abs/2502.18443) | [GitHub](https://github.com/allenai/olmocr) | [HF Bench](https://huggingface.co/datasets/allenai/olmOCR-bench) |
| **PaddleOCR-VL** | 2025.10 | compact multilingual document parsing VLM | [arXiv](https://arxiv.org/abs/2510.14528) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | [Docs](https://paddlepaddle.github.io/PaddleOCR/) |
| **PP-DocBee2** | 2025.06 | efficient data and stronger document baselines | [arXiv](https://arxiv.org/abs/2506.18023) | [GitHub](https://github.com/PaddlePaddle/PaddleMIX/tree/develop/paddlemix/examples/ppdocbee2) | - |
| **Infinity-Parser** | 2025.06 | layout-aware reinforcement learning for scanned document parsing | [arXiv](https://arxiv.org/abs/2506.03197) | [GitHub](https://github.com/infly-ai/INF-MLLM/tree/main/research/InfM2/Infinity-Parser) | [HF](https://huggingface.co/infly/Infinity-Parser-7B) |
| **MonkeyOCR** | 2025.06 | structure-recognition-relation document parser | [arXiv](https://arxiv.org/abs/2506.05218) | [GitHub](https://github.com/Yuliang-Liu/MonkeyOCR) | - |
| **SmolDocling** | 2025.03 | ultra-compact document conversion VLM | [arXiv](https://arxiv.org/abs/2503.11576) | - | [Hugging Face](https://huggingface.co/ds4sd/SmolDocling-256M-preview) |
| **PP-DocBee** | 2025.03 | multimodal document understanding baseline | [arXiv](https://arxiv.org/abs/2503.04065) | [GitHub](https://github.com/PaddlePaddle/PaddleMIX/tree/develop/paddlemix/examples/ppdocbee) | - |

### Emerging Generation and Training Routes

| Model / System | Date | Route | Paper | Code | Docs / Model |
|---|:---:|---|---|---|---|
| **MinerU-Diffusion** | 2026.03 | diffusion-style inverse-rendering OCR | [arXiv](https://arxiv.org/abs/2603.22458) | - | - |
| **Risk-Controlled Generative OCR / GRC** | 2026.03 | selective accept/abstain risk control for frozen VLM OCR | [arXiv](https://arxiv.org/abs/2603.19790) | [GitHub](https://github.com/phare111/GRC) | - |
| **PAR for Faithful OCR / GlitchText** | 2026.01 | training-free mitigation of linguistic-prior OCR hallucination | [OpenReview](https://openreview.net/forum?id=M8zr7QvasK) | [GitHub](https://github.com/Zoeyyao27/PAR-for-Faithful-OCR) | - |
| **Teaching VLMs to Admit Uncertainty in OCR** | 2026.01 | uncertainty-aware OCR with explicit unreliable-span tags | [ICLR](https://openreview.net/forum?id=zyCjizqOxB) | [GitHub](https://github.com/NikoGuan/Uncertainty_OCR) | - |
| **FDRL for Document OCR** | 2026.01 | format-decoupled reinforcement learning | [arXiv](https://arxiv.org/abs/2601.08834) | - | - |
| **Reading Between the Lines / LRP** | 2025.11 | latent-representation probes for abstaining from VLM-generated OCR errors | [arXiv](https://arxiv.org/abs/2511.19806) | - | - |
| **OCR-Critic / OCR-ERROR** | 2025.10 | critical feedback alignment and OCR error diagnosis for MLLMs | [ACM DL](https://dl.acm.org/doi/10.1145/3746027.3754585) | - | - |
| **HalluText / OCRAssistor** | 2025.09 | OCR hallucination diagnosis and plug-and-play mitigation | [OpenReview](https://openreview.net/forum?id=LRnt6foJ3q) | - | - |
| **ReViCo** | 2025.09 | real-world visual spelling correction for VLMs | [arXiv](https://arxiv.org/abs/2509.17418) | - | - |
| **When Semantics Mislead Vision / TextHalu-Bench** | 2025.06 | training-free mitigation of semantic hallucination in scene-text perception | [arXiv](https://arxiv.org/abs/2506.05551) | [GitHub](https://github.com/shuyansy/MLLM-Semantic-Hallucination) | [HF Dataset](https://huggingface.co/datasets/sy1998/TextHalu-Bench) |
| **Seeing is Believing? / KIE-HVQA** | 2025.06 | OCR hallucination mitigation under visual degradation | [arXiv](https://arxiv.org/abs/2506.20168) | - | [HF Dataset](https://huggingface.co/datasets/bytedance-research/KIE-HVQA) |
| **Consensus Entropy / CE-OCR** | 2025.04 | multi-VLM agreement for self-verifying and self-improving OCR | [CVPR](https://arxiv.org/abs/2504.11101) | [GitHub](https://github.com/Aslan-yulong/consensus-entropy) | [HF Dataset](https://huggingface.co/datasets/Aslan-mingye/OCR-Quality) |

</details>

<a id="f3-hybrid-document-parsing-workflows"></a>

<details>
<summary><strong>F3. Hybrid Document Parsing Workflows</strong></summary>

### Full Document Parsing Workflows

| Model / System | Date | Route | Paper | Code | Docs / Model |
|---|:---:|---|---|---|---|
| **MinerU-Popo** | 2026.05 | document-level post-processing for OCR outputs and document-tree assembly | [arXiv](https://arxiv.org/abs/2605.24973) | [GitHub](https://github.com/opendatalab/MinerU-Popo) | [HF](https://huggingface.co/DreamEternal/MinerU-Popo) |
| **MinerU / MinerU2.5-Pro** | 2024.09 / 2026.04 | layout decomposition + VLM parsing | [MinerU](https://arxiv.org/abs/2409.18839) / [2.5-Pro](https://arxiv.org/abs/2604.04771) | [GitHub](https://github.com/opendatalab/MinerU) | - |
| **Dolphin-v2** | 2026.02 | anchor prompting + document parsing workflow | [arXiv](https://arxiv.org/abs/2602.05384) | [GitHub](https://github.com/bytedance/Dolphin) | - |
| **Docling** | 2024.08 | production document conversion workflow | [arXiv](https://arxiv.org/abs/2408.09869) | [GitHub](https://github.com/docling-project/docling) | [Docs](https://docling-project.github.io/docling/) |

### PDF-to-Structured-Output Workflows

| Model / System | Date | Route | Paper | Code | Docs / Model |
|---|:---:|---|---|---|---|
| **Pix2Text** | 2024.08 | layout + formula + OCR workflow | [arXiv](https://arxiv.org/abs/2408.04015) | [GitHub](https://github.com/breezedeus/Pix2Text) | - |
| **Surya** | 2024 | OCR, layout, reading order, line detection | - | [GitHub](https://github.com/datalab-to/surya) | - |
| **Marker** | 2023 | PDF-to-Markdown workflow | - | [GitHub](https://github.com/datalab-to/marker) | - |

</details>

<a id="f4-general-purpose-vlms-used-as-ocr-interfaces"></a>

<details>
<summary><strong>F4. General-Purpose VLMs Used as OCR Interfaces</strong></summary>

### Open General VLMs

| Model / System | Date | OCR-Relevant Role | Paper | Code | Demo / Docs |
|---|:---:|---|---|---|---|
| **MiniCPM-V / MiniCPM-o** | 2024.08 / 2026.04 / 2026.05 | compact open VLM and omni-modal line with OCRBench-oriented small-model baselines | [MiniCPM-V](https://arxiv.org/abs/2408.01800), [MiniCPM-o 4.5](https://arxiv.org/abs/2604.27393) | [GitHub](https://github.com/OpenBMB/MiniCPM-V) | [HF 4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6), [Demo](https://minicpm-omni.openbmb.cn/) |
| **Granite Vision 4.1** | 2026.04 | enterprise VLM for visual document extraction, charts, tables, and key-value extraction | - | [GitHub](https://github.com/ibm-granite/granite-vision-models) | [HF](https://huggingface.co/ibm-granite/granite-vision-4.1-4b), [Docs](https://www.ibm.com/granite/docs/models/vision) |
| **Intern-S1 / Intern-S1-Pro** | 2025.08 / 2026.03 | scientific multimodal foundation models with general visual reasoning and OCR-rich scientific document understanding | [S1](https://arxiv.org/abs/2508.15763), [S1-Pro](https://arxiv.org/abs/2603.25040) | [GitHub](https://github.com/InternLM/Intern-S1) | [HF S1](https://huggingface.co/internlm/Intern-S1), [HF S1-Pro](https://huggingface.co/internlm/Intern-S1-Pro) |
| **STEP3-VL-10B** | 2026.01 | compact StepFun VLM for OCR, document, GUI, and visual reasoning at 10B scale | [arXiv](https://arxiv.org/abs/2601.09668) | [GitHub](https://github.com/stepfun-ai/Step3-VL-10B) | [HF](https://huggingface.co/stepfun-ai/Step3-VL-10B), [Project](https://stepfun-ai.github.io/Step3-VL-10B/) |
| **Qwen-VL family** | 2023.08 / 2024.09 / 2025.02 / 2025.11 | Qwen VLM family for visual text reading, dynamic resolution, long-context image/video/document prompting | [Qwen-VL](https://arxiv.org/abs/2308.12966), [Qwen2-VL](https://arxiv.org/abs/2409.12191), [Qwen2.5-VL](https://arxiv.org/abs/2502.13923), [Qwen3-VL](https://arxiv.org/abs/2511.21631) | [GitHub](https://github.com/QwenLM) | [Demo](https://chat.qwen.ai/) |
| **Nemotron Nano V2 VL** | 2025.11 | efficient NVIDIA VLM for OCRBench v2, document intelligence, long video, and multi-image reasoning | [arXiv](https://arxiv.org/abs/2511.03929) | - | [HF](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16), [Docs](https://docs.nvidia.com/nemo/megatron-bridge/latest/models/vlm/nemotron-nano-v2-vl.html) |
| **SAIL-VL2** | 2025.09 | ByteDance 2B/8B open VLM suite for fine-grained text-rich visual reasoning | [arXiv](https://arxiv.org/abs/2509.14033) | - | [HF 8B](https://huggingface.co/BytedanceDouyinContent/SAIL-VL2-8B), [Collection](https://huggingface.co/collections/BytedanceDouyinContent/sail-vl2) |
| **LLaVA family** | 2023.04 / 2024.07 / 2024.08 / 2025.09 | visual instruction tuning, interleaved input, and OneVision OCR-rich prompting | [LLaVA](https://arxiv.org/abs/2304.08485), [NeXT-Interleave](https://arxiv.org/abs/2407.07895), [OneVision](https://arxiv.org/abs/2408.03326), [OneVision-1.5](https://arxiv.org/abs/2509.23661) | [LLaVA](https://github.com/haotian-liu/LLaVA), [NeXT](https://github.com/LLaVA-VL/LLaVA-NeXT) | - |
| **InternVL family** | 2023.12 / 2024.04 / 2024.12 / 2025.04 / 2025.08 | open general VLM suite with high-resolution OCR and document prompting | [InternVL](https://arxiv.org/abs/2312.14238), [1.5](https://arxiv.org/abs/2404.16821), [2.5](https://arxiv.org/abs/2412.05271), [3](https://arxiv.org/abs/2504.10479), [3.5](https://arxiv.org/abs/2508.18265) | [GitHub](https://github.com/OpenGVLab/InternVL) | [Demo](https://chat.intern-ai.org.cn/) |
| **Ovis2.5** | 2025.08 | native-resolution open VLM for charts, documents, and dense visual perception | [arXiv](https://arxiv.org/abs/2508.11737) | [GitHub](https://github.com/AIDC-AI/Ovis) | [HF](https://huggingface.co/AIDC-AI/Ovis2.5-9B) |
| **Skywork-R1V / R1V2** | 2025.07 | open multimodal reasoning VLM for visual reasoning and OCR-rich perception | [arXiv](https://arxiv.org/abs/2507.06167) | [GitHub](https://github.com/SkyworkAI/Skywork-R1V) | [HF](https://huggingface.co/Skywork/Skywork-R1V2-38B) |
| **GLM-V family** | 2024.06 / 2025.07 | GLM-4V and GLM-4.1V/4.5V/4.6V for OCR-rich prompting, charts, documents, GUI, and tool use | [GLM-4V](https://arxiv.org/abs/2406.12793), [GLM-4.6V/4.5V/4.1V](https://arxiv.org/abs/2507.01006) | [GitHub](https://github.com/zai-org/GLM-V) | [HF 4.6V](https://huggingface.co/zai-org/GLM-4.6V), [HF 4.6V-Flash](https://huggingface.co/zai-org/GLM-4.6V-Flash) |
| **MiMo-VL** | 2025.06 | open visual-language reasoning model for GUI and OCR-rich general VLM evaluation | [arXiv](https://arxiv.org/abs/2506.03569) | [GitHub](https://github.com/XiaomiMiMo/MiMo-VL) | [HF](https://huggingface.co/XiaomiMiMo/MiMo-VL-7B-RL) |
| **Seed1.5-VL** | 2025.05 | general VLM baseline with text-rich image ability | [arXiv](https://arxiv.org/abs/2505.07062) | [GitHub](https://github.com/ByteDance-Seed/Seed1.5-VL) | - |
| **Aya Vision** | 2025.05 | open-weight multilingual VLM for OCR and visual reasoning across languages | [arXiv](https://arxiv.org/abs/2505.08751) | - | [HF](https://huggingface.co/CohereLabs/aya-vision-8b), [Docs](https://huggingface.co/docs/transformers/en/model_doc/aya_vision) |
| **Kimi-VL** | 2025.04 | general VLM OCR and document prompting | [arXiv](https://arxiv.org/abs/2504.07491) | [GitHub](https://github.com/MoonshotAI/Kimi-VL) | - |
| **Eagle 2 / Eagle 2.5** | 2025.01 / 2025.04 | NVIDIA data-centric VLM line for OCRBench, DocVQA, high-resolution image, and long-context multimodal evaluation | [Eagle 2](https://arxiv.org/abs/2501.14818), [2.5](https://arxiv.org/abs/2504.15271) | [GitHub](https://github.com/NVlabs/Eagle) | [HF Eagle2](https://huggingface.co/nvidia/Eagle2-9B), [Project](https://nvlabs.github.io/EAGLE/) |
| **SmolVLM / SmolVLM2** | 2025.02 / 2025.04 | compact open VLM and video-VLM family for efficient image/video understanding | [SmolVLM](https://arxiv.org/abs/2504.05299) | [GitHub](https://github.com/huggingface/smollm) | [SmolVLM](https://huggingface.co/blog/smolvlm), [SmolVLM2](https://huggingface.co/blog/smolvlm2) |
| **Phi-4-multimodal / Gemma 3** | 2025.03 / 2025.03 | compact and open multimodal baselines for image-text understanding and multilingual OCR prompting | [Phi-4](https://arxiv.org/abs/2503.01743), [Gemma 3](https://arxiv.org/abs/2503.19786) | - | [Phi-4 HF](https://huggingface.co/microsoft/Phi-4-multimodal-instruct), [Gemma 3 Blog](https://huggingface.co/blog/gemma3) |
| **Janus-Pro / MiniMax-VL-01** | 2025.01 / 2025.01 | open visual understanding and long-context VLM baselines for document and chart prompting | [Janus-Pro](https://arxiv.org/abs/2501.17811), [MiniMax-VL-01](https://arxiv.org/abs/2501.08313) | [Janus](https://github.com/deepseek-ai/Janus), [MiniMax-01](https://github.com/MiniMax-AI/MiniMax-01) | [Janus HF](https://huggingface.co/deepseek-ai/Janus-Pro-7B), [MiniMax HF](https://huggingface.co/MiniMaxAI/MiniMax-VL-01) |
| **FastVLM / DeepSeek-VL2 / PaliGemma 2** | 2024.12 / 2024.12 / 2024.12 | efficient and transfer-oriented VLM baselines with OCR/document use cases | [FastVLM](https://arxiv.org/abs/2412.13303), [DeepSeek-VL2](https://arxiv.org/abs/2412.10302), [PaliGemma 2](https://arxiv.org/abs/2412.03555) | [FastVLM](https://github.com/apple/ml-fastvlm), [DeepSeek-VL2](https://github.com/deepseek-ai/DeepSeek-VL2) | [FastVLM HF](https://huggingface.co/collections/apple/fastvlm), [PaliGemma 2 HF](https://huggingface.co/google/paligemma2-28b-mix-224) |
| **Pixtral / Aria** | 2024.10 / 2024.10 | open multimodal models for multi-image, long-context, OCR-rich prompting | [Pixtral 12B](https://arxiv.org/abs/2410.07073), [Aria](https://arxiv.org/abs/2410.05993) | [Aria](https://github.com/rhymes-ai/Aria) | [Pixtral HF](https://huggingface.co/mistralai/Pixtral-12B-2409) |
| **Molmo / NVLM** | 2024.09 / 2024.09 | open general VLM baselines for visual grounding, document, and OCR-rich perception | [Molmo](https://arxiv.org/abs/2409.17146), [NVLM](https://arxiv.org/abs/2409.11402) | [Molmo](https://github.com/allenai/molmo) | [NVLM HF](https://huggingface.co/nvidia) |
| **CogVLM / CogVLM2** | 2023.11 / 2024.08 | visual expert VLM baseline and high-resolution successor | [CogVLM](https://arxiv.org/abs/2311.03079), [CogVLM2](https://arxiv.org/abs/2408.16500) | [CogVLM](https://github.com/THUDM/CogVLM), [CogVLM2](https://github.com/THUDM/CogVLM2) | - |
| **mPLUG-Owl3** | 2024.08 | long image-sequence MLLM for multi-image and video visual-language tasks | [arXiv](https://arxiv.org/abs/2408.04840) | [GitHub](https://github.com/X-PLUG/mPLUG-Owl) | [HF](https://huggingface.co/mPLUG/mPLUG-Owl3-7B-241101) |
| **Idefics2 / Idefics3** | 2024.05 / 2024.08 | open Hugging Face VLM line for OCR, document understanding, and visual reasoning | [Idefics2](https://arxiv.org/abs/2405.02246), [Idefics3](https://arxiv.org/abs/2408.12637) | - | [Idefics2 HF](https://huggingface.co/HuggingFaceM4/idefics2-8b), [Idefics3 HF](https://huggingface.co/HuggingFaceM4/Idefics3-8B-Llama3) |
| **Mantis** | 2024.05 | interleaved multi-image instruction-tuned LMM with strong single-image and multi-image performance | [arXiv](https://arxiv.org/abs/2405.01483) | [GitHub](https://github.com/TIGER-AI-Lab/Mantis) | [HF](https://huggingface.co/TIGER-Lab/Mantis-8B-siglip-llama3) |
| **DeepSeek-VL / Yi-VL / Mini-Gemini** | 2024.03 / 2024.03 / 2024.03 | early 2024 open general VLM baselines for text-rich images and high-resolution visual detail | [DeepSeek-VL](https://arxiv.org/abs/2403.05525), [Yi-VL](https://arxiv.org/abs/2403.04652), [Mini-Gemini](https://arxiv.org/abs/2403.18814) | [DeepSeek-VL](https://github.com/deepseek-ai/DeepSeek-VL), [Yi](https://github.com/01-ai/Yi), [MGM](https://github.com/dvlab-research/MGM) | [Yi-VL HF](https://huggingface.co/01-ai/Yi-VL-34B), [MGM Project](https://mini-gemini.github.io/) |
| **BLIP-2 / MiniGPT-4 / InstructBLIP / Florence-2 / VILA** | 2023.01 / 2023.04 / 2023.05 / 2023.11 / 2023.12 | earlier open VLM baselines used as OCR interfaces before modern document-specialized VLMs | [BLIP-2](https://arxiv.org/abs/2301.12597), [MiniGPT-4](https://arxiv.org/abs/2304.10592), [InstructBLIP](https://arxiv.org/abs/2305.06500), [Florence-2](https://arxiv.org/abs/2311.06242), [VILA](https://arxiv.org/abs/2312.07533) | [LAVIS](https://github.com/salesforce/LAVIS), [MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4), [VILA](https://github.com/NVlabs/VILA) | [Florence-2 HF](https://huggingface.co/microsoft/Florence-2-large), [VILA Project](https://hanlab.mit.edu/projects/vila) |

### Closed/API General VLMs

| Model / System | Date | OCR-Relevant Role | Paper | Code | Demo / Docs |
|---|:---:|---|---|---|---|
| **GPT-4V / GPT-4o** | 2023-2024 | closed general VLM OCR interface | [GPT-4V system card](https://cdn.openai.com/papers/GPTV_System_Card.pdf) | - | [Docs](https://platform.openai.com/docs) |
| **Gemini family** | 2023.12 | closed general VLM OCR interface | [arXiv](https://arxiv.org/abs/2312.11805) | - | [Docs](https://ai.google.dev/gemini-api/docs) |
| **Claude 3 / 3.5 / 4** | 2024-2025 | closed general VLM OCR interface | - | - | [Docs](https://docs.anthropic.com/) |

</details>

<a id="f5-commercial-ocr-and-document-ai-services"></a>

<details>
<summary><strong>F5. Commercial OCR and Document AI Services</strong></summary>

### Enterprise OCR and Document AI

| System | Access Mode | Native Input | Output Contract | Docs / Website |
|---|---|---|---|---|
| **ABBYY FineReader / ABBYY Vantage** | commercial, on-prem / SDK / cloud | scanned document / PDF | searchable PDF, text, export formats, fields | [FineReader](https://www.abbyy.com/finereader/) / [Vantage](https://www.abbyy.com/vantage/) |
| **TextIn** | commercial cloud API | document / receipt / form | JSON, Markdown, key-value fields | [Website](https://www.textin.com/) |

### Scientific OCR and Managed Parsing APIs

| System | Access Mode | Native Input | Output Contract | Docs / Website |
|---|---|---|---|---|
| **Mathpix** | commercial cloud API | formula / paper / document | LaTeX / Markdown | [Website](https://mathpix.com/) |
| **Mistral OCR** | commercial cloud API | document / PDF / image | Markdown / structured response | [Docs](https://docs.mistral.ai/capabilities/document_ai/basic_ocr/) |
| **Qwen-OCR API** | commercial cloud API | document / image | structured OCR output | [Docs](https://help.aliyun.com/zh/model-studio/) |

</details>
