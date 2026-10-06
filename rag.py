from retriever import search_knowledge
import ollama


def build_prompt(question: str, knowledge: str) -> str:
    """Build a grounded RAG prompt with source information."""

    prompt = f"""
You are an Application Support Assistant.

Answer the user's question using ONLY the support knowledge provided below.

Support Knowledge:
------------------
{knowledge}
------------------

User Question:
{question}

Instructions:
- Use the provided support knowledge as the primary source.
- Do not invent a root cause.
- Clearly distinguish symptoms, possible causes, and confirmed evidence.
- Give practical troubleshooting steps.
- Recommend escalation when appropriate.
- If the knowledge does not contain enough information, say so.
- Keep the answer concise and structured.
- At the end, include a "Sources" section.
- In the Sources section, list the knowledge file and section used.
- Do not invent sources.
"""

    return prompt


def ask_llm(prompt: str) -> str:
    """Send the RAG prompt to the local Qwen model."""

    response = ollama.chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


if __name__ == "__main__":

    question = input("Enter your support question: ")

    results = search_knowledge(question)

    if not results:
        print("No relevant knowledge found.")
        exit()

    # Build context from Top-K results
    knowledge_parts = []

    for i, result in enumerate(results, start=1):

        knowledge_parts.append(
            f"""Knowledge Chunk {i}
Source File: {result['file']}
Section: {result['section']}
Similarity: {result['similarity']:.4f}

Knowledge:
{result['text']}"""
        )

    knowledge = "\n\n".join(knowledge_parts)

    prompt = build_prompt(
        question,
        knowledge
    )

    answer = ask_llm(prompt)

    print("\n--- RAG SUPPORT ANSWER ---")
    print(answer)