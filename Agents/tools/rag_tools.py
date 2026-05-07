import os
import time
from dotenv import load_dotenv

load_dotenv()
from typing_extensions import List, TypedDict

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain.chat_models import init_chat_model

from langchain_ollama import OllamaEmbeddings

from langchain_chroma import Chroma

from langchain_community.document_loaders import TextLoader

from langchain_core.documents import Document

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langgraph.graph import START, StateGraph


if not os.environ.get("GOOGLE_API_KEY"):
    print("GOOGLE_API_KEY not found.")


rag_llm = init_chat_model(
    "gemini-2.5-flash",
    model_provider="google_genai"
)


embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


vector_store = Chroma(
    collection_name="rag_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",
)


rag_prompt = ChatPromptTemplate.from_template(
    """
    Answer the question based only on the provided context.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
)


class RagState(TypedDict):
    question: str
    context: List[Document]
    answer: str


def retrieve(state: RagState):

    retrieved_docs = vector_store.similarity_search(
        state["question"]
    )

    return {
        "context": retrieved_docs
    }


def generate(state: RagState):

    docs_content = "\n\n".join(
        doc.page_content
        for doc in state["context"]
    )

    messages = rag_prompt.format_messages(
        question=state["question"],
        context=docs_content
    )

    response = rag_llm.invoke(messages)

    return {
        "answer": response.content
    }


rag_graph_builder = StateGraph(
    RagState
).add_sequence([
    retrieve,
    generate
])

rag_graph_builder.add_edge(
    START,
    "retrieve"
)

rag_graph = rag_graph_builder.compile()


@tool
def ingest_document(file_path: str) -> str:
    """
    Loads document into ChromaDB.
    """

    try:

        loader = TextLoader(file_path)

        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        all_splits = text_splitter.split_documents(
            docs
        )

        vector_store.add_documents(
            documents=all_splits
        )

        return (
            f"Document '{file_path}' "
            "ingested successfully."
        )

    except Exception as e:

        return (
            f"Error ingesting document: "
            f"{str(e)}"
        )

@tool
def ask_rag(question: str) -> str:
    """
    Ask question using RAG system.
    """

    try:

        start = time.time()

        inputs = {
            "question": question
        }

        result = rag_graph.invoke(inputs)

        end = time.time()

        latency = round(end - start, 2)

        return (
            f"Latency: {latency}s\n\n"
            f"{result['answer']}"
        )

    except Exception as e:

        return (
            f"Error asking RAG: "
            f"{str(e)}"
        )