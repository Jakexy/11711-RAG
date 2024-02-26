import json
import argparse
from transformers import DPRQuestionEncoderTokenizer, DPRQuestionEncoder, AutoModelForSeq2SeqLM, AutoTokenizer
import faiss  # Ensure FAISS is installed for efficient similarity search
import numpy as np

# Path to your JSON file
json_file_path = 'data/knowledge_source.json'

# Load the JSON file
with open(json_file_path, 'r') as file:
    documents = json.load(file)

# Assuming you have a preprocessed dataset of documents encoded and stored in FAISS
# and their corresponding texts and metadata in a list for retrieval after search
# For this example, we will simulate this with dummy data and a simple FAISS index

# Initialize models and tokenizers
question_encoder_tokenizer = DPRQuestionEncoderTokenizer.from_pretrained('facebook/dpr-question_encoder-single-nq-base')
question_encoder = DPRQuestionEncoder.from_pretrained('facebook/dpr-question_encoder-single-nq-base')
generator_tokenizer = AutoTokenizer.from_pretrained('gpt2')  # Change to your model of choice
generator_model = AutoModelForSeq2SeqLM.from_pretrained('gpt2')  # Change to your model of choice

# Simulate a database of documents (here with dummy embeddings and metadata)
doc_embeddings = np.random.rand(100, 768).astype('float32')  # Simulate 100 document embeddings
faiss_index = faiss.IndexFlatL2(768)
faiss_index.add(doc_embeddings)

documents = [{"text": "Document text " + str(i), "source": "Source " + str(i)} for i in range(100)]  # Dummy documents

# retriever
def search_documents(query_text, k=3):
    # Encode the query using DPR
    inputs = question_encoder_tokenizer(query_text, return_tensors="pt")
    question_embeddings = question_encoder(**inputs).pooler_output.detach().numpy()
    
    # Search the FAISS index
    distances, indices = faiss_index.search(question_embeddings, k)
    return [(documents[i], 1 - distances[0][idx]) for idx, i in enumerate(indices[0])]

# reader
def generate_response(context, question):
    prompt = f"Answer the following question based on the context: {context}\n\nQuestion: {question}\n\nAnswer:"
    input_ids = generator_tokenizer.encode(prompt, return_tensors="pt")
    outputs = generator_model.generate(input_ids, max_length=1000, early_stopping=True)
    response = generator_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text

    # Search the simulated database
    results = search_documents(query_text, k=3)
    if not results:
        print("Unable to find matching results.")
        return
    
    context_text = " ".join([result[0]["text"] for result in results])
    response_text = generate_response(context_text, query_text)
    
    sources = [result[0]["source"] for result in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)

if __name__ == "__main__":
    main()