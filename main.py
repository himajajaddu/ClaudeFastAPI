from fastapi import FastAPI, UploadFile, File, Form
from utils.tools import route_tool, summarize, extract, classify

app = FastAPI(title="Claude Agent Chat API")

@app.post("/chat")
async def chat_route(query: str = Form(...), file: UploadFile = File(...)):
    doc = await file.read()
    doc_text = doc.decode(errors="ignore")

    tool = route_tool(query)

    if tool == "summarizer":
        result = summarize(doc_text)
    elif tool == "extractor":
        result = extract(doc_text, query)
    elif tool == "classifier":
        result = classify(doc_text)
    else:
        result = "❌ Could not determine intent from query."

    return {
        "tool": tool,
        "response": result
    }