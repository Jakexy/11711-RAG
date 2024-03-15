Faculty: Graham Neubig
Title: Learning to Filter Context for Retrieval-Augmented Generation
Abstract: On-the-fly retrieval of relevant knowledge has proven an essential element of reliable systems for tasks such as open-domain question answering and fact verification. However, because retrieval systems are not perfect, generation models are required to generate outputs given partially or entirely irrelevant passages. This can cause over- or under-reliance on context, and result in problems in the generated output such as hallucinations. To alleviate these problems, we propose FILCO, a method that improves the quality of the context provided to the generator by (1) identifying useful context based on lexical and information-theoretic approaches, and (2) training context filtering models that can filter retrieved contexts at test time. We experiment on six knowledge-intensive tasks with FLAN-T5 and LLaMa2, and demonstrate that our method outperforms existing approaches on extractive question answering (QA), complex multi-hop and long-form QA, fact verification, and dialog generation tasks. FILCO effectively improves the quality of context, whether or not it supports the canonical output.
Year: 2023
Authors: Zhiruo Wang, Jun Araki, Zhengbao Jiang, Md. Rizwan Parvez, Graham Neubig
Publication ID: 1901e811-ee72-4b20-8f7e-de08cd395a10
Publication Name: arXiv.org
Publication Alternate Names: ArXiv
Publication Issn: 2331-8422
Publication Url: https://arxiv.org
