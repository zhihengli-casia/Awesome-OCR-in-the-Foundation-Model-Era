# Awesome OCR in the Foundation-Model Era

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-24292f?logo=github)](https://github.com/zhihengli-casia/Awesome-OCR-in-the-Foundation-Model-Era)
[![Star](https://img.shields.io/github/stars/zhihengli-casia/Awesome-OCR-in-the-Foundation-Model-Era.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/zhihengli-casia/Awesome-OCR-in-the-Foundation-Model-Era)
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
- [Benchmarks and Datasets](#benchmarks-and-datasets)
- [Cross-era OCR Arena](arena/README.md)
- [Related Awesome Lists](#related-awesome-lists)

<a id="related-awesome-lists"></a>

<details open>
<summary>Related Awesome Lists</summary>

Existing OCR awesome lists remain useful, especially for classical OCR tooling, preprocessing, GUI utilities, OCR file formats, historical document OCR, and scene-text-specific papers. This repository focuses on connecting those older OCR resources with foundation-model-era document parsers, VLM interfaces, commercial APIs, and cross-era evaluation.

| Repository | Strong Coverage | Links |
|:---:|:---:|:---:|
| [![GitHub](https://img.shields.io/badge/GitHub-kba%2Fawesome--ocr-24292f?logo=github)](https://github.com/kba/awesome-ocr) [![Star](https://img.shields.io/github/stars/kba/awesome-ocr.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/kba/awesome-ocr)<br>**kba/awesome-ocr** | historical-document OCR; OCR engines; hOCR / ALTO / PAGE XML; GUI tools; preprocessing; datasets; older literature | [GitHub](https://github.com/kba/awesome-ocr) |
| [![GitHub](https://img.shields.io/badge/GitHub-zacharywhitley%2Fawesome--ocr-24292f?logo=github)](https://github.com/zacharywhitley/awesome-ocr) [![Star](https://img.shields.io/github/stars/zacharywhitley/awesome-ocr.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/zacharywhitley/awesome-ocr)<br>**zacharywhitley/awesome-ocr** | pipeline-era engineering resources; deskewing and dewarping; segmentation; text detection; recognition; table extraction; HTR; post-processing | [GitHub](https://github.com/zacharywhitley/awesome-ocr) |
| [![GitHub](https://img.shields.io/badge/GitHub-ZumingHuang%2Fawesome--ocr--resources-24292f?logo=github)](https://github.com/ZumingHuang/awesome-ocr-resources) [![Star](https://img.shields.io/github/stars/ZumingHuang/awesome-ocr-resources.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/ZumingHuang/awesome-ocr-resources)<br>**ZumingHuang/awesome-ocr-resources** | chronological OCR paper and dataset tracking; useful bibliography scaffold for pre-2025 methods | [GitHub](https://github.com/ZumingHuang/awesome-ocr-resources) |
| [![GitHub](https://img.shields.io/badge/GitHub-wanghaisheng%2Fawesome--ocr-24292f?logo=github)](https://github.com/wanghaisheng/awesome-ocr) [![Star](https://img.shields.io/github/stars/wanghaisheng/awesome-ocr.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/wanghaisheng/awesome-ocr)<br>**wanghaisheng/awesome-ocr** | Chinese engineering resources; APIs; OCR wrappers; practical libraries; older project tracking | [GitHub](https://github.com/wanghaisheng/awesome-ocr) |
| [![GitHub](https://img.shields.io/badge/GitHub-chongyangtao%2FAwesome--Scene--Text--Recognition-24292f?logo=github)](https://github.com/chongyangtao/Awesome-Scene-Text-Recognition) [![Star](https://img.shields.io/github/stars/chongyangtao/Awesome-Scene-Text-Recognition.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/chongyangtao/Awesome-Scene-Text-Recognition)<br>**Awesome Scene Text Recognition** | scene text detection / recognition / spotting papers and resources | [GitHub](https://github.com/chongyangtao/Awesome-Scene-Text-Recognition) |

Coverage gaps identified from these lists and not fully duplicated here: OCR file-format tooling (`hOCR`, `ALTO`, `PAGE XML`), annotation/GUI utilities, preprocessing and document restoration, handwriting and historical-document OCR ecosystems, OCR post-correction, language-model cleanup, and narrow industrial OCR applications such as license plates or ID cards. These are adjacent to the survey scope and may be expanded as separate resource files rather than folded into the main model-family taxonomy.

</details>

## Model Collections

Badges indicate venue/source and year when available; Star badges follow the live Shields.io style used by common awesome lists; explicit GitHub links remain available for every public repository. The Date column records the paper or public source date; active ranges such as `2020-2026` mark projects that continue to evolve beyond their first release. Repository-only entries use the public GitHub repository creation date. Entries are ordered newest first within each subsection. Each model-family block and subsection is expandable and remains open by default for direct browsing.

<a id="f1-modular-ocr-toolkits-and-specialized-components"></a>

<details open>
<summary><strong>F1. Modular OCR Toolkits and Specialized Components</strong></summary>


Systems that follow or support the detector-recognizer pipeline: OCR engines, open toolkits, text detectors, cropped recognizers, formula recognizers, and structured-object components.

<details open>
<summary>OCR Engines and Toolkits</summary>


| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2020-2026 | [![Project 2020-2026](https://img.shields.io/badge/Project-2020--2026-24292f?logo=github)](https://github.com/PaddlePaddle/PaddleOCR) [![Star](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/PaddlePaddle/PaddleOCR)<br>**PaddleOCR / PP-OCR** | active industrial OCR toolkit; PP-OCR, PP-Structure, PP-FormulaNet, PaddleOCR-VL ecosystem | [Paper](https://arxiv.org/abs/2009.09941)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR)<br>[Docs](https://paddlepaddle.github.io/PaddleOCR/) |
| 2005-2026 | [![Project 2005-2026](https://img.shields.io/badge/Project-2005--2026-24292f?logo=github)](https://github.com/tesseract-ocr/tesseract) [![Star](https://img.shields.io/github/stars/tesseract-ocr/tesseract.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/tesseract-ocr/tesseract)<br>**Tesseract** | active open-source OCR engine; LSTM OCR; searchable document workflows | [Paper](https://doi.org/10.1109/ICDAR.2007.4376991)<br>[GitHub](https://github.com/tesseract-ocr/tesseract)<br>[Docs](https://tesseract-ocr.github.io/) |
| 2026.03 | [![arXiv 2026.03](https://img.shields.io/badge/arXiv-2026.03-b31b1b)](https://arxiv.org/abs/2603.24373) [![Star](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/PaddlePaddle/PaddleOCR)<br>**PP-OCRv5** | specialized 5M-parameter OCR model family; text detection and recognition in PaddleOCR 3.x | [Paper](https://arxiv.org/abs/2603.24373)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR)<br>[Docs](https://paddlepaddle.github.io/PaddleOCR/) |
| 2024.05 | [![GitHub 2024.05](https://img.shields.io/badge/GitHub-2024.05-24292f?logo=github)](https://github.com/topdu/openocr) [![Star](https://img.shields.io/github/stars/topdu/openocr.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/topdu/openocr)<br>**OpenOCR** | open OCR training and evaluation toolkit; detection / recognition baselines | [GitHub](https://github.com/topdu/openocr) |
| 2021.08 | [![arXiv 2021.08](https://img.shields.io/badge/arXiv-2021.08-b31b1b)](https://arxiv.org/abs/2108.06543) [![Star](https://img.shields.io/github/stars/open-mmlab/mmocr.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/open-mmlab/mmocr)<br>**MMOCR** | OCR research toolbox; detection/recognition/spotting | [Paper](https://arxiv.org/abs/2108.06543)<br>[GitHub](https://github.com/open-mmlab/mmocr)<br>[Docs](https://mmocr.readthedocs.io/) |
| 2021.01 | [![GitHub 2021.01](https://img.shields.io/badge/GitHub-2021.01-24292f?logo=github)](https://github.com/mindee/doctr) [![Star](https://img.shields.io/github/stars/mindee/doctr.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/mindee/doctr)<br>**docTR** | document OCR toolkit; detection + recognition | [GitHub](https://github.com/mindee/doctr)<br>[Docs](https://mindee.github.io/doctr/) |
| 2021.01 | [![GitHub 2021.01](https://img.shields.io/badge/GitHub-2021.01-24292f?logo=github)](https://github.com/RapidAI/RapidOCR) [![Star](https://img.shields.io/github/stars/RapidAI/RapidOCR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/RapidAI/RapidOCR)<br>**RapidOCR** | lightweight OCR toolkit; ONNX / OpenVINO / Paddle / PyTorch backends | [GitHub](https://github.com/RapidAI/RapidOCR)<br>[Docs](https://rapidai.github.io/RapidOCRDocs/) |
| 2020.03 | [![GitHub 2020.03](https://img.shields.io/badge/GitHub-2020.03-24292f?logo=github)](https://github.com/JaidedAI/EasyOCR) [![Star](https://img.shields.io/github/stars/JaidedAI/EasyOCR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/JaidedAI/EasyOCR)<br>**EasyOCR** | ready-to-use OCR engine; multilingual OCR | [GitHub](https://github.com/JaidedAI/EasyOCR) |
| 2019.07 | [![GitHub 2019.07](https://img.shields.io/badge/GitHub-2019.07-24292f?logo=github)](https://github.com/faustomorales/keras-ocr) [![Star](https://img.shields.io/github/stars/faustomorales/keras-ocr.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/faustomorales/keras-ocr)<br>**keras-ocr** | CRAFT + CRNN-style Python OCR pipeline | [GitHub](https://github.com/faustomorales/keras-ocr)<br>[Docs](https://keras-ocr.readthedocs.io/) |
| 2019.03 | [![GitHub 2019.03](https://img.shields.io/badge/GitHub-2019.03-24292f?logo=github)](https://github.com/breezedeus/CnOCR) [![Star](https://img.shields.io/github/stars/breezedeus/CnOCR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/breezedeus/CnOCR)<br>**CnOCR** | Chinese OCR toolkit; line/crop recognition | [GitHub](https://github.com/breezedeus/CnOCR)<br>[Docs](https://cnocr.readthedocs.io/) |
| 2018-2026 | [![Project 2018-2026](https://img.shields.io/badge/Project-2018--2026-24292f?logo=github)](https://github.com/Calamari-OCR/calamari) [![Star](https://img.shields.io/github/stars/Calamari-OCR/calamari.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/Calamari-OCR/calamari)<br>**Calamari OCR** | line-based OCR engine; historical-document OCR; ensemble recognition | [Paper](https://rlskoeser.github.io/dhqwords/vol/14/2/000451/)<br>[GitHub](https://github.com/Calamari-OCR/calamari)<br>[Docs](https://calamari-ocr.readthedocs.io/) |
| 2016-2026 | [![Project 2016-2026](https://img.shields.io/badge/Project-2016--2026-24292f?logo=github)](https://github.com/mittagessen/kraken) [![Star](https://img.shields.io/github/stars/mittagessen/kraken.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/mittagessen/kraken)<br>**Kraken** | trainable OCR engine; historical scripts; handwritten and printed text | [GitHub](https://github.com/mittagessen/kraken)<br>[Docs](https://kraken.re/) |
| 2013.12 | [![GitHub 2013.12](https://img.shields.io/badge/GitHub-2013.12-24292f?logo=github)](https://github.com/ocrmypdf/OCRmyPDF) [![Star](https://img.shields.io/github/stars/ocrmypdf/OCRmyPDF.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/ocrmypdf/OCRmyPDF)<br>**OCRmyPDF** | searchable-PDF OCR workflow | [GitHub](https://github.com/ocrmypdf/OCRmyPDF)<br>[Docs](https://ocrmypdf.readthedocs.io/) |
| 2007-2018 | [![GitHub 2007-2018](https://img.shields.io/badge/GitHub-2007--2018-24292f?logo=github)](https://github.com/tmbdev/ocropy) [![Star](https://img.shields.io/github/stars/tmbdev/ocropy.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/tmbdev/ocropy)<br>**OCRopus / ocropy** | open OCR research toolkit; segmentation and recognizer training | [GitHub](https://github.com/tmbdev/ocropy)<br>[Project](https://ocropus.github.io/) |


</details>

<details open>
<summary>Text Detection and Spotting Components</summary>


| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2023 | [![CVPR 2023](https://img.shields.io/badge/CVPR-2023-4b4b4b)](https://arxiv.org/abs/2211.10772)<br>**DeepSolo** | explicit-point transformer text spotting | [Paper](https://arxiv.org/abs/2211.10772) |
| 2023 | [![AAAI 2023](https://img.shields.io/badge/AAAI-2023-4b4b4b)](https://arxiv.org/abs/2207.04491)<br>**DPText-DETR** | dynamic-point transformer text detection | [Paper](https://arxiv.org/abs/2207.04491) |
| 2023 | [![TPAMI 2023](https://img.shields.io/badge/TPAMI-2023-4b4b4b)](https://doi.org/10.1109/TPAMI.2022.3155612) [![Star](https://img.shields.io/github/stars/MhLiao/DB.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/MhLiao/DB)<br>**DBNet++** | adaptive-scale DB text detection | [Paper](https://doi.org/10.1109/TPAMI.2022.3155612)<br>[GitHub](https://github.com/MhLiao/DB) |
| 2022 | [![CVPR 2022](https://img.shields.io/badge/CVPR-2022-4b4b4b)](https://arxiv.org/abs/2204.01918)<br>**Text Spotting Transformer** | transformer-based end-to-end spotting | [Paper](https://arxiv.org/abs/2204.01918) |
| 2022 | [![ACM MM 2022](https://img.shields.io/badge/ACM%20MM-2022-4b4b4b)](https://arxiv.org/abs/2112.07917)<br>**SPTS** | single-point text spotting via sequence generation | [Paper](https://arxiv.org/abs/2112.07917) |
| 2021 | [![CVPR 2021](https://img.shields.io/badge/CVPR-2021-4b4b4b)](https://arxiv.org/abs/2104.10442)<br>**FCENet** | Fourier-contour text detection | [Paper](https://arxiv.org/abs/2104.10442) |
| 2021 | [![CVPR 2021](https://img.shields.io/badge/CVPR-2021-4b4b4b)](https://arxiv.org/abs/2104.01070)<br>**MOST** | multi-oriented detector with localization refinement | [Paper](https://arxiv.org/abs/2104.01070) |
| 2021 | [![TPAMI 2021](https://img.shields.io/badge/TPAMI-2021-4b4b4b)](https://arxiv.org/abs/2105.03620) [![Star](https://img.shields.io/github/stars/Yuliang-Liu/AdelaiDet.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/Yuliang-Liu/AdelaiDet)<br>**ABCNet v2** | Bezier-curve scene text spotting; efficient detector-recognizer | [Paper](https://arxiv.org/abs/2105.03620)<br>[GitHub](https://github.com/Yuliang-Liu/AdelaiDet) |
| 2020 | [![CVPR 2020](https://img.shields.io/badge/CVPR-2020-4b4b4b)](https://doi.org/10.1109/CVPR42600.2020.01177)<br>**ContourNet** | contour-based arbitrary-shape detector | [Paper](https://doi.org/10.1109/CVPR42600.2020.01177) |
| 2020 | [![CVPR 2020](https://img.shields.io/badge/CVPR-2020-4b4b4b)](https://doi.org/10.1109/CVPR42600.2020.00972)<br>**DRRG** | graph-reasoning arbitrary-shape detector | [Paper](https://doi.org/10.1109/CVPR42600.2020.00972) |
| 2020 | [![ECCV 2020](https://img.shields.io/badge/ECCV-2020-4b4b4b)](https://arxiv.org/abs/2007.09482) [![Star](https://img.shields.io/github/stars/MhLiao/MaskTextSpotterV3.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/MhLiao/MaskTextSpotterV3)<br>**Mask TextSpotter v3** | segmentation-proposal scene text spotting | [Paper](https://arxiv.org/abs/2007.09482)<br>[GitHub](https://github.com/MhLiao/MaskTextSpotterV3) |
| 2020 | [![CVPR 2020](https://img.shields.io/badge/CVPR-2020-4b4b4b)](https://arxiv.org/abs/2002.10200) [![Star](https://img.shields.io/github/stars/Yuliang-Liu/bezier_curve_text_spotting.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/Yuliang-Liu/bezier_curve_text_spotting)<br>**ABCNet** | adaptive Bezier-curve text spotting | [Paper](https://arxiv.org/abs/2002.10200)<br>[GitHub](https://github.com/Yuliang-Liu/bezier_curve_text_spotting) |
| 2020 | [![AAAI 2020](https://img.shields.io/badge/AAAI-2020-4b4b4b)](https://doi.org/10.1609/aaai.v34i07.6812) [![Star](https://img.shields.io/github/stars/MhLiao/DB.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/MhLiao/DB)<br>**DBNet** | differentiable-binarization text detection | [Paper](https://doi.org/10.1609/aaai.v34i07.6812)<br>[GitHub](https://github.com/MhLiao/DB) |
| 2019 | [![CVPR 2019](https://img.shields.io/badge/CVPR-2019-4b4b4b)](https://arxiv.org/abs/1904.01941) [![Star](https://img.shields.io/github/stars/clovaai/CRAFT-pytorch.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/clovaai/CRAFT-pytorch)<br>**CRAFT** | character-region text detection | [Paper](https://arxiv.org/abs/1904.01941)<br>[GitHub](https://github.com/clovaai/CRAFT-pytorch) |
| 2019 | [![CVPR 2019](https://img.shields.io/badge/CVPR-2019-4b4b4b)](https://arxiv.org/abs/1806.02559) [![Star](https://img.shields.io/github/stars/whai362/PSENet.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/whai362/PSENet)<br>**PSENet** | arbitrary-shape text detection | [Paper](https://arxiv.org/abs/1806.02559)<br>[GitHub](https://github.com/whai362/PSENet) |
| 2019 | [![ICCV 2019](https://img.shields.io/badge/ICCV-2019-4b4b4b)](https://doi.org/10.1109/ICCV.2019.00853)<br>**PAN** | pixel aggregation for arbitrary-shape text detection | [Paper](https://doi.org/10.1109/ICCV.2019.00853) |
| 2018 | [![ECCV 2018](https://img.shields.io/badge/ECCV-2018-4b4b4b)](https://arxiv.org/abs/1807.01544)<br>**TextSnake** | flexible representation for arbitrary-shape text | [Paper](https://arxiv.org/abs/1807.01544) |
| 2018 | [![ECCV 2018](https://img.shields.io/badge/ECCV-2018-4b4b4b)](https://arxiv.org/abs/1807.02242) [![Star](https://img.shields.io/github/stars/MhLiao/MaskTextSpotter.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/MhLiao/MaskTextSpotter)<br>**Mask TextSpotter** | segmentation-based arbitrary-shape text spotting | [Paper](https://arxiv.org/abs/1807.02242)<br>[GitHub](https://github.com/MhLiao/MaskTextSpotter) |
| 2018 | [![CVPR 2018](https://img.shields.io/badge/CVPR-2018-4b4b4b)](https://arxiv.org/abs/1801.01671)<br>**FOTS** | fast oriented text spotting with shared detection-recognition features | [Paper](https://arxiv.org/abs/1801.01671) |
| 2018 | [![AAAI 2018](https://img.shields.io/badge/AAAI-2018-4b4b4b)](https://arxiv.org/abs/1801.01315)<br>**PixelLink** | instance-segmentation text detector | [Paper](https://arxiv.org/abs/1801.01315) |
| 2018 | [![TIP 2018](https://img.shields.io/badge/TIP-2018-4b4b4b)](https://doi.org/10.1109/TIP.2018.2825107)<br>**TextBoxes++** | oriented scene text detector | [Paper](https://doi.org/10.1109/TIP.2018.2825107) |
| 2017 | [![CVPR 2017](https://img.shields.io/badge/CVPR-2017-4b4b4b)](https://arxiv.org/abs/1704.03155)<br>**EAST** | text detection; dense prediction | [Paper](https://arxiv.org/abs/1704.03155) |
| 2017 | [![AAAI 2017](https://img.shields.io/badge/AAAI-2017-4b4b4b)](https://ojs.aaai.org/index.php/AAAI/article/view/11196)<br>**TextBoxes** | single-shot horizontal text detector | [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/11196) |
| 2016 | [![ECCV 2016](https://img.shields.io/badge/ECCV-2016-4b4b4b)](https://arxiv.org/abs/1609.03605)<br>**CTPN** | connectionist text proposal network | [Paper](https://arxiv.org/abs/1609.03605) |


</details>

<details open>
<summary>Cropped Text Recognizers</summary>


| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2024.11 | [![arXiv 2024.11](https://img.shields.io/badge/arXiv-2024.11-b31b1b)](https://arxiv.org/abs/2411.15858) [![Star](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/PaddlePaddle/PaddleOCR)<br>**SVTRv2** | upgraded cropped recognizer | [Paper](https://arxiv.org/abs/2411.15858)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| 2023 | [![AAAI 2023](https://img.shields.io/badge/AAAI-2023-4b4b4b)](https://arxiv.org/abs/2109.10282)<br>**TrOCR** | pretrained encoder-decoder recognizer | [Paper](https://arxiv.org/abs/2109.10282)<br>[HF Docs](https://huggingface.co/docs/transformers/model_doc/trocr) |
| 2022 | [![ECCV 2022](https://img.shields.io/badge/ECCV-2022-4b4b4b)](https://arxiv.org/abs/2209.03592)<br>**MGP-STR** | multi-granularity prediction recognizer | [Paper](https://arxiv.org/abs/2209.03592) |
| 2022 | [![ECCV 2022](https://img.shields.io/badge/ECCV-2022-4b4b4b)](https://arxiv.org/abs/2207.06966) [![Star](https://img.shields.io/github/stars/baudm/parseq.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/baudm/parseq)<br>**PARSeq** | permuted autoregressive recognizer | [Paper](https://arxiv.org/abs/2207.06966)<br>[GitHub](https://github.com/baudm/parseq) |
| 2022 | [![IJCAI 2022](https://img.shields.io/badge/IJCAI-2022-4b4b4b)](https://doi.org/10.24963/ijcai.2022/124) [![Star](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/PaddlePaddle/PaddleOCR)<br>**SVTR** | efficient single-visual-model recognizer | [Paper](https://doi.org/10.24963/ijcai.2022/124)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| 2021 | [![IJCV 2021](https://img.shields.io/badge/IJCV-2021-4b4b4b)](https://arxiv.org/abs/2111.11011)<br>**CDistNet** | multi-domain character-distance recognizer | [Paper](https://arxiv.org/abs/2111.11011) |
| 2021 | [![ICCV 2021](https://img.shields.io/badge/ICCV-2021-4b4b4b)](https://arxiv.org/abs/2108.09661)<br>**VisionLAN** | visual-language modeling recognizer | [Paper](https://arxiv.org/abs/2108.09661) |
| 2021 | [![ICDAR 2021](https://img.shields.io/badge/ICDAR-2021-4b4b4b)](https://arxiv.org/abs/2105.08582) [![Star](https://img.shields.io/github/stars/roatienza/deep-text-recognition-benchmark.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/roatienza/deep-text-recognition-benchmark)<br>**ViTSTR** | ViT recognizer | [Paper](https://arxiv.org/abs/2105.08582)<br>[GitHub](https://github.com/roatienza/deep-text-recognition-benchmark) |
| 2021 | [![CVPR 2021](https://img.shields.io/badge/CVPR-2021-4b4b4b)](https://arxiv.org/abs/2103.06495)<br>**ABINet** | language-aware recognizer | [Paper](https://arxiv.org/abs/2103.06495) |
| 2021 | [![PR 2021](https://img.shields.io/badge/PR-2021-4b4b4b)](https://doi.org/10.1016/j.patcog.2021.107980)<br>**MASTER** | multi-aspect non-local recognizer | [Paper](https://doi.org/10.1016/j.patcog.2021.107980) |
| 2020 | [![ECCV 2020](https://img.shields.io/badge/ECCV-2020-4b4b4b)](https://arxiv.org/abs/2007.07542)<br>**RobustScanner** | positional-clue enhanced recognizer | [Paper](https://arxiv.org/abs/2007.07542) |
| 2020 | [![CVPR 2020](https://img.shields.io/badge/CVPR-2020-4b4b4b)](https://arxiv.org/abs/2003.12294)<br>**SRN** | semantic reasoning recognizer | [Paper](https://arxiv.org/abs/2003.12294) |
| 2020 | [![CVPR 2020](https://img.shields.io/badge/CVPR-2020-4b4b4b)](https://arxiv.org/abs/2003.11288)<br>**SCATTER** | selective-context attention recognizer | [Paper](https://arxiv.org/abs/2003.11288) |
| 2020 | [![AAAI 2020](https://img.shields.io/badge/AAAI-2020-4b4b4b)](https://arxiv.org/abs/1912.12422)<br>**TextScanner** | order-aware character scanner | [Paper](https://arxiv.org/abs/1912.12422) |
| 2020 | [![AAAI 2020](https://img.shields.io/badge/AAAI-2020-4b4b4b)](https://arxiv.org/abs/1912.10205)<br>**DAN** | decoupled attention recognizer | [Paper](https://arxiv.org/abs/1912.10205) |
| 2020 | [![CVPRW 2020](https://img.shields.io/badge/CVPRW-2020-4b4b4b)](https://arxiv.org/abs/1910.04396)<br>**SATRN** | 2D self-attention text recognizer | [Paper](https://arxiv.org/abs/1910.04396) |
| 2019 | [![ICCV 2019](https://img.shields.io/badge/ICCV-2019-4b4b4b)](https://arxiv.org/abs/1904.01906) [![Star](https://img.shields.io/github/stars/clovaai/deep-text-recognition-benchmark.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/clovaai/deep-text-recognition-benchmark)<br>**STR Benchmark (Baek et al.)** | unified training/evaluation benchmark for cropped text recognition | [Paper](https://arxiv.org/abs/1904.01906)<br>[GitHub](https://github.com/clovaai/deep-text-recognition-benchmark) |
| 2019 | [![AAAI 2019](https://img.shields.io/badge/AAAI-2019-4b4b4b)](https://arxiv.org/abs/1811.00751)<br>**SAR** | show-attend-and-read baseline for irregular text recognition | [Paper](https://arxiv.org/abs/1811.00751) |
| 2019 | [![TPAMI 2019](https://img.shields.io/badge/TPAMI-2019-4b4b4b)](https://doi.org/10.1109/TPAMI.2018.2848939) [![Star](https://img.shields.io/github/stars/bgshih/aster.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/bgshih/aster)<br>**ASTER** | rectified irregular text recognition | [Paper](https://doi.org/10.1109/TPAMI.2018.2848939)<br>[GitHub](https://github.com/bgshih/aster) |
| 2019 | [![PR 2019](https://img.shields.io/badge/PR-2019-4b4b4b)](https://doi.org/10.1016/j.patcog.2019.01.020)<br>**MORAN** | rectified attention recognizer | [Paper](https://doi.org/10.1016/j.patcog.2019.01.020) |
| 2019 | [![ICDAR 2019](https://img.shields.io/badge/ICDAR-2019-4b4b4b)](https://doi.org/10.1109/ICDAR.2019.00130)<br>**NRTR** | no-recurrence seq2seq recognizer | [Paper](https://doi.org/10.1109/ICDAR.2019.00130) |
| 2017 | [![TPAMI 2017](https://img.shields.io/badge/TPAMI-2017-4b4b4b)](https://doi.org/10.1109/TPAMI.2016.2646371) [![Star](https://img.shields.io/github/stars/meijieru/crnn.pytorch.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/meijieru/crnn.pytorch)<br>**CRNN** | cropped sequence recognition; CTC | [Paper](https://doi.org/10.1109/TPAMI.2016.2646371)<br>[GitHub](https://github.com/meijieru/crnn.pytorch) |
| 2016 | [![CVPR 2016](https://img.shields.io/badge/CVPR-2016-4b4b4b)](https://doi.org/10.1109/CVPR.2016.452)<br>**RARE** | rectified attention recognizer | [Paper](https://doi.org/10.1109/CVPR.2016.452) |
| 2016 | [![CVPR 2016](https://img.shields.io/badge/CVPR-2016-4b4b4b)](https://doi.org/10.1109/CVPR.2016.464)<br>**STAR-Net** | spatial transformer network for scene text recognition | [Paper](https://doi.org/10.1109/CVPR.2016.464) |


</details>

<details open>
<summary>Formula, Table, and Structured-Object Components</summary>


| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2026.02 | [![arXiv 2026.02](https://img.shields.io/badge/arXiv-2026.02-b31b1b)](https://arxiv.org/abs/2602.17189)<br>**Texo** | 20M-parameter formula recognizer | [Paper](https://arxiv.org/abs/2602.17189) |
| 2025.03 | [![arXiv 2025.03](https://img.shields.io/badge/arXiv-2025.03-b31b1b)](https://arxiv.org/abs/2503.18382) [![Star](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/PaddlePaddle/PaddleOCR)<br>**PP-FormulaNet** | formula recognition; PaddleOCR component | [Paper](https://arxiv.org/abs/2503.18382)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| 2024.04 | [![arXiv 2024.04](https://img.shields.io/badge/arXiv-2024.04-b31b1b)](https://arxiv.org/abs/2404.15254) [![Star](https://img.shields.io/github/stars/opendatalab/UniMERNet.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/opendatalab/UniMERNet)<br>**UniMERNet** | formula recognition; LaTeX output | [Paper](https://arxiv.org/abs/2404.15254)<br>[GitHub](https://github.com/opendatalab/UniMERNet) |
| 2024 | [![CVPR 2024](https://img.shields.io/badge/CVPR-2024-4b4b4b)](https://arxiv.org/abs/2410.12628)<br>**DocLayout-YOLO** | document layout detection | [Paper](https://arxiv.org/abs/2410.12628) |
| 2024 | [![IJCAI 2024](https://img.shields.io/badge/IJCAI-2024-4b4b4b)](https://doi.org/10.24963/ijcai.2024/105)<br>**TFLOP** | table structure recognition with layout pointer | [Paper](https://doi.org/10.24963/ijcai.2024/105) |
| 2022.10 | [![arXiv 2022.10](https://img.shields.io/badge/arXiv-2022.10-b31b1b)](https://arxiv.org/abs/2210.08208)<br>**GrTS** | grounded table structure recognition | [Paper](https://arxiv.org/abs/2210.08208) |
| 2022.09 | [![GitHub 2022.09](https://img.shields.io/badge/GitHub-2022.09-24292f?logo=github)](https://github.com/AlibabaResearch/AdvancedLiterateMachinery) [![Star](https://img.shields.io/github/stars/AlibabaResearch/AdvancedLiterateMachinery.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/AlibabaResearch/AdvancedLiterateMachinery)<br>**StructEqTable** | equation/table structure parsing | [GitHub](https://github.com/AlibabaResearch/AdvancedLiterateMachinery) |
| 2022.03 | [![arXiv 2022.03](https://img.shields.io/badge/arXiv-2022.03-b31b1b)](https://arxiv.org/abs/2203.01017)<br>**TableFormer** | table structure recognition; table-to-HTML modeling | [Paper](https://arxiv.org/abs/2203.01017) |
| 2022 | [![ICPR 2022](https://img.shields.io/badge/ICPR-2022-4b4b4b)](https://arxiv.org/abs/2207.11463)<br>**BTTR** | transformer formula recognition | [Paper](https://arxiv.org/abs/2207.11463) |
| 2022 | [![PR 2022](https://img.shields.io/badge/PR-2022-4b4b4b)](https://doi.org/10.1016/j.patcog.2022.109006)<br>**LGPMA** | table detection and structure recognition | [Paper](https://doi.org/10.1016/j.patcog.2022.109006) |
| 2021.10 | [![arXiv 2021.10](https://img.shields.io/badge/arXiv-2021.10-b31b1b)](https://arxiv.org/abs/2110.00061) [![Star](https://img.shields.io/github/stars/microsoft/table-transformer.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/microsoft/table-transformer)<br>**Table Transformer / TATR** | table detection and structure recognition; PubTables-1M baseline | [Paper](https://arxiv.org/abs/2110.00061)<br>[GitHub](https://github.com/microsoft/table-transformer) |
| 2021.03 | [![arXiv 2021.03](https://img.shields.io/badge/arXiv-2021.03-b31b1b)](https://arxiv.org/abs/2103.15348) [![Star](https://img.shields.io/github/stars/Layout-Parser/layout-parser.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/Layout-Parser/layout-parser)<br>**LayoutParser** | layout analysis toolkit; model zoo and document layout pipelines | [Paper](https://arxiv.org/abs/2103.15348)<br>[GitHub](https://github.com/Layout-Parser/layout-parser)<br>[Docs](https://layout-parser.github.io/) |
| 2021 | [![ICDAR 2021](https://img.shields.io/badge/ICDAR-2021-4b4b4b)](https://arxiv.org/abs/2105.01848)<br>**TableMaster** | sequence-based table-to-HTML recognizer | [Paper](https://arxiv.org/abs/2105.01848) |
| 2020.12 | [![GitHub 2020.12](https://img.shields.io/badge/GitHub-2020.12-24292f?logo=github)](https://github.com/lukas-blecher/LaTeX-OCR) [![Star](https://img.shields.io/github/stars/lukas-blecher/LaTeX-OCR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/lukas-blecher/LaTeX-OCR)<br>**pix2tex / LaTeX-OCR** | formula image to LaTeX | [GitHub](https://github.com/lukas-blecher/LaTeX-OCR) |
| 2020.04 | [![arXiv 2020.04](https://img.shields.io/badge/arXiv-2020.04-b31b1b)](https://arxiv.org/abs/2004.12629) [![Star](https://img.shields.io/github/stars/DevashishPrasad/CascadeTabNet.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/DevashishPrasad/CascadeTabNet)<br>**CascadeTabNet** | end-to-end table detection and structure recognition | [Paper](https://arxiv.org/abs/2004.12629)<br>[GitHub](https://github.com/DevashishPrasad/CascadeTabNet) |
| 2020 | [![ECCV 2020](https://img.shields.io/badge/ECCV-2020-4b4b4b)](https://arxiv.org/abs/1911.10683)<br>**PubTabNet / EDD** | table structure recognition baseline | [Paper](https://arxiv.org/abs/1911.10683) |
| 2017 | [![PR 2017](https://img.shields.io/badge/PR-2017-4b4b4b)](https://doi.org/10.1016/j.patcog.2017.06.017)<br>**WAP** | handwritten mathematical expression recognition | [Paper](https://doi.org/10.1016/j.patcog.2017.06.017) |
| 2016.09 | [![arXiv 2016.09](https://img.shields.io/badge/arXiv-2016.09-b31b1b)](https://arxiv.org/abs/1609.04938)<br>**Im2Markup** | image-to-LaTeX generation | [Paper](https://arxiv.org/abs/1609.04938) |


</details>

</details>

<a id="f2-foundation-model-document-parsers"></a>

<details open>
<summary><strong>F2. Foundation-Model Document Parsers</strong></summary>


End-to-end or near end-to-end models that read page images and generate structured representations such as Markdown, HTML, LaTeX, JSON, or OCR-formatted text.

<details open>
<summary>OCR-Free and Transitional Encoder-Decoders</summary>


| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2023.09 | [![arXiv 2023.09](https://img.shields.io/badge/arXiv-2023.09-b31b1b)](https://arxiv.org/abs/2309.11419)<br>**KOSMOS-2.5** | spatially-aware text block + Markdown generation | [Paper](https://arxiv.org/abs/2309.11419) |
| 2023.08 | [![arXiv 2023.08](https://img.shields.io/badge/arXiv-2023.08-b31b1b)](https://arxiv.org/abs/2308.13418) [![Star](https://img.shields.io/github/stars/facebookresearch/nougat.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/facebookresearch/nougat)<br>**Nougat** | scholarly PDF-to-Markdown parser | [Paper](https://arxiv.org/abs/2308.13418)<br>[GitHub](https://github.com/facebookresearch/nougat) |
| 2023 | [![CVPR 2023](https://img.shields.io/badge/CVPR-2023-4b4b4b)](https://arxiv.org/abs/2212.02623)<br>**UDOP** | unified vision-text-layout generation | [Paper](https://arxiv.org/abs/2212.02623) |
| 2023 | [![ICML 2023](https://img.shields.io/badge/ICML-2023-4b4b4b)](https://arxiv.org/abs/2210.03347) [![Star](https://img.shields.io/github/stars/google-research/pix2struct.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/google-research/pix2struct)<br>**Pix2Struct** | screenshot/page-to-sequence pretraining | [Paper](https://arxiv.org/abs/2210.03347)<br>[GitHub](https://github.com/google-research/pix2struct) |
| 2022 | [![ECCV 2022](https://img.shields.io/badge/ECCV-2022-4b4b4b)](https://arxiv.org/abs/2111.15664) [![Star](https://img.shields.io/github/stars/clovaai/donut.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/clovaai/donut)<br>**Donut** | OCR-free encoder-decoder; document understanding | [Paper](https://arxiv.org/abs/2111.15664)<br>[GitHub](https://github.com/clovaai/donut) |
| 2022.03 | [![arXiv 2022.03](https://img.shields.io/badge/arXiv-2022.03-b31b1b)](https://arxiv.org/abs/2203.16618)<br>**Dessurt** | end-to-end document recognition and understanding | [Paper](https://arxiv.org/abs/2203.16618) |


</details>

<details open>
<summary>Early Document VLMs</summary>


| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2024.10 | [![arXiv 2024.10](https://img.shields.io/badge/arXiv-2024.10-b31b1b)](https://arxiv.org/abs/2410.05261)<br>**TextHawk2** | bilingual OCR and grounding MLLM | [Paper](https://arxiv.org/abs/2410.05261)<br>[Hugging Face](https://huggingface.co/TencentBAC) |
| 2024.09 | [![arXiv 2024.09](https://img.shields.io/badge/arXiv-2024.09-b31b1b)](https://arxiv.org/abs/2409.03420) [![Star](https://img.shields.io/github/stars/X-PLUG/mPLUG-DocOwl.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/X-PLUG/mPLUG-DocOwl)<br>**DocOwl 2** | high-resolution multi-page document VLM | [Paper](https://arxiv.org/abs/2409.03420)<br>[GitHub](https://github.com/X-PLUG/mPLUG-DocOwl) |
| 2024.09 | [![arXiv 2024.09](https://img.shields.io/badge/arXiv-2024.09-b31b1b)](https://arxiv.org/abs/2409.01704) [![Star](https://img.shields.io/github/stars/Ucas-HaoranWei/GOT-OCR2.0.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/Ucas-HaoranWei/GOT-OCR2.0)<br>**GOT-OCR 2.0** | unified OCR-specialized VLM | [Paper](https://arxiv.org/abs/2409.01704)<br>[GitHub](https://github.com/Ucas-HaoranWei/GOT-OCR2.0) |
| 2024.05 | [![arXiv 2024.05](https://img.shields.io/badge/arXiv-2024.05-b31b1b)](https://arxiv.org/abs/2405.14295) [![Star](https://img.shields.io/github/stars/ucaslcl/Fox.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/ucaslcl/Fox)<br>**Fox** | multi-page document understanding system | [Paper](https://arxiv.org/abs/2405.14295)<br>[GitHub](https://github.com/ucaslcl/Fox) |
| 2024.04 | [![arXiv 2024.04](https://img.shields.io/badge/arXiv-2024.04-b31b1b)](https://arxiv.org/abs/2404.09204)<br>**TextHawk** | fine-grained text perception in MLLMs | [Paper](https://arxiv.org/abs/2404.09204)<br>[Hugging Face](https://huggingface.co/TencentBAC) |
| 2024.04 | [![arXiv 2024.04](https://img.shields.io/badge/arXiv-2024.04-b31b1b)](https://arxiv.org/abs/2404.05225)<br>**LayoutLLM** | layout instruction tuning for document understanding | [Paper](https://arxiv.org/abs/2404.05225) |
| 2024.03 | [![arXiv 2024.03](https://img.shields.io/badge/arXiv-2024.03-b31b1b)](https://arxiv.org/abs/2403.12895) [![Star](https://img.shields.io/github/stars/X-PLUG/mPLUG-DocOwl.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/X-PLUG/mPLUG-DocOwl)<br>**DocOwl 1.5** | OCR-free structure learning | [Paper](https://arxiv.org/abs/2403.12895)<br>[GitHub](https://github.com/X-PLUG/mPLUG-DocOwl) |
| 2024.03 | [![arXiv 2024.03](https://img.shields.io/badge/arXiv-2024.03-b31b1b)](https://arxiv.org/abs/2403.04473) [![Star](https://img.shields.io/github/stars/Yuliang-Liu/Monkey.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/Yuliang-Liu/Monkey)<br>**TextMonkey** | OCR-free document MLLM | [Paper](https://arxiv.org/abs/2403.04473)<br>[GitHub](https://github.com/Yuliang-Liu/Monkey) |
| 2024 | [![CVPR 2024](https://img.shields.io/badge/CVPR-2024-4b4b4b)](https://arxiv.org/abs/2311.06607) [![Star](https://img.shields.io/github/stars/Yuliang-Liu/Monkey.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/Yuliang-Liu/Monkey)<br>**Monkey** | text-centric MLLM | [Paper](https://arxiv.org/abs/2311.06607)<br>[GitHub](https://github.com/Yuliang-Liu/Monkey) |
| 2023.12 | [![arXiv 2023.12](https://img.shields.io/badge/arXiv-2023.12-b31b1b)](https://arxiv.org/abs/2312.06109) [![Star](https://img.shields.io/github/stars/Ucas-HaoranWei/Vary.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/Ucas-HaoranWei/Vary)<br>**Vary** | document-specialized VLM | [Paper](https://arxiv.org/abs/2312.06109)<br>[GitHub](https://github.com/Ucas-HaoranWei/Vary) |
| 2023.11 | [![arXiv 2023.11](https://img.shields.io/badge/arXiv-2023.11-b31b1b)](https://arxiv.org/abs/2311.11810)<br>**DocPedia** | frequency-domain OCR-free document understanding | [Paper](https://arxiv.org/abs/2311.11810)<br>[Hugging Face](https://huggingface.co/papers/2311.11810) |
| 2023.10 | [![arXiv 2023.10](https://img.shields.io/badge/arXiv-2023.10-b31b1b)](https://arxiv.org/abs/2310.05126)<br>**UReader** | OCR-free visually situated language understanding | [Paper](https://arxiv.org/abs/2310.05126) |
| 2023.08 | [![arXiv 2023.08](https://img.shields.io/badge/arXiv-2023.08-b31b1b)](https://arxiv.org/abs/2308.11592)<br>**UniDoc** | simultaneous text detection, recognition, spotting, and understanding | [Paper](https://arxiv.org/abs/2308.11592) |
| 2023.07 | [![arXiv 2023.07](https://img.shields.io/badge/arXiv-2023.07-b31b1b)](https://arxiv.org/abs/2307.02499) [![Star](https://img.shields.io/github/stars/X-PLUG/mPLUG-DocOwl.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/X-PLUG/mPLUG-DocOwl)<br>**DocOwl** | document-oriented VLM | [Paper](https://arxiv.org/abs/2307.02499)<br>[GitHub](https://github.com/X-PLUG/mPLUG-DocOwl) |
| 2023.06 | [![arXiv 2023.06](https://img.shields.io/badge/arXiv-2023.06-b31b1b)](https://arxiv.org/abs/2306.17107) [![Star](https://img.shields.io/github/stars/llavar/LLaVAR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/llavar/LLaVAR)<br>**LLaVAR** | visual instruction tuning for text-rich image understanding | [Paper](https://arxiv.org/abs/2306.17107)<br>[GitHub](https://github.com/llavar/LLaVAR)<br>[Project](https://llavar.github.io/) |


</details>

<details open>
<summary>2025-2026 OCR-Specialized Parsers</summary>


| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2026.06 | [![arXiv 2026.06](https://img.shields.io/badge/arXiv-2026.06-b31b1b)](https://arxiv.org/abs/2606.03264) [![Star](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/PaddlePaddle/PaddleOCR)<br>**PaddleOCR-VL-1.6** | latest compact document parsing VLM in the PaddleOCR-VL line | [Paper](https://arxiv.org/abs/2606.03264)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR)<br>[Docs](https://paddlepaddle.github.io/PaddleOCR/) |
| 2026.05 | [![arXiv 2026.05](https://img.shields.io/badge/arXiv-2026.05-b31b1b)](https://arxiv.org/abs/2605.27978)<br>**ABot-OCR** | AMap end-to-end OCR VLM; page image to clean Markdown; structure-constrained RL | [Paper](https://arxiv.org/abs/2605.27978) |
| 2026.03 | [![arXiv 2026.03](https://img.shields.io/badge/arXiv-2026.03-b31b1b)](https://arxiv.org/abs/2603.13398)<br>**Qianfan-OCR** | end-to-end document intelligence model | [Paper](https://arxiv.org/abs/2603.13398)<br>[Website](https://cloud.baidu.com/product/wenxinworkshop) |
| 2026.03 | [![arXiv 2026.03](https://img.shields.io/badge/arXiv-2026.03-b31b1b)](https://arxiv.org/abs/2603.10910)<br>**GLM-OCR** | OCR-specialized document parser | [Paper](https://arxiv.org/abs/2603.10910) |
| 2026.03 | [![arXiv 2026.03](https://img.shields.io/badge/arXiv-2026.03-b31b1b)](https://arxiv.org/abs/2603.01840) [![Star](https://img.shields.io/github/stars/FireRedTeam/FireRed-OCR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/FireRedTeam/FireRed-OCR)<br>**FireRed-OCR** | OCR-specialized VLM | [Paper](https://arxiv.org/abs/2603.01840)<br>[GitHub](https://github.com/FireRedTeam/FireRed-OCR) |
| 2026.03 | [![arXiv 2026.03](https://img.shields.io/badge/arXiv-2026.03-b31b1b)](https://arxiv.org/abs/2603.09677) [![Star](https://img.shields.io/github/stars/alibaba/Logics-Parsing.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/alibaba/Logics-Parsing)<br>**Logics-Parsing-Omni** | Alibaba unified parser for heterogeneous documents and videos | [Paper](https://arxiv.org/abs/2603.09677)<br>[GitHub](https://github.com/alibaba/Logics-Parsing) |
| 2026.03 | [![arXiv 2026.03](https://img.shields.io/badge/arXiv-2026.03-b31b1b)](https://arxiv.org/abs/2603.13032) [![Star](https://img.shields.io/github/stars/rednote-hilab/dots.mocr.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/rednote-hilab/dots.mocr)<br>**MOCR / dots.mocr** | RedNote/Xiaohongshu multimodal OCR parser; text, charts, diagrams, tables, icons, and code-level outputs | [Paper](https://arxiv.org/abs/2603.13032)<br>[GitHub](https://github.com/rednote-hilab/dots.mocr) |
| 2026.02 | [![arXiv 2026.02](https://img.shields.io/badge/arXiv-2026.02-b31b1b)](https://arxiv.org/abs/2602.06402)<br>**MeDocVL** | medical document understanding and parsing VLM | [Paper](https://arxiv.org/abs/2602.06402) |
| 2026.01 | [![arXiv 2026.01](https://img.shields.io/badge/arXiv-2026.01-b31b1b)](https://arxiv.org/abs/2601.21957) [![Star](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/PaddlePaddle/PaddleOCR)<br>**PaddleOCR-VL-1.5** | compact multi-task document parsing VLM | [Paper](https://arxiv.org/abs/2601.21957)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| 2026.01 | [![arXiv 2026.01](https://img.shields.io/badge/arXiv-2026.01-b31b1b)](https://arxiv.org/abs/2601.20552) [![Star](https://img.shields.io/github/stars/deepseek-ai/DeepSeek-OCR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/deepseek-ai/DeepSeek-OCR)<br>**DeepSeek-OCR 2** | causal-flow reordering and document parsing | [Paper](https://arxiv.org/abs/2601.20552)<br>[GitHub](https://github.com/deepseek-ai/DeepSeek-OCR) |
| 2026.01 | [![arXiv 2026.01](https://img.shields.io/badge/arXiv-2026.01-b31b1b)](https://arxiv.org/abs/2601.14490)<br>**GutenOCR** | grounded OCR front-end fine-tuned from Qwen2.5-VL | [Paper](https://arxiv.org/abs/2601.14490) |
| 2026.01 | [![arXiv 2026.01](https://img.shields.io/badge/arXiv-2026.01-b31b1b)](https://arxiv.org/abs/2601.14251)<br>**LightOnOCR-2-1B** | 1B multilingual end-to-end OCR VLM | [Paper](https://arxiv.org/abs/2601.14251) |
| 2026.01 | [![arXiv 2026.01](https://img.shields.io/badge/arXiv-2026.01-b31b1b)](https://arxiv.org/abs/2601.21639)<br>**OCRVerse** | Meituan holistic OCR VLM; unified text-centric and vision-centric OCR | [Paper](https://arxiv.org/abs/2601.21639) |
| 2026 | [![GitHub 2026](https://img.shields.io/badge/GitHub-2026-24292f?logo=github)](https://github.com/datalab-to/chandra) [![Star](https://img.shields.io/github/stars/datalab-to/chandra.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/datalab-to/chandra)<br>**Chandra / Chandra OCR 2** | full-page HTML / Markdown / JSON OCR model | [GitHub](https://github.com/datalab-to/chandra)<br>[HF](https://huggingface.co/datalab-to/chandra-ocr-2)<br>[Blog](https://landing.datalab.to/blog/introducing-chandra) |
| 2026 | [![HF 2026](https://img.shields.io/badge/HF-2026-ffcc4d?logo=huggingface)](https://huggingface.co/ibm-granite/granite-docling-258M)<br>**Granite-Docling-258M** | compact DocTags document conversion model | [Hugging Face](https://huggingface.co/ibm-granite/granite-docling-258M) |
| 2025.12 | [![arXiv 2025.12](https://img.shields.io/badge/arXiv-2025.12-b31b1b)](https://arxiv.org/abs/2512.02498)<br>**dots.ocr** | multilingual document layout parsing VLM | [Paper](https://arxiv.org/abs/2512.02498) |
| 2025.11 | [![arXiv 2025.11](https://img.shields.io/badge/arXiv-2025.11-b31b1b)](https://arxiv.org/abs/2511.19575)<br>**HunyuanOCR** | OCR-specialized document VLM | [Paper](https://arxiv.org/abs/2511.19575) |
| 2025.10 | [![arXiv 2025.10](https://img.shields.io/badge/arXiv-2025.10-b31b1b)](https://arxiv.org/abs/2510.19817) [![Star](https://img.shields.io/github/stars/allenai/olmocr.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/allenai/olmocr)<br>**olmOCR-2** | unit-test reward training for document OCR | [Paper](https://arxiv.org/abs/2510.19817)<br>[GitHub](https://github.com/allenai/olmocr) |
| 2025.10 | [![arXiv 2025.10](https://img.shields.io/badge/arXiv-2025.10-b31b1b)](https://arxiv.org/abs/2510.18234) [![Star](https://img.shields.io/github/stars/deepseek-ai/DeepSeek-OCR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/deepseek-ai/DeepSeek-OCR)<br>**DeepSeek-OCR** | visual token compression for OCR | [Paper](https://arxiv.org/abs/2510.18234)<br>[GitHub](https://github.com/deepseek-ai/DeepSeek-OCR) |
| 2025.10 | [![arXiv 2025.10](https://img.shields.io/badge/arXiv-2025.10-b31b1b)](https://arxiv.org/abs/2510.14528) [![Star](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/PaddlePaddle/PaddleOCR)<br>**PaddleOCR-VL** | compact multilingual document parsing VLM | [Paper](https://arxiv.org/abs/2510.14528)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| 2025.10 | [![HF 2025.10](https://img.shields.io/badge/HF-2025.10-ffcc4d?logo=huggingface)](https://huggingface.co/nanonets/Nanonets-OCR2-1.5B-exp)<br>**Nanonets-OCR2** | open-source image-to-Markdown OCR2 model family; tables, formulas, flowcharts, handwriting, checkboxes | [Website](https://nanonets.com/research/nanonets-ocr-2/)<br>[Hugging Face](https://huggingface.co/nanonets/Nanonets-OCR2-1.5B-exp) |
| 2025.09 | [![EMNLP 2025](https://img.shields.io/badge/EMNLP-2025-4b4b4b)](https://arxiv.org/abs/2509.01215) [![Star](https://img.shields.io/github/stars/Tencent/POINTS-Reader.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/Tencent/POINTS-Reader)<br>**POINTS-Reader** | distillation-free VLM adaptation for document conversion | [Paper](https://arxiv.org/abs/2509.01215)<br>[GitHub](https://github.com/Tencent/POINTS-Reader)<br>[Hugging Face](https://huggingface.co/tencent/POINTS-Reader) |
| 2025.09 | [![arXiv 2025.09](https://img.shields.io/badge/arXiv-2025.09-b31b1b)](https://arxiv.org/abs/2509.19760) [![Star](https://img.shields.io/github/stars/alibaba/Logics-Parsing.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/alibaba/Logics-Parsing)<br>**Logics-Parsing** | Alibaba structured document parsing with logical extraction and LLM framework | [Paper](https://arxiv.org/abs/2509.19760)<br>[GitHub](https://github.com/alibaba/Logics-Parsing) |
| 2025.06 | [![arXiv 2025.06](https://img.shields.io/badge/arXiv-2025.06-b31b1b)](https://arxiv.org/abs/2506.18023)<br>**PP-DocBee2** | efficient data and stronger document baselines | [Paper](https://arxiv.org/abs/2506.18023) |
| 2025.06 | [![arXiv 2025.06](https://img.shields.io/badge/arXiv-2025.06-b31b1b)](https://arxiv.org/abs/2506.03197)<br>**Infinity-Parser** | layout-aware reinforcement learning for scanned document parsing | [Paper](https://arxiv.org/abs/2506.03197) |
| 2025.06 | [![arXiv 2025.06](https://img.shields.io/badge/arXiv-2025.06-b31b1b)](https://arxiv.org/abs/2506.05218) [![Star](https://img.shields.io/github/stars/Yuliang-Liu/MonkeyOCR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/Yuliang-Liu/MonkeyOCR)<br>**MonkeyOCR** | structure-recognition-relation document parser | [Paper](https://arxiv.org/abs/2506.05218)<br>[GitHub](https://github.com/Yuliang-Liu/MonkeyOCR) |
| 2025.04 | [![HF 2025.04](https://img.shields.io/badge/HF-2025.04-ffcc4d?logo=huggingface)](https://huggingface.co/reducto/RolmOCR)<br>**RolmOCR** | faster lightweight open OCR model; Qwen2.5-VL-based page text extraction | [Hugging Face](https://huggingface.co/reducto/RolmOCR) |
| 2025.04 | [![arXiv 2025.04](https://img.shields.io/badge/arXiv-2025.04-b31b1b)](https://arxiv.org/abs/2504.03621)<br>**VISTA-OCR** | generative and interactive end-to-end OCR; printed and handwritten document OCR | [Paper](https://arxiv.org/abs/2504.03621) |
| 2025.03 | [![arXiv 2025.03](https://img.shields.io/badge/arXiv-2025.03-b31b1b)](https://arxiv.org/abs/2503.11576)<br>**SmolDocling** | ultra-compact document conversion VLM | [Paper](https://arxiv.org/abs/2503.11576)<br>[Hugging Face](https://huggingface.co/ds4sd/SmolDocling-256M-preview) |
| 2025.03 | [![arXiv 2025.03](https://img.shields.io/badge/arXiv-2025.03-b31b1b)](https://arxiv.org/abs/2503.04065)<br>**PP-DocBee** | multimodal document understanding baseline | [Paper](https://arxiv.org/abs/2503.04065) |
| 2025.02 | [![arXiv 2025.02](https://img.shields.io/badge/arXiv-2025.02-b31b1b)](https://arxiv.org/abs/2502.18443) [![Star](https://img.shields.io/github/stars/allenai/olmocr.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/allenai/olmocr)<br>**olmOCR** | open PDF-to-Markdown / page linearization model | [Paper](https://arxiv.org/abs/2502.18443)<br>[GitHub](https://github.com/allenai/olmocr) |
| 2025 | [![HF 2025](https://img.shields.io/badge/HF-2025-ffcc4d?logo=huggingface)](https://huggingface.co/nanonets/Nanonets-OCR-s)<br>**Nanonets-OCR-s** | 4B structured Markdown OCR model | [Hugging Face](https://huggingface.co/nanonets/Nanonets-OCR-s) |


</details>

<details open>
<summary>Emerging Generation and Training Routes</summary>


| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2026.03 | [![arXiv 2026.03](https://img.shields.io/badge/arXiv-2026.03-b31b1b)](https://arxiv.org/abs/2603.22458)<br>**MinerU-Diffusion** | diffusion-style inverse-rendering OCR | [Paper](https://arxiv.org/abs/2603.22458) |
| 2026.01 | [![arXiv 2026.01](https://img.shields.io/badge/arXiv-2026.01-b31b1b)](https://arxiv.org/abs/2601.08834)<br>**FDRL for Document OCR** | format-decoupled reinforcement learning | [Paper](https://arxiv.org/abs/2601.08834) |
| 2025.12 | [![arXiv 2025.12](https://img.shields.io/badge/arXiv-2025.12-b31b1b)](https://arxiv.org/abs/2512.18550) [![Star](https://img.shields.io/github/stars/ZZZZZQT/DOCR-Inspector.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/ZZZZZQT/DOCR-Inspector)<br>**DOCR-Inspector** | fine-grained evaluation and strategic optimization for document OCR parsing | [Paper](https://arxiv.org/abs/2512.18550)<br>[GitHub](https://github.com/ZZZZZQT/DOCR-Inspector) |
| 2025.08 | [![arXiv 2025.08](https://img.shields.io/badge/arXiv-2025.08-b31b1b)](https://arxiv.org/abs/2508.13238)<br>**DianJin-OCR-R1** | reasoning-and-tool interleaved OCR VLM route | [Paper](https://arxiv.org/abs/2508.13238) |


</details>

</details>

<a id="f3-hybrid-document-parsing-workflows"></a>

<details open>
<summary><strong>F3. Hybrid Document Parsing Workflows</strong></summary>


Systems that combine layout detection, OCR, region decomposition, VLM generation, rule-based validators, and document assembly.

<details open>
<summary>Full Document Parsing Workflows</summary>


| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2026.05 | [![arXiv 2026.05](https://img.shields.io/badge/arXiv-2026.05-b31b1b)](https://arxiv.org/abs/2605.24973) [![Star](https://img.shields.io/github/stars/opendatalab/MinerU.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/opendatalab/MinerU)<br>**MinerU-Popo** | post-processing tool for document parsing; layout/text/format repair | [Paper](https://arxiv.org/abs/2605.24973)<br>[GitHub](https://github.com/opendatalab/MinerU) |
| 2026.04 | [![arXiv 2026.04](https://img.shields.io/badge/arXiv-2026.04-b31b1b)](https://arxiv.org/abs/2604.04771) [![Star](https://img.shields.io/github/stars/opendatalab/MinerU.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/opendatalab/MinerU)<br>**MinerU2.5-Pro** | data-centric document parsing system | [Paper](https://arxiv.org/abs/2604.04771)<br>[GitHub](https://github.com/opendatalab/MinerU) |
| 2026.02 | [![arXiv 2026.02](https://img.shields.io/badge/arXiv-2026.02-b31b1b)](https://arxiv.org/abs/2602.05384) [![Star](https://img.shields.io/github/stars/bytedance/Dolphin.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/bytedance/Dolphin)<br>**Dolphin-v2** | anchor prompting + document parsing workflow | [Paper](https://arxiv.org/abs/2602.05384)<br>[GitHub](https://github.com/bytedance/Dolphin) |
| 2025.07 | [![arXiv 2025.07](https://img.shields.io/badge/arXiv-2025.07-b31b1b)](https://arxiv.org/abs/2507.05595) [![Star](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/PaddlePaddle/PaddleOCR)<br>**PaddleOCR 3.0 / PP-StructureV3** | industrial document parsing toolkit | [Paper](https://arxiv.org/abs/2507.05595)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR)<br>[Docs](https://paddlepaddle.github.io/PaddleOCR/) |
| 2025.02 | [![arXiv 2025.02](https://img.shields.io/badge/arXiv-2025.02-b31b1b)](https://arxiv.org/abs/2502.16161)<br>**OmniParser V2** | structured-points-of-thought for unified visual text parsing | [Paper](https://arxiv.org/abs/2502.16161) |
| 2024.08 | [![arXiv 2024.08](https://img.shields.io/badge/arXiv-2024.08-b31b1b)](https://arxiv.org/abs/2408.09869) [![Star](https://img.shields.io/github/stars/docling-project/docling.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/docling-project/docling)<br>**Docling** | production document conversion workflow | [Paper](https://arxiv.org/abs/2408.09869)<br>[GitHub](https://github.com/docling-project/docling)<br>[Docs](https://docling-project.github.io/docling/) |
| 2024.03 | [![arXiv 2024.03](https://img.shields.io/badge/arXiv-2024.03-b31b1b)](https://arxiv.org/abs/2403.19128)<br>**OmniParser** | unified text spotting, key information extraction, and table recognition | [Paper](https://arxiv.org/abs/2403.19128) |
| 2024.02 | [![GitHub 2024.02](https://img.shields.io/badge/GitHub-2024.02-24292f?logo=github)](https://github.com/opendatalab/MinerU) [![Star](https://img.shields.io/github/stars/opendatalab/MinerU.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/opendatalab/MinerU)<br>**MinerU** | layout decomposition + document parsing workflow | [GitHub](https://github.com/opendatalab/MinerU) |
| 2022.10 | [![arXiv 2022.10](https://img.shields.io/badge/arXiv-2022.10-b31b1b)](https://arxiv.org/abs/2210.05391) [![Star](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/PaddlePaddle/PaddleOCR)<br>**PP-Structure / PP-StructureV2** | layout + table + OCR document analysis workflow | [Paper](https://arxiv.org/abs/2210.05391)<br>[GitHub](https://github.com/PaddlePaddle/PaddleOCR)<br>[Docs](https://paddlepaddle.github.io/PaddleOCR/) |
| 2022.09 | [![GitHub 2022.09](https://img.shields.io/badge/GitHub-2022.09-24292f?logo=github)](https://github.com/Unstructured-IO/unstructured) [![Star](https://img.shields.io/github/stars/Unstructured-IO/unstructured.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/Unstructured-IO/unstructured)<br>**Unstructured** | document partitioning and ingestion workflow | [GitHub](https://github.com/Unstructured-IO/unstructured)<br>[Docs](https://docs.unstructured.io/) |


</details>

<details open>
<summary>PDF-to-Structured-Output Workflows</summary>


| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2025 | [![GitHub 2025](https://img.shields.io/badge/GitHub-2025-24292f?logo=github)](https://github.com/chatdoc-com/OCRFlux) [![Star](https://img.shields.io/github/stars/chatdoc-com/OCRFlux.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/chatdoc-com/OCRFlux)<br>**OCRFlux** | PDF/document parsing workflow; Markdown-oriented OCR pipeline | [GitHub](https://github.com/chatdoc-com/OCRFlux) |
| 2024.12 | [![GitHub 2024.12](https://img.shields.io/badge/GitHub-2024.12-24292f?logo=github)](https://github.com/QuivrHQ/MegaParse) [![Star](https://img.shields.io/github/stars/QuivrHQ/MegaParse.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/QuivrHQ/MegaParse)<br>**MegaParse** | document-to-Markdown parsing workflow for RAG ingestion | [GitHub](https://github.com/QuivrHQ/MegaParse)<br>[Docs](https://megaparse.com/) |
| 2024.11 | [![GitHub 2024.11](https://img.shields.io/badge/GitHub-2024.11-24292f?logo=github)](https://github.com/microsoft/markitdown) [![Star](https://img.shields.io/github/stars/microsoft/markitdown.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/microsoft/markitdown)<br>**MarkItDown** | Microsoft document-to-Markdown conversion utility; PDF / Office / image ingestion | [GitHub](https://github.com/microsoft/markitdown) |
| 2024.01 | [![GitHub 2024.01](https://img.shields.io/badge/GitHub-2024.01-24292f?logo=github)](https://github.com/datalab-to/surya) [![Star](https://img.shields.io/github/stars/datalab-to/surya.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/datalab-to/surya)<br>**Surya** | OCR, layout, reading order, line detection | [GitHub](https://github.com/datalab-to/surya) |
| 2023.10 | [![GitHub 2023.10](https://img.shields.io/badge/GitHub-2023.10-24292f?logo=github)](https://github.com/datalab-to/marker) [![Star](https://img.shields.io/github/stars/datalab-to/marker.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/datalab-to/marker)<br>**Marker** | PDF-to-Markdown workflow | [GitHub](https://github.com/datalab-to/marker) |
| 2022.09 | [![GitHub 2022.09](https://img.shields.io/badge/GitHub-2022.09-24292f?logo=github)](https://github.com/breezedeus/Pix2Text) [![Star](https://img.shields.io/github/stars/breezedeus/Pix2Text.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/breezedeus/Pix2Text)<br>**Pix2Text** | layout + formula + OCR workflow | [GitHub](https://github.com/breezedeus/Pix2Text) |
| 2022.06 | [![GitHub 2022.06](https://img.shields.io/badge/GitHub-2022.06-24292f?logo=github)](https://github.com/pymupdf/pymupdf4llm) [![Star](https://img.shields.io/github/stars/pymupdf/pymupdf4llm.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/pymupdf/pymupdf4llm)<br>**PyMuPDF4LLM** | PDF-to-Markdown / RAG document ingestion utility | [GitHub](https://github.com/pymupdf/pymupdf4llm)<br>[Docs](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/) |
| 2015.08 | [![GitHub 2015.08](https://img.shields.io/badge/GitHub-2015.08-24292f?logo=github)](https://github.com/jsvine/pdfplumber) [![Star](https://img.shields.io/github/stars/jsvine/pdfplumber.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/jsvine/pdfplumber)<br>**pdfplumber** | born-digital PDF text/table extraction utility | [GitHub](https://github.com/jsvine/pdfplumber)<br>[Docs](https://github.com/jsvine/pdfplumber) |
| 2012.10 | [![GitHub 2012.10](https://img.shields.io/badge/GitHub-2012.10-24292f?logo=github)](https://github.com/pymupdf/PyMuPDF) [![Star](https://img.shields.io/github/stars/pymupdf/PyMuPDF.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/pymupdf/PyMuPDF)<br>**PyMuPDF** | PDF page rendering and extraction utility | [GitHub](https://github.com/pymupdf/PyMuPDF)<br>[Docs](https://pymupdf.readthedocs.io/) |
| 2012.09 | [![GitHub 2012.09](https://img.shields.io/badge/GitHub-2012.09-24292f?logo=github)](https://github.com/kermitt2/grobid) [![Star](https://img.shields.io/github/stars/kermitt2/grobid.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/kermitt2/grobid)<br>**GROBID** | scholarly PDF structure extraction workflow | [GitHub](https://github.com/kermitt2/grobid)<br>[Docs](https://grobid.readthedocs.io/) |


</details>

</details>

<a id="f4-general-purpose-vlms-used-as-ocr-interfaces"></a>

<details open>
<summary><strong>F4. General-Purpose VLMs Used as OCR Interfaces</strong></summary>


General multimodal models that can perform OCR-related tasks through prompts, while OCR is only one part of their capability.

<details open>
<summary>Open General VLMs</summary>


| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2026.05 | [![HF 2026.05](https://img.shields.io/badge/HF-2026.05-ffcc4d?logo=huggingface)](https://huggingface.co/ibm-granite/granite-vision-4.1-4b) [![Star](https://img.shields.io/github/stars/ibm-granite/granite-vision-models.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/ibm-granite/granite-vision-models)<br>**Granite Vision 4.1** | open enterprise VLM; visual document extraction, charts, tables, and key-value extraction | [HF](https://huggingface.co/ibm-granite/granite-vision-4.1-4b)<br>[GitHub](https://github.com/ibm-granite/granite-vision-models)<br>[Docs](https://www.ibm.com/granite/docs/models/vision) |
| 2026.05 | [![GitHub 2026.05](https://img.shields.io/badge/GitHub-2026.05-24292f?logo=github)](https://github.com/OpenBMB/MiniCPM-V) [![Star](https://img.shields.io/github/stars/OpenBMB/MiniCPM-V.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/OpenBMB/MiniCPM-V)<br>**MiniCPM-V 4.6** | compact open VLM series; OCRBench-oriented small-model baseline | [GitHub](https://github.com/OpenBMB/MiniCPM-V)<br>[HF](https://huggingface.co/openbmb/MiniCPM-V-4.6) |
| 2026.04 | [![HF Blog 2026.04](https://img.shields.io/badge/HF%20Blog-2026.04-ffcc4d?logo=huggingface)](https://huggingface.co/blog/gemma4)<br>**Gemma 4** | open Gemma multimodal family; image/text/audio input and document understanding baseline | [HF Blog](https://huggingface.co/blog/gemma4)<br>[HF 31B](https://huggingface.co/google/gemma-4-31B-it) |
| 2026.04 | [![arXiv 2026.04](https://img.shields.io/badge/arXiv-2026.04-b31b1b)](https://arxiv.org/abs/2604.27393) [![Star](https://img.shields.io/github/stars/OpenBMB/MiniCPM-V.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/OpenBMB/MiniCPM-V)<br>**MiniCPM-o 4.5** | open omni-modal VLM; compact text/image/video/audio interface with OCR-rich image ability | [Paper](https://arxiv.org/abs/2604.27393)<br>[GitHub](https://github.com/OpenBMB/MiniCPM-V)<br>[HF](https://huggingface.co/openbmb/MiniCPM-V-4_5) |
| 2026.01 | [![Blog 2026.01](https://img.shields.io/badge/Blog-2026.01-24292f)](https://www.liquid.ai/blog/introducing-lfm2-5-the-next-generation-of-on-device-ai)<br>**LFM2.5-VL** | open-weight on-device VLM; multi-image, multilingual, OCRBench v2, and InfoVQA baseline | [Blog](https://www.liquid.ai/blog/introducing-lfm2-5-the-next-generation-of-on-device-ai)<br>[HF](https://huggingface.co/LiquidAI/LFM2.5-VL-1.6B-Extract) |
| 2025.11 | [![HF Paper 2025.11](https://img.shields.io/badge/HF%20Paper-2025.11-ffcc4d?logo=huggingface)](https://huggingface.co/papers/2511.21631) [![Star](https://img.shields.io/github/stars/QwenLM/Qwen3-VL.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/QwenLM/Qwen3-VL)<br>**Qwen3-VL** | dense/MoE open VLM family; long-context image/video/document prompting | [Paper](https://huggingface.co/papers/2511.21631)<br>[GitHub](https://github.com/QwenLM/Qwen3-VL)<br>[HF](https://huggingface.co/collections/Qwen/qwen3-vl) |
| 2025.09 | [![arXiv 2025.09](https://img.shields.io/badge/arXiv-2025.09-b31b1b)](https://arxiv.org/abs/2509.23661) [![Star](https://img.shields.io/github/stars/LLaVA-VL/LLaVA-NeXT.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/LLaVA-VL/LLaVA-NeXT)<br>**LLaVA-OneVision-1.5** | open LLaVA-OneVision upgrade; multimodal instruction baseline | [Paper](https://arxiv.org/abs/2509.23661)<br>[GitHub](https://github.com/LLaVA-VL/LLaVA-NeXT) |
| 2025.08 | [![arXiv 2025.08](https://img.shields.io/badge/arXiv-2025.08-b31b1b)](https://arxiv.org/abs/2508.18265) [![Star](https://img.shields.io/github/stars/OpenGVLab/InternVL.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/OpenGVLab/InternVL)<br>**InternVL3.5** | open VLM suite with cascade RL and visual resolution router | [Paper](https://arxiv.org/abs/2508.18265)<br>[GitHub](https://github.com/OpenGVLab/InternVL)<br>[Demo](https://chat.intern-ai.org.cn/) |
| 2025.08 | [![HF Paper 2025.08](https://img.shields.io/badge/HF%20Paper-2025.08-ffcc4d?logo=huggingface)](https://huggingface.co/papers/2508.11737) [![Star](https://img.shields.io/github/stars/AIDC-AI/Ovis.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/AIDC-AI/Ovis)<br>**Ovis2.5** | native-resolution open VLM; strong chart/document and dense-visual perception | [Paper](https://huggingface.co/papers/2508.11737)<br>[GitHub](https://github.com/AIDC-AI/Ovis)<br>[HF](https://huggingface.co/AIDC-AI/Ovis2.5-9B) |
| 2025.07 | [![arXiv 2025.07](https://img.shields.io/badge/arXiv-2025.07-b31b1b)](https://arxiv.org/abs/2507.06167) [![Star](https://img.shields.io/github/stars/SkyworkAI/Skywork-R1V.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/SkyworkAI/Skywork-R1V)<br>**Skywork-R1V / R1V2** | open multimodal reasoning VLM; visual reasoning and OCR-rich perception baseline | [Paper](https://arxiv.org/abs/2507.06167)<br>[GitHub](https://github.com/SkyworkAI/Skywork-R1V)<br>[HF](https://huggingface.co/Skywork/Skywork-R1V2-38B) |
| 2025.06 | [![CVPR 2025](https://img.shields.io/badge/CVPR-2025-4b4b4b)](https://arxiv.org/abs/2412.13303) [![Star](https://img.shields.io/github/stars/apple/ml-fastvlm.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/apple/ml-fastvlm)<br>**FastVLM** | efficient open VLM family; fast high-resolution image encoding and on-device deployment | [Paper](https://arxiv.org/abs/2412.13303)<br>[GitHub](https://github.com/apple/ml-fastvlm)<br>[HF](https://huggingface.co/collections/apple/fastvlm) |
| 2025.06 | [![arXiv 2025.06](https://img.shields.io/badge/arXiv-2025.06-b31b1b)](https://arxiv.org/abs/2506.03569) [![Star](https://img.shields.io/github/stars/XiaomiMiMo/MiMo-VL.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/XiaomiMiMo/MiMo-VL)<br>**MiMo-VL** | open visual-language reasoning model; GUI/OCR-rich general VLM baseline | [Paper](https://arxiv.org/abs/2506.03569)<br>[GitHub](https://github.com/XiaomiMiMo/MiMo-VL)<br>[HF](https://huggingface.co/XiaomiMiMo/MiMo-VL-7B-RL) |
| 2025.06 | [![HF Blog 2025.06](https://img.shields.io/badge/HF%20Blog-2025.06-ffcc4d?logo=huggingface)](https://huggingface.co/blog/gemma3n)<br>**Gemma 3n** | open on-device multimodal Gemma model; image/text/audio/video inputs | [HF Blog](https://huggingface.co/blog/gemma3n)<br>[HF Collection](https://huggingface.co/collections/google/gemma-3n) |
| 2025.05 | [![arXiv 2025.05](https://img.shields.io/badge/arXiv-2025.05-b31b1b)](https://arxiv.org/abs/2505.07062)<br>**Seed1.5-VL** | general VLM baseline with text-rich image ability | [Paper](https://arxiv.org/abs/2505.07062) |
| 2025.04 | [![arXiv 2025.04](https://img.shields.io/badge/arXiv-2025.04-b31b1b)](https://arxiv.org/abs/2504.10479) [![Star](https://img.shields.io/github/stars/OpenGVLab/InternVL.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/OpenGVLab/InternVL)<br>**InternVL3** | open general VLM OCR baseline | [Paper](https://arxiv.org/abs/2504.10479)<br>[GitHub](https://github.com/OpenGVLab/InternVL)<br>[Demo](https://chat.intern-ai.org.cn/) |
| 2025.04 | [![arXiv 2025.04](https://img.shields.io/badge/arXiv-2025.04-b31b1b)](https://arxiv.org/abs/2504.07491)<br>**Kimi-VL** | general VLM OCR and document prompting | [Paper](https://arxiv.org/abs/2504.07491) |
| 2025.04 | [![arXiv 2025.04](https://img.shields.io/badge/arXiv-2025.04-b31b1b)](https://arxiv.org/abs/2504.05299)<br>**SmolVLM** | compact open VLM family for efficient image/video understanding | [Paper](https://arxiv.org/abs/2504.05299)<br>[HF Blog](https://huggingface.co/blog/smolvlm) |
| 2025.04 | [![arXiv 2025.04](https://img.shields.io/badge/arXiv-2025.04-b31b1b)](https://arxiv.org/abs/2504.13181) [![Star](https://img.shields.io/github/stars/zai-org/GLM-V.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/zai-org/GLM-V)<br>**GLM-4.1V / GLM-4V family** | open general VLM baseline for high-resolution OCR-rich prompting | [Paper](https://arxiv.org/abs/2504.13181)<br>[GitHub](https://github.com/zai-org/GLM-V)<br>[Hugging Face](https://huggingface.co/collections/THUDM/glm-4v-667f2dfe7a4e15e9e6f55e9c) |
| 2025.04 | [![Blog 2025.04](https://img.shields.io/badge/Blog-2025.04-24292f)](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)<br>**Llama 4 Scout / Maverick** | open-weight native multimodal models; long-context OCR/document prompting baseline | [Blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)<br>[HF Scout](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E) |
| 2025.03 | [![HF Paper 2025.03](https://img.shields.io/badge/HF%20Paper-2025.03-ffcc4d?logo=huggingface)](https://huggingface.co/papers/2503.20215) [![Star](https://img.shields.io/github/stars/QwenLM/Qwen2.5-Omni.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/QwenLM/Qwen2.5-Omni)<br>**Qwen2.5-Omni** | open omni-modal model; text/image/audio/video perception and speech response | [Paper](https://huggingface.co/papers/2503.20215)<br>[GitHub](https://github.com/QwenLM/Qwen2.5-Omni)<br>[HF](https://huggingface.co/Qwen/Qwen2.5-Omni-7B) |
| 2025.03 | [![arXiv 2025.03](https://img.shields.io/badge/arXiv-2025.03-b31b1b)](https://arxiv.org/abs/2503.19786)<br>**Gemma 3** | open multimodal Gemma family; image-text understanding and multilingual OCR prompting | [Paper](https://arxiv.org/abs/2503.19786)<br>[HF Blog](https://huggingface.co/blog/gemma3) |
| 2025.03 | [![Blog 2025.03](https://img.shields.io/badge/Blog-2025.03-24292f)](https://mistral.ai/news/mistral-small-3-1/)<br>**Mistral Small 3.1** | open-weight text+vision model; compact OCR/document prompting baseline | [Blog](https://mistral.ai/news/mistral-small-3-1/)<br>[Kaggle](https://www.kaggle.com/models/mistral-ai/mistral-small-3.1) |
| 2025.03 | [![HF 2025.03](https://img.shields.io/badge/HF-2025.03-ffcc4d?logo=huggingface)](https://huggingface.co/CohereLabs/aya-vision-8b)<br>**Aya Vision** | open-weight multilingual VLM; OCR and visual reasoning across languages | [HF](https://huggingface.co/CohereLabs/aya-vision-8b)<br>[Docs](https://huggingface.co/docs/transformers/en/model_doc/aya_vision) |
| 2025.03 | [![HF 2025.03](https://img.shields.io/badge/HF-2025.03-ffcc4d?logo=huggingface)](https://huggingface.co/amd/Instella-VL-1B) [![Star](https://img.shields.io/github/stars/AMD-AGI/InstellaVL.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/AMD-AGI/InstellaVL)<br>**Instella-VL-1B** | fully open 1B VLM; reproducible small-model baseline with training code | [HF](https://huggingface.co/amd/Instella-VL-1B)<br>[GitHub](https://github.com/AMD-AGI/InstellaVL)<br>[Blog](https://rocm.blogs.amd.com/artificial-intelligence/Instella-BL-1B-VLM/README.html) |
| 2025.02 | [![arXiv 2025.02](https://img.shields.io/badge/arXiv-2025.02-b31b1b)](https://arxiv.org/abs/2502.13923) [![Star](https://img.shields.io/github/stars/QwenLM/Qwen2.5-VL.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/QwenLM/Qwen2.5-VL)<br>**Qwen2.5-VL** | general VLM OCR and document prompting | [Paper](https://arxiv.org/abs/2502.13923)<br>[GitHub](https://github.com/QwenLM/Qwen2.5-VL)<br>[Demo](https://chat.qwen.ai/) |
| 2025.02 | [![arXiv 2025.02](https://img.shields.io/badge/arXiv-2025.02-b31b1b)](https://arxiv.org/abs/2502.05371)<br>**Phi-4-multimodal / Phi-4-Vision** | compact general VLM baseline | [Paper](https://arxiv.org/abs/2502.05371)<br>[Hugging Face](https://huggingface.co/microsoft/Phi-4-multimodal-instruct) |
| 2025.02 | [![HF Blog 2025.02](https://img.shields.io/badge/HF%20Blog-2025.02-ffcc4d?logo=huggingface)](https://huggingface.co/blog/smolvlm2)<br>**SmolVLM2** | tiny open VLM/video models; edge-device multimodal baseline | [HF Blog](https://huggingface.co/blog/smolvlm2) |
| 2025.01 | [![arXiv 2025.01](https://img.shields.io/badge/arXiv-2025.01-b31b1b)](https://arxiv.org/abs/2501.04658) [![Star](https://img.shields.io/github/stars/OpenGVLab/InternVL.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/OpenGVLab/InternVL)<br>**InternVL2.5** | open general VLM suite | [Paper](https://arxiv.org/abs/2501.04658)<br>[GitHub](https://github.com/OpenGVLab/InternVL)<br>[Demo](https://chat.intern-ai.org.cn/) |
| 2025.01 | [![arXiv 2025.01](https://img.shields.io/badge/arXiv-2025.01-b31b1b)](https://arxiv.org/abs/2501.17811) [![Star](https://img.shields.io/github/stars/deepseek-ai/Janus.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/deepseek-ai/Janus)<br>**Janus-Pro** | unified multimodal understanding and generation model; open visual understanding baseline | [Paper](https://arxiv.org/abs/2501.17811)<br>[GitHub](https://github.com/deepseek-ai/Janus)<br>[HF](https://huggingface.co/deepseek-ai/Janus-Pro-7B) |
| 2024.12 | [![arXiv 2024.12](https://img.shields.io/badge/arXiv-2024.12-b31b1b)](https://arxiv.org/abs/2412.10302) [![Star](https://img.shields.io/github/stars/deepseek-ai/DeepSeek-VL2.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/deepseek-ai/DeepSeek-VL2)<br>**DeepSeek-VL2** | MoE general VLM for text-rich images | [Paper](https://arxiv.org/abs/2412.10302)<br>[GitHub](https://github.com/deepseek-ai/DeepSeek-VL2) |
| 2024.12 | [![arXiv 2024.12](https://img.shields.io/badge/arXiv-2024.12-b31b1b)](https://arxiv.org/abs/2412.03555)<br>**PaliGemma 2** | versatile transfer VLM family; OCR/table/formula-related transfer tasks | [Paper](https://arxiv.org/abs/2412.03555)<br>[HF](https://huggingface.co/google/paligemma2-28b-mix-224) |
| 2024.11 | [![HF 2024.11](https://img.shields.io/badge/HF-2024.11-ffcc4d?logo=huggingface)](https://huggingface.co/mistralai/Pixtral-Large-Instruct-2411)<br>**Pixtral Large** | open-weight frontier multimodal model; documents, charts, and natural images | [HF](https://huggingface.co/mistralai/Pixtral-Large-Instruct-2411) |
| 2024.10 | [![arXiv 2024.10](https://img.shields.io/badge/arXiv-2024.10-b31b1b)](https://arxiv.org/abs/2410.05993) [![Star](https://img.shields.io/github/stars/rhymes-ai/Aria.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/rhymes-ai/Aria)<br>**Aria** | open native multimodal MoE; long-context document/video understanding | [Paper](https://arxiv.org/abs/2410.05993)<br>[GitHub](https://github.com/rhymes-ai/Aria) |
| 2024.10 | [![arXiv 2024.10](https://img.shields.io/badge/arXiv-2024.10-b31b1b)](https://arxiv.org/abs/2410.07073)<br>**Pixtral 12B** | open-weight multimodal model; multi-image dialogue and OCR-rich prompting | [Paper](https://arxiv.org/abs/2410.07073)<br>[HF](https://huggingface.co/mistralai/Pixtral-12B-2409) |
| 2024.09 | [![arXiv 2024.09](https://img.shields.io/badge/arXiv-2024.09-b31b1b)](https://arxiv.org/abs/2409.17146) [![Star](https://img.shields.io/github/stars/allenai/molmo.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/allenai/molmo)<br>**Molmo** | open general VLM baseline | [Paper](https://arxiv.org/abs/2409.17146)<br>[GitHub](https://github.com/allenai/molmo) |
| 2024.09 | [![arXiv 2024.09](https://img.shields.io/badge/arXiv-2024.09-b31b1b)](https://arxiv.org/abs/2409.11402)<br>**NVLM** | open frontier-class multimodal LLM baseline | [Paper](https://arxiv.org/abs/2409.11402)<br>[Hugging Face](https://huggingface.co/nvidia) |
| 2024.09 | [![arXiv 2024.09](https://img.shields.io/badge/arXiv-2024.09-b31b1b)](https://arxiv.org/abs/2409.12191) [![Star](https://img.shields.io/github/stars/QwenLM/Qwen2-VL.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/QwenLM/Qwen2-VL)<br>**Qwen2-VL** | dynamic-resolution VLM with OCR ability | [Paper](https://arxiv.org/abs/2409.12191)<br>[GitHub](https://github.com/QwenLM/Qwen2-VL) |
| 2024.09 | [![arXiv 2024.09](https://img.shields.io/badge/arXiv-2024.09-b31b1b)](https://arxiv.org/abs/2409.03213)<br>**Phi-3.5-Vision** | compact general VLM baseline | [Paper](https://arxiv.org/abs/2409.03213)<br>[Hugging Face](https://huggingface.co/microsoft/Phi-3.5-vision-instruct) |
| 2024.09 | [![Model 2024.09](https://img.shields.io/badge/Model-2024.09-24292f)](https://www.llama.com/)<br>**Llama 3.2 Vision** | open-weight Llama vision model; general VLM baseline | [Website](https://www.llama.com/)<br>[HF](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) |
| 2024.08 | [![arXiv 2024.08](https://img.shields.io/badge/arXiv-2024.08-b31b1b)](https://arxiv.org/abs/2408.12637)<br>**Idefics3** | open multimodal model; OCR/document understanding and visual reasoning | [Paper](https://arxiv.org/abs/2408.12637)<br>[HF](https://huggingface.co/HuggingFaceM4/Idefics3-8B-Llama3) |
| 2024.08 | [![arXiv 2024.08](https://img.shields.io/badge/arXiv-2024.08-b31b1b)](https://arxiv.org/abs/2408.16500) [![Star](https://img.shields.io/github/stars/THUDM/CogVLM2.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/THUDM/CogVLM2)<br>**CogVLM2** | open general VLM baseline with high-resolution perception | [Paper](https://arxiv.org/abs/2408.16500)<br>[GitHub](https://github.com/THUDM/CogVLM2) |
| 2024.08 | [![arXiv 2024.08](https://img.shields.io/badge/arXiv-2024.08-b31b1b)](https://arxiv.org/abs/2408.03326) [![Star](https://img.shields.io/github/stars/LLaVA-VL/LLaVA-NeXT.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/LLaVA-VL/LLaVA-NeXT)<br>**LLaVA-OneVision** | open general VLM baseline | [Paper](https://arxiv.org/abs/2408.03326)<br>[GitHub](https://github.com/LLaVA-VL/LLaVA-NeXT) |
| 2024.08 | [![arXiv 2024.08](https://img.shields.io/badge/arXiv-2024.08-b31b1b)](https://arxiv.org/abs/2408.01800) [![Star](https://img.shields.io/github/stars/OpenBMB/MiniCPM-o.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/OpenBMB/MiniCPM-o)<br>**MiniCPM-V** | mobile-scale general MLLM with OCR ability | [Paper](https://arxiv.org/abs/2408.01800)<br>[GitHub](https://github.com/OpenBMB/MiniCPM-o)<br>[Demo](https://minicpm-omni.openbmb.cn/) |
| 2024.08 | [![arXiv 2024.08](https://img.shields.io/badge/arXiv-2024.08-b31b1b)](https://arxiv.org/abs/2408.12688) [![Star](https://img.shields.io/github/stars/zai-org/GLM-V.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/zai-org/GLM-V)<br>**GLM-4V** | open general VLM for image, chart, and document prompting | [Paper](https://arxiv.org/abs/2408.12688)<br>[GitHub](https://github.com/zai-org/GLM-V) |
| 2024.07 | [![arXiv 2024.07](https://img.shields.io/badge/arXiv-2024.07-b31b1b)](https://arxiv.org/abs/2407.07726)<br>**PaliGemma** | open VLM baseline for OCR prompting | [Paper](https://arxiv.org/abs/2407.07726)<br>[Hugging Face](https://huggingface.co/google/paligemma-3b-mix-448) |
| 2024.06 | [![arXiv 2024.06](https://img.shields.io/badge/arXiv-2024.06-b31b1b)](https://arxiv.org/abs/2406.16860) [![Star](https://img.shields.io/github/stars/cambrian-mllm/cambrian.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/cambrian-mllm/cambrian)<br>**Cambrian-1** | vision-centric MLLM baseline for visual and OCR-rich perception | [Paper](https://arxiv.org/abs/2406.16860)<br>[GitHub](https://github.com/cambrian-mllm/cambrian)<br>[Project](https://cambrian-mllm.github.io/) |
| 2024.05 | [![arXiv 2024.05](https://img.shields.io/badge/arXiv-2024.05-b31b1b)](https://arxiv.org/abs/2405.02246)<br>**Idefics2** | open multimodal instruction model for visual document prompting | [Paper](https://arxiv.org/abs/2405.02246)<br>[Hugging Face](https://huggingface.co/HuggingFaceM4/idefics2-8b) |
| 2024.04 | [![arXiv 2024.04](https://img.shields.io/badge/arXiv-2024.04-b31b1b)](https://arxiv.org/abs/2404.16821) [![Star](https://img.shields.io/github/stars/OpenGVLab/InternVL.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/OpenGVLab/InternVL)<br>**InternVL 1.5** | open general VLM suite | [Paper](https://arxiv.org/abs/2404.16821)<br>[GitHub](https://github.com/OpenGVLab/InternVL)<br>[Demo](https://chat.intern-ai.org.cn/) |
| 2024.03 | [![arXiv 2024.03](https://img.shields.io/badge/arXiv-2024.03-b31b1b)](https://arxiv.org/abs/2403.05525) [![Star](https://img.shields.io/github/stars/deepseek-ai/DeepSeek-VL.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/deepseek-ai/DeepSeek-VL)<br>**DeepSeek-VL** | general VLM baseline for text-rich images | [Paper](https://arxiv.org/abs/2403.05525)<br>[GitHub](https://github.com/deepseek-ai/DeepSeek-VL) |
| 2024 | [![CVPR 2024](https://img.shields.io/badge/CVPR-2024-4b4b4b)](https://arxiv.org/abs/2312.14238) [![Star](https://img.shields.io/github/stars/OpenGVLab/InternVL.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/OpenGVLab/InternVL)<br>**InternVL** | open general VLM baseline | [Paper](https://arxiv.org/abs/2312.14238)<br>[GitHub](https://github.com/OpenGVLab/InternVL)<br>[Demo](https://chat.intern-ai.org.cn/) |
| 2024 | [![ICLR 2024](https://img.shields.io/badge/ICLR-2024-4b4b4b)](https://arxiv.org/abs/2311.03079) [![Star](https://img.shields.io/github/stars/THUDM/CogVLM.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/THUDM/CogVLM)<br>**CogVLM** | visual expert for language models | [Paper](https://arxiv.org/abs/2311.03079)<br>[GitHub](https://github.com/THUDM/CogVLM) |
| 2024 | [![NeurIPS 2024](https://img.shields.io/badge/NeurIPS-2024-4b4b4b)](https://arxiv.org/abs/2304.08485) [![Star](https://img.shields.io/github/stars/haotian-liu/LLaVA.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/haotian-liu/LLaVA)<br>**LLaVA** | visual instruction tuning baseline | [Paper](https://arxiv.org/abs/2304.08485)<br>[GitHub](https://github.com/haotian-liu/LLaVA) |
| 2023.12 | [![arXiv 2023.12](https://img.shields.io/badge/arXiv-2023.12-b31b1b)](https://arxiv.org/abs/2312.07533) [![Star](https://img.shields.io/github/stars/NVlabs/VILA.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/NVlabs/VILA)<br>**VILA** | visual language model pretraining baseline | [Paper](https://arxiv.org/abs/2312.07533)<br>[GitHub](https://github.com/NVlabs/VILA)<br>[Project](https://hanlab.mit.edu/projects/vila) |
| 2023.11 | [![arXiv 2023.11](https://img.shields.io/badge/arXiv-2023.11-b31b1b)](https://arxiv.org/abs/2311.06242)<br>**Florence-2** | fixed-token general vision foundation model | [Paper](https://arxiv.org/abs/2311.06242)<br>[Hugging Face](https://huggingface.co/microsoft/Florence-2-large) |
| 2023.08 | [![arXiv 2023.08](https://img.shields.io/badge/arXiv-2023.08-b31b1b)](https://arxiv.org/abs/2308.12966) [![Star](https://img.shields.io/github/stars/QwenLM/Qwen-VL.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/QwenLM/Qwen-VL)<br>**Qwen-VL** | visual text reading; grounding; document QA | [Paper](https://arxiv.org/abs/2308.12966)<br>[GitHub](https://github.com/QwenLM/Qwen-VL) |
| 2023.05 | [![NeurIPS 2023](https://img.shields.io/badge/NeurIPS-2023-4b4b4b)](https://arxiv.org/abs/2305.06500) [![Star](https://img.shields.io/github/stars/salesforce/LAVIS.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/salesforce/LAVIS)<br>**InstructBLIP** | instruction-tuned BLIP-family VLM baseline | [Paper](https://arxiv.org/abs/2305.06500)<br>[GitHub](https://github.com/salesforce/LAVIS) |
| 2023.04 | [![arXiv 2023.04](https://img.shields.io/badge/arXiv-2023.04-b31b1b)](https://arxiv.org/abs/2304.10592) [![Star](https://img.shields.io/github/stars/Vision-CAIR/MiniGPT-4.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/Vision-CAIR/MiniGPT-4)<br>**MiniGPT-4** | early open multimodal instruction model | [Paper](https://arxiv.org/abs/2304.10592)<br>[GitHub](https://github.com/Vision-CAIR/MiniGPT-4)<br>[Demo](https://minigpt-4.github.io/) |
| 2023.01 | [![ICML 2023](https://img.shields.io/badge/ICML-2023-4b4b4b)](https://arxiv.org/abs/2301.12597) [![Star](https://img.shields.io/github/stars/salesforce/LAVIS.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/salesforce/LAVIS)<br>**BLIP-2** | Q-Former-based VLM baseline | [Paper](https://arxiv.org/abs/2301.12597)<br>[GitHub](https://github.com/salesforce/LAVIS) |


</details>

<details open>
<summary>Closed/API General VLMs</summary>


| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2024-2025 | [![API 2024-2025](https://img.shields.io/badge/API-2024--2025-6f42c1)](https://docs.anthropic.com/)<br>**Claude 3 / 3.5 / 4** | closed general VLM OCR interface | [Docs](https://docs.anthropic.com/) |
| 2025 | [![API 2025](https://img.shields.io/badge/API-2025-6f42c1)](https://platform.openai.com/docs)<br>**GPT-5 family** | closed general VLM OCR interface | [Docs](https://platform.openai.com/docs) |
| 2024 | [![API 2024](https://img.shields.io/badge/API-2024-6f42c1)](https://platform.openai.com/docs)<br>**GPT-4o** | closed general VLM OCR interface | [Docs](https://platform.openai.com/docs) |
| 2023.12 | [![Report 2023.12](https://img.shields.io/badge/Report-2023.12-6f42c1)](https://arxiv.org/abs/2312.11805)<br>**Gemini family** | closed general VLM OCR interface | [Report](https://arxiv.org/abs/2312.11805)<br>[Docs](https://ai.google.dev/gemini-api/docs) |
| 2023 | [![System Card 2023](https://img.shields.io/badge/System%20Card-2023-6f42c1)](https://cdn.openai.com/papers/GPTV_System_Card.pdf)<br>**GPT-4V** | closed general VLM OCR interface | [System Card](https://cdn.openai.com/papers/GPTV_System_Card.pdf)<br>[Docs](https://platform.openai.com/docs) |


</details>

</details>

<a id="f5-commercial-ocr-and-document-ai-services"></a>

<details open>
<summary><strong>F5. Commercial OCR and Document AI Services</strong></summary>


Closed-source or managed systems for document conversion, enterprise OCR, scientific document parsing, formula OCR, receipts, forms, invoices, and other vertical workflows.

<details open>
<summary>Enterprise OCR and Document AI</summary>


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


</details>

<details open>
<summary>Scientific OCR and Managed Parsing APIs</summary>


| Date | Title | Task / Tags | Links |
|:---:|:---:|:---:|:---:|
| 2026 | [![Product docs 2026](https://img.shields.io/badge/Product%20docs-2026-6f42c1)](https://mathpix.com/)<br>**Mathpix** | formula / paper / document OCR; LaTeX / Markdown | [Website](https://mathpix.com/) |
| 2026 | [![Product docs 2026](https://img.shields.io/badge/Product%20docs-2026-6f42c1)](https://www.llamaindex.ai/llamaparse)<br>**LlamaParse** | managed PDF/document parsing for RAG pipelines | [Website](https://www.llamaindex.ai/llamaparse)<br>[Docs](https://docs.cloud.llamaindex.ai/llamaparse/getting_started) |
| 2026 | [![Product docs 2026](https://img.shields.io/badge/Product%20docs-2026-6f42c1)](https://unstructured.io/)<br>**Unstructured Platform** | managed document partitioning and RAG ingestion | [Website](https://unstructured.io/)<br>[Docs](https://docs.unstructured.io/) |
| 2026 | [![Product docs 2026](https://img.shields.io/badge/Product%20docs-2026-6f42c1)](https://cloud.baidu.com/product/wenxinworkshop)<br>**Baidu Qianfan / Wenxin document services** | managed document OCR and model API access | [Website](https://cloud.baidu.com/product/wenxinworkshop) |
| 2025 | [![Product docs 2025](https://img.shields.io/badge/Product%20docs-2025-6f42c1)](https://docs.mistral.ai/capabilities/document_ai/basic_ocr/)<br>**Mistral OCR** | managed OCR API; Markdown / structured response | [Docs](https://docs.mistral.ai/capabilities/document_ai/basic_ocr/) |
| 2025 | [![Product docs 2025](https://img.shields.io/badge/Product%20docs-2025-6f42c1)](https://help.aliyun.com/zh/model-studio/)<br>**Qwen-OCR API** | managed OCR API; structured OCR output | [Docs](https://help.aliyun.com/zh/model-studio/) |


</details>

</details>

<a id="benchmarks-and-datasets"></a>

## Benchmark and Dataset Collections

Benchmarks are organized by the capability layer they evaluate rather than by a single leaderboard. The table below keeps representative OCR, document parsing, document understanding, and VLM-OCR datasets visible on the front page; the fuller inventory is maintained in [`resources/benchmarks.md`](resources/benchmarks.md).

<details open>
<summary><strong>B1. Cropped Text Recognition and Line Recognition</strong></summary>

| Date | Name | Type | Input / Target | Metric / Scale | Links |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 2023 | [![arXiv 2023](https://img.shields.io/badge/arXiv-2023-b31b1b)](https://arxiv.org/abs/2303.16968)<br>**Union14M / Union14M-Benchmark** | training corpus / benchmark | word crops; multi-source text recognition | accuracy / NED; 14M-scale training pool | [Paper](https://arxiv.org/abs/2303.16968) |
| 2015 | [![ICDAR 2015](https://img.shields.io/badge/ICDAR-2015-4b4b4b)](https://rrc.cvc.uab.es/?ch=4)<br>**ICDAR 2015 Recognition** | benchmark | cropped incidental scene text | word accuracy | [Website](https://rrc.cvc.uab.es/?ch=4) |
| 2014 | [![Dataset 2014](https://img.shields.io/badge/Dataset-2014-4b4b4b)](https://www.robots.ox.ac.uk/~vgg/data/text/)<br>**MJSynth / Synth90k** | synthetic training data | rendered word crops | synthetic 9M word images | [Website](https://www.robots.ox.ac.uk/~vgg/data/text/) |
| 2013 | [![ICDAR 2013](https://img.shields.io/badge/ICDAR-2013-4b4b4b)](https://rrc.cvc.uab.es/?ch=2)<br>**ICDAR 2013 Recognition** | benchmark | focused scene word crops | word accuracy | [Website](https://rrc.cvc.uab.es/?ch=2) |
| 2011 | [![Dataset 2011](https://img.shields.io/badge/Dataset-2011-4b4b4b)](https://cvit.iiit.ac.in/research/projects/cvit-projects/the-iiit-5k-word-dataset)<br>**IIIT5K** | benchmark | cropped word images | word accuracy; 3K test words | [Website](https://cvit.iiit.ac.in/research/projects/cvit-projects/the-iiit-5k-word-dataset) |
| 2011 | [![Dataset 2011](https://img.shields.io/badge/Dataset-2011-4b4b4b)](http://www.iapr-tc11.org/mediawiki/index.php/The_Street_View_Text_Dataset)<br>**SVT** | benchmark | street-view word crops | word accuracy | [Website](http://www.iapr-tc11.org/mediawiki/index.php/The_Street_View_Text_Dataset) |
| 2011 | [![Dataset 2011](https://img.shields.io/badge/Dataset-2011-4b4b4b)](http://www.iapr-tc11.org/mediawiki/index.php/SVTP_Dataset)<br>**SVTP** | benchmark | perspective-distorted word crops | word accuracy | [Website](http://www.iapr-tc11.org/mediawiki/index.php/SVTP_Dataset) |
| 2011 | [![Dataset 2011](https://img.shields.io/badge/Dataset-2011-4b4b4b)](http://cs-chan.com/downloads_CUTE80_dataset.html)<br>**CUTE80** | benchmark | curved cropped words | word accuracy | [Website](http://cs-chan.com/downloads_CUTE80_dataset.html) |
| 2002 | [![Dataset 2002](https://img.shields.io/badge/Dataset-2002-4b4b4b)](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database)<br>**IAM** | handwriting benchmark | handwritten lines / words | CER / WER; line recognition | [Website](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database) |

</details>

<details open>
<summary><strong>B2. Scene Text Detection, Spotting, and Dense Text</strong></summary>

| Date | Name | Type | Input / Target | Metric / Scale | Links |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 2022 | [![CVPR 2022](https://img.shields.io/badge/CVPR-2022-4b4b4b)](https://arxiv.org/abs/2203.15143) [![Star](https://img.shields.io/github/stars/google-research-datasets/hiertext.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/google-research-datasets/hiertext)<br>**HierText** | benchmark | natural images; word/line/paragraph hierarchy | detection / recognition / hierarchy | [Paper](https://arxiv.org/abs/2203.15143)<br>[GitHub](https://github.com/google-research-datasets/hiertext) |
| 2021 | [![Dataset 2021](https://img.shields.io/badge/Dataset-2021-4b4b4b)](https://textvqa.org/textocr/)<br>**TextOCR** | benchmark | natural images with dense text | localization + transcription | [Website](https://textvqa.org/textocr/) |
| 2019 | [![ICDAR 2019](https://img.shields.io/badge/ICDAR-2019-4b4b4b)](https://rrc.cvc.uab.es/?ch=16)<br>**LSVT** | benchmark | large-scale Chinese scene text | detection / recognition / spotting | [Website](https://rrc.cvc.uab.es/?ch=16) |
| 2019 | [![ICDAR 2019](https://img.shields.io/badge/ICDAR-2019-4b4b4b)](https://rrc.cvc.uab.es/?ch=14)<br>**ArT** | benchmark | arbitrary-shape scene text | polygon detection / spotting | [Website](https://rrc.cvc.uab.es/?ch=14) |
| 2017 | [![ICDAR 2017](https://img.shields.io/badge/ICDAR-2017-4b4b4b)](https://rrc.cvc.uab.es/?ch=8)<br>**ICDAR 2017 MLT** | benchmark | multilingual scene text | multilingual detection / recognition | [Website](https://rrc.cvc.uab.es/?ch=8) |
| 2017 | [![CVPR 2017](https://img.shields.io/badge/CVPR-2017-4b4b4b)](https://github.com/Yuliang-Liu/Curve-Text-Detector)<br>**CTW1500** | benchmark | curved text-line images | polygon detection F1 | [GitHub](https://github.com/Yuliang-Liu/Curve-Text-Detector) |
| 2017 | [![CVPR 2017](https://img.shields.io/badge/CVPR-2017-4b4b4b)](https://github.com/cs-chan/Total-Text-Dataset)<br>**Total-Text** | benchmark | curved and horizontal scene text | polygon detection / spotting | [GitHub](https://github.com/cs-chan/Total-Text-Dataset) |
| 2016 | [![CVPR 2016](https://img.shields.io/badge/CVPR-2016-4b4b4b)](https://www.robots.ox.ac.uk/~vgg/data/scenetext/)<br>**SynthText** | synthetic training data | synthetic text in natural images | detection / recognition training | [Website](https://www.robots.ox.ac.uk/~vgg/data/scenetext/) |
| 2015 | [![ICDAR 2015](https://img.shields.io/badge/ICDAR-2015-4b4b4b)](https://rrc.cvc.uab.es/?ch=4)<br>**ICDAR 2015 Incidental Text** | benchmark | camera-captured incidental text | detection / spotting Hmean | [Website](https://rrc.cvc.uab.es/?ch=4) |
| 2012 | [![Dataset 2012](https://img.shields.io/badge/Dataset-2012-4b4b4b)](https://github.com/ut-text-detection/UTD-Text-Detection)<br>**MSRA-TD500** | benchmark | long multi-oriented text lines | text-line detection F1 | [GitHub](https://github.com/ut-text-detection/UTD-Text-Detection) |

</details>

<details open>
<summary><strong>B3. Layout, KIE, Forms, and Receipts</strong></summary>

| Date | Name | Type | Input / Target | Metric / Scale | Links |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 2022 | [![KDD 2022](https://img.shields.io/badge/KDD-2022-4b4b4b)](https://arxiv.org/abs/2206.01062)<br>**DocLayNet** | layout benchmark | diverse document pages; 11 layout classes | layout mAP; 80K pages | [Paper](https://arxiv.org/abs/2206.01062)<br>[HF](https://huggingface.co/datasets/ds4sd/DocLayNet) |
| 2022 | [![ACL 2022](https://img.shields.io/badge/ACL-2022-4b4b4b)](https://arxiv.org/abs/2104.08836) [![Star](https://img.shields.io/github/stars/doc-analysis/XFUND.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/doc-analysis/XFUND)<br>**XFUND** | multilingual form understanding | form images; entities and relations | entity / relation F1 | [Paper](https://arxiv.org/abs/2104.08836)<br>[GitHub](https://github.com/doc-analysis/XFUND) |
| 2021 | [![ICDAR 2021](https://img.shields.io/badge/ICDAR-2021-4b4b4b)](https://arxiv.org/abs/2103.10213)<br>**Kleister-NDA / Kleister-Charity** | KIE benchmark | long business documents | key-value extraction F1 | [Paper](https://arxiv.org/abs/2103.10213) |
| 2020 | [![COLING 2020](https://img.shields.io/badge/COLING-2020-4b4b4b)](https://arxiv.org/abs/2006.01038)<br>**DocBank** | layout / token benchmark | PDF pages; token-level labels | token classification; 500K pages | [Paper](https://arxiv.org/abs/2006.01038) |
| 2019 | [![ICDAR 2019](https://img.shields.io/badge/ICDAR-2019-4b4b4b)](https://rrc.cvc.uab.es/?ch=13)<br>**SROIE** | receipt KIE benchmark | scanned receipts | OCR + field extraction F1 | [Website](https://rrc.cvc.uab.es/?ch=13) |
| 2019 | [![NeurIPS 2019](https://img.shields.io/badge/NeurIPS-2019-4b4b4b)](https://arxiv.org/abs/1908.07836)<br>**PubLayNet** | layout benchmark | scientific articles; 5 layout classes | layout mAP; 340K pages | [Paper](https://arxiv.org/abs/1908.07836) |
| 2019 | [![Dataset 2019](https://img.shields.io/badge/Dataset-2019-4b4b4b)](https://github.com/clovaai/cord) [![Star](https://img.shields.io/github/stars/clovaai/cord.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/clovaai/cord)<br>**CORD** | receipt KIE benchmark | receipt images; semantic fields | entity F1 | [GitHub](https://github.com/clovaai/cord) |
| 2019 | [![ICDAR 2019](https://img.shields.io/badge/ICDAR-2019-4b4b4b)](https://guillaumejaume.github.io/FUNSD/)<br>**FUNSD** | form understanding benchmark | scanned forms; entities and links | entity / relation F1 | [Website](https://guillaumejaume.github.io/FUNSD/) |

</details>

<details open>
<summary><strong>B4. Tables, Formulas, and Structured Objects</strong></summary>

| Date | Name | Type | Input / Target | Metric / Scale | Links |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 2024 | [![arXiv 2024](https://img.shields.io/badge/arXiv-2024-b31b1b)](https://arxiv.org/abs/2404.15254) [![Star](https://img.shields.io/github/stars/opendatalab/UniMERNet.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/opendatalab/UniMERNet)<br>**UniMER-1M** | formula dataset | printed / handwritten formulas to LaTeX | edit distance; 1M-scale | [Paper](https://arxiv.org/abs/2404.15254)<br>[GitHub](https://github.com/opendatalab/UniMERNet) |
| 2021 | [![CVPR 2021](https://img.shields.io/badge/CVPR-2021-4b4b4b)](https://arxiv.org/abs/2110.00061) [![Star](https://img.shields.io/github/stars/microsoft/table-transformer.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/microsoft/table-transformer)<br>**PubTables-1M** | table benchmark | PDF tables; structure and cells | AP / GriTS; 1M tables | [Paper](https://arxiv.org/abs/2110.00061)<br>[GitHub](https://github.com/microsoft/table-transformer) |
| 2021 | [![Dataset 2021](https://img.shields.io/badge/Dataset-2021-4b4b4b)](https://github.com/wangwen-whu/WTW-Dataset) [![Star](https://img.shields.io/github/stars/wangwen-whu/WTW-Dataset.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/wangwen-whu/WTW-Dataset)<br>**WTW** | wild table benchmark | natural-scene / document tables | table detection / structure | [GitHub](https://github.com/wangwen-whu/WTW-Dataset) |
| 2020 | [![Dataset 2020](https://img.shields.io/badge/Dataset-2020-4b4b4b)](https://developer.ibm.com/exchanges/data/all/fintabnet/)<br>**FinTabNet** | table benchmark | financial report tables to HTML | TEDS / structure | [Website](https://developer.ibm.com/exchanges/data/all/fintabnet/) |
| 2020 | [![ECCV 2020](https://img.shields.io/badge/ECCV-2020-4b4b4b)](https://arxiv.org/abs/1911.10683)<br>**PubTabNet** | table benchmark | table images to HTML | TEDS; 500K+ tables | [Paper](https://arxiv.org/abs/1911.10683) |
| 2019 | [![arXiv 2019](https://img.shields.io/badge/arXiv-2019-b31b1b)](https://arxiv.org/abs/1908.04729)<br>**SciTSR** | table benchmark | scientific tables; cell structure | structure F1 | [Paper](https://arxiv.org/abs/1908.04729) |
| 2019 | [![arXiv 2019](https://img.shields.io/badge/arXiv-2019-b31b1b)](https://arxiv.org/abs/1903.01949)<br>**TableBank** | table benchmark | Word / LaTeX document tables | detection / structure; 417K tables | [Paper](https://arxiv.org/abs/1903.01949) |
| 2016 | [![arXiv 2016](https://img.shields.io/badge/arXiv-2016-b31b1b)](https://arxiv.org/abs/1609.04938)<br>**Im2LaTeX-100K** | formula dataset | rendered formulas to LaTeX | edit distance; 100K formulas | [Paper](https://arxiv.org/abs/1609.04938) |
| 2014- | [![Competition 2014-](https://img.shields.io/badge/Competition-2014--4b4b4b)](https://www.isical.ac.in/~crohme/)<br>**CROHME** | handwritten formula benchmark | online/offline math expressions | expression recognition rate | [Website](https://www.isical.ac.in/~crohme/) |
| 2020 | [![Dataset 2020](https://img.shields.io/badge/Dataset-2020-4b4b4b)](https://github.com/HCIILAB/HME100K-Dataset)<br>**HME100K** | formula benchmark | handwritten math images to LaTeX | edit distance / expression rate | [GitHub](https://github.com/HCIILAB/HME100K-Dataset) |

</details>

<details open>
<summary><strong>B5. Document QA, Chart QA, and OCR-Dependent Understanding</strong></summary>

| Date | Name | Type | Input / Target | Metric / Scale | Links |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 2024.07 | [![arXiv 2024.07](https://img.shields.io/badge/arXiv-2024.07-b31b1b)](https://arxiv.org/abs/2407.01523)<br>**MMLongBench-Doc** | long-document VQA benchmark | long documents + questions | answer accuracy / LLM judging | [Paper](https://arxiv.org/abs/2407.01523) |
| 2023 | [![ICCV 2023](https://img.shields.io/badge/ICCV-2023-4b4b4b)](https://arxiv.org/abs/2305.14828)<br>**DUDE** | document QA benchmark | diverse documents + questions | ANLS / accuracy | [Paper](https://arxiv.org/abs/2305.14828) |
| 2023 | [![Dataset 2023](https://img.shields.io/badge/Dataset-2023-4b4b4b)](https://rrc.cvc.uab.es/?ch=17)<br>**MP-DocVQA** | multi-page document QA | multi-page documents + questions | ANLS | [Website](https://rrc.cvc.uab.es/?ch=17) |
| 2022 | [![ACL 2022](https://img.shields.io/badge/ACL-2022-4b4b4b)](https://arxiv.org/abs/2203.10244) [![Star](https://img.shields.io/github/stars/vis-nlp/ChartQA.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/vis-nlp/ChartQA)<br>**ChartQA** | chart QA benchmark | chart images + questions | relaxed accuracy | [Paper](https://arxiv.org/abs/2203.10244)<br>[GitHub](https://github.com/vis-nlp/ChartQA) |
| 2021 | [![WACV 2021](https://img.shields.io/badge/WACV-2021-4b4b4b)](https://arxiv.org/abs/2104.12756)<br>**InfographicVQA** | infographic QA benchmark | infographics + questions | ANLS / accuracy | [Paper](https://arxiv.org/abs/2104.12756)<br>[Website](https://www.docvqa.org/datasets/infographicvqa) |
| 2020 | [![WACV 2020](https://img.shields.io/badge/WACV-2020-4b4b4b)](https://arxiv.org/abs/2007.00398)<br>**DocVQA** | document QA benchmark | document images + questions | ANLS | [Paper](https://arxiv.org/abs/2007.00398)<br>[Website](https://www.docvqa.org/) |
| 2019 | [![ICCV 2019](https://img.shields.io/badge/ICCV-2019-4b4b4b)](https://arxiv.org/abs/1904.08920)<br>**TextVQA** | text-rich VQA benchmark | natural images + questions | VQA accuracy | [Paper](https://arxiv.org/abs/1904.08920)<br>[Website](https://textvqa.org/) |
| 2019 | [![ICDAR 2019](https://img.shields.io/badge/ICDAR-2019-4b4b4b)](https://rrc.cvc.uab.es/?ch=11)<br>**ST-VQA** | scene-text VQA benchmark | text-rich images + questions | ANLS | [Website](https://rrc.cvc.uab.es/?ch=11) |
| 2018 | [![ICLR 2018](https://img.shields.io/badge/ICLR-2018-4b4b4b)](https://arxiv.org/abs/1710.07300)<br>**FigureQA** | chart / figure QA | synthetic figures + questions | accuracy | [Paper](https://arxiv.org/abs/1710.07300) |

</details>

<details open>
<summary><strong>B6. Page-Level Parsing and VLM-OCR Stress Tests</strong></summary>

| Date | Name | Type | Input / Target | Metric / Scale | Links |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 2026.06 | [![arXiv 2026.06](https://img.shields.io/badge/arXiv-2026.06-b31b1b)](https://arxiv.org/abs/2606.07401)<br>**RealDocBench** | real-world parsing benchmark | degraded real documents | parsing robustness | [Paper](https://arxiv.org/abs/2606.07401) |
| 2026.05 | [![arXiv 2026.05](https://img.shields.io/badge/arXiv-2026.05-b31b1b)](https://arxiv.org/abs/2605.22100)<br>**MPDocBench-Parse** | multi-page parsing benchmark | multi-page documents to structured output | parsing / multi-page consistency | [Paper](https://arxiv.org/abs/2605.22100) |
| 2026.05 | [![arXiv 2026.05](https://img.shields.io/badge/arXiv-2026.05-b31b1b)](https://arxiv.org/abs/2605.07492)<br>**PureDocBench** | page parsing benchmark | text-free / layout-focused document pages | structural parsing | [Paper](https://arxiv.org/abs/2605.07492) |
| 2026.05 | [![arXiv 2026.05](https://img.shields.io/badge/arXiv-2026.05-b31b1b)](https://arxiv.org/abs/2605.03903)<br>**CC-OCR v2** | VLM-OCR benchmark | multi-domain text-rich images | OCR capability and reasoning scores | [Paper](https://arxiv.org/abs/2605.03903) |
| 2025.12 | [![arXiv 2025.12](https://img.shields.io/badge/arXiv-2025.12-b31b1b)](https://arxiv.org/abs/2512.15872) [![Star](https://img.shields.io/github/stars/Topdu/DocPTBench.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/Topdu/DocPTBench)<br>**DocPTBench** | photographed document parsing | physical capture / perspective / lighting | parsing robustness | [Paper](https://arxiv.org/abs/2512.15872)<br>[GitHub](https://github.com/Topdu/DocPTBench) |
| 2025.08 | [![arXiv 2025.08](https://img.shields.io/badge/arXiv-2025.08-b31b1b)](https://arxiv.org/abs/2508.11236)<br>**Real5-OmniDocBench** | real-world parsing benchmark | five real degradation types | parse score / degradation drop | [Paper](https://arxiv.org/abs/2508.11236)<br>[HF](https://huggingface.co/datasets/PaddlePaddle/Real5-OmniDocBench) |
| 2025.05 | [![arXiv 2025.05](https://img.shields.io/badge/arXiv-2025.05-b31b1b)](https://arxiv.org/abs/2505.17163) [![Star](https://img.shields.io/github/stars/SCUT-DLVCLab/OCR-Reasoning.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/SCUT-DLVCLab/OCR-Reasoning)<br>**OCR-Reasoning** | reasoning-heavy OCR benchmark | text-rich images + questions | OCR reasoning accuracy | [Paper](https://arxiv.org/abs/2505.17163)<br>[GitHub](https://github.com/SCUT-DLVCLab/OCR-Reasoning)<br>[Project](https://ocr-reasoning.github.io/) |
| 2025.05 | [![arXiv 2025.05](https://img.shields.io/badge/arXiv-2025.05-b31b1b)](https://arxiv.org/abs/2505.12766)<br>**Reasoning-OCR** | reasoning-oriented OCR benchmark | text-rich images + reasoning tasks | answer accuracy | [Paper](https://arxiv.org/abs/2505.12766) |
| 2025.05 | [![arXiv 2025.05](https://img.shields.io/badge/arXiv-2025.05-b31b1b)](https://arxiv.org/abs/2505.05438)<br>**MDPBench** | multilingual parsing benchmark | multilingual document pages | multilingual parse score | [Paper](https://arxiv.org/abs/2505.05438) |
| 2025.02 | [![arXiv 2025.02](https://img.shields.io/badge/arXiv-2025.02-b31b1b)](https://arxiv.org/abs/2502.18411)<br>**olmOCR-Bench** | document OCR benchmark | PDF pages to text / Markdown | OCR parsing quality | [Paper](https://arxiv.org/abs/2502.18411) |
| 2025.02 | [![arXiv 2025.02](https://img.shields.io/badge/arXiv-2025.02-b31b1b)](https://arxiv.org/abs/2502.14949)<br>**KITAB-Bench** | multilingual OCR / document benchmark | Arabic text-rich documents | OCR and document understanding scores | [Paper](https://arxiv.org/abs/2502.14949) |
| 2025.01 | [![arXiv 2025.01](https://img.shields.io/badge/arXiv-2025.01-b31b1b)](https://arxiv.org/abs/2501.00321)<br>**OCRBench v2** | VLM-OCR benchmark | text-rich natural / document / chart images | scenario scores / total score | [Paper](https://arxiv.org/abs/2501.00321) |
| 2024.12 | [![arXiv 2024.12](https://img.shields.io/badge/arXiv-2024.12-b31b1b)](https://arxiv.org/abs/2412.07626) [![Star](https://img.shields.io/github/stars/opendatalab/OmniDocBench.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/opendatalab/OmniDocBench)<br>**OmniDocBench** | page-level parsing benchmark | PDF/page images to Markdown-like structure | module-level parse scores | [Paper](https://arxiv.org/abs/2412.07626)<br>[GitHub](https://github.com/opendatalab/OmniDocBench) |
| 2024.12 | [![arXiv 2024.12](https://img.shields.io/badge/arXiv-2024.12-b31b1b)](https://arxiv.org/abs/2412.02210)<br>**CC-OCR** | VLM-OCR benchmark | cross-domain text-rich images | OCR literacy scores | [Paper](https://arxiv.org/abs/2412.02210) |
| 2023.05 | [![arXiv 2023.05](https://img.shields.io/badge/arXiv-2023.05-b31b1b)](https://arxiv.org/abs/2305.07895) [![Star](https://img.shields.io/github/stars/Yuliang-Liu/MultimodalOCR.svg?style=social&label=Star&cacheSeconds=86400)](https://github.com/Yuliang-Liu/MultimodalOCR)<br>**OCRBench** | VLM-OCR benchmark | mixed text-rich images | OCR task accuracy / total score | [Paper](https://arxiv.org/abs/2305.07895)<br>[GitHub](https://github.com/Yuliang-Liu/MultimodalOCR) |

</details>

## Other Resource Files

- `resources/models.md`: standalone expandable model collections for longer maintenance notes.
- `resources/benchmarks.md`: fuller OCR, document parsing, document understanding, and VLM-OCR benchmark inventory.
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
