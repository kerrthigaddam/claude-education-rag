from src.pdf_loader import load_pdf
from src.chunking import chunk_text

text = load_pdf("data/sample.pdf")

chunks = chunk_text(text)

print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")

print(chunks[0])