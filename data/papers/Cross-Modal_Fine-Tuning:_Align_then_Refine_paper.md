Faculty: Graham Neubig
Title: Cross-Modal Fine-Tuning: Align then Refine
Abstract: Fine-tuning large-scale pretrained models has led to tremendous progress in well-studied modalities such as vision and NLP. However, similar gains have not been observed in many other modalities due to a lack of relevant pretrained models. In this work, we propose ORCA, a general cross-modal fine-tuning framework that extends the applicability of a single large-scale pretrained model to diverse modalities. ORCA adapts to a target task via an align-then-refine workflow: given the target input, ORCA first learns an embedding network that aligns the embedded feature distribution with the pretraining modality. The pretrained model is then fine-tuned on the embedded data to exploit the knowledge shared across modalities. Through extensive experiments, we show that ORCA obtains state-of-the-art results on 3 benchmarks containing over 60 datasets from 12 modalities, outperforming a wide range of hand-designed, AutoML, general-purpose, and task-specific methods. We highlight the importance of data alignment via a series of ablation studies and demonstrate ORCA's utility in data-limited regimes.
Year: 2023
Authors: Junhong Shen, Liam Li, L. Dery, Corey Staten, M. Khodak, Graham Neubig, Ameet Talwalkar
Publication ID: fc0a208c-acb7-47dc-a0d4-af8190e21d29
Publication Name: International Conference on Machine Learning
Publication Type: conference
Publication Alternate Names: ICML, Int Conf Mach Learn
Publication Url: https://icml.cc/