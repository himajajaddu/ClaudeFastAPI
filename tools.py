from utils.claude_client import invoke_claude

def route_tool(query: str) -> str:
    prompt = f"""
You are a smart routing agent. Based on the user query, choose one of:
- Summarizer
- Extractor
- Classifier

Query: \"{query}\"
Respond with only the tool name.
"""
    tool = invoke_claude(prompt).lower()
    if "summarizer" in tool:
        return "summarizer"
    elif "extractor" in tool:
        return "extractor"
    elif "classifier" in tool:
        return "classifier"
    return "unknown"

def summarize(text: str) -> str:
    return invoke_claude(f"Human: Summarize this:\n\n{text}\n\nAssistant:")

def extract(text: str, query: str) -> str:
    return invoke_claude(f"Human: Extract the relevant answer for '{query}' from the document:\n\n{text}\n\nAssistant:")

def classify(text: str) -> str:
    return invoke_claude(f"Human: Classify this document into one of: spam, invoice, legal, other:\n\n{text}\n\nAssistant:")
