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
| **PaddleOCR / PP-OCR / PP-OCRv5** | 2020.09 / 2026.03 | active industrial OCR toolkit and compact OCR model family | [PP-OCR](https://arxiv.org/abs/2009.09941), [PP-OCRv5](https://arxiv.org/abs/2603.24373), [PP-OCRv5 CVPR](https://openaccess.thecvf.com/content/CVPR2026/html/Cui_PP-OCRv5_A_Specialized_5M-Parameter_Model_Rivaling_Billion-Parameter_Vision-Language_Models_on_CVPR_2026_paper.html) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | [Docs](https://paddlepaddle.github.io/PaddleOCR/) |
| **Tesseract** | 2005-2026 | active open-source OCR engine; LSTM OCR and searchable document workflows | [ICDAR](https://doi.org/10.1109/ICDAR.2007.4376991) | [GitHub](https://github.com/tesseract-ocr/tesseract) | [Docs](https://tesseract-ocr.github.io/) |
| **OpenOCR** | 2024.05 | open OCR training and evaluation toolkit | - | [GitHub](https://github.com/topdu/openocr) | - |
| **Surya** | 2024.01 | OCR, layout, reading-order, and line-detection toolkit | - | [GitHub](https://github.com/datalab-to/surya) | - |
| **EffOCR / EfficientOCR** | 2023.10 | sample-efficient OCR package based on character / word image retrieval | [arXiv](https://arxiv.org/abs/2310.10050) | [GitHub](https://github.com/dell-research-harvard/efficient_ocr) | [Project](https://effocr.github.io/) |
| **MMOCR** | 2021.08 | OCR research toolkit | [arXiv](https://arxiv.org/abs/2108.06543), [ACM MM](https://dl.acm.org/doi/10.1145/3474085.3478328) | [GitHub](https://github.com/open-mmlab/mmocr) | [Docs](https://mmocr.readthedocs.io/) |
| **eScriptorium** | 2021.05 | open OCR/HTR production platform for segmentation, transcription, correction, and model training | - | [GitLab](https://gitlab.com/scripta/escriptorium) | [Docs](https://escriptorium.readthedocs.io/) |
| **docTR** | 2021.01 | document OCR toolkit | - | [GitHub](https://github.com/mindee/doctr) | [Docs](https://mindee.github.io/doctr/) |
| **RapidOCR** | 2021.01 | lightweight OCR toolkit with ONNX, OpenVINO, Paddle, and PyTorch backends | - | [GitHub](https://github.com/RapidAI/RapidOCR) | [Docs](https://rapidai.github.io/RapidOCRDocs/) |
| **EasyOCR** | 2020.03 | ready-to-use multilingual OCR engine | - | [GitHub](https://github.com/JaidedAI/EasyOCR) | - |
| **OCR-D / ocrd_all** | 2019.10 | modular OCR workflow framework and processor ecosystem | - | [GitHub](https://github.com/OCR-D/ocrd_all) | [Docs](https://ocr-d.de/en/) |
| **OCR4all** | 2019.09 | open OCR workflow for historical printings, including preprocessing, layout, recognition, correction, and training | [arXiv](https://arxiv.org/abs/1909.04032), [Applied Sciences](https://www.mdpi.com/2076-3417/9/22/4853) | [GitHub](https://github.com/OCR4all/OCR4all) | [Website](https://www.ocr4all.org/) |
| **keras-ocr** | 2019.07 | CRAFT + CRNN-style Python OCR pipeline | - | [GitHub](https://github.com/faustomorales/keras-ocr) | [Docs](https://keras-ocr.readthedocs.io/) |
| **CnOCR** | 2019.03 | Chinese OCR toolkit for line and crop recognition | - | [GitHub](https://github.com/breezedeus/CnOCR) | [Docs](https://cnocr.readthedocs.io/) |
| **Calamari OCR** | 2018-2026 | line-based OCR engine for historical documents and ensemble recognition | [DHQ](https://rlskoeser.github.io/dhqwords/vol/14/2/000451/) | [GitHub](https://github.com/Calamari-OCR/calamari) | [Docs](https://calamari-ocr.readthedocs.io/) |
| **Kraken** | 2016-2026 | trainable OCR/HTR engine for historical, handwritten, and non-Latin scripts | - | [GitHub](https://github.com/mittagessen/kraken) | [Docs](https://kraken.re/) |
| **OCRmyPDF** | 2013.12 | searchable-PDF OCR workflow | - | [GitHub](https://github.com/ocrmypdf/OCRmyPDF) | [Docs](https://ocrmypdf.readthedocs.io/) |
| **CuneiForm OCR** | 2008-2011 | legacy open-source multi-language OCR engine with layout analysis | - | [GitHub mirror](https://github.com/jwilk-mirrors/cuneiform-linux) | [Launchpad](https://launchpad.net/cuneiform-linux) |
| **OCRopus / ocropy** | 2007-2018 | open OCR research toolkit for segmentation and recognizer training | - | [GitHub](https://github.com/tmbdev/ocropy) | [Project](https://ocropus.github.io/) |
| **GNU Ocrad** | 2003-2022 | legacy GNU command-line OCR engine and library with layout analysis | - | [Website](https://www.gnu.org/software/ocrad/ocrad.html) | [Manual](https://www.gnu.org/software/ocrad/manual/ocrad_manual.html) |
| **GOCR / JOCR** | 2000-2018 | legacy GPL command-line OCR engine | - | [SourceForge](https://sourceforge.net/projects/jocr/) | [Website](https://jocr.sourceforge.net/) |

### Text Detection and Spotting Components

| Model / System | Date | Role | Paper | Code | Docs / Model |
|---|:---:|---|---|---|---|
| **InstructOCR** | 2024.12 | instruction-boosted scene text spotting | [arXiv](https://arxiv.org/abs/2412.15523), [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/32286) | [GitHub](https://github.com/ChenD-VL/InstructOCR) | - |
| **DNTextSpotter** | 2024.08 | denoising-training transformer for arbitrary-shape text spotting | [arXiv](https://arxiv.org/abs/2408.00355), [ACM MM](https://dl.acm.org/doi/10.1145/3664647.3680981) | [GitHub](https://github.com/yyyyyxie/DNTextSpotter) | - |
| **FastTextSpotter** | 2024.08 | high-efficiency multilingual transformer text spotting | [arXiv](https://arxiv.org/abs/2408.14998), [ICPR](https://doi.org/10.1007/978-3-031-78498-9_10) | [GitHub](https://github.com/alloydas/Fast-Textspotter) | - |
| **Bridging Text Spotting** | 2024.04 | bridge between modular detector-recognizer and end-to-end spotting | [arXiv](https://arxiv.org/abs/2404.04624), [CVPR](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_Bridging_the_Gap_Between_End-to-End_and_Two-Step_Text_Spotting_CVPR_2024_paper.html) | [GitHub](https://github.com/mxin262/Bridging-Text-Spotting) | - |
| **SwinTextSpotter v2** | 2024.01 | recognition-conversion and recognition-alignment text spotting | [arXiv](https://arxiv.org/abs/2401.07641), [IJCV](https://link.springer.com/article/10.1007/s11263-025-02428-0) | [GitHub](https://github.com/mxin262/SwinTextSpotterv2) | - |
| **ESTextSpotter** | 2023.08 | explicit-synergy transformer text spotting | [arXiv](https://arxiv.org/abs/2308.10147), [ICCV](https://openaccess.thecvf.com/content/ICCV2023/html/Huang_ESTextSpotter_Towards_Better_Scene_Text_Spotting_with_Explicit_Synergy_in_ICCV_2023_paper.html) | [GitHub](https://github.com/mxin262/ESTextSpotter) | - |
| **UNITS** | 2023.04 | unified scene text spotting via sequence generation | [arXiv](https://arxiv.org/abs/2304.03435), [CVPR](https://openaccess.thecvf.com/content/CVPR2023/html/Kil_Towards_Unified_Scene_Text_Spotting_Based_on_Sequence_Generation_CVPR_2023_paper.html) | [GitHub](https://github.com/clovaai/units) | - |
| **DeepSolo** | 2022.11 | explicit-point transformer text spotting | [arXiv](https://arxiv.org/abs/2211.10772), [CVPR](https://openaccess.thecvf.com/content/CVPR2023/html/Ye_DeepSolo_Let_Transformer_Decoder_With_Explicit_Points_Solo_for_Text_CVPR_2023_paper.html) | [GitHub](https://github.com/ViTAE-Transformer/DeepSolo) | - |
| **GLASS** | 2022.08 | global-to-local attention for scene text spotting | [arXiv](https://arxiv.org/abs/2208.03364), [ECCV](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136880248.pdf) | [GitHub](https://github.com/amazon-science/glass-text-spotting) | - |
| **DPText-DETR** | 2022.07 | dynamic-point transformer text detection | [arXiv](https://arxiv.org/abs/2207.04491), [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/25430) | [GitHub](https://github.com/ymy-k/DPText-DETR) | - |
| **TextBPN / TextBPN++** | 2021.07 / 2022.05 | boundary-proposal and boundary-transformer arbitrary-shape detection | [TextBPN](https://arxiv.org/abs/2107.12664), [ICCV](https://openaccess.thecvf.com/content/ICCV2021/html/Zhang_Adaptive_Boundary_Proposal_Network_for_Arbitrary_Shape_Text_Detection_ICCV_2021_paper.html), [TextBPN++](https://arxiv.org/abs/2205.05320), [TMM](https://doi.org/10.1109/TMM.2023.3286657) | [GitHub](https://github.com/GXYM/TextBPN-Plus-Plus) | - |
| **Text Spotting Transformer / TESTR** | 2022.04 | transformer-based end-to-end spotting | [arXiv](https://arxiv.org/abs/2204.01918), [CVPR](https://openaccess.thecvf.com/content/CVPR2022/html/Zhang_Text_Spotting_Transformers_CVPR_2022_paper.html) | [GitHub](https://github.com/mlpc-ucsd/TESTR) | - |
| **SwinTextSpotter** | 2022.03 | synergy-aware transformer text spotting | [arXiv](https://arxiv.org/abs/2203.10209), [CVPR](https://openaccess.thecvf.com/content/CVPR2022/html/Huang_SwinTextSpotter_Scene_Text_Spotting_via_Better_Synergy_Between_Text_Detection_CVPR_2022_paper.html) | [GitHub](https://github.com/mxin262/swintextspotter) | - |
| **DBNet++** | 2022.02 | adaptive-scale DB text detection | [arXiv](https://arxiv.org/abs/2202.10304), [TPAMI](https://www.computer.org/csdl/journal/tp/2023/01/09726868/1BrwkXHiM24) | [GitHub](https://github.com/MhLiao/DB) | - |
| **SPTS** | 2021.12 | single-point text spotting via sequence generation | [arXiv](https://arxiv.org/abs/2112.07917), [ACM MM](https://dl.acm.org/doi/10.1145/3503161.3547942) | [GitHub](https://github.com/shannanyinxiang/SPTS) | - |
| **FAST** | 2021.11 | faster arbitrary-shape text detector with minimalist kernel representation | [arXiv](https://arxiv.org/abs/2111.02394) | [GitHub](https://github.com/czczup/FAST) | - |
| **ABCNet v2** | 2021.05 | Bezier-curve scene text spotting | [arXiv](https://arxiv.org/abs/2105.03620), [TPAMI](https://www.computer.org/csdl/journal/tp/2022/11/09525302/1wuoVjl3Eu4) | [GitHub](https://github.com/aim-uofa/AdelaiDet) | - |
| **FCENet** | 2021.04 | Fourier-contour arbitrary-shape text detection | [arXiv](https://arxiv.org/abs/2104.10442), [CVPR](https://openaccess.thecvf.com/content/CVPR2021/html/Zhu_Fourier_Contour_Embedding_for_Arbitrary-Shaped_Text_Detection_CVPR_2021_paper.html) | [GitHub](https://github.com/yuchenwang815/FCENet) | - |
| **MOST** | 2021.04 | multi-oriented text detection with localization refinement | [arXiv](https://arxiv.org/abs/2104.01070), [CVPR](https://openaccess.thecvf.com/content/CVPR2021/html/He_MOST_A_Multi-Oriented_Scene_Text_Detector_With_Localization_Refinement_CVPR_2021_paper.html) | - | - |
| **PGNet** | 2021.04 | real-time point-gathering arbitrary-shape text spotting | [arXiv](https://arxiv.org/abs/2104.05458), [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/16383) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | - |
| **MANGO** | 2020.12 | mask-attention-guided one-stage text spotting | [arXiv](https://arxiv.org/abs/2012.04350), [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/16348) | [GitHub](https://github.com/hikopensource/DAVAR-Lab-OCR) | - |
| **Mask TextSpotter v3** | 2020.07 | segmentation-proposal scene text spotting | [arXiv](https://arxiv.org/abs/2007.09482), [ECCV](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/1436_ECCV_2020_paper.php) | [GitHub](https://github.com/MhLiao/MaskTextSpotterV3) | - |
| **ContourNet** | 2020.04 | contour-based arbitrary-shape text detection | [arXiv](https://arxiv.org/abs/2004.04940), [CVPR](https://openaccess.thecvf.com/content_CVPR_2020/html/Wang_ContourNet_Taking_a_Further_Step_Toward_Accurate_Arbitrary-Shaped_Scene_Text_CVPR_2020_paper.html) | - | - |
| **DRRG** | 2020.03 | graph-reasoning arbitrary-shape text detection | [arXiv](https://arxiv.org/abs/2003.07493), [CVPR](https://openaccess.thecvf.com/content_CVPR_2020/html/Zhang_Deep_Relational_Reasoning_Graph_Network_for_Arbitrary_Shape_Text_Detection_CVPR_2020_paper.html) | [GitHub](https://github.com/GXYM/DRRG) | - |
| **ABCNet** | 2020.02 | adaptive Bezier-curve text spotting | [arXiv](https://arxiv.org/abs/2002.10200), [CVPR](https://openaccess.thecvf.com/content_CVPR_2020/html/Liu_ABCNet_Real-Time_Scene_Text_Spotting_With_Adaptive_Bezier-Curve_Network_CVPR_2020_paper.html) | [GitHub](https://github.com/Yuliang-Liu/bezier_curve_text_spotting) | - |
| **TextFuseNet** | 2020 | richer fused features for arbitrary-shape text detection | [IJCAI](https://www.ijcai.org/proceedings/2020/72) | [GitHub](https://github.com/ying09/TextFuseNet) | - |
| **DBNet** | 2019.11 | differentiable-binarization text detection | [arXiv](https://arxiv.org/abs/1911.08947), [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/6812) | [GitHub](https://github.com/MhLiao/DB) | - |
| **CharNet** | 2019.10 | one-stage convolutional character network for detection and spotting | [arXiv](https://arxiv.org/abs/1910.07954), [ICCV](https://openaccess.thecvf.com/content_ICCV_2019/html/Xing_Convolutional_Character_Networks_ICCV_2019_paper.html) | [GitHub](https://github.com/msight-tech/research-charnet) | - |
| **PAN** | 2019.08 | pixel aggregation for arbitrary-shape text detection | [arXiv](https://arxiv.org/abs/1908.05900), [ICCV](https://openaccess.thecvf.com/content_ICCV_2019/html/Wang_Efficient_and_Accurate_Arbitrary-Shaped_Text_Detection_With_Pixel_Aggregation_Network_ICCV_2019_paper.html) | [GitHub](https://github.com/whai362/pan_pp.pytorch) | - |
| **CRAFT** | 2019.04 | character-region text detection | [arXiv](https://arxiv.org/abs/1904.01941), [CVPR](https://openaccess.thecvf.com/content_CVPR_2019/html/Baek_Character_Region_Awareness_for_Text_Detection_CVPR_2019_paper.html) | [GitHub](https://github.com/clovaai/CRAFT-pytorch) | - |
| **TextDragon** | 2019 | end-to-end arbitrary-shape text spotting with RoISlide | [CVF](https://openaccess.thecvf.com/content_ICCV_2019/papers/Feng_TextDragon_An_End-to-End_Framework_for_Arbitrary_Shaped_Text_Spotting_ICCV_2019_paper.pdf) | - | - |
| **TextSnake** | 2018.07 | flexible representation for arbitrary-shape text detection | [arXiv](https://arxiv.org/abs/1807.01544), [ECCV](https://openaccess.thecvf.com/content_ECCV_2018/html/Shangbang_Long_TextSnake_A_Flexible_ECCV_2018_paper.html) | [GitHub](https://github.com/princewang1994/TextSnake.pytorch) | - |
| **Mask TextSpotter** | 2018.07 | segmentation-based arbitrary-shape text spotting | [arXiv](https://arxiv.org/abs/1807.02242), [ECCV](https://openaccess.thecvf.com/content_ECCV_2018/html/Pengyuan_Lyu_Mask_TextSpotter_An_ECCV_2018_paper.html) | [GitHub](https://github.com/MhLiao/MaskTextSpotter) | - |
| **PSENet** | 2018.06 | progressive-scale arbitrary-shape text detection | [arXiv](https://arxiv.org/abs/1806.02559), [CVPR](https://openaccess.thecvf.com/content_CVPR_2019/html/Wang_Shape_Robust_Text_Detection_With_Progressive_Scale_Expansion_Network_CVPR_2019_paper.html) | [GitHub](https://github.com/whai362/PSENet) | - |
| **FOTS** | 2018.01 | fast oriented text spotting with shared detection-recognition features | [arXiv](https://arxiv.org/abs/1801.01671), [CVPR](https://openaccess.thecvf.com/content_cvpr_2018/html/Liu_FOTS_Fast_Oriented_CVPR_2018_paper.html) | - | - |
| **PixelLink** | 2018.01 | instance-segmentation text detector | [arXiv](https://arxiv.org/abs/1801.01315), [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/12269) | [GitHub](https://github.com/ZJULearning/pixel_link) | - |
| **TextBoxes++** | 2018.01 | oriented scene text detector | [arXiv](https://arxiv.org/abs/1801.02765) | [GitHub](https://github.com/MhLiao/TextBoxes_plusplus) | - |
| **EAST** | 2017.04 | dense-prediction text detection | [arXiv](https://arxiv.org/abs/1704.03155), [CVPR](https://openaccess.thecvf.com/content_cvpr_2017/html/Zhou_EAST_An_Efficient_CVPR_2017_paper.html) | [GitHub](https://github.com/argman/EAST) | - |
| **SegLink** | 2017.03 | oriented text detection by linking local segments | [arXiv](https://arxiv.org/abs/1703.06520) | [GitHub](https://github.com/bgshih/seglink) | - |
| **TextBoxes** | 2016.11 | single-shot horizontal text detector | [arXiv](https://arxiv.org/abs/1611.06779) | - | - |
| **CTPN** | 2016.09 | connectionist text proposal network | [arXiv](https://arxiv.org/abs/1609.03605) | [GitHub](https://github.com/tianzhi0549/CTPN) | - |

### Cropped Text Recognizers

| Model / System | Date | Role | Paper | Code | Docs / Model |
|---|:---:|---|---|---|---|
| **UniRec-0.1B** | 2025.12 | unified text and formula recognizer for word, line, paragraph, and document levels | [arXiv](https://arxiv.org/abs/2512.21095) | [GitHub](https://github.com/Topdu/OpenOCR) | [HF](https://huggingface.co/topdu/unirec-0.1b) |
| **MDiff4STR** | 2025.12 | mask-diffusion scene text recognizer | [arXiv](https://arxiv.org/abs/2512.01422) | [GitHub](https://github.com/Topdu/OpenOCR) | - |
| **SVTRv2** | 2024.11 | CTC recognizer with irregular-text handling and semantic guidance | [arXiv](https://arxiv.org/abs/2411.15858), [ICCV](https://openaccess.thecvf.com/content/ICCV2025/html/Du_SVTRv2_CTC_Beats_Encoder-Decoder_Models_in_Scene_Text_Recognition_ICCV_2025_paper.html) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | - |
| **SMTR / FocalSVTR** | 2024.07 | out-of-length text recognition with sub-string matching | [arXiv](https://arxiv.org/abs/2407.12317), [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/32285) | [GitHub](https://github.com/Topdu/OpenOCR/tree/main/configs/rec/smtr) | - |
| **IGTR** | 2024.01 | instruction-guided scene text recognition | [arXiv](https://arxiv.org/abs/2401.17851), [TPAMI](https://www.computer.org/csdl/journal/tp/2025/04/10820836/23d1lCCI3sI) | [GitHub](https://github.com/Topdu/OpenOCR) | - |
| **DTrOCR** | 2023.08 | decoder-only transformer for printed, handwritten, and scene text recognition | [arXiv](https://arxiv.org/abs/2308.15996), [WACV](https://openaccess.thecvf.com/content/WACV2024/html/Fujitake_DTrOCR_Decoder-Only_Transformer_for_Optical_Character_Recognition_WACV_2024_paper.html) | [GitHub reimpl.](https://github.com/arvindrajan92/DTrOCR) | - |
| **LISTER** | 2023.08 | length-insensitive scene text recognizer with neighbor decoding | [arXiv](https://arxiv.org/abs/2308.12774), [ICCV](https://openaccess.thecvf.com/content/ICCV2023/html/Cheng_LISTER_Neighbor_Decoding_for_Length-Insensitive_Scene_Text_Recognition_ICCV_2023_paper.html) | [GitHub](https://github.com/AlibabaResearch/AdvancedLiterateMachinery) | - |
| **CPPD** | 2023.07 | context-perception parallel decoder for fast STR | [arXiv](https://arxiv.org/abs/2307.12270), [TPAMI](https://www.computer.org/csdl/journal/tp/2025/06/10902187/24CDy8nNwHK) | [GitHub](https://github.com/Topdu/OpenOCR/tree/main/configs/rec/cppd) | - |
| **MAERec / Union14M** | 2023.07 | data-centric STR benchmark and MAE-pretrained recognizer | [arXiv](https://arxiv.org/abs/2307.08723), [ICCV](https://openaccess.thecvf.com/content/ICCV2023/html/Jiang_Revisiting_Scene_Text_Recognition_A_Data_Perspective_ICCV_2023_paper.html) | [GitHub](https://github.com/Mountchicken/Union14M) | [Project](https://union14m.github.io/) |
| **DiffusionSTR** | 2023.06 | diffusion model for scene text recognition | [arXiv](https://arxiv.org/abs/2306.16707) | - | - |
| **CLIP4STR** | 2023.05 | CLIP-based vision-language scene text recognizer | [arXiv](https://arxiv.org/abs/2305.14014) | [GitHub reimpl.](https://github.com/VamosC/CLIP4STR) | [HF](https://huggingface.co/mzhaoshuai/CLIP4STR) |
| **TPS++** | 2023.05 | attention-enhanced thin-plate-spline rectifier for STR | [arXiv](https://arxiv.org/abs/2305.05322), [IJCAI](https://www.ijcai.org/proceedings/2023/197) | [GitHub](https://github.com/simplify23/TPS_PP) | - |
| **LPV** | 2023.05 | linguistic-perception vision model for efficient STR | [arXiv](https://arxiv.org/abs/2305.05140), [IJCAI](https://www.ijcai.org/proceedings/2023/189) | [GitHub](https://github.com/CyrilSterling/LPV) | - |
| **LevOCR** | 2022.09 | Levenshtein-transformer STR with iterative sequence refinement | [arXiv](https://arxiv.org/abs/2209.03594), [ECCV](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/3820_ECCV_2022_paper.php) | [GitHub](https://github.com/AlibabaResearch/AdvancedLiterateMachinery) | - |
| **MGP-STR** | 2022.09 | multi-granularity prediction recognizer | [arXiv](https://arxiv.org/abs/2209.03592), [ECCV](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/3821_ECCV_2022_paper.php) | [GitHub](https://github.com/AlibabaResearch/AdvancedLiterateMachinery) | - |
| **PARSeq** | 2022.07 | permuted autoregressive recognizer | [arXiv](https://arxiv.org/abs/2207.06966), [ECCV](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/556_ECCV_2022_paper.php) | [GitHub](https://github.com/baudm/parseq) | - |
| **SVTR** | 2022.05 | efficient single-visual-model recognizer | [arXiv](https://arxiv.org/abs/2205.00159), [IJCAI](https://www.ijcai.org/proceedings/2022/124) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | - |
| **MATRN** | 2021.11 | interactive visual-semantic text recognition network | [arXiv](https://arxiv.org/abs/2111.15263), [ECCV](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/6583_ECCV_2022_paper.php) | [GitHub](https://github.com/byeonghu-na/MATRN) | - |
| **CDistNet** | 2021.11 | multi-domain character-distance recognizer | [arXiv](https://arxiv.org/abs/2111.11011), [IJCV](https://link.springer.com/article/10.1007/s11263-023-01880-0) | [GitHub](https://github.com/simplify23/CDistNet) | - |
| **TrOCR** | 2021.09 | pretrained encoder-decoder recognizer | [arXiv](https://arxiv.org/abs/2109.10282), [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/26538) | [GitHub](https://github.com/microsoft/unilm/tree/master/trocr) | [HF Docs](https://huggingface.co/docs/transformers/model_doc/trocr) |
| **VisionLAN** | 2021.08 | visual-language modeling recognizer | [arXiv](https://arxiv.org/abs/2108.09661) | [GitHub](https://github.com/wangyuxin87/VisionLAN) | - |
| **ViTSTR** | 2021.05 | ViT recognizer | [arXiv](https://arxiv.org/abs/2105.08582) | [GitHub](https://github.com/roatienza/deep-text-recognition-benchmark) | - |
| **ABINet** | 2021.03 | language-aware recognizer | [arXiv](https://arxiv.org/abs/2103.06495), [CVPR](https://openaccess.thecvf.com/content/CVPR2021/html/Fang_Read_Like_Humans_Autonomous_Bidirectional_and_Iterative_Language_Modeling_for_CVPR_2021_paper.html) | [GitHub](https://github.com/FangShancheng/ABINet) | - |
| **DiG** | 2021 | dictionary-guided scene text recognition | [CVF](https://openaccess.thecvf.com/content/CVPR2021/papers/Nguyen_Dictionary-Guided_Scene_Text_Recognition_CVPR_2021_paper.pdf) | [GitHub](https://github.com/VinAIResearch/dict-guided) | - |
| **RobustScanner** | 2020.07 | positional-clue enhanced recognizer | [arXiv](https://arxiv.org/abs/2007.07542) | - | - |
| **SEED** | 2020.05 | semantics-enhanced encoder-decoder recognizer | [arXiv](https://arxiv.org/abs/2005.10977) | [GitHub](https://github.com/Pay20Y/SEED) | - |
| **SRN** | 2020.03 | semantic reasoning recognizer | [arXiv](https://arxiv.org/abs/2003.12294) | - | - |
| **SCATTER** | 2020.03 | selective-context attention recognizer | [arXiv](https://arxiv.org/abs/2003.11288) | - | - |
| **TextScanner** | 2019.12 | order-aware character scanner | [arXiv](https://arxiv.org/abs/1912.12422) | - | - |
| **DAN** | 2019.12 | decoupled attention recognizer | [arXiv](https://arxiv.org/abs/1912.10205) | - | - |
| **SATRN** | 2019.10 | 2D self-attention text recognizer | [arXiv](https://arxiv.org/abs/1910.04396) | [GitHub](https://github.com/clovaai/satrn) | - |
| **MASTER** | 2019.10 | multi-aspect non-local recognizer | [arXiv](https://arxiv.org/abs/1910.02562) | [GitHub](https://github.com/wenwenyu/MASTER-pytorch) | - |
| **2D-CTC** | 2019.07 | two-dimensional CTC recognizer for irregular scene text | [arXiv](https://arxiv.org/abs/1907.09705) | - | - |
| **STR Benchmark (Baek et al.)** | 2019.04 | unified training and evaluation benchmark for cropped text recognition | [arXiv](https://arxiv.org/abs/1904.01906) | [GitHub](https://github.com/clovaai/deep-text-recognition-benchmark) | - |
| **ASTER** | 2019 | rectified irregular text recognition | [TPAMI](https://doi.org/10.1109/TPAMI.2018.2848939) | [GitHub](https://github.com/bgshih/aster) | - |
| **MORAN** | 2019.01 | rectified attention recognizer | [arXiv](https://arxiv.org/abs/1901.03003) | [GitHub](https://github.com/Canjie-Luo/MORAN_v2) | - |
| **ESIR** | 2018.12 | iterative image rectification for irregular text recognition | [arXiv](https://arxiv.org/abs/1812.05824) | [GitHub](https://github.com/YuckFu/ESIR) | - |
| **SAR** | 2018.11 | show-attend-and-read baseline for irregular text recognition | [arXiv](https://arxiv.org/abs/1811.00751) | - | - |
| **NRTR** | 2018.06 | no-recurrence seq2seq recognizer | [arXiv](https://arxiv.org/abs/1806.00926) | - | - |
| **AON** | 2017.11 | arbitrary-orientation scene text recognition | [arXiv](https://arxiv.org/abs/1711.04226) | - | - |
| **FAN** | 2017.09 | focusing-attention recognizer for attention drift | [arXiv](https://arxiv.org/abs/1709.02054) | - | - |
| **R2AM** | 2016.03 | recursive recurrent attention model for OCR in the wild | [arXiv](https://arxiv.org/abs/1603.03101) | - | - |
| **RARE** | 2016.03 | rectified attention recognizer | [arXiv](https://arxiv.org/abs/1603.03915) | - | - |
| **STAR-Net** | 2016 | spatial transformer network for scene text recognition | [BMVC](https://www.bmva-archive.org.uk/bmvc/2016/papers/paper043/abstract043.pdf) | - | - |
| **CRNN** | 2015.07 | cropped sequence recognition with CTC | [TPAMI](https://arxiv.org/abs/1507.05717) | [GitHub](https://github.com/meijieru/crnn.pytorch) | - |

### Formula, Table, and Structured-Object Components

| Model / System | Date | Role | Paper | Code | Docs / Model |
|---|:---:|---|---|---|---|
| **FastTab** | 2026.05 | fast grid-centric table structure recognition | [arXiv](https://arxiv.org/abs/2605.22422) | [GitHub](https://github.com/hamdilaziz/FastTab) | - |
| **TableSeq** | 2026.04 | unified generation of table structure, content, and layout | [arXiv](https://arxiv.org/abs/2604.16070), [IJDAR](https://link.springer.com/article/10.1007/s10032-026-00586-6) | [GitHub](https://github.com/hamdilaziz/TableSeq) | - |
| **TDATR** | 2026.03 | end-to-end table recognition with detail-aware learning and cell alignment | [arXiv](https://arxiv.org/abs/2603.22819) | [GitHub](https://github.com/Chunchunwumu/TDATR) | - |
| **Texo** | 2026.02 | compact formula recognizer | [arXiv](https://arxiv.org/abs/2602.17189) | - | - |
| **Tables Decoded / DELTA** | 2026 | decoupled table reconstruction with OTSL output | [WACV](https://openaccess.thecvf.com/content/WACV2026/html/Rajput_Tables_Decoded_DELTA_for_Structure_TARQA_for_Understanding_WACV_2026_paper.html) | [GitHub](https://github.com/Bharatgen-Tech/Tables-Decoded) | - |
| **IMPO / From Pixel to Precision** | 2026 | HMER with image-level reward | [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_From_Pixel_to_Precision_Enhancing_Handwritten_Mathematical_Expression_Recognition_with_CVPR_2026_paper.html) | - | - |
| **TexTeller / Tex80M** | 2025.08 | scalable handwritten formula recognition | [arXiv](https://arxiv.org/abs/2508.09220) | [GitHub](https://github.com/OleehyO/TexTeller) | [HF](https://huggingface.co/OleehyO/TexTeller) |
| **TABLET** | 2025.06 | encoder-only transformer for table structure recognition | [arXiv](https://arxiv.org/abs/2506.07015) | - | - |
| **PP-FormulaNet** | 2025.03 | formula recognition | [arXiv](https://arxiv.org/abs/2503.18382) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | - |
| **SemiHMER** | 2025.02 | semi-supervised HMER | [arXiv](https://arxiv.org/abs/2502.07172) | - | - |
| **TFLOP** | 2025.01 | table structure recognition with layout pointer | [arXiv](https://arxiv.org/abs/2501.11800) | [GitHub](https://github.com/UpstageAI/TFLOP) | - |
| **DocLayout-YOLO** | 2024.10 | document layout detection | [arXiv](https://arxiv.org/abs/2410.12628) | [GitHub](https://github.com/opendatalab/DocLayout-YOLO) | - |
| **TAMER** | 2024.08 | tree-aware transformer for HMER | [arXiv](https://arxiv.org/abs/2408.08578) | [GitHub](https://github.com/qingzhenduyu/TAMER) | - |
| **PosFormer** | 2024.07 | position-aware HMER | [arXiv](https://arxiv.org/abs/2407.07764), [ECCV](https://doi.org/10.1007/978-3-031-72670-5_8) | [GitHub](https://github.com/SJTU-DeepVisionLab/PosFormer) | - |
| **DLAFormer** | 2024.05 | unified document layout analysis with reading-order relations | [arXiv](https://arxiv.org/abs/2405.11757) | - | - |
| **UniMERNet** | 2024.04 | formula recognition | [arXiv](https://arxiv.org/abs/2404.15254) | [GitHub](https://github.com/opendatalab/UniMERNet) | - |
| **UniTable** | 2024.03 | unified table structure, cell content, and cell-box recognition | [arXiv](https://arxiv.org/abs/2403.04822) | [GitHub](https://github.com/poloclub/unitable) | [HF](https://huggingface.co/poloclub/UniTable) |
| **GAP** | 2024 | grammar- and position-aware multi-line formula recognition | [DOI](https://doi.org/10.1145/3616855.3635776) | - | - |
| **LAST** | 2023.10 | line-aware semi-autoregressive HMER | [DOI](https://doi.org/10.1145/3581783.3612499) | [GitHub](https://github.com/HCIILAB/LAST) | - |
| **VGT** | 2023.08 | vision-grid transformer for document layout analysis | [arXiv](https://arxiv.org/abs/2308.14978) | [GitHub](https://github.com/AlibabaResearch/AdvancedLiterateMachinery/tree/main/DocumentUnderstanding/VGT) | - |
| **SGRL** | 2023.08 | semantic graph representation learning for HMER | [arXiv](https://arxiv.org/abs/2308.10493) | - | - |
| **UniChart** | 2023.05 | chart comprehension and chart-to-table pretraining | [arXiv](https://arxiv.org/abs/2305.14761) | [GitHub](https://github.com/vis-nlp/UniChart) | [HF](https://huggingface.co/ahmed-masry/unichart-base-960) |
| **VAST** | 2023.03 | visual-alignment sequential coordinate modeling for TSR | [arXiv](https://arxiv.org/abs/2303.06949) | - | - |
| **TSRFormer / DQ-DETR** | 2023.03 | dynamic-query DETR for robust table structure recognition | [arXiv](https://arxiv.org/abs/2303.11615) | - | - |
| **MatCha** | 2022.12 | math reasoning and chart-derendering pretraining | [arXiv](https://arxiv.org/abs/2212.09662) | [GitHub](https://github.com/google-research/google-research/tree/master/deplot) | [HF](https://huggingface.co/google/matcha-chartqa) |
| **DePlot** | 2022.12 | plot-to-table translation for chart reasoning | [arXiv](https://arxiv.org/abs/2212.10505), [ACL](https://aclanthology.org/2023.findings-acl.660/) | [GitHub](https://github.com/google-research/google-research/tree/master/deplot) | [Kaggle](https://www.kaggle.com/models/google/deplot) |
| **StructEqTable** | 2022.09 | equation/table structure parsing | - | [GitHub](https://github.com/AlibabaResearch/AdvancedLiterateMachinery) | - |
| **CoMER** | 2022.07 | coverage modeling for transformer-based HMER | [arXiv](https://arxiv.org/abs/2207.04410), [ECCV](https://doi.org/10.1007/978-3-031-19815-1_23) | [GitHub](https://github.com/Green-Wood/CoMER) | - |
| **CAN** | 2022.07 | counting-aware HMER | [arXiv](https://arxiv.org/abs/2207.11463), [ECCV](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/685_ECCV_2022_paper.php) | [GitHub](https://github.com/LBH1024/CAN) | - |
| **GriTS** | 2022.03 | grid table similarity metric for table structure recognition | [arXiv](https://arxiv.org/abs/2203.12555) | [GitHub](https://github.com/microsoft/table-transformer) | - |
| **TableFormer** | 2022.03 | table structure recognition; table-to-HTML modeling | [arXiv](https://arxiv.org/abs/2203.01017), [CVPR](https://openaccess.thecvf.com/content/CVPR2022/html/Nassar_TableFormer_Table_Structure_Understanding_With_Transformers_CVPR_2022_paper.html) | - | - |
| **LGPMA** | 2022.03 | table detection and structure recognition | [arXiv](https://arxiv.org/abs/2203.09056) | - | - |
| **SAN** | 2022.03 | syntax-aware HMER | [arXiv](https://arxiv.org/abs/2203.01601), [CVPR](https://openaccess.thecvf.com/content/CVPR2022/html/Yuan_Syntax-Aware_Network_for_Handwritten_Mathematical_Expression_Recognition_CVPR_2022_paper.html) | [GitHub](https://github.com/tal-tech/san) | - |
| **Table Transformer / TATR** | 2021.10 | table detection and structure recognition; PubTables-1M baseline | [arXiv](https://arxiv.org/abs/2110.00061), [CVPR](https://openaccess.thecvf.com/content/CVPR2022/html/Smock_PubTables-1M_Towards_Comprehensive_Table_Extraction_From_Unstructured_Documents_CVPR_2022_paper.html) | [GitHub](https://github.com/microsoft/table-transformer) | [HF](https://huggingface.co/microsoft/table-transformer-structure-recognition) |
| **SEM** | 2021.07 | split-embed-merge table structure recognition | [arXiv](https://arxiv.org/abs/2107.05214) | [GitHub](https://github.com/ZZR8066/SEM) | - |
| **TableMaster** | 2021.05 | sequence-based table-to-HTML recognizer | [arXiv](https://arxiv.org/abs/2105.01848) | [GitHub](https://github.com/JiaquanYe/TableMASTER-mmocr) | - |
| **BTTR** | 2021.05 | bidirectionally trained transformer for HMER | [arXiv](https://arxiv.org/abs/2105.02412), [ICDAR](https://doi.org/10.1007/978-3-030-86331-9_37) | [GitHub](https://github.com/Green-Wood/BTTR) | - |
| **LayoutParser** | 2021.03 | layout analysis toolkit; model zoo and document layout pipelines | [arXiv](https://arxiv.org/abs/2103.15348), [ICDAR](https://doi.org/10.1007/978-3-030-86549-8_9) | [GitHub](https://github.com/Layout-Parser/layout-parser) | [Docs](https://layout-parser.github.io/) |
| **ChartOCR / DeepRule** | 2021 | chart data extraction via structural keypoints and rules | [WACV](https://openaccess.thecvf.com/content/WACV2021/html/Luo_ChartOCR_Data_Extraction_From_Charts_Images_via_a_Deep_Hybrid_WACV_2021_paper.html) | [GitHub](https://github.com/soap117/DeepRule) | - |
| **pix2tex / LaTeX-OCR** | 2020.12 | formula image to LaTeX | - | [GitHub](https://github.com/lukas-blecher/LaTeX-OCR) | - |
| **CascadeTabNet** | 2020.04 | end-to-end table detection and structure recognition | [arXiv](https://arxiv.org/abs/2004.12629), [CVPRW](https://openaccess.thecvf.com/content_CVPRW_2020/papers/w34/Prasad_CascadeTabNet_An_Approach_for_End_to_End_Table_Detection_and_CVPRW_2020_paper.pdf) | [GitHub](https://github.com/DevashishPrasad/CascadeTabNet) | - |
| **PubTabNet / EDD** | 2019.11 | table structure recognition baseline | [arXiv](https://arxiv.org/abs/1911.10683) | [GitHub](https://github.com/ibm-aur-nlp/PubTabNet), [EDD](https://github.com/ibm-aur-nlp/EDD) | - |
| **WAP** | 2017 | handwritten mathematical expression recognition | [DOI](https://doi.org/10.1016/j.patcog.2017.06.017) | - | - |
| **Im2Markup** | 2016.09 | image-to-LaTeX generation | [arXiv](https://arxiv.org/abs/1609.04938), [ICML](https://proceedings.mlr.press/v70/deng17a.html) | [GitHub](https://github.com/harvardnlp/im2markup) | - |

</details>

<a id="f2-foundation-model-document-parsers"></a>

<details>
<summary><strong>F2. Foundation-Model Document Parsers</strong></summary>

### OCR-Free and Transitional Encoder-Decoders

| Model / System | Date | Route | Paper | Code | Docs / Model |
|---|:---:|---|---|---|---|
| **PILOT / VISTA-OCR** | 2025.04 | promptable layout-aware encoder-decoder for full-page OCR, region reading, and text spotting | [arXiv](https://arxiv.org/abs/2504.03621) | - | - |
| **Arctic-TILT** | 2024.08 | efficient text-image-layout encoder-decoder for business document understanding | [arXiv](https://arxiv.org/abs/2408.04632), [ACL](https://aclanthology.org/2025.acl-industry.20/) | [GitHub](https://github.com/Snowflake-Labs/arctic-tilt) | [HF](https://huggingface.co/Snowflake/snowflake-arctic-tilt-v1.3) |
| **muGAT** | 2024.08 | Nougat-style multi-page context for document parsing | [arXiv](https://arxiv.org/abs/2408.15646) | [GitHub](https://github.com/aimagelab/mugat) | - |
| **LOCR** | 2024.03 | location-guided autoregressive document OCR to Markdown | [arXiv](https://arxiv.org/abs/2403.02127), [ACL](https://aclanthology.org/2024.findings-emnlp.314/) | [GitHub](https://github.com/Merry-bee/LOCR) | - |
| **KOSMOS-2.5** | 2023.09 | multimodal literate model for text-intensive images | [arXiv](https://arxiv.org/abs/2309.11419) | [GitHub](https://github.com/microsoft/unilm/tree/master/kosmos-2.5) | [HF](https://huggingface.co/microsoft/kosmos-2.5) |
| **Nougat** | 2023.08 | scholarly PDF-to-Markdown parser | [arXiv](https://arxiv.org/abs/2308.13418), [ICLR](https://openreview.net/forum?id=fUtxNAKpdV) | [GitHub](https://github.com/facebookresearch/nougat) | [Project](https://facebookresearch.github.io/nougat/) |
| **UDOP** | 2022.12 | unified vision-text-layout generation | [arXiv](https://arxiv.org/abs/2212.02623) | [GitHub](https://github.com/microsoft/UDOP) | - |
| **Pix2Struct** | 2022.10 | screenshot/page-to-sequence pretraining | [arXiv](https://arxiv.org/abs/2210.03347) | [GitHub](https://github.com/google-research/pix2struct) | - |
| **Dessurt** | 2022.03 | end-to-end document recognition and understanding | [arXiv](https://arxiv.org/abs/2203.16618), [ECCV Workshops](https://github.com/herobd/dessurt) | [GitHub](https://github.com/herobd/dessurt) | - |
| **Donut** | 2021.11 | OCR-free encoder-decoder | [arXiv](https://arxiv.org/abs/2111.15664) | [GitHub](https://github.com/clovaai/donut) | [HF Docs](https://huggingface.co/docs/transformers/model_doc/donut) |
| **TILT** | 2021.02 | OCR-assisted text-image-layout encoder-decoder for document understanding | [arXiv](https://arxiv.org/abs/2102.09550) | [GitHub (impl.)](https://github.com/uakarsh/TiLT-Implementation) | - |

### Document-VLM Precursors and Adaptations

| Model / System | Date | Route | Paper | Code | Docs / Model |
|---|:---:|---|---|---|---|
| **DocSLM** | 2025.11 | small VLM for efficient long multimodal document understanding | [arXiv](https://arxiv.org/abs/2511.11313), [CVF](https://openaccess.thecvf.com/content/CVPR2026F/html/Hannan_DocSLM_A_Small_Vision-Language_Model_for_Long_Multimodal_Document_Understanding_CVPRF_2026_paper.html) | - | - |
| **Docopilot** | 2025.07 | native document-level VLM and Doc-750K multi-page instruction data | [arXiv](https://arxiv.org/abs/2507.14675) | [GitHub](https://github.com/OpenGVLab/Docopilot) | [HF Dataset](https://huggingface.co/datasets/OpenGVLab/Doc-750K) |
| **TokenFD / TokenVL** | 2025.03 | token-level text-image foundation model and document-level MLLM | [arXiv](https://arxiv.org/abs/2503.02304) | [GitHub](https://github.com/Token-family/TokenFD) | - |
| **LayTokenLLM** | 2025.03 | single-token layout representation for document LLMs | [arXiv](https://arxiv.org/abs/2503.18434), [CVF](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhu_A_Simple_yet_Effective_Layout_Token_in_Large_Language_Models_CVPR_2025_paper.pdf) | - | - |
| **DocVLM** | 2024.12 | OCR-modality adapter for making frozen VLMs efficient document readers | [arXiv](https://arxiv.org/abs/2412.08746) | - | - |
| **HVFA** | 2024.11 | hierarchical visual feature aggregation for OCR-free document MLLMs | [arXiv](https://arxiv.org/abs/2411.05254), [NeurIPS](https://openreview.net/forum?id=PWkjxjgGLP) | - | - |
| **TextHawk2** | 2024.10 | bilingual OCR and grounding MLLM | [arXiv](https://arxiv.org/abs/2410.05261) | [GitHub](https://github.com/yuyq96/TextHawk) | [Hugging Face](https://huggingface.co/TencentBAC) |
| **DocOwl 2** | 2024.09 | high-resolution multi-page document VLM | [arXiv](https://arxiv.org/abs/2409.03420), [ACL](https://aclanthology.org/2025.acl-long.291/) | [GitHub](https://github.com/X-PLUG/mPLUG-DocOwl) | - |
| **GOT-OCR 2.0** | 2024.09 | unified OCR-specialized VLM | [arXiv](https://arxiv.org/abs/2409.01704) | [GitHub](https://github.com/Ucas-HaoranWei/GOT-OCR2.0) | - |
| **DocLayLLM** | 2024.08 | efficient multimodal extension of LLMs for text-rich document understanding | [arXiv](https://arxiv.org/abs/2408.15045) | [GitHub](https://github.com/whlscut/DocLayLLM) | - |
| **LLaVA-Read** | 2024.07 | dual-encoder MLLM for visual text understanding | [arXiv](https://arxiv.org/abs/2407.19185), [OpenReview](https://openreview.net/forum?id=pPK6sNbFWV) | - | - |
| **LayTextLLM** | 2024.07 | interleaved layout-text tokens for document understanding | [arXiv](https://arxiv.org/abs/2407.01976), [ACL](https://aclanthology.org/2025.findings-acl.379/) | [GitHub](https://github.com/laytextllm/laytextllm) | - |
| **StrucTexTv3** | 2024.05 | efficient VLM for text-rich image perception and comprehension | [arXiv](https://arxiv.org/abs/2405.21013) | - | - |
| **Fox** | 2024.05 | multi-page document understanding system | [arXiv](https://arxiv.org/abs/2405.14295) | [GitHub](https://github.com/ucaslcl/Fox) | - |
| **TextSquare / Square-10M** | 2024.04 | large-scale text-centric visual instruction tuning | [arXiv](https://arxiv.org/abs/2404.12803), [OpenReview](https://openreview.net/forum?id=a1adEtVoHS) | - | - |
| **HRVDA** | 2024.04 | high-resolution visual document assistant for LVLMs | [arXiv](https://arxiv.org/abs/2404.06918) | - | - |
| **TextHawk** | 2024.04 | fine-grained text perception in MLLMs | [arXiv](https://arxiv.org/abs/2404.09204) | [GitHub](https://github.com/yuyq96/TextHawk) | [Hugging Face](https://huggingface.co/TencentBAC) |
| **LayoutLLM** | 2024.04 | layout instruction tuning for document understanding | [arXiv](https://arxiv.org/abs/2404.05225) | [GitHub/Data](https://github.com/AlibabaResearch/AdvancedLiterateMachinery/tree/main/DocumentUnderstanding/LayoutLLM) | - |
| **DocOwl 1.5** | 2024.03 | OCR-free structure learning | [arXiv](https://arxiv.org/abs/2403.12895), [ACL](https://aclanthology.org/2024.findings-emnlp.175/) | [GitHub](https://github.com/X-PLUG/mPLUG-DocOwl) | - |
| **TextMonkey** | 2024.03 | OCR-free document MLLM | [arXiv](https://arxiv.org/abs/2403.04473), [TPAMI](https://www.computer.org/csdl/journal/tp/2026/05/11364328/2dAZUa3VEUE) | [GitHub](https://github.com/Yuliang-Liu/Monkey) | - |
| **DoCo** | 2024.02 | contrastive pretraining for fine-grained visual document understanding in LVLMs | [arXiv](https://arxiv.org/abs/2402.19014) | - | - |
| **DocLLM** | 2023.12 | layout-aware generative LLM for multimodal document understanding | [arXiv](https://arxiv.org/abs/2401.00908), [ACL](https://aclanthology.org/2024.acl-long.463/) | [GitHub](https://github.com/dswang2011/DocLLM) | - |
| **Vary** | 2023.12 | document-specialized VLM | [arXiv](https://arxiv.org/abs/2312.06109) | [GitHub](https://github.com/Ucas-HaoranWei/Vary) | - |
| **Monkey** | 2023.11 | text-centric MLLM | [arXiv](https://arxiv.org/abs/2311.06607) | [GitHub](https://github.com/Yuliang-Liu/Monkey) | - |
| **mPLUG-PaperOwl** | 2023.11 | scientific diagram and paper figure analysis with MLLMs | [arXiv](https://arxiv.org/abs/2311.18248) | [GitHub](https://github.com/X-PLUG/mPLUG-DocOwl/tree/main/PaperOwl) | - |
| **TGDoc** | 2023.11 | text-grounding document understanding with MLLMs | [arXiv](https://arxiv.org/abs/2311.13194) | [GitHub](https://github.com/harrytea/TGDoc) | - |
| **DocPedia** | 2023.11 | frequency-domain OCR-free document understanding | [arXiv](https://arxiv.org/abs/2311.11810), [SCIS](https://doi.org/10.1007/s11432-024-4250-y) | - | [HF Paper](https://huggingface.co/papers/2311.11810) |
| **UReader** | 2023.10 | OCR-free visually situated language understanding | [arXiv](https://arxiv.org/abs/2310.05126), [ACL](https://aclanthology.org/2023.findings-emnlp.187/) | [GitHub](https://github.com/LukeForeverYoung/UReader) | - |
| **UniDoc** | 2023.08 | simultaneous text detection, recognition, spotting, and understanding | [arXiv](https://arxiv.org/abs/2308.11592) | - | - |
| **DocOwl** | 2023.07 | document-oriented VLM | [arXiv](https://arxiv.org/abs/2307.02499) | [GitHub](https://github.com/X-PLUG/mPLUG-DocOwl) | - |
| **LLaVAR** | 2023.06 | visual instruction tuning for text-rich image understanding | [arXiv](https://arxiv.org/abs/2306.17107) | [GitHub](https://github.com/SALT-NLP/LLaVAR) | [Project](https://llavar.github.io/) |

### OCR-Specialized Page Parsers

| Model / System | Date | Route | Paper | Code | Docs / Model |
|---|:---:|---|---|---|---|
| **PaddleOCR-VL-1.6** | 2026.06 | latest compact document parsing VLM in the PaddleOCR-VL line | [arXiv](https://arxiv.org/abs/2606.03264) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | [Docs](https://paddlepaddle.github.io/PaddleOCR/) |
| **ABot-OCR** | 2026.05 | AMap end-to-end OCR VLM | [arXiv](https://arxiv.org/abs/2605.27978) | [GitHub](https://github.com/amap-cvlab/ABot-OCR) | - |
| **Qianfan-OCR** | 2026.03 | end-to-end document intelligence model | [arXiv](https://arxiv.org/abs/2603.13398) | - | [Website](https://cloud.baidu.com/product/wenxinworkshop) |
| **GLM-OCR** | 2026.03 | OCR-specialized document parser | [arXiv](https://arxiv.org/abs/2603.10910) | [GitHub](https://github.com/zai-org/GLM-OCR) | [HF](https://huggingface.co/zai-org/GLM-OCR) |
| **FireRed-OCR** | 2026.03 | OCR-specialized VLM | [arXiv](https://arxiv.org/abs/2603.01840) | [GitHub](https://github.com/FireRedTeam/FireRed-OCR) | - |
| **Logics-Parsing-Omni** | 2026.03 | Alibaba unified parser for heterogeneous documents and videos | [arXiv](https://arxiv.org/abs/2603.09677) | [GitHub](https://github.com/alibaba/Logics-Parsing) | - |
| **MOCR / dots.mocr** | 2026.03 | multimodal OCR parser for text, charts, diagrams, tables, icons, and code-level outputs | [arXiv](https://arxiv.org/abs/2603.13032) | [GitHub](https://github.com/rednote-hilab/dots.mocr) | - |
| **Chandra / Chandra OCR 2** | 2026.03 | full-page HTML / Markdown / JSON OCR model | - | [GitHub](https://github.com/datalab-to/chandra) | [HF](https://huggingface.co/datalab-to/chandra-ocr-2), [Blog](https://www.datalab.to/blog/chandra-2) |
| **MeDocVL** | 2026.02 | medical document understanding and parsing VLM | [arXiv](https://arxiv.org/abs/2602.06402) | - | - |
| **PaddleOCR-VL-1.5** | 2026.01 | compact multi-task document parsing VLM | [arXiv](https://arxiv.org/abs/2601.21957) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | - |
| **DeepSeek-OCR 2** | 2026.01 | causal-flow reordering and document parsing | [arXiv](https://arxiv.org/abs/2601.20552) | [GitHub](https://github.com/deepseek-ai/DeepSeek-OCR) | - |
| **Typhoon OCR / Typhoon OCR v1.5** | 2026.01 | Thai-English document extraction with Markdown/HTML layout reconstruction | [arXiv](https://arxiv.org/abs/2601.14722) | [GitHub](https://github.com/scb-10x/typhoon-ocr) | [HF](https://huggingface.co/typhoon-ai/typhoon-ocr-3b), [Docs](https://docs.opentyphoon.ai/en/ocr/) |
| **GutenOCR** | 2026.01 | grounded OCR front-end fine-tuned from Qwen2.5-VL | [arXiv](https://arxiv.org/abs/2601.14490) | [GitHub](https://github.com/Roots-Automation/GutenOCR) | - |
| **LightOnOCR-2-1B** | 2026.01 | 1B multilingual end-to-end OCR VLM | [arXiv](https://arxiv.org/abs/2601.14251) | - | [HF](https://huggingface.co/lightonai/LightOnOCR-2-1B) |
| **OCRVerse** | 2026.01 | holistic OCR VLM for text-centric and vision-centric OCR | [arXiv](https://arxiv.org/abs/2601.21639) | [GitHub](https://github.com/DocTron-hub/OCRVerse) | - |
| **dots.ocr** | 2025.12 | multilingual document layout parsing VLM | [arXiv](https://arxiv.org/abs/2512.02498) | [GitHub](https://github.com/rednote-hilab/dots.ocr) | [HF](https://huggingface.co/rednote-hilab/dots.ocr) |
| **MonkeyOCR v1.5** | 2025.11 | robust document parsing for complex layouts, tables, and cross-page patterns | [arXiv](https://arxiv.org/abs/2511.10390) | [GitHub](https://github.com/Yuliang-Liu/MonkeyOCR) | - |
| **HunyuanOCR** | 2025.11 | OCR-specialized document VLM | [arXiv](https://arxiv.org/abs/2511.19575) | [GitHub](https://github.com/Tencent-Hunyuan/HunyuanOCR) | [HF](https://huggingface.co/tencent/HunyuanOCR) |
| **olmOCR-2** | 2025.10 | unit-test reward training for document OCR | [arXiv](https://arxiv.org/abs/2510.19817) | [GitHub](https://github.com/allenai/olmocr) | - |
| **DeepSeek-OCR** | 2025.10 | visual token compression for OCR | [arXiv](https://arxiv.org/abs/2510.18234) | [GitHub](https://github.com/deepseek-ai/DeepSeek-OCR) | - |
| **PaddleOCR-VL** | 2025.10 | compact multilingual document parsing VLM | [arXiv](https://arxiv.org/abs/2510.14528) | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) | [Docs](https://paddlepaddle.github.io/PaddleOCR/) |
| **Nanonets-OCR2** | 2025.10 | image-to-Markdown OCR2 family for tables, formulas, flowcharts, handwriting, and checkboxes | - | - | [Website](https://nanonets.com/research/nanonets-ocr-2/), [HF](https://huggingface.co/nanonets/Nanonets-OCR2-1.5B-exp) |
| **POINTS-Reader** | 2025.09 | distillation-free VLM adaptation for document conversion | [arXiv](https://arxiv.org/abs/2509.01215) | [GitHub](https://github.com/Tencent/POINTS-Reader) | [HF](https://huggingface.co/tencent/POINTS-Reader) |
| **Logics-Parsing** | 2025.09 | structured document parsing with logical extraction and LLM framework | [arXiv](https://arxiv.org/abs/2509.19760) | [GitHub](https://github.com/alibaba/Logics-Parsing) | - |
| **Granite-Docling-258M** | 2025.09 | compact DocTags document conversion model | - | - | [HF](https://huggingface.co/ibm-granite/granite-docling-258M), [Docs](https://www.ibm.com/granite/docs/models/docling) |
| **OCRFlux-3B** | 2025.06 | 3B PDF/image-to-Markdown parser with page parsing and cross-page merging | - | [GitHub](https://github.com/chatdoc-com/OCRFlux) | [HF](https://huggingface.co/ChatDOC/OCRFlux-3B) |
| **PP-DocBee2** | 2025.06 | efficient data and stronger document baselines | [arXiv](https://arxiv.org/abs/2506.18023) | [GitHub](https://github.com/PaddlePaddle/PaddleMIX/tree/develop/paddlemix/examples/ppdocbee2) | - |
| **Infinity-Parser** | 2025.06 | layout-aware reinforcement learning for scanned document parsing | [arXiv](https://arxiv.org/abs/2506.03197) | [GitHub](https://github.com/infly-ai/INF-MLLM) | [HF](https://huggingface.co/infly/Infinity-Parser-7B) |
| **MonkeyOCR** | 2025.06 | structure-recognition-relation document parser | [arXiv](https://arxiv.org/abs/2506.05218) | [GitHub](https://github.com/Yuliang-Liu/MonkeyOCR) | - |
| **Nanonets-OCR-s** | 2025.06 | 3B structured Markdown OCR model for LaTeX, tables, signatures, watermarks, and checkboxes | - | [docext](https://github.com/NanoNets/docext) | [Blog](https://nanonets.com/research/nanonets-ocr-s/), [HF](https://huggingface.co/nanonets/Nanonets-OCR-s) |
| **RolmOCR** | 2025.04 | lightweight Qwen2.5-VL-based page text extraction model | - | - | [HF](https://huggingface.co/reducto/RolmOCR) |
| **SmolDocling** | 2025.03 | ultra-compact document conversion VLM | [arXiv](https://arxiv.org/abs/2503.11576) | - | [Hugging Face](https://huggingface.co/ds4sd/SmolDocling-256M-preview) |
| **PP-DocBee** | 2025.03 | multimodal document understanding baseline | [arXiv](https://arxiv.org/abs/2503.04065) | [GitHub](https://github.com/PaddlePaddle/PaddleMIX/tree/develop/paddlemix/examples/ppdocbee) | - |
| **olmOCR** | 2025.02 | open PDF-to-Markdown / page linearization model | [arXiv](https://arxiv.org/abs/2502.18443) | [GitHub](https://github.com/allenai/olmocr) | [HF Bench](https://huggingface.co/datasets/allenai/olmOCR-bench) |

### Emerging Generation and Training Routes

| Model / System | Date | Route | Paper | Code | Docs / Model |
|---|:---:|---|---|---|---|
| **AGAR** | 2026.06 | attention-guided adaptive rendering for visual text comprehension | [arXiv](https://arxiv.org/abs/2606.12898) | - | - |
| **LoMo** | 2026.05 | local modality substitution for cross-modal visual-text carrier alignment | [arXiv](https://arxiv.org/abs/2605.30265) | - | - |
| **FastOCR** | 2026.05 | training-free dynamic visual fixation and KV-cache pruning for efficient VLM document parsing | [arXiv](https://arxiv.org/abs/2605.17447) | - | - |
| **RTPrune** | 2026.05 | reading-twice inspired token pruning for efficient DeepSeek-OCR inference | [arXiv](https://arxiv.org/abs/2605.00392) | - | - |
| **TexOCR** | 2026.04 | SFT and RL with verifiable LaTeX unit-test rewards for page-to-LaTeX OCR | [arXiv](https://arxiv.org/abs/2604.22880) | [GitHub](https://github.com/QDRhhhh/TexOCR) | - |
| **MinerU-Diffusion** | 2026.03 | diffusion-style inverse-rendering OCR | [arXiv](https://arxiv.org/abs/2603.22458) | - | - |
| **Risk-Controlled Generative OCR / GRC** | 2026.03 | selective accept/abstain risk control for frozen VLM OCR | [arXiv](https://arxiv.org/abs/2603.19790) | [GitHub](https://github.com/phare111/GRC) | - |
| **SimpleOCR** | 2026.02 | rendered visualized-question training to force MLLMs to read text visually | [arXiv](https://arxiv.org/abs/2602.22426) | [GitHub](https://github.com/aiming-lab/SimpleOCR) | - |
| **PAR for Faithful OCR / GlitchText** | 2026.01 | training-free mitigation of linguistic-prior OCR hallucination | [OpenReview](https://openreview.net/forum?id=M8zr7QvasK) | [GitHub](https://github.com/Zoeyyao27/PAR-for-Faithful-OCR) | - |
| **Teaching VLMs to Admit Uncertainty in OCR** | 2026.01 | uncertainty-aware OCR with explicit unreliable-span tags | [ICLR](https://openreview.net/forum?id=zyCjizqOxB) | [GitHub](https://github.com/NikoGuan/Uncertainty_OCR) | - |
| **FDRL for Document OCR** | 2026.01 | format-decoupled reinforcement learning | [arXiv](https://arxiv.org/abs/2601.08834), [CVPR](https://openaccess.thecvf.com/content/CVPR2026/html/Zhong_Reading_or_Reasoning_Format_Decoupled_Reinforcement_Learning_for_Document_OCR_CVPR_2026_paper.html) | [GitHub](https://github.com/DocTron-hub/FD-RL) | [HF](https://huggingface.co/DocTron/FD-RL) |
| **DOCR-Inspector** | 2025.12 | fine-grained evaluation and strategic optimization for document OCR parsing | [arXiv](https://arxiv.org/abs/2512.10619) | [GitHub](https://github.com/ZZZZZQT/DOCR-Inspector) | - |
| **DocVAL** | 2025.11 | validated chain-of-thought distillation for grounded document VQA | [arXiv](https://arxiv.org/abs/2511.22521) | [GitHub](https://github.com/ahmad-shirazi/DocVAL) | - |
| **CropVLM** | 2025.11 | RL-trained dynamic zoom wrapper for scene-text and document perception | [arXiv](https://arxiv.org/abs/2511.19820) | [GitHub](https://github.com/miguelscarv/cropvlm) | - |
| **Reading Between the Lines / LRP** | 2025.11 | latent-representation probes for abstaining from VLM-generated OCR errors | [arXiv](https://arxiv.org/abs/2511.19806) | - | - |
| **OCR-Critic / OCR-ERROR** | 2025.10 | critical feedback alignment and OCR error diagnosis for MLLMs | [ACM DL](https://dl.acm.org/doi/10.1145/3746027.3754585) | - | - |
| **HalluText / OCRAssistor** | 2025.09 | OCR hallucination diagnosis and plug-and-play mitigation | [OpenReview](https://openreview.net/forum?id=LRnt6foJ3q) | - | - |
| **ReViCo** | 2025.09 | real-world visual spelling correction for VLMs | [arXiv](https://arxiv.org/abs/2509.17418) | - | - |
| **When Semantics Mislead Vision / TextHalu-Bench** | 2025.06 | training-free mitigation of semantic hallucination in scene-text perception | [arXiv](https://arxiv.org/abs/2506.05551) | [GitHub](https://github.com/shuyansy/MLLM-Semantic-Hallucination) | [HF Dataset](https://huggingface.co/datasets/sy1998/TextHalu-Bench) |
| **Seeing is Believing? / KIE-HVQA** | 2025.06 | OCR hallucination mitigation under visual degradation | [arXiv](https://arxiv.org/abs/2506.20168), [NeurIPS 2025](https://arxiv.org/abs/2506.20168) | - | [HF Dataset](https://huggingface.co/datasets/bytedance-research/KIE-HVQA) |
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
| **LLaVA family** | 2023.04 / 2024.07 / 2024.08 / 2025.09 | visual instruction tuning, interleaved input, and OneVision OCR-rich prompting | [LLaVA](https://arxiv.org/abs/2304.08485), [LLaVA NeurIPS](https://papers.nips.cc/paper_files/paper/2023/hash/6dcf277ea32ce3288914faf369fe6de0-Abstract-Conference.html), [NeXT-Interleave](https://arxiv.org/abs/2407.07895), [OneVision](https://arxiv.org/abs/2408.03326), [OneVision-1.5](https://arxiv.org/abs/2509.23661) | [LLaVA](https://github.com/haotian-liu/LLaVA), [NeXT](https://github.com/LLaVA-VL/LLaVA-NeXT) | - |
| **InternVL family** | 2023.12 / 2024.04 / 2024.12 / 2025.04 / 2025.08 | open general VLM suite with high-resolution OCR and document prompting | [InternVL](https://arxiv.org/abs/2312.14238), [InternVL CVPR](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_InternVL_Scaling_up_Vision_Foundation_Models_and_Aligning_for_Generic_CVPR_2024_paper.html), [1.5](https://arxiv.org/abs/2404.16821), [1.5 SCIS](https://link.springer.com/article/10.1007/s11432-024-4231-5), [2.5](https://arxiv.org/abs/2412.05271), [3](https://arxiv.org/abs/2504.10479), [3.5](https://arxiv.org/abs/2508.18265) | [GitHub](https://github.com/OpenGVLab/InternVL) | [Demo](https://chat.intern-ai.org.cn/) |
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
| **CogVLM / CogVLM2** | 2023.11 / 2024.08 | visual expert VLM baseline and high-resolution successor | [CogVLM](https://arxiv.org/abs/2311.03079), [CogVLM NeurIPS](https://openreview.net/forum?id=6dYBP3BIwx), [CogVLM2](https://arxiv.org/abs/2408.16500) | [CogVLM](https://github.com/THUDM/CogVLM), [CogVLM2](https://github.com/THUDM/CogVLM2) | - |
| **mPLUG-Owl3** | 2024.08 | long image-sequence MLLM for multi-image and video visual-language tasks | [arXiv](https://arxiv.org/abs/2408.04840) | [GitHub](https://github.com/X-PLUG/mPLUG-Owl) | [HF](https://huggingface.co/mPLUG/mPLUG-Owl3-7B-241101) |
| **Idefics2 / Idefics3** | 2024.05 / 2024.08 | open Hugging Face VLM line for OCR, document understanding, and visual reasoning | [Idefics2](https://arxiv.org/abs/2405.02246), [Idefics3](https://arxiv.org/abs/2408.12637) | - | [Idefics2 HF](https://huggingface.co/HuggingFaceM4/idefics2-8b), [Idefics3 HF](https://huggingface.co/HuggingFaceM4/Idefics3-8B-Llama3) |
| **Mantis** | 2024.05 | interleaved multi-image instruction-tuned LMM with strong single-image and multi-image performance | [arXiv](https://arxiv.org/abs/2405.01483), [TMLR](https://openreview.net/forum?id=skLtdUVaJa) | [GitHub](https://github.com/TIGER-AI-Lab/Mantis) | [HF](https://huggingface.co/TIGER-Lab/Mantis-8B-siglip-llama3) |
| **DeepSeek-VL / Yi-VL / Mini-Gemini** | 2024.03 / 2024.03 / 2024.03 | early 2024 open general VLM baselines for text-rich images and high-resolution visual detail | [DeepSeek-VL](https://arxiv.org/abs/2403.05525), [Yi-VL](https://arxiv.org/abs/2403.04652), [Mini-Gemini](https://arxiv.org/abs/2403.18814), [Mini-Gemini TPAMI](https://ieeexplore.ieee.org/document/11269745) | [DeepSeek-VL](https://github.com/deepseek-ai/DeepSeek-VL), [Yi](https://github.com/01-ai/Yi), [MGM](https://github.com/dvlab-research/MGM) | [Yi-VL HF](https://huggingface.co/01-ai/Yi-VL-34B), [MGM Project](https://mini-gemini.github.io/) |
| **BLIP-2 / MiniGPT-4 / InstructBLIP / Florence-2 / VILA** | 2023.01 / 2023.04 / 2023.05 / 2023.11 / 2023.12 | earlier open VLM baselines used as OCR interfaces before modern document-specialized VLMs | [BLIP-2](https://arxiv.org/abs/2301.12597), [BLIP-2 ICML](https://proceedings.mlr.press/v202/li23q.html), [MiniGPT-4](https://arxiv.org/abs/2304.10592), [MiniGPT-4 ICLR](https://openreview.net/forum?id=1tZbq88f27), [InstructBLIP](https://arxiv.org/abs/2305.06500), [InstructBLIP NeurIPS](https://openreview.net/forum?id=vvoWPYqZJA), [Florence-2](https://arxiv.org/abs/2311.06242), [Florence-2 CVPR](https://openaccess.thecvf.com/content/CVPR2024/html/Xiao_Florence-2_Advancing_a_Unified_Representation_for_a_Variety_of_Vision_CVPR_2024_paper.html), [VILA](https://arxiv.org/abs/2312.07533), [VILA CVPR](https://openaccess.thecvf.com/content/CVPR2024/html/Lin_VILA_On_Pre-training_for_Visual_Language_Models_CVPR_2024_paper.html) | [LAVIS](https://github.com/salesforce/LAVIS), [MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4), [VILA](https://github.com/NVlabs/VILA) | [Florence-2 HF](https://huggingface.co/microsoft/Florence-2-large), [VILA Project](https://hanlab.mit.edu/projects/vila) |

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
