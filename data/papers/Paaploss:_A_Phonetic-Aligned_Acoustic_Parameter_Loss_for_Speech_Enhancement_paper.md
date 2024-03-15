Faculty: Shinji Watanabe
Title: Paaploss: A Phonetic-Aligned Acoustic Parameter Loss for Speech Enhancement
Abstract: Despite rapid advancement in recent years, current speech enhancement models often produce speech that differs in perceptual quality from real clean speech. We propose a learning objective that formalizes differences in perceptual quality, by using domain knowledge of acoustic-phonetics. We identify temporal acoustic parameters – such as spectral tilt, spectral flux, shimmer, etc. – that are non-differentiable, and we develop a neural network estimator that can accurately predict their time-series values across an utterance. We also model phoneme-specific weights for each feature, as the acoustic parameters are known to show different behavior in different phonemes. We can add this criterion as an auxiliary loss to any model that produces speech, to optimize speech outputs to match the values of clean speech in these features. Experimentally we show that it improves speech enhancement workflows in both time-domain and time-frequency domain, as measured by standard evaluation metrics. We also provide an analysis of phoneme-dependent improvement on acoustic parameters, demonstrating the additional interpretability that our method provides. This analysis can suggest which features are currently the bottleneck for improvement.
Year: 2023
Authors: Muqiao Yang, Joseph Konan, David Bick, YUNYANG ZENG, Shuo Han, Anurag Kumar, Shinji Watanabe, B. Raj
Publication ID: 0d6f7fba-7092-46b3-8039-93458dba736b
Publication Name: IEEE International Conference on Acoustics, Speech, and Signal Processing
Publication Type: conference
Publication Alternate Names: Int Conf Acoust Speech Signal Process, IEEE Int Conf Acoust Speech Signal Process, ICASSP, International Conference on Acoustics, Speech, and Signal Processing
Publication Url: http://ieeexplore.ieee.org/xpl/conhome.jsp?punumber=1000002