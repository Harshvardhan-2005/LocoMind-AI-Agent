from langchain_core.tools import tool

@tool
def subtract(a: int, b: int) -> int:
    """Subtracts the second integer from the first."""

    return a - b