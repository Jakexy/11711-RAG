Faculty: Shinji Watanabe
Title: BASS: Block-wise Adaptation for Speech Summarization
Abstract: End-to-end speech summarization has been shown to improve performance over cascade baselines. However, such models are difficult to train on very large inputs (dozens of minutes or hours) owing to compute restrictions and are hence trained with truncated model inputs. Truncation leads to poorer models, and a solution to this problem rests in block-wise modeling, i.e., processing a portion of the input frames at a time. In this paper, we develop a method that allows one to train summarization models on very long sequences in an incremental manner. Speech summarization is realized as a streaming process, where hypothesis summaries are updated every block based on new acoustic information. We devise and test strategies to pass semantic context across the blocks. Experiments on the How2 dataset demonstrate that the proposed block-wise training method improves by 3 points absolute on ROUGE-L over a truncated input baseline.
Year: 2023
Authors: Roshan Sharma, Kenneth Zheng, Siddhant Arora, Shinji Watanabe, Rita Singh, B. Raj
Publication ID: af90489e-312f-4514-bea2-bcb399cb8ece
Publication Name: Interspeech
Publication Type: conference
Publication Alternate Names: Conf Int Speech Commun Assoc, INTERSPEECH, Conference of the International Speech Communication Association
Publication Issn: 2308-457X
Publication Url: https://www.isca-speech.org/iscaweb/index.php/conferences/interspeech
Publication Alternate Urls: http://www.isca-speech.org/