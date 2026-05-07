import os

from Agents.tools.rag_tools import ingest_document


folder = "knowledge_base"

for file in os.listdir(folder):

    path = os.path.join(folder, file)

    print(f"Ingesting: {file}")

    result = ingest_document.invoke(path)

    print(result)