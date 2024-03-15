Faculty: Shinji Watanabe
Title: Structured Pruning of Self-Supervised Pre-Trained Models for Speech Recognition and Understanding
Abstract: Self-supervised speech representation learning (SSL) has shown to be effective in various downstream tasks, but SSL models are usually large and slow. Model compression techniques such as pruning aim to reduce the model size and computation without degradation in accuracy. Prior studies focus on the pruning of Transformers; however, speech models not only utilize a stack of Transformer blocks, but also combine a frontend network based on multiple convolutional layers for low-level feature representation learning. This frontend has a small size but a heavy computational cost. In this work, we propose three task-specific structured pruning methods to deal with such heterogeneous networks. Experiments on LibriSpeech and SLURP show that the proposed method is more accurate than the original wav2vec2-base with 10% to 30% less computation, and is able to reduce the computation by 40% to 50% without any degradation.
Year: 2023
Authors: Yifan Peng, Kwangyoun Kim, Felix Wu, Prashant Sridhar, Shinji Watanabe
Publication ID: 0d6f7fba-7092-46b3-8039-93458dba736b
Publication Name: IEEE International Conference on Acoustics, Speech, and Signal Processing
Publication Type: conference
Publication Alternate Names: Int Conf Acoust Speech Signal Process, IEEE Int Conf Acoust Speech Signal Process, ICASSP, International Conference on Acoustics, Speech, and Signal Processing
Publication Url: http://ieeexplore.ieee.org/xpl/conhome.jsp?punumber=1000002
