Faculty: Shinji Watanabe
Title: Segment-Level Vectorized Beam Search Based on Partially Autoregressive Inference
Abstract: Attention-based encoder-decoder models with autoregressive (AR) decoding have proven to be the dominant approach for automatic speech recognition (ASR) due to their superior accuracy. However, they often suffer from slow inference. This is primarily attributed to the incremental calculation of the decoder. This work proposes a partially AR framework, which employs segment-level vectorized beam search for improving the inference speed of an ASR model based on the hybrid connectionist temporal classification (CTC) attention-based architecture. It first generates an initial hypothesis using greedy CTC decoding, identifying low-confidence tokens based on their output probabilities. We then utilize the decoder to perform segment-level vectorized beam search on these tokens, re-predicting in parallel with minimal decoder calculations. Experimental results show that our method is 12 to 13 times faster in inference on the LibriSpeech corpus over AR decoding whilst preserving high accuracy.
Year: 2023
Authors: Masao Someki, N. Eng, Yosuke Higuchi, Shinji Watanabe
Publication ID: 29014a7c-861f-43bd-b4d6-63edf4cd57ef
Publication Name: Automatic Speech Recognition & Understanding
Publication Type: conference
Publication Alternate Names: IEEE Automatic Speech Recognition and Understanding Workshop, Autom Speech Recognit  Underst, ASRU, IEEE Autom Speech Recognit Underst Workshop
