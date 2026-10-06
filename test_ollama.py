import ollama

response = ollama.chat(
    model="qwen3:4b",
    messages=[
        {
            "role": "user",
            "content": "Explain database connection timeout in one short sentence."
        }
    ]
)

print(response["message"]["content"])