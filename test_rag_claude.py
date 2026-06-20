from src.pdf_loader import load_pdf
from src.chunking import chunk_text
from src.retrieval import build_index, retrieve_chunks
from src.claude_summarizer import summarize_context

text = load_pdf("data/sample.pdf")

chunks = chunk_text(text)

index, chunks = build_index(chunks)

question = "What is the job title?"

relevant_chunks = retrieve_chunks(
    index,
    chunks,
    question
)

context = "\n".join(relevant_chunks)

answer = summarize_context(
    context,
    question
)

print("\nQuestion:")
print(question)

print("\nAnswer:")
print(answer)