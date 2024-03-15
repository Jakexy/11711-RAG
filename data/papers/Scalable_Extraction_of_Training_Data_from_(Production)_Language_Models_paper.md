Faculty: Daphne Ippolito
Title: Scalable Extraction of Training Data from (Production) Language Models
Abstract: This paper studies extractable memorization: training data that an adversary can efficiently extract by querying a machine learning model without prior knowledge of the training dataset. We show an adversary can extract gigabytes of training data from open-source language models like Pythia or GPT-Neo, semi-open models like LLaMA or Falcon, and closed models like ChatGPT. Existing techniques from the literature suffice to attack unaligned models; in order to attack the aligned ChatGPT, we develop a new divergence attack that causes the model to diverge from its chatbot-style generations and emit training data at a rate 150x higher than when behaving properly. Our methods show practical attacks can recover far more data than previously thought, and reveal that current alignment techniques do not eliminate memorization.
Year: 2023
Authors: Milad Nasr, Nicholas Carlini, Jonathan Hayase, Matthew Jagielski, A. F. Cooper, Daphne Ippolito, Christopher A. Choquette-Choo, Eric Wallace, Florian Tramèr, Katherine Lee
Publication ID: 1901e811-ee72-4b20-8f7e-de08cd395a10
Publication Name: arXiv.org
Publication Alternate Names: ArXiv
Publication Issn: 2331-8422
Publication Url: https://arxiv.org
