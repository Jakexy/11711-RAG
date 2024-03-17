# RAG Model Implementation

This repository contains the implementation of the Retrieval-Augmented Generation (RAG) model, which combines the power of a retriever and a generator to provide informative answers to queries. This model is particularly useful for tasks that require external knowledge or context.

## Installation

Before running the model, ensure you have the following packages installed:

- `transformers`
- `faiss`

You can install these packages using `pip` by running the following command:

```bash
pip install transformers faiss-cpu # Use faiss-cpu or faiss-gpu depending on your setup
```

## Getting started 

### Navigate to the Root Directory

Open your terminal and navigate to the root directory of this project.

### Run the Model
```bash
python3 code/main.py '[query]'
```
Ensure you include the query in quotes if it consists of multiple words.

## Example
To get answers related to "How many people does it take to maneuver the .84 -mile course around Schenley Park's Flagstaff Hill?", run:
```bash
python3 code/main.py "How many people does it take to maneuver the .84 -mile course around Schenley Park's Flagstaff Hill?"
```

## Authors
Yuxin (Vincy) Zheng (Andrew Id: yuxinzhe)
Xiaoyang (Jake) Wen (Andrew Id: xwen2)

