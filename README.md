Project Documentation:  RAG-based PDF Question-Answering System

 1. Executive Summary

This project implements a local Retrieval-Augmented Generation (RAG) web application designed to allow users to interact intelligently with their unstructured PDF documents. By combining document parsing, vector embeddings, and a local Large Language Model (LLM), the system retrieves precise context from uploaded documents to answer user queries accurately without relying on external cloud APIs.

2. Core Tech Stack

 (i)Backend: Python, FastAPI (for high-performance API routing and handling asynchronous requests)

 (ii)RAG Framework: LangChain (document processing and retrieval chains)

 (iii)Vector Database: FAISS (Facebook AI Similarity Search for fast local vector storage and similarity matching)

 (iv)Embeddings: HuggingFace Embeddings (all-MiniLM-L6-v2 model for efficient text vectorization)

 (iv)Large Language Model: Llama 3 running locally via Ollama

 (v)Frontend: HTML5, CSS, and JavaScript (index.html)

3. End-to-End System Workflow

 The application operates through an automated pipeline divided into document ingestion and query retrieval:

 (i)Document Ingestion & Splitting: The user uploads a PDF through the frontend web interface. The FastAPI backend receives the file, and LangChain's PyPDFLoader reads the raw text, which is then broken down into manageable text chunks using RecursiveCharacterTextSplitter.

 (ii)Embedding & Storage: These chunks are converted into dense numerical vector embeddings using HuggingFace and indexed locally inside a FAISS vector database for rapid semantic searching.

 (iii)Semantic Retrieval: When a user enters a query, the system queries the FAISS database to extract the top-k most contextually relevant text chunks matching the question.

 (iv)Answer Generation: The retrieved context chunks and the user's prompt are passed to the local Llama 3 model via Ollama using LangChain’s RetrievalQA chain, generating a precise, grounded response displayed directly on the UI.

4. How to Run Locally

Step 1: Start Ollama 

open your terminal or command prompt and make sure your local LLM is running:-

    ollama run llama3

Step 2: Install the required Python dependencies (fastapi, uvicorn, langchain, faiss-cpu, sentence-transformers).

Step 3: Start the FastAPI backend server (paste the command written below in VS terminal):

    uvicorn main:app --reload

Step 4: Open index.html in your web browser to use the interactive interface
