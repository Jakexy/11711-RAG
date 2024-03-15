Faculty: Kemal Oflazer
Title: Abstractive summarization with deep reinforcement learning using semantic similarity rewards
Abstract: 
 Abstractive summarization is an approach to document summarization that is not limited to selecting sentences from the document but can generate new sentences as well. We address the two main challenges in abstractive summarization: how to evaluate the performance of a summarization model and what is a good training objective. We first introduce new evaluation measures based on the semantic similarity of the input and corresponding summary. The similarity scores are obtained by the fine-tuned BERTurk model using either the cross-encoder or a bi-encoder architecture. The fine-tuning is done on the Turkish Natural Language Inference and Semantic Textual Similarity benchmark datasets. We show that these measures have better correlations with human evaluations compared to Recall-Oriented Understudy for Gisting Evaluation (ROUGE) scores and BERTScore. We then introduce a deep reinforcement learning algorithm that uses the proposed semantic similarity measures as rewards, together with a mixed training objective, in order to generate more natural summaries in terms of human readability. We show that training with a mixed training objective function compared to only the maximum-likelihood objective improves similarity scores.
Year: 2023
Authors: Figen Beken Fikri, Kemal Oflazer, B. Yanikoglu
Publication ID: b0dc264e-1ef6-4c58-be54-d2e6137ac35f
Publication Name: Natural Language Engineering
Publication Type: journal
Publication Alternate Names: Nat Lang Eng
Publication Issn: 1351-3249
Publication Url: https://www.cambridge.org/core/journals/natural-language-engineering
Publication Alternate Urls: http://journals.cambridge.org/action/displayJournal?jid=NLE