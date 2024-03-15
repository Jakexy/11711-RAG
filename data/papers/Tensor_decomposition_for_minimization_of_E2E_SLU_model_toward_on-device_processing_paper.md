Faculty: Shinji Watanabe
Title: Tensor decomposition for minimization of E2E SLU model toward on-device processing
Abstract: Spoken Language Understanding (SLU) is a critical speech recognition application and is often deployed on edge devices. Consequently, on-device processing plays a significant role in the practical implementation of SLU. This paper focuses on the end-to-end (E2E) SLU model due to its small latency property, unlike a cascade system, and aims to minimize the computational cost. We reduce the model size by applying tensor decomposition to the Conformer and E-Branchformer architectures used in our E2E SLU models. We propose to apply singular value decomposition to linear layers and the Tucker decomposition to convolution layers, respectively. We also compare COMP/PARFAC decomposition and Tensor-Train decomposition to the Tucker decomposition. Since the E2E model is represented by a single neural network, our tensor decomposition can flexibly control the number of parameters without changing feature dimensions. On the STOP dataset, we achieved 70.9% exact match accuracy under the tight constraint of only 15 million parameters.
Year: 2023
Authors: Yosuke Kashiwagi, Siddhant Arora, Hayato Futami, Jessica Huynh, Shih-Lun Wu, Yifan Peng, Brian Yan, E. Tsunoo, Shinji Watanabe
Publication ID: af90489e-312f-4514-bea2-bcb399cb8ece
Publication Name: Interspeech
Publication Type: conference
Publication Alternate Names: Conf Int Speech Commun Assoc, INTERSPEECH, Conference of the International Speech Communication Association
Publication Issn: 2308-457X
Publication Url: https://www.isca-speech.org/iscaweb/index.php/conferences/interspeech
Publication Alternate Urls: http://www.isca-speech.org/