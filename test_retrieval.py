from src.pdf_loader import load_pdf
from src.chunking import chunk_text
from src.retrieval import build_index, retrieve_chunks

text = load_pdf("data/sample.pdf")

chunks = chunk_text(text)

index, chunks = build_index(chunks)

query = "What is the job title?"

results = retrieve_chunks(index, chunks, query)

print("\nRetrieved Results:\n")

for result in results:
    print(result)
    print("-" * 50)