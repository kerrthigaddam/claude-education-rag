# claude-education-rag
Claude-powered Educational Content Summarization and Evaluation Framework using RAG, Amazon Bedrock, LlamaIndex, and Streamlit.
# Claude-Powered RAG Document Question Answering System

## Project Overview

This project is an end-to-end Retrieval-Augmented Generation (RAG) application built using Python, FAISS, Sentence Transformers, and Anthropic Claude.

The system processes PDF documents, creates semantic embeddings, stores them in a FAISS vector database, retrieves relevant content based on user queries, and generates context-aware answers using Claude Sonnet.

---

## Architecture

PDF Document
↓
PyPDF
↓
Text Chunking
↓
Sentence Transformers Embeddings
↓
FAISS Vector Store
↓
Semantic Retrieval
↓
Claude Sonnet 4.6
↓
Generated Answer

---

## Features

- PDF document ingestion
- Text chunking and preprocessing
- Semantic embeddings generation
- FAISS vector similarity search
- Retrieval-Augmented Generation (RAG)
- Claude Sonnet integration
- Context-aware question answering

---

## Technologies Used

- Python
- Anthropic Claude API
- FAISS
- Sentence Transformers
- PyPDF
- NumPy
- Python Dotenv

---

## Project Structure

```text
claude-education-rag/
│
├── data/
│   └── sample.pdf
│
├── src/
│   ├── pdf_loader.py
│   ├── chunking.py
│   ├── retrieval.py
│   ├── claude_summarizer.py
│   ├── evaluator.py
│   └── rubrics.py
│
├── test_pdf.py
├── test_chunking.py
├── test_retrieval.py
├── test_claude.py
├── test_rag_claude.py
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone https://github.com/kerrthigaddam/claude-education-rag.git

cd claude-education-rag

pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

## Run the Application

```bash
python test_rag_claude.py
```

## Example Question

```text
Question:
What is the job title?
```

## Example Response

```text
Answer:
Based on the offer letter, the job title is Network Engineer.
```

## Learning Outcomes

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- Large Language Models
- Claude API Integration
- AI Application Development

## Author

Keerthi Yadav
Master's in Computer Information Systems
Auburn University at Montgomery
