from langchain_core.tools import tool

@tool
def create_file(fileName: str) -> str:
    """Creates a text file and writes the file name inside."""

    try:
        fileName += ".txt" if not fileName.endswith(".txt") else ""

        with open(fileName, "w") as file:
            file.write(f"{fileName}\n")

        return f"File '{fileName}' created successfully."

    except Exception as e:
        return f"Error creating file: {str(e)}"