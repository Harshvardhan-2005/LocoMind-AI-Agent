from langchain_core.tools import tool
from ddgs import DDGS

@tool
def search_duckduckgo(query: str) -> str:
    """
    Searches the web using DuckDuckGo.
    """

    try:

        with DDGS() as ddgs:

            results = list(
                ddgs.text(query, max_results=3)
            )

            if not results:
                return "No results found."

            formatted_results = []

            for r in results:

                formatted_results.append(
                    f"Title: {r.get('title')}\n"
                    f"Link: {r.get('href')}\n"
                    f"Body: {r.get('body')}\n"
                )

            return "\n\n".join(formatted_results)

    except Exception as e:

        return f"Search error: {str(e)}"