import os


KNOWLEDGE_DIR = "knowledge"


def load_documents():

    documents = []

    if not os.path.exists(KNOWLEDGE_DIR):
        return documents

    for filename in os.listdir(KNOWLEDGE_DIR):

        path = os.path.join(KNOWLEDGE_DIR, filename)

        if filename.endswith(".txt"):

            with open(path, "r", encoding="utf-8") as file:
                text = file.read()

            documents.append({
                "filename": filename,
                "content": text
            })

    return documents


def retrieve(query: str):

    documents = load_documents()

    if not documents:
        return []

    query_words = set(query.lower().split())

    scored = []

    for document in documents:

        content_words = set(
            document["content"].lower().split()
        )

        score = len(query_words & content_words)

        scored.append({
            "filename": document["filename"],
            "content": document["content"],
            "score": score
        })

    scored.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return scored[:3]