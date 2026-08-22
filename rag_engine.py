from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain_classic.chains import RetrievalQA

class RAGAssistant:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.knowledge_base = None
        self.qa_system = None
        self.llm = Ollama(model="llama3")

    def process_file(self, file_path: str):
        loader = PyPDFLoader(file_path)
        pages = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        text_chunks = text_splitter.split_documents(pages)

        self.knowledge_base = FAISS.from_documents(text_chunks, self.embeddings)

        retriever = self.knowledge_base.as_retriever(search_kwargs={"k": 3})
        self.qa_system = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever
        )
        return "PDF processed successfully!"

    def ask_question(self, question: str):
        if not self.qa_system:
            return "Please upload a PDF first."
        
        response = self.qa_system.run(question)
        
        if not response or "don't know" in response.lower():
            return "Information was not found in the uploaded document."
            
        return response