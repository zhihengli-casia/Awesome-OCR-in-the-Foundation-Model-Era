# Awesome OCR in the Foundation-Model Era

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-24292f?logo=github)](https://github.com/zhihengli-casia/Awesome-OCR-in-the-Foundation-Model-Era)
[![Maintained](https://img.shields.io/badge/Maintained-2026-blue)](https://github.com/zhihengli-casia/Awesome-OCR-in-the-Foundation-Model-Era/commits/main)
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

Badges indicate venue/source and year when available; GitHub badges link to public repositories when available. The Date column records the paper or public source date; active ranges such as `2020-2026` mark projects that continue to evolve beyond their first release. Repository-only entries use the public GitHub repository creation date. Entries are ordered newest first within each subsection.

<a id="f1-modular-ocr-toolkits-and-specialized-components"></a>

## F1. Modular OCR Toolkits and Specialized Components

Systems that follow or support the detector-recognizer pipeline: OCR engines, open toolkits, text detectors, cropped recognizers, formula recognizers, and structured-object components.

### OCR Engines and Toolkits

| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2020-2026 | [![Project 2020-2026](https://img.shields.io/badge/Project-2020--2026-24292f?logo=github)](https://github.com/PaddlePaddle/PaddleOCR)<br>**PaddleOCR / PP-OCR** | active industrial OCR toolkit; PP-OCR, PP-Structure, PP-FormulaNet, PaddleOCR-VL ecosystem | [Paper](https://arxiv.org/abs/2009.09941)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR)<br>[Docs](https://paddlepaddle.github.io/PaddleOCR/) |
| 2005-2026 | [![Project 2005-2026](https://img.shields.io/badge/Project-2005--2026-24292f?logo=github)](https://github.com/tesseract-ocr/tesseract)<br>**Tesseract** | active open-source OCR engine; LSTM OCR; searchable document workflows | [Paper](https://doi.org/10.1109/ICDAR.2007.4376991)<br>[GitHub](https://github.com/tesseract-ocr/tesseract)<br>[Docs](https://tesseract-ocr.github.io/) |
| 2026.03 | [![arXiv 2026.03](https://img.shields.io/badge/arXiv-2026.03-b31b1b)](https://arxiv.org/abs/2603.24373) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/PaddlePaddle/PaddleOCR)<br>**PP-OCRv5** | specialized 5M-parameter OCR model family; text detection and recognition in PaddleOCR 3.x | [Paper](https://arxiv.org/abs/2603.24373)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR)<br>[Docs](https://paddlepaddle.github.io/PaddleOCR/) |
| 2024.05 | [![GitHub 2024.05](https://img.shields.io/badge/GitHub-2024.05-24292f?logo=github)](https://github.com/topdu/openocr)<br>**OpenOCR** | open OCR training and evaluation toolkit; detection / recognition baselines | [GitHub](https://github.com/topdu/openocr) |
| 2021.08 | [![arXiv 2021.08](https://img.shields.io/badge/arXiv-2021.08-b31b1b)](https://arxiv.org/abs/2108.06543) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/open-mmlab/mmocr)<br>**MMOCR** | OCR research toolbox; detection/recognition/spotting | [Paper](https://arxiv.org/abs/2108.06543)<br>[GitHub](https://github.com/open-mmlab/mmocr)<br>[Docs](https://mmocr.readthedocs.io/) |
| 2021.01 | [![GitHub 2021.01](https://img.shields.io/badge/GitHub-2021.01-24292f?logo=github)](https://github.com/mindee/doctr)<br>**docTR** | document OCR toolkit; detection + recognition | [GitHub](https://github.com/mindee/doctr)<br>[Docs](https://mindee.github.io/doctr/) |
| 2021.01 | [![GitHub 2021.01](https://img.shields.io/badge/GitHub-2021.01-24292f?logo=github)](https://github.com/RapidAI/RapidOCR)<br>**RapidOCR** | lightweight OCR toolkit; ONNX / OpenVINO / Paddle / PyTorch backends | [GitHub](https://github.com/RapidAI/RapidOCR)<br>[Docs](https://rapidai.github.io/RapidOCRDocs/) |
| 2020.03 | [![GitHub 2020.03](https://img.shields.io/badge/GitHub-2020.03-24292f?logo=github)](https://github.com/JaidedAI/EasyOCR)<br>**EasyOCR** | ready-to-use OCR engine; multilingual OCR | [GitHub](https://github.com/JaidedAI/EasyOCR) |
| 2019.03 | [![GitHub 2019.03](https://img.shields.io/badge/GitHub-2019.03-24292f?logo=github)](https://github.com/breezedeus/CnOCR)<br>**CnOCR** | Chinese OCR toolkit; line/crop recognition | [GitHub](https://github.com/breezedeus/CnOCR)<br>[Docs](https://cnocr.readthedocs.io/) |
| 2013.12 | [![GitHub 2013.12](https://img.shields.io/badge/GitHub-2013.12-24292f?logo=github)](https://github.com/ocrmypdf/OCRmyPDF)<br>**OCRmyPDF** | searchable-PDF OCR workflow | [GitHub](https://github.com/ocrmypdf/OCRmyPDF)<br>[Docs](https://ocrmypdf.readthedocs.io/) |

### Text Detection and Spotting Components

| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2023 | [![CVPR 2023](https://img.shields.io/badge/CVPR-2023-4b4b4b)](https://arxiv.org/abs/2211.10772)<br>**DeepSolo** | explicit-point transformer text spotting | [Paper](https://arxiv.org/abs/2211.10772) |
| 2023 | [![AAAI 2023](https://img.shields.io/badge/AAAI-2023-4b4b4b)](https://arxiv.org/abs/2207.04491)<br>**DPText-DETR** | dynamic-point transformer text detection | [Paper](https://arxiv.org/abs/2207.04491) |
| 2023 | [![TPAMI 2023](https://img.shields.io/badge/TPAMI-2023-4b4b4b)](https://doi.org/10.1109/TPAMI.2022.3155612) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/MhLiao/DB)<br>**DBNet++** | adaptive-scale DB text detection | [Paper](https://doi.org/10.1109/TPAMI.2022.3155612)<br>[GitHub](https://github.com/MhLiao/DB) |
| 2022 | [![CVPR 2022](https://img.shields.io/badge/CVPR-2022-4b4b4b)](https://arxiv.org/abs/2204.01918)<br>**Text Spotting Transformer** | transformer-based end-to-end spotting | [Paper](https://arxiv.org/abs/2204.01918) |
| 2022 | [![ACM MM 2022](https://img.shields.io/badge/ACM%20MM-2022-4b4b4b)](https://arxiv.org/abs/2112.07917)<br>**SPTS** | single-point text spotting via sequence generation | [Paper](https://arxiv.org/abs/2112.07917) |
| 2021 | [![CVPR 2021](https://img.shields.io/badge/CVPR-2021-4b4b4b)](https://arxiv.org/abs/2104.10442)<br>**FCENet** | Fourier-contour text detection | [Paper](https://arxiv.org/abs/2104.10442) |
| 2021 | [![CVPR 2021](https://img.shields.io/badge/CVPR-2021-4b4b4b)](https://arxiv.org/abs/2104.01070)<br>**MOST** | multi-oriented detector with localization refinement | [Paper](https://arxiv.org/abs/2104.01070) |
| 2020 | [![CVPR 2020](https://img.shields.io/badge/CVPR-2020-4b4b4b)](https://doi.org/10.1109/CVPR42600.2020.01177)<br>**ContourNet** | contour-based arbitrary-shape detector | [Paper](https://doi.org/10.1109/CVPR42600.2020.01177) |
| 2020 | [![CVPR 2020](https://img.shields.io/badge/CVPR-2020-4b4b4b)](https://doi.org/10.1109/CVPR42600.2020.00972)<br>**DRRG** | graph-reasoning arbitrary-shape detector | [Paper](https://doi.org/10.1109/CVPR42600.2020.00972) |
| 2020 | [![AAAI 2020](https://img.shields.io/badge/AAAI-2020-4b4b4b)](https://doi.org/10.1609/aaai.v34i07.6812) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/MhLiao/DB)<br>**DBNet** | differentiable-binarization text detection | [Paper](https://doi.org/10.1609/aaai.v34i07.6812)<br>[GitHub](https://github.com/MhLiao/DB) |
| 2019 | [![CVPR 2019](https://img.shields.io/badge/CVPR-2019-4b4b4b)](https://arxiv.org/abs/1904.01941) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/clovaai/CRAFT-pytorch)<br>**CRAFT** | character-region text detection | [Paper](https://arxiv.org/abs/1904.01941)<br>[GitHub](https://github.com/clovaai/CRAFT-pytorch) |
| 2019 | [![CVPR 2019](https://img.shields.io/badge/CVPR-2019-4b4b4b)](https://arxiv.org/abs/1806.02559) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/whai362/PSENet)<br>**PSENet** | arbitrary-shape text detection | [Paper](https://arxiv.org/abs/1806.02559)<br>[GitHub](https://github.com/whai362/PSENet) |
| 2019 | [![ICCV 2019](https://img.shields.io/badge/ICCV-2019-4b4b4b)](https://doi.org/10.1109/ICCV.2019.00853)<br>**PAN** | pixel aggregation for arbitrary-shape text detection | [Paper](https://doi.org/10.1109/ICCV.2019.00853) |
| 2018 | [![ECCV 2018](https://img.shields.io/badge/ECCV-2018-4b4b4b)](https://arxiv.org/abs/1807.01544)<br>**TextSnake** | flexible representation for arbitrary-shape text | [Paper](https://arxiv.org/abs/1807.01544) |
| 2018 | [![AAAI 2018](https://img.shields.io/badge/AAAI-2018-4b4b4b)](https://arxiv.org/abs/1801.01315)<br>**PixelLink** | instance-segmentation text detector | [Paper](https://arxiv.org/abs/1801.01315) |
| 2018 | [![TIP 2018](https://img.shields.io/badge/TIP-2018-4b4b4b)](https://doi.org/10.1109/TIP.2018.2825107)<br>**TextBoxes++** | oriented scene text detector | [Paper](https://doi.org/10.1109/TIP.2018.2825107) |
| 2017 | [![CVPR 2017](https://img.shields.io/badge/CVPR-2017-4b4b4b)](https://arxiv.org/abs/1704.03155)<br>**EAST** | text detection; dense prediction | [Paper](https://arxiv.org/abs/1704.03155) |
| 2017 | [![AAAI 2017](https://img.shields.io/badge/AAAI-2017-4b4b4b)](https://ojs.aaai.org/index.php/AAAI/article/view/11196)<br>**TextBoxes** | single-shot horizontal text detector | [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/11196) |
| 2016 | [![ECCV 2016](https://img.shields.io/badge/ECCV-2016-4b4b4b)](https://arxiv.org/abs/1609.03605)<br>**CTPN** | connectionist text proposal network | [Paper](https://arxiv.org/abs/1609.03605) |

### Cropped Text Recognizers

| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2024.11 | [![arXiv 2024.11](https://img.shields.io/badge/arXiv-2024.11-b31b1b)](https://arxiv.org/abs/2411.15858) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/PaddlePaddle/PaddleOCR)<br>**SVTRv2** | upgraded cropped recognizer | [Paper](https://arxiv.org/abs/2411.15858)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| 2023 | [![AAAI 2023](https://img.shields.io/badge/AAAI-2023-4b4b4b)](https://arxiv.org/abs/2109.10282)<br>**TrOCR** | pretrained encoder-decoder recognizer | [Paper](https://arxiv.org/abs/2109.10282)<br>[HF Docs](https://huggingface.co/docs/transformers/model_doc/trocr) |
| 2022 | [![ECCV 2022](https://img.shields.io/badge/ECCV-2022-4b4b4b)](https://arxiv.org/abs/2209.03592)<br>**MGP-STR** | multi-granularity prediction recognizer | [Paper](https://arxiv.org/abs/2209.03592) |
| 2022 | [![ECCV 2022](https://img.shields.io/badge/ECCV-2022-4b4b4b)](https://arxiv.org/abs/2207.06966) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/baudm/parseq)<br>**PARSeq** | permuted autoregressive recognizer | [Paper](https://arxiv.org/abs/2207.06966)<br>[GitHub](https://github.com/baudm/parseq) |
| 2022 | [![IJCAI 2022](https://img.shields.io/badge/IJCAI-2022-4b4b4b)](https://doi.org/10.24963/ijcai.2022/124) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/PaddlePaddle/PaddleOCR)<br>**SVTR** | efficient single-visual-model recognizer | [Paper](https://doi.org/10.24963/ijcai.2022/124)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| 2021 | [![IJCV 2021](https://img.shields.io/badge/IJCV-2021-4b4b4b)](https://arxiv.org/abs/2111.11011)<br>**CDistNet** | multi-domain character-distance recognizer | [Paper](https://arxiv.org/abs/2111.11011) |
| 2021 | [![ICCV 2021](https://img.shields.io/badge/ICCV-2021-4b4b4b)](https://arxiv.org/abs/2108.09661)<br>**VisionLAN** | visual-language modeling recognizer | [Paper](https://arxiv.org/abs/2108.09661) |
| 2021 | [![ICDAR 2021](https://img.shields.io/badge/ICDAR-2021-4b4b4b)](https://arxiv.org/abs/2105.08582) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/roatienza/deep-text-recognition-benchmark)<br>**ViTSTR** | ViT recognizer | [Paper](https://arxiv.org/abs/2105.08582)<br>[GitHub](https://github.com/roatienza/deep-text-recognition-benchmark) |
| 2021 | [![CVPR 2021](https://img.shields.io/badge/CVPR-2021-4b4b4b)](https://arxiv.org/abs/2103.06495)<br>**ABINet** | language-aware recognizer | [Paper](https://arxiv.org/abs/2103.06495) |
| 2021 | [![PR 2021](https://img.shields.io/badge/PR-2021-4b4b4b)](https://doi.org/10.1016/j.patcog.2021.107980)<br>**MASTER** | multi-aspect non-local recognizer | [Paper](https://doi.org/10.1016/j.patcog.2021.107980) |
| 2020 | [![ECCV 2020](https://img.shields.io/badge/ECCV-2020-4b4b4b)](https://arxiv.org/abs/2007.07542)<br>**RobustScanner** | positional-clue enhanced recognizer | [Paper](https://arxiv.org/abs/2007.07542) |
| 2020 | [![CVPR 2020](https://img.shields.io/badge/CVPR-2020-4b4b4b)](https://arxiv.org/abs/2003.12294)<br>**SRN** | semantic reasoning recognizer | [Paper](https://arxiv.org/abs/2003.12294) |
| 2020 | [![CVPR 2020](https://img.shields.io/badge/CVPR-2020-4b4b4b)](https://arxiv.org/abs/2003.11288)<br>**SCATTER** | selective-context attention recognizer | [Paper](https://arxiv.org/abs/2003.11288) |
| 2020 | [![AAAI 2020](https://img.shields.io/badge/AAAI-2020-4b4b4b)](https://arxiv.org/abs/1912.12422)<br>**TextScanner** | order-aware character scanner | [Paper](https://arxiv.org/abs/1912.12422) |
| 2020 | [![AAAI 2020](https://img.shields.io/badge/AAAI-2020-4b4b4b)](https://arxiv.org/abs/1912.10205)<br>**DAN** | decoupled attention recognizer | [Paper](https://arxiv.org/abs/1912.10205) |
| 2020 | [![CVPRW 2020](https://img.shields.io/badge/CVPRW-2020-4b4b4b)](https://arxiv.org/abs/1910.04396)<br>**SATRN** | 2D self-attention text recognizer | [Paper](https://arxiv.org/abs/1910.04396) |
| 2019 | [![TPAMI 2019](https://img.shields.io/badge/TPAMI-2019-4b4b4b)](https://doi.org/10.1109/TPAMI.2018.2848939) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/bgshih/aster)<br>**ASTER** | rectified irregular text recognition | [Paper](https://doi.org/10.1109/TPAMI.2018.2848939)<br>[GitHub](https://github.com/bgshih/aster) |
| 2019 | [![PR 2019](https://img.shields.io/badge/PR-2019-4b4b4b)](https://doi.org/10.1016/j.patcog.2019.01.020)<br>**MORAN** | rectified attention recognizer | [Paper](https://doi.org/10.1016/j.patcog.2019.01.020) |
| 2019 | [![ICDAR 2019](https://img.shields.io/badge/ICDAR-2019-4b4b4b)](https://doi.org/10.1109/ICDAR.2019.00130)<br>**NRTR** | no-recurrence seq2seq recognizer | [Paper](https://doi.org/10.1109/ICDAR.2019.00130) |
| 2017 | [![TPAMI 2017](https://img.shields.io/badge/TPAMI-2017-4b4b4b)](https://doi.org/10.1109/TPAMI.2016.2646371) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/meijieru/crnn.pytorch)<br>**CRNN** | cropped sequence recognition; CTC | [Paper](https://doi.org/10.1109/TPAMI.2016.2646371)<br>[GitHub](https://github.com/meijieru/crnn.pytorch) |
| 2016 | [![CVPR 2016](https://img.shields.io/badge/CVPR-2016-4b4b4b)](https://doi.org/10.1109/CVPR.2016.452)<br>**RARE** | rectified attention recognizer | [Paper](https://doi.org/10.1109/CVPR.2016.452) |

### Formula, Table, and Structured-Object Components

| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2026.02 | [![arXiv 2026.02](https://img.shields.io/badge/arXiv-2026.02-b31b1b)](https://arxiv.org/abs/2602.17189)<br>**Texo** | 20M-parameter formula recognizer | [Paper](https://arxiv.org/abs/2602.17189) |
| 2025.03 | [![arXiv 2025.03](https://img.shields.io/badge/arXiv-2025.03-b31b1b)](https://arxiv.org/abs/2503.18382) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/PaddlePaddle/PaddleOCR)<br>**PP-FormulaNet** | formula recognition; PaddleOCR component | [Paper](https://arxiv.org/abs/2503.18382)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| 2024.04 | [![arXiv 2024.04](https://img.shields.io/badge/arXiv-2024.04-b31b1b)](https://arxiv.org/abs/2404.15254) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/opendatalab/UniMERNet)<br>**UniMERNet** | formula recognition; LaTeX output | [Paper](https://arxiv.org/abs/2404.15254)<br>[GitHub](https://github.com/opendatalab/UniMERNet) |
| 2024 | [![CVPR 2024](https://img.shields.io/badge/CVPR-2024-4b4b4b)](https://arxiv.org/abs/2410.12628)<br>**DocLayout-YOLO** | document layout detection | [Paper](https://arxiv.org/abs/2410.12628) |
| 2024 | [![IJCAI 2024](https://img.shields.io/badge/IJCAI-2024-4b4b4b)](https://doi.org/10.24963/ijcai.2024/105)<br>**TFLOP** | table structure recognition with layout pointer | [Paper](https://doi.org/10.24963/ijcai.2024/105) |
| 2022.10 | [![arXiv 2022.10](https://img.shields.io/badge/arXiv-2022.10-b31b1b)](https://arxiv.org/abs/2210.08208)<br>**GrTS** | grounded table structure recognition | [Paper](https://arxiv.org/abs/2210.08208) |
| 2022.09 | [![GitHub 2022.09](https://img.shields.io/badge/GitHub-2022.09-24292f?logo=github)](https://github.com/AlibabaResearch/AdvancedLiterateMachinery)<br>**StructEqTable** | equation/table structure parsing | [GitHub](https://github.com/AlibabaResearch/AdvancedLiterateMachinery) |
| 2022.03 | [![arXiv 2022.03](https://img.shields.io/badge/arXiv-2022.03-b31b1b)](https://arxiv.org/abs/2203.01017)<br>**TableFormer** | table structure recognition; table-to-HTML modeling | [Paper](https://arxiv.org/abs/2203.01017) |
| 2022 | [![ICPR 2022](https://img.shields.io/badge/ICPR-2022-4b4b4b)](https://arxiv.org/abs/2207.11463)<br>**BTTR** | transformer formula recognition | [Paper](https://arxiv.org/abs/2207.11463) |
| 2022 | [![PR 2022](https://img.shields.io/badge/PR-2022-4b4b4b)](https://doi.org/10.1016/j.patcog.2022.109006)<br>**LGPMA** | table detection and structure recognition | [Paper](https://doi.org/10.1016/j.patcog.2022.109006) |
| 2021.10 | [![arXiv 2021.10](https://img.shields.io/badge/arXiv-2021.10-b31b1b)](https://arxiv.org/abs/2110.00061) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/microsoft/table-transformer)<br>**Table Transformer / TATR** | table detection and structure recognition; PubTables-1M baseline | [Paper](https://arxiv.org/abs/2110.00061)<br>[GitHub](https://github.com/microsoft/table-transformer) |
| 2021 | [![ICDAR 2021](https://img.shields.io/badge/ICDAR-2021-4b4b4b)](https://arxiv.org/abs/2105.01848)<br>**TableMaster** | sequence-based table-to-HTML recognizer | [Paper](https://arxiv.org/abs/2105.01848) |
| 2020.12 | [![GitHub 2020.12](https://img.shields.io/badge/GitHub-2020.12-24292f?logo=github)](https://github.com/lukas-blecher/LaTeX-OCR)<br>**pix2tex / LaTeX-OCR** | formula image to LaTeX | [GitHub](https://github.com/lukas-blecher/LaTeX-OCR) |
| 2020.04 | [![arXiv 2020.04](https://img.shields.io/badge/arXiv-2020.04-b31b1b)](https://arxiv.org/abs/2004.12629) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/DevashishPrasad/CascadeTabNet)<br>**CascadeTabNet** | end-to-end table detection and structure recognition | [Paper](https://arxiv.org/abs/2004.12629)<br>[GitHub](https://github.com/DevashishPrasad/CascadeTabNet) |
| 2020 | [![ECCV 2020](https://img.shields.io/badge/ECCV-2020-4b4b4b)](https://arxiv.org/abs/1911.10683)<br>**PubTabNet / EDD** | table structure recognition baseline | [Paper](https://arxiv.org/abs/1911.10683) |
| 2017 | [![PR 2017](https://img.shields.io/badge/PR-2017-4b4b4b)](https://doi.org/10.1016/j.patcog.2017.06.017)<br>**WAP** | handwritten mathematical expression recognition | [Paper](https://doi.org/10.1016/j.patcog.2017.06.017) |
| 2016.09 | [![arXiv 2016.09](https://img.shields.io/badge/arXiv-2016.09-b31b1b)](https://arxiv.org/abs/1609.04938)<br>**Im2Markup** | image-to-LaTeX generation | [Paper](https://arxiv.org/abs/1609.04938) |

<a id="f2-foundation-model-document-parsers"></a>

## F2. Foundation-Model Document Parsers

End-to-end or near end-to-end models that read page images and generate structured representations such as Markdown, HTML, LaTeX, JSON, or OCR-formatted text.

### OCR-Free and Transitional Encoder-Decoders

| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2023.09 | [![arXiv 2023.09](https://img.shields.io/badge/arXiv-2023.09-b31b1b)](https://arxiv.org/abs/2309.11419)<br>**KOSMOS-2.5** | spatially-aware text block + Markdown generation | [Paper](https://arxiv.org/abs/2309.11419) |
| 2023.08 | [![arXiv 2023.08](https://img.shields.io/badge/arXiv-2023.08-b31b1b)](https://arxiv.org/abs/2308.13418) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/facebookresearch/nougat)<br>**Nougat** | scholarly PDF-to-Markdown parser | [Paper](https://arxiv.org/abs/2308.13418)<br>[GitHub](https://github.com/facebookresearch/nougat) |
| 2023 | [![CVPR 2023](https://img.shields.io/badge/CVPR-2023-4b4b4b)](https://arxiv.org/abs/2212.02623)<br>**UDOP** | unified vision-text-layout generation | [Paper](https://arxiv.org/abs/2212.02623) |
| 2023 | [![ICML 2023](https://img.shields.io/badge/ICML-2023-4b4b4b)](https://arxiv.org/abs/2210.03347) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/google-research/pix2struct)<br>**Pix2Struct** | screenshot/page-to-sequence pretraining | [Paper](https://arxiv.org/abs/2210.03347)<br>[GitHub](https://github.com/google-research/pix2struct) |
| 2022 | [![ECCV 2022](https://img.shields.io/badge/ECCV-2022-4b4b4b)](https://arxiv.org/abs/2111.15664) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/clovaai/donut)<br>**Donut** | OCR-free encoder-decoder; document understanding | [Paper](https://arxiv.org/abs/2111.15664)<br>[GitHub](https://github.com/clovaai/donut) |

### Early Document VLMs

| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2024.10 | [![arXiv 2024.10](https://img.shields.io/badge/arXiv-2024.10-b31b1b)](https://arxiv.org/abs/2410.05261)<br>**TextHawk2** | bilingual OCR and grounding MLLM | [Paper](https://arxiv.org/abs/2410.05261)<br>[Hugging Face](https://huggingface.co/TencentBAC) |
| 2024.09 | [![arXiv 2024.09](https://img.shields.io/badge/arXiv-2024.09-b31b1b)](https://arxiv.org/abs/2409.03420) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/X-PLUG/mPLUG-DocOwl)<br>**DocOwl 2** | high-resolution multi-page document VLM | [Paper](https://arxiv.org/abs/2409.03420)<br>[GitHub](https://github.com/X-PLUG/mPLUG-DocOwl) |
| 2024.09 | [![arXiv 2024.09](https://img.shields.io/badge/arXiv-2024.09-b31b1b)](https://arxiv.org/abs/2409.01704) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/Ucas-HaoranWei/GOT-OCR2.0)<br>**GOT-OCR 2.0** | unified OCR-specialized VLM | [Paper](https://arxiv.org/abs/2409.01704)<br>[GitHub](https://github.com/Ucas-HaoranWei/GOT-OCR2.0) |
| 2024.05 | [![arXiv 2024.05](https://img.shields.io/badge/arXiv-2024.05-b31b1b)](https://arxiv.org/abs/2405.14295) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/ucaslcl/Fox)<br>**Fox** | multi-page document understanding system | [Paper](https://arxiv.org/abs/2405.14295)<br>[GitHub](https://github.com/ucaslcl/Fox) |
| 2024.04 | [![arXiv 2024.04](https://img.shields.io/badge/arXiv-2024.04-b31b1b)](https://arxiv.org/abs/2404.09204)<br>**TextHawk** | fine-grained text perception in MLLMs | [Paper](https://arxiv.org/abs/2404.09204)<br>[Hugging Face](https://huggingface.co/TencentBAC) |
| 2024.04 | [![arXiv 2024.04](https://img.shields.io/badge/arXiv-2024.04-b31b1b)](https://arxiv.org/abs/2404.05225)<br>**LayoutLLM** | layout instruction tuning for document understanding | [Paper](https://arxiv.org/abs/2404.05225) |
| 2024.03 | [![arXiv 2024.03](https://img.shields.io/badge/arXiv-2024.03-b31b1b)](https://arxiv.org/abs/2403.12895) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/X-PLUG/mPLUG-DocOwl)<br>**DocOwl 1.5** | OCR-free structure learning | [Paper](https://arxiv.org/abs/2403.12895)<br>[GitHub](https://github.com/X-PLUG/mPLUG-DocOwl) |
| 2024.03 | [![arXiv 2024.03](https://img.shields.io/badge/arXiv-2024.03-b31b1b)](https://arxiv.org/abs/2403.04473) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/Yuliang-Liu/Monkey)<br>**TextMonkey** | OCR-free document MLLM | [Paper](https://arxiv.org/abs/2403.04473)<br>[GitHub](https://github.com/Yuliang-Liu/Monkey) |
| 2024 | [![CVPR 2024](https://img.shields.io/badge/CVPR-2024-4b4b4b)](https://arxiv.org/abs/2311.06607) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/Yuliang-Liu/Monkey)<br>**Monkey** | text-centric MLLM | [Paper](https://arxiv.org/abs/2311.06607)<br>[GitHub](https://github.com/Yuliang-Liu/Monkey) |
| 2023.12 | [![arXiv 2023.12](https://img.shields.io/badge/arXiv-2023.12-b31b1b)](https://arxiv.org/abs/2312.06109) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/Ucas-HaoranWei/Vary)<br>**Vary** | document-specialized VLM | [Paper](https://arxiv.org/abs/2312.06109)<br>[GitHub](https://github.com/Ucas-HaoranWei/Vary) |
| 2023.10 | [![arXiv 2023.10](https://img.shields.io/badge/arXiv-2023.10-b31b1b)](https://arxiv.org/abs/2310.05126)<br>**UReader** | OCR-free visually situated language understanding | [Paper](https://arxiv.org/abs/2310.05126) |
| 2023.07 | [![arXiv 2023.07](https://img.shields.io/badge/arXiv-2023.07-b31b1b)](https://arxiv.org/abs/2307.02499) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/X-PLUG/mPLUG-DocOwl)<br>**DocOwl** | document-oriented VLM | [Paper](https://arxiv.org/abs/2307.02499)<br>[GitHub](https://github.com/X-PLUG/mPLUG-DocOwl) |

### 2025-2026 OCR-Specialized Parsers

| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2026.05 | [![arXiv 2026.05](https://img.shields.io/badge/arXiv-2026.05-b31b1b)](https://arxiv.org/abs/2605.27978)<br>**ABot-OCR** | AMap end-to-end OCR VLM; page image to clean Markdown; structure-constrained RL | [Paper](https://arxiv.org/abs/2605.27978) |
| 2026.03 | [![arXiv 2026.03](https://img.shields.io/badge/arXiv-2026.03-b31b1b)](https://arxiv.org/abs/2603.13398)<br>**Qianfan-OCR** | end-to-end document intelligence model | [Paper](https://arxiv.org/abs/2603.13398)<br>[Website](https://cloud.baidu.com/product/wenxinworkshop) |
| 2026.03 | [![arXiv 2026.03](https://img.shields.io/badge/arXiv-2026.03-b31b1b)](https://arxiv.org/abs/2603.10910)<br>**GLM-OCR** | OCR-specialized document parser | [Paper](https://arxiv.org/abs/2603.10910) |
| 2026.03 | [![arXiv 2026.03](https://img.shields.io/badge/arXiv-2026.03-b31b1b)](https://arxiv.org/abs/2603.01840) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/FireRedTeam/FireRed-OCR)<br>**FireRed-OCR** | OCR-specialized VLM | [Paper](https://arxiv.org/abs/2603.01840)<br>[GitHub](https://github.com/FireRedTeam/FireRed-OCR) |
| 2026.03 | [![arXiv 2026.03](https://img.shields.io/badge/arXiv-2026.03-b31b1b)](https://arxiv.org/abs/2603.09677) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/alibaba/Logics-Parsing)<br>**Logics-Parsing-Omni** | Alibaba unified parser for heterogeneous documents and videos | [Paper](https://arxiv.org/abs/2603.09677)<br>[GitHub](https://github.com/alibaba/Logics-Parsing) |
| 2026.03 | [![arXiv 2026.03](https://img.shields.io/badge/arXiv-2026.03-b31b1b)](https://arxiv.org/abs/2603.13032) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/rednote-hilab/dots.mocr)<br>**MOCR / dots.mocr** | RedNote/Xiaohongshu multimodal OCR parser; text, charts, diagrams, tables, icons, and code-level outputs | [Paper](https://arxiv.org/abs/2603.13032)<br>[GitHub](https://github.com/rednote-hilab/dots.mocr) |
| 2026.01 | [![arXiv 2026.01](https://img.shields.io/badge/arXiv-2026.01-b31b1b)](https://arxiv.org/abs/2601.21957) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/PaddlePaddle/PaddleOCR)<br>**PaddleOCR-VL-1.5** | compact multi-task document parsing VLM | [Paper](https://arxiv.org/abs/2601.21957)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| 2026.01 | [![arXiv 2026.01](https://img.shields.io/badge/arXiv-2026.01-b31b1b)](https://arxiv.org/abs/2601.20552) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/deepseek-ai/DeepSeek-OCR)<br>**DeepSeek-OCR 2** | causal-flow reordering and document parsing | [Paper](https://arxiv.org/abs/2601.20552)<br>[GitHub](https://github.com/deepseek-ai/DeepSeek-OCR) |
| 2026.01 | [![arXiv 2026.01](https://img.shields.io/badge/arXiv-2026.01-b31b1b)](https://arxiv.org/abs/2601.14490)<br>**GutenOCR** | grounded OCR front-end fine-tuned from Qwen2.5-VL | [Paper](https://arxiv.org/abs/2601.14490) |
| 2026.01 | [![arXiv 2026.01](https://img.shields.io/badge/arXiv-2026.01-b31b1b)](https://arxiv.org/abs/2601.14251)<br>**LightOnOCR-2-1B** | 1B multilingual end-to-end OCR VLM | [Paper](https://arxiv.org/abs/2601.14251) |
| 2026.01 | [![arXiv 2026.01](https://img.shields.io/badge/arXiv-2026.01-b31b1b)](https://arxiv.org/abs/2601.21639)<br>**OCRVerse** | Meituan holistic OCR VLM; unified text-centric and vision-centric OCR | [Paper](https://arxiv.org/abs/2601.21639) |
| 2026 | [![GitHub 2026](https://img.shields.io/badge/GitHub-2026-24292f?logo=github)](https://github.com/datalab-to/chandra)<br>**Chandra / Chandra OCR 2** | full-page HTML / Markdown / JSON OCR model | [GitHub](https://github.com/datalab-to/chandra)<br>[HF](https://huggingface.co/datalab-to/chandra-ocr-2)<br>[Blog](https://landing.datalab.to/blog/introducing-chandra) |
| 2026 | [![HF 2026](https://img.shields.io/badge/HF-2026-ffcc4d?logo=huggingface)](https://huggingface.co/ibm-granite/granite-docling-258M)<br>**Granite-Docling-258M** | compact DocTags document conversion model | [Hugging Face](https://huggingface.co/ibm-granite/granite-docling-258M) |
| 2025.12 | [![arXiv 2025.12](https://img.shields.io/badge/arXiv-2025.12-b31b1b)](https://arxiv.org/abs/2512.02498)<br>**dots.ocr** | multilingual document layout parsing VLM | [Paper](https://arxiv.org/abs/2512.02498) |
| 2025.11 | [![arXiv 2025.11](https://img.shields.io/badge/arXiv-2025.11-b31b1b)](https://arxiv.org/abs/2511.19575)<br>**HunyuanOCR** | OCR-specialized document VLM | [Paper](https://arxiv.org/abs/2511.19575) |
| 2025.10 | [![arXiv 2025.10](https://img.shields.io/badge/arXiv-2025.10-b31b1b)](https://arxiv.org/abs/2510.19817) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/allenai/olmocr)<br>**olmOCR-2** | unit-test reward training for document OCR | [Paper](https://arxiv.org/abs/2510.19817)<br>[GitHub](https://github.com/allenai/olmocr) |
| 2025.10 | [![arXiv 2025.10](https://img.shields.io/badge/arXiv-2025.10-b31b1b)](https://arxiv.org/abs/2510.18234) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/deepseek-ai/DeepSeek-OCR)<br>**DeepSeek-OCR** | visual token compression for OCR | [Paper](https://arxiv.org/abs/2510.18234)<br>[GitHub](https://github.com/deepseek-ai/DeepSeek-OCR) |
| 2025.10 | [![arXiv 2025.10](https://img.shields.io/badge/arXiv-2025.10-b31b1b)](https://arxiv.org/abs/2510.14528) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/PaddlePaddle/PaddleOCR)<br>**PaddleOCR-VL** | compact multilingual document parsing VLM | [Paper](https://arxiv.org/abs/2510.14528)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| 2025.09 | [![arXiv 2025.09](https://img.shields.io/badge/arXiv-2025.09-b31b1b)](https://arxiv.org/abs/2509.19760) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/alibaba/Logics-Parsing)<br>**Logics-Parsing** | Alibaba structured document parsing with logical extraction and LLM framework | [Paper](https://arxiv.org/abs/2509.19760)<br>[GitHub](https://github.com/alibaba/Logics-Parsing) |
| 2025.06 | [![arXiv 2025.06](https://img.shields.io/badge/arXiv-2025.06-b31b1b)](https://arxiv.org/abs/2506.18023)<br>**PP-DocBee2** | efficient data and stronger document baselines | [Paper](https://arxiv.org/abs/2506.18023) |
| 2025.06 | [![arXiv 2025.06](https://img.shields.io/badge/arXiv-2025.06-b31b1b)](https://arxiv.org/abs/2506.05218) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/Yuliang-Liu/MonkeyOCR)<br>**MonkeyOCR** | structure-recognition-relation document parser | [Paper](https://arxiv.org/abs/2506.05218)<br>[GitHub](https://github.com/Yuliang-Liu/MonkeyOCR) |
| 2025.03 | [![arXiv 2025.03](https://img.shields.io/badge/arXiv-2025.03-b31b1b)](https://arxiv.org/abs/2503.11576)<br>**SmolDocling** | ultra-compact document conversion VLM | [Paper](https://arxiv.org/abs/2503.11576)<br>[Hugging Face](https://huggingface.co/ds4sd/SmolDocling-256M-preview) |
| 2025.03 | [![arXiv 2025.03](https://img.shields.io/badge/arXiv-2025.03-b31b1b)](https://arxiv.org/abs/2503.04065)<br>**PP-DocBee** | multimodal document understanding baseline | [Paper](https://arxiv.org/abs/2503.04065) |
| 2025.02 | [![arXiv 2025.02](https://img.shields.io/badge/arXiv-2025.02-b31b1b)](https://arxiv.org/abs/2502.18443) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/allenai/olmocr)<br>**olmOCR** | open PDF-to-Markdown / page linearization model | [Paper](https://arxiv.org/abs/2502.18443)<br>[GitHub](https://github.com/allenai/olmocr) |
| 2025 | [![HF 2025](https://img.shields.io/badge/HF-2025-ffcc4d?logo=huggingface)](https://huggingface.co/nanonets/Nanonets-OCR-s)<br>**Nanonets-OCR-s** | 4B structured Markdown OCR model | [Hugging Face](https://huggingface.co/nanonets/Nanonets-OCR-s) |

### Emerging Generation and Training Routes

| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2026.03 | [![arXiv 2026.03](https://img.shields.io/badge/arXiv-2026.03-b31b1b)](https://arxiv.org/abs/2603.22458)<br>**MinerU-Diffusion** | diffusion-style inverse-rendering OCR | [Paper](https://arxiv.org/abs/2603.22458) |
| 2026.01 | [![arXiv 2026.01](https://img.shields.io/badge/arXiv-2026.01-b31b1b)](https://arxiv.org/abs/2601.08834)<br>**FDRL for Document OCR** | format-decoupled reinforcement learning | [Paper](https://arxiv.org/abs/2601.08834) |
| 2025.12 | [![arXiv 2025.12](https://img.shields.io/badge/arXiv-2025.12-b31b1b)](https://arxiv.org/abs/2512.18550) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/ZZZZZQT/DOCR-Inspector)<br>**DOCR-Inspector** | fine-grained evaluation and strategic optimization for document OCR parsing | [Paper](https://arxiv.org/abs/2512.18550)<br>[GitHub](https://github.com/ZZZZZQT/DOCR-Inspector) |
| 2025.08 | [![arXiv 2025.08](https://img.shields.io/badge/arXiv-2025.08-b31b1b)](https://arxiv.org/abs/2508.13238)<br>**DianJin-OCR-R1** | reasoning-and-tool interleaved OCR VLM route | [Paper](https://arxiv.org/abs/2508.13238) |

<a id="f3-hybrid-document-parsing-workflows"></a>

## F3. Hybrid Document Parsing Workflows

Systems that combine layout detection, OCR, region decomposition, VLM generation, rule-based validators, and document assembly.

### Full Document Parsing Workflows

| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2026.05 | [![arXiv 2026.05](https://img.shields.io/badge/arXiv-2026.05-b31b1b)](https://arxiv.org/abs/2605.13330) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/opendatalab/MinerU)<br>**MinerU-Popo** | post-processing tool for document parsing; layout/text/format repair | [Paper](https://arxiv.org/abs/2605.13330)<br>[GitHub](https://github.com/opendatalab/MinerU) |
| 2026.04 | [![arXiv 2026.04](https://img.shields.io/badge/arXiv-2026.04-b31b1b)](https://arxiv.org/abs/2604.04771) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/opendatalab/MinerU)<br>**MinerU2.5-Pro** | data-centric document parsing system | [Paper](https://arxiv.org/abs/2604.04771)<br>[GitHub](https://github.com/opendatalab/MinerU) |
| 2026.02 | [![arXiv 2026.02](https://img.shields.io/badge/arXiv-2026.02-b31b1b)](https://arxiv.org/abs/2602.05384) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/bytedance/Dolphin)<br>**Dolphin-v2** | anchor prompting + document parsing workflow | [Paper](https://arxiv.org/abs/2602.05384)<br>[GitHub](https://github.com/bytedance/Dolphin) |
| 2025.07 | [![arXiv 2025.07](https://img.shields.io/badge/arXiv-2025.07-b31b1b)](https://arxiv.org/abs/2507.05595) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/PaddlePaddle/PaddleOCR)<br>**PaddleOCR 3.0 / PP-StructureV3** | industrial document parsing toolkit | [Paper](https://arxiv.org/abs/2507.05595)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR)<br>[Docs](https://paddlepaddle.github.io/PaddleOCR/) |
| 2025.02 | [![arXiv 2025.02](https://img.shields.io/badge/arXiv-2025.02-b31b1b)](https://arxiv.org/abs/2502.16161)<br>**OmniParser V2** | structured-points-of-thought for unified visual text parsing | [Paper](https://arxiv.org/abs/2502.16161) |
| 2024.08 | [![arXiv 2024.08](https://img.shields.io/badge/arXiv-2024.08-b31b1b)](https://arxiv.org/abs/2408.09869) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/docling-project/docling)<br>**Docling** | production document conversion workflow | [Paper](https://arxiv.org/abs/2408.09869)<br>[GitHub](https://github.com/docling-project/docling)<br>[Docs](https://docling-project.github.io/docling/) |
| 2024.03 | [![arXiv 2024.03](https://img.shields.io/badge/arXiv-2024.03-b31b1b)](https://arxiv.org/abs/2403.19128)<br>**OmniParser** | unified text spotting, key information extraction, and table recognition | [Paper](https://arxiv.org/abs/2403.19128) |
| 2024.02 | [![GitHub 2024.02](https://img.shields.io/badge/GitHub-2024.02-24292f?logo=github)](https://github.com/opendatalab/MinerU)<br>**MinerU** | layout decomposition + document parsing workflow | [GitHub](https://github.com/opendatalab/MinerU) |
| 2022.10 | [![arXiv 2022.10](https://img.shields.io/badge/arXiv-2022.10-b31b1b)](https://arxiv.org/abs/2210.05391) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/PaddlePaddle/PaddleOCR)<br>**PP-Structure / PP-StructureV2** | layout + table + OCR document analysis workflow | [Paper](https://arxiv.org/abs/2210.05391)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR)<br>[Docs](https://paddlepaddle.github.io/PaddleOCR/) |
| 2022.09 | [![GitHub 2022.09](https://img.shields.io/badge/GitHub-2022.09-24292f?logo=github)](https://github.com/Unstructured-IO/unstructured)<br>**Unstructured** | document partitioning and ingestion workflow | [GitHub](https://github.com/Unstructured-IO/unstructured)<br>[Docs](https://docs.unstructured.io/) |

### PDF-to-Structured-Output Workflows

| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2024.11 | [![GitHub 2024.11](https://img.shields.io/badge/GitHub-2024.11-24292f?logo=github)](https://github.com/microsoft/markitdown)<br>**MarkItDown** | Microsoft document-to-Markdown conversion utility; PDF / Office / image ingestion | [GitHub](https://github.com/microsoft/markitdown) |
| 2024.01 | [![GitHub 2024.01](https://img.shields.io/badge/GitHub-2024.01-24292f?logo=github)](https://github.com/datalab-to/surya)<br>**Surya** | OCR, layout, reading order, line detection | [GitHub](https://github.com/datalab-to/surya) |
| 2023.10 | [![GitHub 2023.10](https://img.shields.io/badge/GitHub-2023.10-24292f?logo=github)](https://github.com/datalab-to/marker)<br>**Marker** | PDF-to-Markdown workflow | [GitHub](https://github.com/datalab-to/marker) |
| 2022.09 | [![GitHub 2022.09](https://img.shields.io/badge/GitHub-2022.09-24292f?logo=github)](https://github.com/breezedeus/Pix2Text)<br>**Pix2Text** | layout + formula + OCR workflow | [GitHub](https://github.com/breezedeus/Pix2Text) |
| 2015.08 | [![GitHub 2015.08](https://img.shields.io/badge/GitHub-2015.08-24292f?logo=github)](https://github.com/jsvine/pdfplumber)<br>**pdfplumber** | born-digital PDF text/table extraction utility | [GitHub](https://github.com/jsvine/pdfplumber)<br>[Docs](https://github.com/jsvine/pdfplumber) |
| 2012.10 | [![GitHub 2012.10](https://img.shields.io/badge/GitHub-2012.10-24292f?logo=github)](https://github.com/pymupdf/PyMuPDF)<br>**PyMuPDF** | PDF page rendering and extraction utility | [GitHub](https://github.com/pymupdf/PyMuPDF)<br>[Docs](https://pymupdf.readthedocs.io/) |
| 2012.09 | [![GitHub 2012.09](https://img.shields.io/badge/GitHub-2012.09-24292f?logo=github)](https://github.com/kermitt2/grobid)<br>**GROBID** | scholarly PDF structure extraction workflow | [GitHub](https://github.com/kermitt2/grobid)<br>[Docs](https://grobid.readthedocs.io/) |

<a id="f4-general-purpose-vlms-used-as-ocr-interfaces"></a>

## F4. General-Purpose VLMs Used as OCR Interfaces

General multimodal models that can perform OCR-related tasks through prompts, while OCR is only one part of their capability.

### Open General VLMs

| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2025.05 | [![arXiv 2025.05](https://img.shields.io/badge/arXiv-2025.05-b31b1b)](https://arxiv.org/abs/2505.07062)<br>**Seed1.5-VL** | general VLM baseline with text-rich image ability | [Paper](https://arxiv.org/abs/2505.07062) |
| 2025.04 | [![arXiv 2025.04](https://img.shields.io/badge/arXiv-2025.04-b31b1b)](https://arxiv.org/abs/2504.10479) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/OpenGVLab/InternVL)<br>**InternVL3** | open general VLM OCR baseline | [Paper](https://arxiv.org/abs/2504.10479)<br>[GitHub](https://github.com/OpenGVLab/InternVL)<br>[Demo](https://chat.intern-ai.org.cn/) |
| 2025.04 | [![arXiv 2025.04](https://img.shields.io/badge/arXiv-2025.04-b31b1b)](https://arxiv.org/abs/2504.07491)<br>**Kimi-VL** | general VLM OCR and document prompting | [Paper](https://arxiv.org/abs/2504.07491) |
| 2025.02 | [![arXiv 2025.02](https://img.shields.io/badge/arXiv-2025.02-b31b1b)](https://arxiv.org/abs/2502.13923) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/QwenLM/Qwen2.5-VL)<br>**Qwen2.5-VL** | general VLM OCR and document prompting | [Paper](https://arxiv.org/abs/2502.13923)<br>[GitHub](https://github.com/QwenLM/Qwen2.5-VL)<br>[Demo](https://chat.qwen.ai/) |
| 2025.02 | [![arXiv 2025.02](https://img.shields.io/badge/arXiv-2025.02-b31b1b)](https://arxiv.org/abs/2502.05371)<br>**Phi-4-multimodal / Phi-4-Vision** | compact general VLM baseline | [Paper](https://arxiv.org/abs/2502.05371)<br>[Hugging Face](https://huggingface.co/microsoft/Phi-4-multimodal-instruct) |
| 2025.01 | [![arXiv 2025.01](https://img.shields.io/badge/arXiv-2025.01-b31b1b)](https://arxiv.org/abs/2501.04658) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/OpenGVLab/InternVL)<br>**InternVL2.5** | open general VLM suite | [Paper](https://arxiv.org/abs/2501.04658)<br>[GitHub](https://github.com/OpenGVLab/InternVL)<br>[Demo](https://chat.intern-ai.org.cn/) |
| 2025 | [![HF 2025](https://img.shields.io/badge/HF-2025-ffcc4d?logo=huggingface)](https://huggingface.co/Qwen)<br>**Qwen3-VL** | general VLM baseline for OCR-rich prompting | [Hugging Face](https://huggingface.co/Qwen)<br>[Demo](https://chat.qwen.ai/) |
| 2024.12 | [![arXiv 2024.12](https://img.shields.io/badge/arXiv-2024.12-b31b1b)](https://arxiv.org/abs/2412.10302) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/deepseek-ai/DeepSeek-VL2)<br>**DeepSeek-VL2** | MoE general VLM for text-rich images | [Paper](https://arxiv.org/abs/2412.10302)<br>[GitHub](https://github.com/deepseek-ai/DeepSeek-VL2) |
| 2024.09 | [![arXiv 2024.09](https://img.shields.io/badge/arXiv-2024.09-b31b1b)](https://arxiv.org/abs/2409.17146) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/allenai/molmo)<br>**Molmo** | open general VLM baseline | [Paper](https://arxiv.org/abs/2409.17146)<br>[GitHub](https://github.com/allenai/molmo) |
| 2024.09 | [![arXiv 2024.09](https://img.shields.io/badge/arXiv-2024.09-b31b1b)](https://arxiv.org/abs/2409.12191) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/QwenLM/Qwen2-VL)<br>**Qwen2-VL** | dynamic-resolution VLM with OCR ability | [Paper](https://arxiv.org/abs/2409.12191)<br>[GitHub](https://github.com/QwenLM/Qwen2-VL) |
| 2024.09 | [![arXiv 2024.09](https://img.shields.io/badge/arXiv-2024.09-b31b1b)](https://arxiv.org/abs/2409.03213)<br>**Phi-3.5-Vision** | compact general VLM baseline | [Paper](https://arxiv.org/abs/2409.03213)<br>[Hugging Face](https://huggingface.co/microsoft/Phi-3.5-vision-instruct) |
| 2024.08 | [![arXiv 2024.08](https://img.shields.io/badge/arXiv-2024.08-b31b1b)](https://arxiv.org/abs/2408.03326) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/LLaVA-VL/LLaVA-NeXT)<br>**LLaVA-OneVision** | open general VLM baseline | [Paper](https://arxiv.org/abs/2408.03326)<br>[GitHub](https://github.com/LLaVA-VL/LLaVA-NeXT) |
| 2024.08 | [![arXiv 2024.08](https://img.shields.io/badge/arXiv-2024.08-b31b1b)](https://arxiv.org/abs/2408.01800) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/OpenBMB/MiniCPM-o)<br>**MiniCPM-V** | mobile-scale general MLLM with OCR ability | [Paper](https://arxiv.org/abs/2408.01800)<br>[GitHub](https://github.com/OpenBMB/MiniCPM-o)<br>[Demo](https://minicpm-omni.openbmb.cn/) |
| 2024.07 | [![arXiv 2024.07](https://img.shields.io/badge/arXiv-2024.07-b31b1b)](https://arxiv.org/abs/2407.07726)<br>**PaliGemma** | open VLM baseline for OCR prompting | [Paper](https://arxiv.org/abs/2407.07726)<br>[Hugging Face](https://huggingface.co/google/paligemma-3b-mix-448) |
| 2024.04 | [![arXiv 2024.04](https://img.shields.io/badge/arXiv-2024.04-b31b1b)](https://arxiv.org/abs/2404.16821) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/OpenGVLab/InternVL)<br>**InternVL 1.5** | open general VLM suite | [Paper](https://arxiv.org/abs/2404.16821)<br>[GitHub](https://github.com/OpenGVLab/InternVL)<br>[Demo](https://chat.intern-ai.org.cn/) |
| 2024.03 | [![arXiv 2024.03](https://img.shields.io/badge/arXiv-2024.03-b31b1b)](https://arxiv.org/abs/2403.05525) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/deepseek-ai/DeepSeek-VL)<br>**DeepSeek-VL** | general VLM baseline for text-rich images | [Paper](https://arxiv.org/abs/2403.05525)<br>[GitHub](https://github.com/deepseek-ai/DeepSeek-VL) |
| 2024 | [![CVPR 2024](https://img.shields.io/badge/CVPR-2024-4b4b4b)](https://arxiv.org/abs/2312.14238) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/OpenGVLab/InternVL)<br>**InternVL** | open general VLM baseline | [Paper](https://arxiv.org/abs/2312.14238)<br>[GitHub](https://github.com/OpenGVLab/InternVL)<br>[Demo](https://chat.intern-ai.org.cn/) |
| 2024 | [![ICLR 2024](https://img.shields.io/badge/ICLR-2024-4b4b4b)](https://arxiv.org/abs/2311.03079) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/THUDM/CogVLM)<br>**CogVLM** | visual expert for language models | [Paper](https://arxiv.org/abs/2311.03079)<br>[GitHub](https://github.com/THUDM/CogVLM) |
| 2024 | [![NeurIPS 2024](https://img.shields.io/badge/NeurIPS-2024-4b4b4b)](https://arxiv.org/abs/2304.08485) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/haotian-liu/LLaVA)<br>**LLaVA** | visual instruction tuning baseline | [Paper](https://arxiv.org/abs/2304.08485)<br>[GitHub](https://github.com/haotian-liu/LLaVA) |
| 2023.11 | [![arXiv 2023.11](https://img.shields.io/badge/arXiv-2023.11-b31b1b)](https://arxiv.org/abs/2311.06242)<br>**Florence-2** | fixed-token general vision foundation model | [Paper](https://arxiv.org/abs/2311.06242)<br>[Hugging Face](https://huggingface.co/microsoft/Florence-2-large) |
| 2023.08 | [![arXiv 2023.08](https://img.shields.io/badge/arXiv-2023.08-b31b1b)](https://arxiv.org/abs/2308.12966) [![GitHub](https://img.shields.io/badge/GitHub-Repo-24292f?logo=github)](https://github.com/QwenLM/Qwen-VL)<br>**Qwen-VL** | visual text reading; grounding; document QA | [Paper](https://arxiv.org/abs/2308.12966)<br>[GitHub](https://github.com/QwenLM/Qwen-VL) |

### Closed/API General VLMs

| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2024-2025 | [![API 2024-2025](https://img.shields.io/badge/API-2024--2025-6f42c1)](https://docs.anthropic.com/)<br>**Claude 3 / 3.5 / 4** | closed general VLM OCR interface | [Docs](https://docs.anthropic.com/) |
| 2025 | [![API 2025](https://img.shields.io/badge/API-2025-6f42c1)](https://platform.openai.com/docs)<br>**GPT-5 family** | closed general VLM OCR interface | [Docs](https://platform.openai.com/docs) |
| 2024 | [![API 2024](https://img.shields.io/badge/API-2024-6f42c1)](https://platform.openai.com/docs)<br>**GPT-4o** | closed general VLM OCR interface | [Docs](https://platform.openai.com/docs) |
| 2023.12 | [![Report 2023.12](https://img.shields.io/badge/Report-2023.12-6f42c1)](https://arxiv.org/abs/2312.11805)<br>**Gemini family** | closed general VLM OCR interface | [Report](https://arxiv.org/abs/2312.11805)<br>[Docs](https://ai.google.dev/gemini-api/docs) |
| 2023 | [![System Card 2023](https://img.shields.io/badge/System%20Card-2023-6f42c1)](https://cdn.openai.com/papers/GPTV_System_Card.pdf)<br>**GPT-4V** | closed general VLM OCR interface | [System Card](https://cdn.openai.com/papers/GPTV_System_Card.pdf)<br>[Docs](https://platform.openai.com/docs) |

<a id="f5-commercial-ocr-and-document-ai-services"></a>

## F5. Commercial OCR and Document AI Services

Closed-source or managed systems for document conversion, enterprise OCR, scientific document parsing, formula OCR, receipts, forms, invoices, and other vertical workflows.

### Enterprise OCR and Document AI

| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2026 | [![Product docs 2026](https://img.shields.io/badge/Product%20docs-2026-6f42c1)](https://cloud.google.com/document-ai/docs)<br>**Google Document AI** | managed document OCR and entity extraction | [Docs](https://cloud.google.com/document-ai/docs) |
| 2026 | [![Product docs 2026](https://img.shields.io/badge/Product%20docs-2026-6f42c1)](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/)<br>**Azure AI Document Intelligence** | managed form/document OCR and structured extraction | [Docs](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/) |
| 2026 | [![Product docs 2026](https://img.shields.io/badge/Product%20docs-2026-6f42c1)](https://docs.aws.amazon.com/textract/)<br>**Amazon Textract** | managed document OCR, tables, forms, and queries | [Docs](https://docs.aws.amazon.com/textract/) |
| 2026 | [![Product docs 2026](https://img.shields.io/badge/Product%20docs-2026-6f42c1)](https://developer.adobe.com/document-services/docs/overview/pdf-services-api/)<br>**Adobe PDF Services / OCR** | commercial PDF OCR and document services | [Docs](https://developer.adobe.com/document-services/docs/overview/pdf-services-api/) |
| 2026 | [![Product docs 2026](https://img.shields.io/badge/Product%20docs-2026-6f42c1)](https://nanonets.com/ocr-api/)<br>**Nanonets OCR API** | managed OCR and document extraction | [Website](https://nanonets.com/ocr-api/) |
| 2026 | [![Product docs 2026](https://img.shields.io/badge/Product%20docs-2026-6f42c1)](https://rossum.ai/)<br>**Rossum** | commercial document extraction platform | [Website](https://rossum.ai/) |
| 2025 | [![Product docs 2025](https://img.shields.io/badge/Product%20docs-2025-6f42c1)](https://www.textin.com/)<br>**TextIn** | document / receipt / form parsing; JSON / Markdown / fields | [Website](https://www.textin.com/) |
| 1993- | [![Product line 1993-](https://img.shields.io/badge/Product%20line-1993--6f42c1)](https://www.abbyy.com/finereader/)<br>**ABBYY FineReader / ABBYY Vantage** | commercial OCR; on-prem / SDK / cloud; searchable PDF / fields | [FineReader](https://www.abbyy.com/finereader/)<br>[Vantage](https://www.abbyy.com/vantage/) |

### Scientific OCR and Managed Parsing APIs

| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2026 | [![Product docs 2026](https://img.shields.io/badge/Product%20docs-2026-6f42c1)](https://mathpix.com/)<br>**Mathpix** | formula / paper / document OCR; LaTeX / Markdown | [Website](https://mathpix.com/) |
| 2026 | [![Product docs 2026](https://img.shields.io/badge/Product%20docs-2026-6f42c1)](https://www.llamaindex.ai/llamaparse)<br>**LlamaParse** | managed PDF/document parsing for RAG pipelines | [Website](https://www.llamaindex.ai/llamaparse)<br>[Docs](https://docs.cloud.llamaindex.ai/llamaparse/getting_started) |
| 2026 | [![Product docs 2026](https://img.shields.io/badge/Product%20docs-2026-6f42c1)](https://unstructured.io/)<br>**Unstructured Platform** | managed document partitioning and RAG ingestion | [Website](https://unstructured.io/)<br>[Docs](https://docs.unstructured.io/) |
| 2026 | [![Product docs 2026](https://img.shields.io/badge/Product%20docs-2026-6f42c1)](https://cloud.baidu.com/product/wenxinworkshop)<br>**Baidu Qianfan / Wenxin document services** | managed document OCR and model API access | [Website](https://cloud.baidu.com/product/wenxinworkshop) |
| 2025 | [![Product docs 2025](https://img.shields.io/badge/Product%20docs-2025-6f42c1)](https://docs.mistral.ai/capabilities/document_ai/basic_ocr/)<br>**Mistral OCR** | managed OCR API; Markdown / structured response | [Docs](https://docs.mistral.ai/capabilities/document_ai/basic_ocr/) |
| 2025 | [![Product docs 2025](https://img.shields.io/badge/Product%20docs-2025-6f42c1)](https://help.aliyun.com/zh/model-studio/)<br>**Qwen-OCR API** | managed OCR API; structured OCR output | [Docs](https://help.aliyun.com/zh/model-studio/) |

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
