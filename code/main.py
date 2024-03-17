import argparse
import json
import faiss
import os
from transformers import DPRContextEncoder, DPRContextEncoderTokenizer, DPRQuestionEncoder, DPRQuestionEncoderTokenizer, pipeline

# Workaround for potential OpenMP conflicts
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

index_path = 'data/embedded_data/faiss_index'
segment_path = 'data/embedded_data/segments.json'
question_path = 'question-answer/questions.txt'
answer_path = 'question-answer/answers_with_bert.txt'

def search_documents(query_embedding, faiss_index, segments, k):
    _, indices = faiss_index.search(query_embedding, k)  # Search the index
    return [segments[idx] for idx in indices[0]]  # Return the top k segment(s)

def generate_response_pipeline(generator, question, context):
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
    
    generator = pipeline('question-answering',model='bert-large-uncased-whole-word-masking-finetuned-squad')
    
    # count = 0
    # with open(answer_path, 'w', encoding='utf-8') as file_anwer:
    #     with open(question_path, 'r', encoding='utf-8') as file:
    #         questions = file.read()
    #         for question in questions.split("\n"):
    #             # print(question)
    #             query_inputs = question_tokenizer(question, return_tensors="pt", padding=True, truncation=True, max_length=1024)
    #             query_embedding = question_encoder(**query_inputs).pooler_output.detach().numpy()
    #             top_segments = search_documents(query_embedding, faiss_index, segments, k=3)
    #             response = generate_response_pipeline(generator, question=question, context=top_segments[0])
    #             response = response.replace("\n", " ")
    #             file_anwer.write(response + "\n")
    #             # print(response)
    #             count += 1
    #             print(count, "out of 125")
    # Encode the query
    query_inputs = question_tokenizer(args.query_text, return_tensors="pt", padding=True, truncation=True, max_length=1024)
    query_embedding = question_encoder(**query_inputs).pooler_output.detach().numpy()
    print("Encode query finished!")

    # Search for the most relevant segment(s)
    top_segments = search_documents(query_embedding, faiss_index, segments, k=3)     

    # Use the top segment for answering the question

    response_pipeline = pipeline('question-answering')
    response = response_pipeline(question=args.query_text, context=top_segments[0])
    response = generate_response_pipeline(generator, question=args.query_text, context=top_segments[0])
    
    print(f"Response: {response}")
    

if __name__ == "__main__":
    main()

