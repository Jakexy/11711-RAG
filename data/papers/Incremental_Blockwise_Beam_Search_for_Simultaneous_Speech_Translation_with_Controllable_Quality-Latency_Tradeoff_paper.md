Faculty: Alexander Waibel
Title: Incremental Blockwise Beam Search for Simultaneous Speech Translation with Controllable Quality-Latency Tradeoff
Abstract: Blockwise self-attentional encoder models have recently emerged as one promising end-to-end approach to simultaneous speech translation. These models employ a blockwise beam search with hypothesis reliability scoring to determine when to wait for more input speech before translating further. However, this method maintains multiple hypotheses until the entire speech input is consumed -- this scheme cannot directly show a single \textit{incremental} translation to users. Further, this method lacks mechanisms for \textit{controlling} the quality vs. latency tradeoff. We propose a modified incremental blockwise beam search incorporating local agreement or hold-$n$ policies for quality-latency control. We apply our framework to models trained for online or offline translation and demonstrate that both types can be effectively used in online mode. Experimental results on MuST-C show 0.6-3.6 BLEU improvement without changing latency or 0.8-1.4 s latency improvement without changing quality.
Year: 2023
Authors: Peter Polák, Brian Yan, Shinji Watanabe, A. Waibel, Ondrej Bojar
Publication ID: af90489e-312f-4514-bea2-bcb399cb8ece
Publication Name: Interspeech
Publication Type: conference
Publication Alternate Names: Conf Int Speech Commun Assoc, INTERSPEECH, Conference of the International Speech Communication Association
Publication Issn: 2308-457X
Publication Url: https://www.isca-speech.org/iscaweb/index.php/conferences/interspeech
Publication Alternate Urls: http://www.isca-speech.org/
