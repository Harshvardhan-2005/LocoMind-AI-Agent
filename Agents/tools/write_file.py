from langchain_core.tools import tool

@tool
def write_file(fileName: str, text: str) -> str:
    """Appends text to the specified file."""

    try:
        fileName += ".txt" if not fileName.endswith(".txt") else ""

        with open(fileName, "a+") as file:
            file.write(text + "\n")

        return f"Text successfully written to '{fileName}'."

    except Exception as e:
        return f"Error writing to file: {str(e)}"