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

# Workaround for potential OpenMP conflicts
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

directory_path = 'data/parsed_data'
directory_path2 = 'data/papers'
output_path_index = 'data/embedded_data/faiss_index_l2'
output_path_segments = 'data/embedded_data/segments_l2.json'

def load_documents(max_chars=1000, overlap_chars=250):
    documents = []
    for file_name in os.listdir(directory_path):
        if file_name.endswith('buggy_1.md'):
            file_path = os.path.join(directory_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Calculate the number of chunks
                num_segments = len(content) // (max_chars - overlap_chars) + 1
                for i in range(num_segments):
                    start_index = i * (max_chars - overlap_chars)
                    end_index = start_index + max_chars
                    chunk = content[start_index:end_index].strip()
                    if chunk:  # Avoid adding empty strings
                        documents.append(chunk)
    return documents

def encode_documents(documents, context_encoder, context_encoder_tokenizer):
    inputs = context_encoder_tokenizer(documents, padding=True, truncation=True, return_tensors="pt", max_length=1024)
    outputs = context_encoder(**inputs)
    return outputs.pooler_output.detach().numpy()

def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    # index = faiss.IndexFlatIP(dimension)
    index.add(embeddings)
    return index

def search_documents(query_embedding, faiss_index, segments, k):
    _, indices = faiss_index.search(query_embedding, k)  # Search the index
    return [segments[idx] for idx in indices[0]]  # Return the top k segment(s)

def appendSegments(segments,path):
    with open(path, 'r') as file:
        json_data = json.load(file)

    json_data.append(segments)

    # Write the updated JSON data back to the file
    with open(path, 'w') as file:
        json.dump(json_data, file)
        
def ini(context_encoder,context_tokenizer):
    # Load segments from the file
    segments = load_documents()
    # print("LOAD documents finished!")


    # Encode segments to embeddings
    inputs = context_tokenizer(segments, padding=True, truncation=True, return_tensors="pt", max_length=512)
    context_embeddings = context_encoder(**inputs).pooler_output.detach().numpy()
    # print("Embeddings segments finished!")
    
    with open(output_path_segments, 'w', encoding='utf-8') as file:
        json.dump(segments, file, indent=4)
    faiss_index = create_faiss_index(context_embeddings)
    faiss.write_index(faiss_index, output_path_index)
        
def helper(segments,context_encoder,context_tokenizer):
    # Encode segments to embeddings
    inputs = context_tokenizer(segments, padding=True, truncation=True, return_tensors="pt", max_length=512)
    context_embeddings = context_encoder(**inputs).pooler_output.detach().numpy()
    # print("Embeddings segments finished!")
    
    appendSegments(segments,output_path_segments)
    faiss_index = faiss.read_index(output_path_index)
    faiss_index.add(context_embeddings)
    faiss.write_index(faiss_index, output_path_index)

def read_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        while True:
            lines = [file.readline() for _ in range(n)]  # Read N lines at a time
            if not any(lines):  # Check if all lines are empty (end of file)
                break
            yield lines
    
def main():
    context_encoder = DPRContextEncoder.from_pretrained('facebook/dpr-ctx_encoder-single-nq-base')
    context_tokenizer = DPRContextEncoderTokenizer.from_pretrained('facebook/dpr-ctx_encoder-single-nq-base')
    max_chars, overlap_chars = 500, 125
    ini(context_encoder,context_tokenizer)    
    count = 1
    print("    Currently done with",count,"files")
    for file_name in os.listdir(directory_path):
        print("Working on",file_name)
        if not file_name.endswith('.md'):
            continue
        elif file_name.endswith('courses.md'):
            file_path = os.path.join(directory_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                for chunk in content.split('\n'):
                    chunk = chunk.strip()
                    # Process each chunk of lines
                    helper(chunk,context_encoder,context_tokenizer)
        else:
            file_path = os.path.join(directory_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Calculate the number of segments
                num_segments = len(content) // (max_chars - overlap_chars) + 1
                for i in range(num_segments):
                    start_index = i * (max_chars - overlap_chars)
                    end_index = start_index + max_chars
                    segment = content[start_index:end_index].strip()
                    # print(segment)
                    # print(start_index,end_index)
                    # print(segment)
                    if segment:  # Avoid processing empty segments
                        helper(segment,context_encoder,context_tokenizer)
        count += 1
        print("    Currently done with",count,"files")
    count = 0
    for file_name in os.listdir(directory_path2):
        if not file_name.endswith('.md'):
            continue
        file_path = os.path.join(directory_path2, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            if content:
                helper(content,context_encoder,context_tokenizer)
        count += 1
        print("    Currently done with",count,"papers")
        
    
if __name__ == "__main__":
    main()
