from pathlib import Path
from sentence_transformers import SentenceTransformer, util

KNOWLEDGE_BASE = Path(__file__).parent.parent / "support-knowledge"

model = SentenceTransformer("all-MiniLM-L6-v2")


def chunk_document(content: str):
    """Split a Markdown document into chunks with section names."""

    lines = content.splitlines()

    chunks = []
    current_chunk = []
    current_section = "Introduction"

    for line in lines:

        if line.startswith("## "):

            # Save the previous chunk
            if current_chunk:
                chunks.append({
                    "section": current_section,
                    "text": "\n".join(current_chunk).strip()
                })

            # Start a new section
            current_section = line.replace("## ", "").strip()
            current_chunk = [line]

        else:
            current_chunk.append(line)

    # Save the final chunk
    if current_chunk:
        chunks.append({
            "section": current_section,
            "text": "\n".join(current_chunk).strip()
        })

    return chunks


def search_knowledge(query: str):
    """Search support knowledge using semantic similarity."""

    query_vector = model.encode(query)

    results = []

    for file in KNOWLEDGE_BASE.glob("*.md"):

        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        chunks = chunk_document(content)

        for chunk in chunks:

            text = chunk["text"]

            # Ignore chunks that contain only a heading
            lines = [
                line.strip()
                for line in text.splitlines()
                if line.strip()
            ]

            if len(lines) <= 1:
                continue

            chunk_vector = model.encode(text)

            similarity = util.cos_sim(
                query_vector,
                chunk_vector
            ).item()

            results.append({
                "file": file.name,
                "section": chunk["section"],
                "similarity": similarity,
                "text": text
            })

    # Highest similarity first
    results.sort(
        key=lambda x: x["similarity"],
        reverse=True
    )

    # Return Top 3 results
    return results[:3]


if __name__ == "__main__":

    query = input("Enter your support question: ")

    results = search_knowledge(query)

    print("\nTop 3 semantic search results:")

    for result in results:

        print(f"\nFile: {result['file']}")
        print(f"Section: {result['section']}")
        print(f"Similarity: {result['similarity']:.4f}")
        print("Knowledge:")
        print(result["text"])