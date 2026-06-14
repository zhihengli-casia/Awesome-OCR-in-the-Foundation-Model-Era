# Benchmark and Dataset Inventory

OCR benchmarks should not be read as a single leaderboard. Different benchmark families measure different input units, output contracts, metrics, semantic load, and deployment assumptions. This file keeps a fuller inventory than the front-page README.

## How to Read This Inventory

| Field | Meaning |
|:---:|:---|
| Date | arXiv `YYYY.MM` month when an arXiv version exists; otherwise the available public release, dataset, or challenge date. |
| Type | Benchmark, training corpus, challenge, or evaluation suite. |
| Input | Word crop, line image, scene image, document page, table crop, formula crop, PDF page, multi-page document, or QA pair. |
| Target / Metric | Typical target representation and common metrics. |
| Notes | Why the dataset matters for OCR or document parsing. |

## Cropped Text Recognition and Handwriting

| Date | Name | Type | Input | Target / Metric | Notes | Links |
|:---:|:---|:---:|:---|:---|:---|:---:|
| 2023.09 | VCTR | benchmark | vertical Chinese scene-text crops | recognition accuracy | vertical Chinese text recognition benchmark introduced with orientation-independent CTR | [Paper](https://arxiv.org/abs/2309.01081), [ICCV-related code](https://github.com/FudanVI/FudanOCR/tree/main/image-ids-CTR) |
| 2023.07 | Union14M / Union14M-Benchmark | training corpus / benchmark | word crops | word accuracy / NED | modern harder recognition pool and benchmark | [Paper](https://arxiv.org/abs/2307.08723), [ICCV](https://openaccess.thecvf.com/content/ICCV2023/html/Jiang_Revisiting_Scene_Text_Recognition_A_Data_Perspective_ICCV_2023_paper.html), [GitHub](https://github.com/Mountchicken/Union14M) |
| 2022.08 | LAM | line-level HTR benchmark | Italian historical manuscript line images | CER / WER | line-level benchmark with basic and date-based splits | [Paper](https://arxiv.org/abs/2208.07682), [Project](https://aimagelab.ing.unimore.it/go/lam) |
| 2021.12 | Chinese Text Recognition Benchmark / CTR | benchmark suite | Chinese scene, web, document, and handwriting text crops / lines | accuracy / CR / AR | broad Chinese text recognition benchmark across multiple domains | [Paper](https://arxiv.org/abs/2112.15093), [GitHub](https://github.com/FudanVI/benchmarking-chinese-text-recognition) |
| 2021.11 | Traditional Chinese STR / TC-STR | synthetic corpus / benchmark | traditional-Chinese text images | word / line recognition accuracy | large synthetic corpus plus real validation data for traditional Chinese STR | [Paper](https://arxiv.org/abs/2111.13327), [GitHub](https://github.com/esun-ai/traditional-chinese-text-recogn-dataset) |
| 2020.07 | MTHv2 | historical-document benchmark | Chinese historical document pages with text lines and characters | line transcription / character detection | line-level and character-level annotations for historical Chinese document digitization | [Paper](https://arxiv.org/abs/2007.06890), [GitHub](https://github.com/HCIILAB/MTHv2_Datasets_Release) |
| 2020.05 | TextZoom | low-resolution recognition benchmark | paired LR / HR cropped scene-text images | recognition accuracy / PSNR / SSIM | evaluates low-resolution text recognition and text super-resolution | [Paper](https://arxiv.org/abs/2005.03341), [ECCV](https://doi.org/10.1007/978-3-030-58607-2_38), [GitHub](https://github.com/WenjiaWang0312/TextZoom) |
| 2020 | SCUT-HCCDoc | camera-captured HCTR benchmark | handwritten Chinese document pages / text lines | detection / recognition / spotting; CR / AR | unconstrained camera-captured handwritten Chinese documents | [Paper](https://doi.org/10.1016/j.patcog.2020.107559), [GitHub](https://github.com/HCIILAB/SCUT-HCCDoc_Dataset_Release) |
| 2018 | SCUT-EPT | HCTR benchmark | Chinese examination-paper text lines | CR / AR | 50K handwritten Chinese examination-paper lines with corrections and noise | [Paper](https://doi.org/10.1109/ACCESS.2018.2885398), [GitHub](https://github.com/HCIILAB/SCUT-EPT_Dataset_Release) |
| 2016.01 | COCO-Text Cropped Word Recognition | challenge task | natural-image cropped word instances | cropped-word recognition accuracy | ICDAR 2017 cropped-word recognition task based on COCO-Text | [Paper](https://arxiv.org/abs/1601.07140), [RRC](https://rrc.cvc.uab.es/?ch=5), [Tasks](https://rrc.cvc.uab.es/?ch=5&com=tasks) |
| 2016 | READ 2016 / HTR Competition | line-level HTR challenge | early-modern German handwritten pages / lines | CER / WER | historical handwritten text recognition competition data | [TC11](https://tc11.cvc.uab.es/datasets/HTR%20Competition%202016_1), [Zenodo](https://zenodo.org/records/1164045) |
| 2015 | ICDAR 2015 Recognition | benchmark | incidental cropped words | word accuracy | blurred / oriented scene text crops | [Website](https://rrc.cvc.uab.es/?ch=4) |
| 2015 | HTRtS 2015 / Bentham | historical HTR challenge | Bentham manuscript pages and segmented lines | CER / WER | handwritten text recognition on tranScriptorium / Bentham data | [Zenodo](https://zenodo.org/records/248733) |
| 2014 | MJSynth / Synth90k | synthetic training data | rendered word crops | training corpus | classic synthetic data for CRNN-era recognition | [Website](https://www.robots.ox.ac.uk/~vgg/data/text/) |
| 2013 | ICDAR 2013 Recognition | benchmark | focused scene word crops | word accuracy | clean focused text recognition | [Website](https://rrc.cvc.uab.es/?ch=2) |
| 2013 | ICDAR 2013 Chinese Handwriting Recognition Competition | handwriting challenge | online / offline Chinese characters and handwritten text | correct rate | competition evaluation built around CASIA-HWDB / OLHWDB | [Summary](https://scholar.xjtlu.edu.cn/en/publications/icdar-2013-chinese-handwriting-recognition-competition/) |
| 2013 | CVL | handwriting benchmark | German / English handwritten words and lines | CER / WER | handwriting recognition and writer-related protocols | [Zenodo](https://zenodo.org/records/1492267) |
| 2012.06 | CASIA-HWDB1.x / OLHWDB1.x | Chinese handwriting corpus | isolated Chinese character images and online trajectories | character recognition accuracy | foundational CASIA online/offline handwritten Chinese character benchmark | [Paper](https://doi.org/10.1016/j.patcog.2012.06.021), [CASIA](https://nlpr.ia.ac.cn/databases/handwriting/Home.html) |
| 2012 | KHATT | Arabic HTR benchmark | handwritten Arabic forms / paragraphs / lines | CER / WER / word accuracy | Arabic offline handwritten text recognition benchmark | [Paper](https://pure.kfupm.edu.sa/en/publications/khatt-arabic-offline-handwritten-text-database/) |
| 2012 | Washington Database | historical handwriting benchmark | George Washington manuscript words / lines | CER / WER / word spotting metrics | small but classic historical handwritten-word and line benchmark | [Website](https://fki.tic.heia-fr.ch/databases/washington-database) |
| 2011 | IIIT5K | benchmark | cropped word images | word accuracy | classic STR benchmark | [Website](https://cvit.iiit.ac.in/research/projects/cvit-projects/the-iiit-5k-word-dataset) |
| 2011 | SVT | benchmark | street-view word crops | word accuracy | Google Street View text recognition | [Website](http://www.iapr-tc11.org/mediawiki/index.php/The_Street_View_Text_Dataset) |
| 2011 | SVTP | benchmark | perspective word crops | word accuracy | perspective-distorted cropped words | [Website](http://www.iapr-tc11.org/mediawiki/index.php/SVTP_Dataset) |
| 2011 | CUTE80 | benchmark | curved word crops | word accuracy | curved cropped text | [Website](http://cs-chan.com/downloads_CUTE80_dataset.html) |
| 2011 | CASIA-HWDB2.0-2.2 | Chinese handwriting corpus | handwritten Chinese text pages / lines | offline HCTR; CR / AR | large Chinese handwritten text corpus paired with CASIA online handwriting data | [Paper](https://nlpr.ia.ac.cn/databases/download/ICDAR2011-CASIA%20databases.pdf) |
| 2011 | RIMES / RIMES-2011-line | handwriting benchmark | French handwritten lines / pages | CER / WER | handwriting recognition and document analysis | [HF](https://huggingface.co/datasets/Teklia/RIMES-2011-line) |
| 2003 | ICDAR 2003 Recognition | benchmark | robust-reading cropped words / characters | word / character recognition | early robust-reading recognition benchmark | [Website](http://www.iapr-tc11.org/mediawiki/index.php/ICDAR_2003_Robust_Reading_Competitions) |
| 2002 | IFN/ENIT | Arabic handwriting benchmark | handwritten Arabic word images | word recognition accuracy | widely used handwritten Tunisian town-name benchmark | [Reference](https://www.semanticscholar.org/paper/IFN-ENIT%3A-database-of-handwritten-arabic-words-Pechwitz-Maddouri/732c94369298f0d3df48ed4035703e56aaf39892) |
| 2002 | IAM | handwriting benchmark | handwritten words / lines | CER / WER | classic offline handwriting recognition benchmark | [Website](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database) |
| 1999 | MNIST | controlled recognition benchmark | digit images | accuracy | controlled character recognition baseline | [Website](http://yann.lecun.com/exdb/mnist/) |
| 1995 | NIST SD19 | handwriting dataset | handwritten digits / characters | accuracy | large handwritten character corpus | [Website](https://www.nist.gov/srd/nist-special-database-19) |
| 1994 | CEDAR | handwriting dataset | words / addresses | recognition metrics | classic postal/address OCR data | [Website](https://cedar.buffalo.edu/Databases/) |
| 1987 | USPS | controlled recognition benchmark | digit images | accuracy | postal digit recognition baseline | [Website](https://www.kaggle.com/datasets/bistaumanga/usps-dataset) |

## Scene Text Detection, Recognition, and Spotting

| Date | Name | Type | Input | Target / Metric | Notes | Links |
|:---:|:---|:---:|:---|:---|:---|:---:|
| 2024.01 | GoMatching / ArTVideo | video text spotting benchmark | arbitrary-shaped video text with curved instances | detection / tracking / spotting | ArTVideo benchmark introduced with the NeurIPS 2024 GoMatching paper; GoMatching++ is the 2025.05 extension | [Paper](https://arxiv.org/abs/2401.07080), [NeurIPS](https://papers.nips.cc/paper_files/paper/2024/hash/2d66a70c770de7835678f1c1e65fe5e1-Abstract-Conference.html), [GoMatching++](https://arxiv.org/abs/2505.22228), [GitHub](https://github.com/Hxyz-123/GoMatching) |
| 2023.12 | DSText V2 | video text reading benchmark | dense and small text in videos | detection / tracking / end-to-end spotting | dense and small video-text benchmark built on the ICDAR 2023 DSText competition | [Paper](https://arxiv.org/abs/2312.01938), [RRC](https://rrc.cvc.uab.es/?ch=22) |
| 2022.03 | HierText | benchmark | natural images | word / line / paragraph hierarchy | dense hierarchical text detection and recognition | [Paper](https://arxiv.org/abs/2203.15143), [GitHub](https://github.com/google-research-datasets/hiertext) |
| 2022 | HUST-ASTD / HUST-ART | Amharic scene-text benchmark | real and synthetic Amharic scene images | detection / recognition | Amharic detection and recognition datasets for low-resource scene text | [Project](https://dk-liang.github.io/HUST-ASTD/) |
| 2021.12 | BOVText | video text spotting benchmark | bilingual open-world videos | detection / tracking / spotting | large-scale bilingual video text benchmark with 2K+ videos and open scenarios | [Paper](https://arxiv.org/abs/2112.04888), [GitHub](https://github.com/weijiawu/BOVText-Benchmark) |
| 2021 | TextOCR | benchmark | natural images | text boxes and transcriptions | dense text in everyday images | [Website](https://textvqa.org/textocr/) |
| 2021 | VinText | Vietnamese scene-text benchmark | urban Vietnamese scene images | recognition / spotting | benchmark used for Vietnamese scene text recognition and spotting | [CVPR](https://openaccess.thecvf.com/content/CVPR2021/papers/Nguyen_Dictionary-Guided_Scene_Text_Recognition_CVPR_2021_paper.pdf), [GitHub](https://github.com/VinAIResearch/dict-guided) |
| 2020.05 | RoadText-1K | driving-video text benchmark | dashcam video clips | detection / recognition / tracking | driving-video benchmark with boxes and transcripts in every frame | [Paper](https://arxiv.org/abs/2005.09496), [RRC](https://rrc.cvc.uab.es/?ch=25) |
| 2019.07 | RRC-MLT-2019 | multilingual benchmark | 10-language scene images | detection / script classification / spotting | multi-lingual robust-reading benchmark with end-to-end task | [Paper](https://arxiv.org/abs/1907.00945), [RRC](https://rrc.cvc.uab.es/?ch=15) |
| 2019 | ReCTS | benchmark | Chinese signboards | detection / recognition / end-to-end | Chinese scene text reading | [Website](https://rrc.cvc.uab.es/?ch=12) |
| 2019 | LSVT | benchmark | large-scale street-view Chinese text | detection / recognition / spotting | large-scale Chinese scene text | [Website](https://rrc.cvc.uab.es/?ch=16) |
| 2019 | ArT | benchmark | arbitrary-shape scene text | polygon detection / spotting | arbitrary-shape text benchmark | [Website](https://rrc.cvc.uab.es/?ch=14) |
| 2018.03 | CTW / Chinese Text in the Wild | Chinese scene-text benchmark | Chinese street-view images | character boxes / detection / recognition | 30K+ street-view images with character-level Chinese annotations | [Paper](https://arxiv.org/abs/1803.00085), [Project](https://ctwdataset.github.io/) |
| 2018 | MTWI-2018 | web-image robust-reading benchmark | Chinese / English multi-type web images | detection / recognition / end-to-end | ICPR 2018 robust-reading contest for multi-type web images | [Docs](https://github.com/mindspore-lab/mindocr/blob/main/docs/en/datasets/mtwi2018.md) |
| 2017.12 | CTW1500 | benchmark | curved text-line images | polygon F1 | curved long text lines | [Paper](https://arxiv.org/abs/1712.02170), [GitHub](https://github.com/Yuliang-Liu/Curve-Text-Detector) |
| 2017.10 | Total-Text | benchmark | curved / horizontal scene text | polygon detection / spotting | curved text benchmark | [Paper](https://arxiv.org/abs/1710.10400), [GitHub](https://github.com/cs-chan/Total-Text-Dataset) |
| 2017.08 | RCTW-17 | Chinese scene-text benchmark | natural images with Chinese text | localization / end-to-end recognition | early large-scale Chinese text reading challenge | [Paper](https://arxiv.org/abs/1708.09585) |
| 2017 | ICDAR 2017 MLT | benchmark | multilingual scene images | detection / recognition | multilingual robust reading | [Website](https://rrc.cvc.uab.es/?ch=8) |
| 2017 | Uber-Text | large-scale street-level OCR dataset | streetside images | text polygons / transcriptions | street-level dataset with 110K+ images and line-level text annotations | [Website](https://s3-us-west-2.amazonaws.com/uber-common-public/ubertext/index.html) |
| 2016.04 | SynthText | synthetic training data | text pasted into natural images | detection / recognition training | classic scene-text synthetic data | [Paper](https://arxiv.org/abs/1604.06646), [Website](https://www.robots.ox.ac.uk/~vgg/data/scenetext/) |
| 2016.01 | COCO-Text | benchmark | MS-COCO images with text | detection / recognition | natural image text benchmark with legibility, script, and transcription annotations | [Paper](https://arxiv.org/abs/1601.07140), [Website](https://bgshih.github.io/cocotext/) |
| 2015 | ICDAR 2015 Incidental Text | benchmark | camera-captured scene images | detection / spotting Hmean | incidental blurred / oriented text | [Website](https://rrc.cvc.uab.es/?ch=4) |
| 2013 | ICDAR 2013 Robust Reading | benchmark | focused scene images | detection / recognition | focused scene text baseline | [Website](https://rrc.cvc.uab.es/?ch=2) |
| 2012 | MSRA-TD500 | benchmark | scene images with long text lines | text-line detection F1 | multi-oriented long text lines | [Website](http://www.iapr-tc11.org/mediawiki/index.php/MSRA_Text_Detection_500_Database_%28MSRA-TD500%29) |
| 2011 | ICDAR 2011 Robust Reading | benchmark | scene images | detection / recognition | early scene text benchmark | [Website](https://rrc.cvc.uab.es/?ch=1) |
| 2003 | ICDAR 2003 Robust Reading | benchmark | scene images | detection / recognition | early robust reading task | [Website](https://rrc.cvc.uab.es/) |

## Document Layout, Forms, KIE, and Receipts

| Date | Name | Type | Input | Target / Metric | Notes | Links |
|:---:|:---|:---:|:---|:---|:---|:---:|
| 2024.06 | DocStructBench | benchmark | document pages | fine-grained structure detection | fine-grained document structure | [Paper](https://arxiv.org/abs/2406.10021) |
| 2022.06 | DocLayNet | benchmark | diverse document pages | layout mAP | 11-class layout detection across document types | [Paper](https://arxiv.org/abs/2206.01062), [GitHub](https://github.com/DS4SD/DocLayNet), [HF](https://huggingface.co/datasets/ds4sd/DocLayNet) |
| 2021.04 | XFUND | multilingual form benchmark | form pages | entity / relation F1 | multilingual form understanding | [Paper](https://arxiv.org/abs/2104.08836), [ACL](https://aclanthology.org/2022.findings-acl.253/), [GitHub](https://github.com/doc-analysis/XFUND) |
| 2021.05 | Kleister-NDA / Kleister-Charity | KIE benchmark | long business documents | key-value extraction F1 | long document key information extraction | [Paper](https://arxiv.org/abs/2105.05796) |
| 2020.06 | DocBank | layout / token benchmark | PDF pages | token-level structure labels | large-scale token-level document layout labels | [Paper](https://arxiv.org/abs/2006.01038), [GitHub](https://github.com/doc-analysis/DocBank) |
| 2019.08 | PubLayNet | layout benchmark | scientific document pages | layout mAP | large document layout benchmark | [Paper](https://arxiv.org/abs/1908.07836), [ICDAR](https://csdl.computer.org/csdl/proceedings-article/icdar/2019/301400b015/1h81wfs4MoM), [GitHub](https://github.com/ibm-aur-nlp/PubLayNet) |
| 2019 | SROIE | receipt benchmark | receipt images | OCR + field extraction F1 | receipt information extraction challenge | [Website](https://rrc.cvc.uab.es/?ch=13) |
| 2019 | CORD | receipt KIE benchmark | receipt images | semantic field extraction F1 | receipt understanding | [GitHub](https://github.com/clovaai/cord) |
| 2019 | FUNSD | form understanding benchmark | scanned forms | entity / relation F1 | noisy form understanding | [Website](https://guillaumejaume.github.io/FUNSD/) |
| 2013 | PRImA Layout | layout benchmark | scanned document pages | layout segmentation | early document layout analysis | [Website](https://www.primaresearch.org/dataset/) |

## Tables, Formulas, and Structured Objects

| Date | Name | Type | Input | Target / Metric | Notes | Links |
|:---:|:---|:---:|:---|:---|:---|:---:|
| 2025.08 | Tex80M / TexTeller data | formula training corpus | synthetic and handwritten formula images | LaTeX recognition training | large-scale HMER training data introduced with TexTeller | [Paper](https://arxiv.org/abs/2508.09220), [GitHub](https://github.com/OleehyO/TexTeller) |
| 2024.04 | UniMER-1M | formula dataset | formula images | LaTeX edit distance | large-scale formula recognition data | [Paper](https://arxiv.org/abs/2404.15254), [GitHub](https://github.com/opendatalab/UniMERNet) |
| 2024.04 | MathWriting | handwritten formula benchmark | online/offline handwritten formulas | CER / expression recognition | 230K human-written and 400K synthetic HME samples | [Paper](https://arxiv.org/abs/2404.10690), [KDD](https://doi.org/10.1145/3711896.3737436) |
| 2022.03 | HME100K | formula benchmark | handwritten formula images | LaTeX / expression rate | handwritten mathematical expression recognition | [Paper](https://arxiv.org/abs/2203.01601), [CVPR](https://openaccess.thecvf.com/content/CVPR2022/html/Yuan_Syntax-Aware_Network_for_Handwritten_Mathematical_Expression_Recognition_CVPR_2022_paper.html), [Dataset](https://ai.100tal.com/dataset) |
| 2021.10 | PubTables-1M | table benchmark | PDF tables | AP / GriTS / cell structure | large table detection and structure benchmark | [Paper](https://arxiv.org/abs/2110.00061), [CVPR](https://openaccess.thecvf.com/content/CVPR2022/html/Smock_PubTables-1M_Towards_Comprehensive_Table_Extraction_From_Unstructured_Documents_CVPR_2022_paper.html), [GitHub](https://github.com/microsoft/table-transformer) |
| 2021.09 | WTW | table benchmark | wild tables | table detection / structure | natural-scene and document tables | [Paper](https://arxiv.org/abs/2109.02199), [GitHub](https://github.com/wangwen-whu/WTW-Dataset) |
| 2020 | FinTabNet | table benchmark | financial report tables | TEDS / structure | complex financial tables | [Website](https://developer.ibm.com/exchanges/data/all/fintabnet/) |
| 2019.11 | PubTabNet | table benchmark | table images | HTML / TEDS | table image-to-HTML benchmark | [Paper](https://arxiv.org/abs/1911.10683), [GitHub](https://github.com/ibm-aur-nlp/PubTabNet), [EDD](https://github.com/ibm-aur-nlp/EDD) |
| 2019.08 | SciTSR | table benchmark | scientific tables | cell structure F1 | scientific table structure recognition | [Paper](https://arxiv.org/abs/1908.04729), [GitHub](https://github.com/Academic-Hammer/SciTSR) |
| 2019.03 | TableBank | table benchmark | Word / LaTeX document tables | detection / structure | large table dataset from office and LaTeX documents | [Paper](https://arxiv.org/abs/1903.01949), [LREC](https://aclanthology.org/2020.lrec-1.236/), [GitHub](https://github.com/doc-analysis/TableBank) |
| 2016.09 | Im2LaTeX-100K | formula dataset | rendered formulas | LaTeX edit distance | image-to-markup formula generation | [Paper](https://arxiv.org/abs/1609.04938), [ICML](https://proceedings.mlr.press/v70/deng17a.html), [GitHub](https://github.com/harvardnlp/im2markup) |
| 2014- | CROHME | formula competition | handwritten math expressions | expression recognition rate | handwriting math expression recognition | [Website](https://www.isical.ac.in/~crohme/) |

## Document QA, Chart QA, and OCR-Dependent Understanding

| Date | Name | Type | Input | Target / Metric | Notes | Links |
|:---:|:---|:---:|:---|:---|:---|:---:|
| 2025.02 | EgoTextVQA | egocentric scene-text video QA | ego-view videos + scene-text-aware questions | answer accuracy | egocentric video QA benchmark requiring scene-text reading and spatio-temporal reasoning; CVPR 2025 | [Paper](https://arxiv.org/abs/2502.07411), [CVPR](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_EgoTextVQA_Towards_Egocentric_Scene-Text_Aware_Video_Question_Answering_CVPR_2025_paper.html), [GitHub](https://github.com/zhousheng97/EgoTextVQA) |
| 2024.07 | MMLongBench-Doc | benchmark | long documents + questions | answer accuracy / LLM judging | long document VQA / reasoning | [Paper](https://arxiv.org/abs/2407.01523), [NeurIPS D&B](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ae0e43289bffea0c1fa34633fc608e92-Abstract-Datasets_and_Benchmarks_Track.html) |
| 2023.05 | DUDE | document QA benchmark | diverse documents + questions | ANLS / accuracy | diverse document understanding | [Paper](https://arxiv.org/abs/2305.08455) |
| 2023 | MP-DocVQA | multi-page document QA | multi-page documents + questions | ANLS | multi-page document question answering | [Website](https://rrc.cvc.uab.es/?ch=17) |
| 2022.03 | ChartQA | chart QA benchmark | chart images + questions | relaxed accuracy | visual and logical chart reasoning | [Paper](https://arxiv.org/abs/2203.10244), [GitHub](https://github.com/vis-nlp/ChartQA) |
| 2022 | ViteVQA / M4-ViteVQA | video text VQA benchmark | videos + questions over visual and textual evidence | answer accuracy / ANLS | video-text VQA benchmark requiring spatio-temporal reasoning over OCR tokens and visual content | [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2022/hash/e726197ffd401df4013cd9f81007b5cf-Abstract-Datasets_and_Benchmarks.html), [OpenReview](https://openreview.net/forum?id=yPZ7w29qSNK), [GitHub](https://github.com/bytedance/VTVQA) |
| 2021.04 | InfographicVQA | infographic QA benchmark | infographics + questions | ANLS / accuracy | infographic document understanding | [Paper](https://arxiv.org/abs/2104.12756), [Website](https://www.docvqa.org/datasets/infographicvqa) |
| 2020.07 | DocVQA | document QA benchmark | document image + question | ANLS | classic document visual question answering | [Paper](https://arxiv.org/abs/2007.00398), [Website](https://www.docvqa.org/) |
| 2019.04 | TextVQA | text-rich VQA benchmark | natural images + questions | VQA accuracy | natural-image QA requiring OCR | [Paper](https://arxiv.org/abs/1904.08920), [CVPR](https://openaccess.thecvf.com/content_CVPR_2019/html/Singh_Towards_VQA_Models_That_Can_Read_CVPR_2019_paper.html), [Website](https://textvqa.org/) |
| 2019 | ST-VQA | scene-text VQA benchmark | text-rich images + questions | ANLS | scene text visual question answering | [Website](https://rrc.cvc.uab.es/?ch=11) |
| 2017.10 | FigureQA | chart / figure QA | synthetic figures + questions | accuracy | synthetic chart and figure reasoning | [Paper](https://arxiv.org/abs/1710.07300), [ICLR Workshops](https://dblp.org/rec/conf/iclr/KahouMAKTB18) |
| 2019.09 | PlotQA | plot QA benchmark | chart images + questions | accuracy | chart reasoning benchmark | [Paper](https://arxiv.org/abs/1909.00997) |

## Page-Level Parsing and VLM-OCR Evaluation

| Date | Name | Type | Input | Target / Metric | Notes | Links |
|:---:|:---|:---:|:---|:---|:---|:---:|
| 2026.06 | RealDocBench | real-world parsing benchmark | degraded real documents | parsing robustness | real degraded document parsing | [Paper](https://arxiv.org/abs/2606.07401) |
| 2026.05 | MPDocBench-Parse | multi-page parsing benchmark | multi-page documents | structured output / consistency | multi-page parsing stress test | [Paper](https://arxiv.org/abs/2605.22100) |
| 2026.05 | PureDocBench | page parsing benchmark | page images | structure / layout parsing | structural parsing without semantic shortcuts | [Paper](https://arxiv.org/abs/2605.07492) |
| 2026.05 | CC-OCR v2 | VLM-OCR benchmark | multi-domain text-rich images | OCR capability and reasoning scores | expanded CC-OCR evaluation | [Paper](https://arxiv.org/abs/2605.03903) |
| 2026.03 | Real5-OmniDocBench | real-world parsing benchmark | physically reconstructed OmniDocBench pages | parse score / degradation drop | five physical reconstruction conditions for robust document parsing | [Paper](https://arxiv.org/abs/2603.04205), [HF](https://huggingface.co/datasets/PaddlePaddle/Real5-OmniDocBench) |
| 2026.03 | MDPBench | multilingual parsing benchmark | digital and photographed multilingual documents | per-language parsing scores / robustness drop | 3,400 images across 17 languages and varied photographic conditions | [Paper](https://arxiv.org/abs/2603.28130), [GitHub](https://github.com/Yuliang-Liu/MultimodalOCR), [HF](https://huggingface.co/datasets/Delores-Lin/MDPBench) |
| 2026.01 | GlitchText | faithful OCR probing dataset | high-familiarity text with visual glitches | CER / identification / correction rates | probes linguistic-prior hallucination in OCR | [Paper](https://openreview.net/forum?id=M8zr7QvasK), [GitHub](https://github.com/Zoeyyao27/PAR-for-Faithful-OCR) |
| 2026.01 | Blur-OCR | uncertainty-aware OCR benchmark | lossy document images | transcription accuracy / uncertainty-tag F1 | benchmark for explicit uncertainty marking in degraded OCR | [Paper](https://openreview.net/forum?id=zyCjizqOxB), [ICLR](https://openreview.net/forum?id=zyCjizqOxB), [GitHub](https://github.com/NikoGuan/Uncertainty_OCR) |
| 2025.11 | DocPTBench | photographed document parsing and translation | photographed documents | parsing and translation robustness | perspective / lighting / capture degradation | [Paper](https://arxiv.org/abs/2511.18434), [GitHub](https://github.com/Topdu/DocPTBench) |
| 2025.10 | OCR-ERROR | OCR error diagnosis benchmark | OCR outputs and images | error detection / error-type classification | 2,400-sample benchmark for detecting and categorizing OCR errors | [Paper](https://dl.acm.org/doi/10.1145/3746027.3754585) |
| 2025.09 | HalluText | OCR hallucination benchmark | OCR-centric image-question-answer triples | accuracy across hallucination subclasses | fine-grained OCR hallucination benchmark with nine subclasses | [Paper](https://openreview.net/forum?id=LRnt6foJ3q) |
| 2025.09 | ReViCo | visual spelling correction benchmark | real-world Chinese and English text images | image-level and token-level correction scores | evaluates visually grounded spelling-error detection and correction | [Paper](https://arxiv.org/abs/2509.17418) |
| 2025.06 | TextHalu-Bench | scene-text hallucination benchmark | semantic / non-semantic scene-text QA | hallucination / QA accuracy | benchmark for semantic hallucination in scene-text spotting and understanding | [Paper](https://arxiv.org/abs/2506.05551), [NeurIPS](https://papers.neurips.cc/paper_files/paper/2025/hash/63b96ace3e28465aff61918e77de2a00-Abstract-Conference.html), [OpenReview](https://openreview.net/forum?id=BbWrp6O8Lm), [GitHub](https://github.com/shuyansy/MLLM-Semantic-Hallucination), [HF](https://huggingface.co/datasets/sy1998/TextHalu-Bench) |
| 2025.06 | KIE-HVQA | OCR hallucination benchmark | degraded identity cards and invoices | hallucination-free accuracy / uncertainty handling | degraded-document benchmark for OCR hallucination in KIE/VQA | [Paper](https://arxiv.org/abs/2506.20168), [NeurIPS](https://openreview.net/forum?id=bjoHB7IN6b), [HF](https://huggingface.co/datasets/bytedance-research/KIE-HVQA) |
| 2025.05 | MME-VideoOCR | video OCR benchmark for MLLMs | videos + OCR-centric QA across 25 tasks | accuracy | video OCR benchmark covering text recognition, grounding, cross-frame understanding, and text-based reasoning | [Paper](https://arxiv.org/abs/2505.21333), [NeurIPS D&B](https://openreview.net/forum?id=hW7Bpu6Kbn), [Project](https://mme-videoocr.github.io/), [GitHub](https://github.com/FrankYang-17/MME-VideoOCR), [HF](https://huggingface.co/datasets/DogNeverSleep/MME-VideoOCR_Dataset) |
| 2025.05 | OCR-Reasoning | reasoning-heavy OCR benchmark | text-rich images + questions | OCR reasoning accuracy | OCR-centered multimodal reasoning benchmark | [Paper](https://arxiv.org/abs/2505.17163), [ICLR](https://openreview.net/forum?id=aH7eyx64pC), [GitHub](https://github.com/SCUT-DLVCLab/OCR-Reasoning), [Project](https://ocr-reasoning.github.io/) |
| 2025.05 | Reasoning-OCR | reasoning-oriented OCR benchmark | text-rich images + reasoning tasks | answer accuracy | OCR reasoning evaluation | [Paper](https://arxiv.org/abs/2505.12766), [GitHub](https://github.com/Hxyz-123/ReasoningOCR) |
| 2025.04 | OCR-Quality | OCR quality assessment dataset | OCR candidates with human quality labels | quality verification / agreement calibration | human-labeled dataset for OCR correctness and calibration | [Paper](https://arxiv.org/abs/2504.11101), [CVPR](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Consensus_Entropy_Harnessing_Multi-VLM_Agreement_for_Self-Verifying_and_Self-Improving_OCR_CVPR_2026_paper.html), [GitHub](https://github.com/Aslan-yulong/consensus-entropy), [HF](https://huggingface.co/datasets/Aslan-mingye/OCR-Quality) |
| 2025.02 | KITAB-Bench | multilingual OCR / document benchmark | Arabic text-rich documents | OCR and document understanding scores | Arabic-centric OCR and document understanding | [Paper](https://arxiv.org/abs/2502.14949), [ACL](https://aclanthology.org/2025.findings-acl.1135/), [GitHub](https://github.com/mbzuai-oryx/KITAB-Bench) |
| 2025.02 | olmOCR-Bench | document OCR benchmark | PDF pages | OCR / Markdown quality via unit tests | document OCR evaluation accompanying olmOCR | [Paper](https://arxiv.org/abs/2502.18443), [GitHub](https://github.com/allenai/olmocr), [HF](https://huggingface.co/datasets/allenai/olmOCR-bench) |
| 2025.01 | OCRBench v2 | VLM-OCR benchmark | mixed text-rich images | scenario scores / total score | expanded VLM OCR capability evaluation | [Paper](https://arxiv.org/abs/2501.00321), [NeurIPS D&B](https://openreview.net/forum?id=Vb6i3Dp24N), [Project](https://99franklin.github.io/ocrbench_v2/), [GitHub](https://github.com/Yuliang-Liu/MultimodalOCR), [HF](https://huggingface.co/datasets/ling99/OCRBench_v2) |
| 2024.12 | OmniDocBench | page-level parsing benchmark | PDF / page images | text / layout / table / formula parse scores | widely used full-page parsing benchmark | [Paper](https://arxiv.org/abs/2412.07626), [CVPR](https://openaccess.thecvf.com/content/CVPR2025/html/Ouyang_OmniDocBench_Benchmarking_Diverse_PDF_Document_Parsing_with_Comprehensive_Annotations_CVPR_2025_paper.html), [GitHub](https://github.com/opendatalab/OmniDocBench) |
| 2024.12 | CC-OCR | VLM-OCR benchmark | cross-domain text-rich images | OCR literacy scores | Chinese-centric and cross-domain OCR evaluation | [Paper](https://arxiv.org/abs/2412.02210), [ICCV](https://openaccess.thecvf.com/content/ICCV2025/html/Yang_CC-OCR_A_Comprehensive_and_Challenging_OCR_Benchmark_for_Evaluating_Large_ICCV_2025_paper.html) |
| 2023.05 | OCRBench | VLM-OCR benchmark | mixed text-rich images | task accuracy / total score | early OCR-oriented MLLM benchmark | [Paper](https://arxiv.org/abs/2305.07895), [SCIS](https://link.springer.com/article/10.1007/s11432-024-4235-6), [GitHub](https://github.com/Yuliang-Liu/MultimodalOCR) |

## Training Corpora and Synthetic Data

| Date | Name | Type | Input | Target / Metric | Notes | Links |
|:---:|:---|:---:|:---|:---|:---|:---:|
| 2023.07 | Union14M | training corpus | word crops | recognition training | unified large-scale STR training data | [Paper](https://arxiv.org/abs/2307.08723), [ICCV](https://openaccess.thecvf.com/content/ICCV2023/html/Jiang_Revisiting_Scene_Text_Recognition_A_Data_Perspective_ICCV_2023_paper.html), [GitHub](https://github.com/Mountchicken/Union14M) |
| 2022 | SynthDoG | synthetic document generator | document pages | document images / labels | synthetic data for Donut-style document understanding | [GitHub](https://github.com/clovaai/donut) |
| 2021 | SynthTIGER | synthetic text image generator | cropped and scene text | detection / recognition training | configurable text-image generation | [GitHub](https://github.com/clovaai/synthtiger) |
| 2016.04 | SynthText | synthetic scene text | natural images with rendered text | detection / recognition labels | detection and spotting pretraining | [Paper](https://arxiv.org/abs/1604.06646), [Website](https://www.robots.ox.ac.uk/~vgg/data/scenetext/) |
| 2014 | MJSynth / Synth90k | synthetic word crops | rendered words | text labels | recognition pretraining | [Website](https://www.robots.ox.ac.uk/~vgg/data/text/) |

## Adjacent but Useful Evaluation Resources

| Date | Name | Type | Input | Target / Metric | Notes | Links |
|:---:|:---|:---:|:---|:---|:---|:---:|
| 2024.07 | Needle-in-a-Document / long-document QA suites | stress tests | long PDFs / docs + questions | answer accuracy | useful for downstream document intelligence, not OCR itself | [MMLongBench-Doc](https://arxiv.org/abs/2407.01523), [NeurIPS D&B](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ae0e43289bffea0c1fa34633fc608e92-Abstract-Datasets_and_Benchmarks_Track.html) |
| 2023.11 | MMMU / multimodal exam benchmarks | VLM benchmark | images + questions | accuracy | may contain text-rich questions but mixes OCR with reasoning | [Paper](https://arxiv.org/abs/2311.16502) |
| 2023.10 | MathVista | VLM benchmark | math diagrams + questions | accuracy | formula/chart-heavy reasoning, not a pure OCR benchmark | [Paper](https://arxiv.org/abs/2310.02255) |
