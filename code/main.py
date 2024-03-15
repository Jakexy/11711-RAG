# model? (only for finetuning or needed for reader model)
# parse knowledge base once or every time (parse data methods)

# parse data & answer questions form for paper/course data

# prepare test data

import argparse
import json
import numpy as np
import faiss
import torch
import os
from transformers import DPRContextEncoder, DPRContextEncoderTokenizer, DPRQuestionEncoder, DPRQuestionEncoderTokenizer, pipeline
# from transformers import DPRQuestionEncoderTokenizer, DPRQuestionEncoder, DPRContextEncoder, AutoModelForCausalLM, AutoTokenizer, pipeline, BertTokenizer, BertModel

# Workaround for potential OpenMP conflicts
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

index_path = 'data/embedded_data/faiss_index'
segment_path = 'data/embedded_data/segments.json'


# def load_documents(file_path):
#     segments = []
#     with open(file_path, 'r', encoding='utf-8') as file:
#         for line in file:
#             line = line.strip()  # Remove leading/trailing whitespace
#             if line:  # Ensure the line is not empty
#                 segments.append(line)
#     return segments

def search_documents(query_embedding, faiss_index, segments, k):
    _, indices = faiss_index.search(query_embedding, k)  # Search the index
    return [segments[idx] for idx in indices[0]]  # Return the top k segment(s)

def generate_response_pipeline(question, context):
    # naver-clova-ix/donut-base-finetuned-docvqa
    generator = pipeline('question-answering')
    response = generator(question=question, context=context, max_answer_len=1024)
    return response['answer']
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()

    # Initialize DPR models
    question_encoder = DPRQuestionEncoder.from_pretrained('facebook/dpr-question_encoder-single-nq-base')
    question_tokenizer = DPRQuestionEncoderTokenizer.from_pretrained('facebook/dpr-question_encoder-single-nq-base')
    print("Initialization finished!")

    # Encode segments to embeddings
    with open(segment_path, 'r') as file:
        segments = json.load(file)
    print("Embeddings segments finished!")

    # Create FAISS index from embeddings
    faiss_index = faiss.read_index(index_path)
    print("Faiss index finished!")

    # Encode the query
    query_inputs = question_tokenizer(args.query_text, return_tensors="pt", padding=True, truncation=True, max_length=1024)
    query_embedding = question_encoder(**query_inputs).pooler_output.detach().numpy()
    print("Encode query finished!")

    # Search for the most relevant segment(s)
    top_segments = search_documents(query_embedding, faiss_index, segments, k=3)
    print(f"Segments: {top_segments}")

    # Use the top segment for answering the question

    # response_pipeline = pipeline('question-answering')
    # response = response_pipeline(question=args.query_text, context=top_segments[0])
    response = generate_response_pipeline(question=args.query_text, context=top_segments[0])
    print(f"Response: {response}")
    

if __name__ == "__main__":
    main()

