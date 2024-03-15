Faculty: Shinji Watanabe
Title: Decoder-only Architecture for Speech Recognition with CTC Prompts and Text Data Augmentation
Abstract: Collecting audio-text pairs is expensive; however, it is much easier to access text-only data. Unless using shallow fusion, end-to-end automatic speech recognition (ASR) models require architecture modifications or additional training schemes to use text-only data. Inspired by recent advances in decoder-only language models (LMs), such as GPT-3 and PaLM adopted for speech-processing tasks, we propose using a decoder-only architecture for ASR with simple text augmentation. To provide audio information, encoder features compressed by CTC prediction are used as prompts for the decoder, which can be regarded as refining CTC prediction using the decoder-only model. Because the decoder architecture is the same as an autoregressive LM, it is simple to enhance the model by leveraging external text data with LM training. An experimental comparison using LibriSpeech and Switchboard shows that our proposed models with text augmentation training reduced word error rates from ordinary CTC by 0.3% and 1.4% on LibriSpeech test-clean and testother set, respectively, and 2.9% and 5.0% on Switchboard and CallHome. The proposed model had advantage on computational efficiency compared with conventional encoder-decoder ASR models with a similar parameter setup, and outperformed them on the LibriSpeech 100h and Switchboard training scenarios.
Year: 2023
Authors: E. Tsunoo, Hayato Futami, Yosuke Kashiwagi, Siddhant Arora, Shinji Watanabe
Publication ID: 1901e811-ee72-4b20-8f7e-de08cd395a10
Publication Name: arXiv.org
Publication Alternate Names: ArXiv
Publication Issn: 2331-8422
Publication Url: https://arxiv.org
