from langchain_community.tools import tool

@tool("Summarize")
def summarize(text: str) -> str:
    """ Summarizes the given text. """
    
    return f"Summary of the text: {text[:100]}..."  # Simple placeholder summary logic
# This tool can be used to summarize text in the crewai_task.py file.