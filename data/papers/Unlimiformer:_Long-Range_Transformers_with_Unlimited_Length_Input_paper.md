Faculty: Graham Neubig
Title: Unlimiformer: Long-Range Transformers with Unlimited Length Input
Abstract: Since the proposal of transformers, these models have been limited to bounded input lengths, because of their need to attend to every token in the input. In this work, we propose Unlimiformer: a general approach that wraps any existing pretrained encoder-decoder transformer, and offloads the cross-attention computation to a single k-nearest-neighbor (kNN) index, while the returned kNN distances are the attention dot-product scores. This kNN index can be kept on either the GPU or CPU memory and queried in sub-linear time; this way, we can index practically unlimited input sequences, while every attention head in every decoder layer retrieves its top-k keys, instead of attending to every key. We evaluate Unlimiformer on several long-document and book-summarization benchmarks, showing that it can process even 500k token-long inputs from the BookSum dataset, without any input truncation at test time. We demonstrate that Unlimiformer improves pretrained models such as BART and Longformer by extending them to unlimited inputs without additional learned weights and without modifying their code. We make our code and models publicly available at https://github.com/abertsch72/unlimiformer .
Year: 2023
Authors: Amanda Bertsch, Uri Alon, Graham Neubig, Matthew R. Gormley
Publication ID: d9720b90-d60b-48bc-9df8-87a30b9a60dd
Publication Name: Neural Information Processing Systems
Publication Type: conference
Publication Alternate Names: Neural Inf Process Syst, NeurIPS, NIPS
Publication Url: http://neurips.cc/