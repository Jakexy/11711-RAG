Faculty: Shinji Watanabe
Title: Speech Summarization of Long Spoken Document: Improving Memory Efficiency of Speech/Text Encoders
Abstract: Speech summarization requires processing several minute-long speech sequences to allow exploiting the whole context of a spoken document. A conventional approach is a cascade of automatic speech recognition (ASR) and text summarization (TS). However, the cascade systems are sensitive to ASR errors. Moreover, the cascade system cannot be optimized for input speech and utilize para-linguistic information. Recently, there has been an increased interest in end-to-end (E2E) approaches optimized to output summaries directly from speech. Such systems can thus mitigate the ASR errors of cascade approaches. However, E2E speech summarization requires massive computational resources because it needs to encode long speech sequences. We propose a speech summarization system that enables E2E summarization from 100 seconds, which is the limit of the conventional method, to up to 10 minutes (i.e., the duration of typical instructional videos on YouTube). However, the modeling capability of this model for minute-long speech sequences is weaker than the conventional approach. We thus exploit auxiliary text information from ASR transcriptions to improve the modeling capabilities. The resultant system consists of a dual speech/text encoder decoder-based summarization system. We perform experiments on the How2 dataset showing the proposed system improved METEOR scores by up to 2.7 points by fully exploiting the long spoken documents.
Year: 2023
Authors: Takatomo Kano, A. Ogawa, Marc Delcroix, Roshan Sharma, Kohei Matsuura, Shinji Watanabe
Publication ID: 0d6f7fba-7092-46b3-8039-93458dba736b
Publication Name: IEEE International Conference on Acoustics, Speech, and Signal Processing
Publication Type: conference
Publication Alternate Names: Int Conf Acoust Speech Signal Process, IEEE Int Conf Acoust Speech Signal Process, ICASSP, International Conference on Acoustics, Speech, and Signal Processing
Publication Url: http://ieeexplore.ieee.org/xpl/conhome.jsp?punumber=1000002