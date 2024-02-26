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

file_path = 'data/parsed_data/faculty_info.txt'

def load_documents(file_path):
    segments = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line:  # Ensure the line is not empty
                segments.append(line)
    return segments


def encode_documents(documents, context_encoder, context_encoder_tokenizer):
    inputs = context_encoder_tokenizer(documents, padding=True, truncation=True, return_tensors="pt", max_length=1024)
    outputs = context_encoder(**inputs)
    return outputs.pooler_output.detach().numpy()

def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def search_documents(query_embedding, faiss_index, segments, k):
    _, indices = faiss_index.search(query_embedding, k)  # Search the index
    return [segments[idx] for idx in indices[0]]  # Return the top k segment(s)

def generate_response_pipeline(context, question):
    generator = pipeline('question-answering', model="gpt2")
    
    response = generator(question=question, context=context, max_answer_len=1024)
    return response['answer']
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()

    # Load segments from the file
    file_path = 'data/parsed_data/faculty_info.txt'
    segments = load_documents(file_path)

    # Initialize DPR models
    context_encoder = DPRContextEncoder.from_pretrained('facebook/dpr-ctx_encoder-single-nq-base')
    context_tokenizer = DPRContextEncoderTokenizer.from_pretrained('facebook/dpr-ctx_encoder-single-nq-base')
    question_encoder = DPRQuestionEncoder.from_pretrained('facebook/dpr-question_encoder-single-nq-base')
    question_tokenizer = DPRQuestionEncoderTokenizer.from_pretrained('facebook/dpr-question_encoder-single-nq-base')

    # Encode segments to embeddings
    inputs = context_tokenizer(segments, padding=True, truncation=True, return_tensors="pt", max_length=1024)
    context_embeddings = context_encoder(**inputs).pooler_output.detach().numpy()

    # Create FAISS index from embeddings
    faiss_index = create_faiss_index(context_embeddings)

    # Encode the query
    query_inputs = question_tokenizer(args.query_text, return_tensors="pt", padding=True, truncation=True, max_length=1024)
    query_embedding = question_encoder(**query_inputs).pooler_output.detach().numpy()

    # Search for the most relevant segment(s)
    top_segments = search_documents(query_embedding, faiss_index, segments, k=1)
    print(f"segments: {top_segments}")

    # Use the top segment for answering the question
    response_pipeline = pipeline('question-answering')
    import pdb; pdb.set_trace()
    response = response_pipeline(question=args.query_text, context=top_segments[0])
    print(f"Response: {response['answer']}")
    

if __name__ == "__main__":
    main()

