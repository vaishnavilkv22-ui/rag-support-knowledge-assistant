# RAG Support Knowledge Assistant

A local Retrieval-Augmented Generation (RAG) application designed for Application Support and Production Support use cases.

The system takes an application-support question, semantically searches a support knowledge base, retrieves the most relevant knowledge chunks, and provides that context to a local Qwen 3 4B language model to generate a grounded troubleshooting response.

## Project Overview

Application Support teams often need to investigate incidents using runbooks, troubleshooting guides, known issues, and operational documentation.

This project demonstrates how RAG can connect an LLM to that support knowledge instead of relying only on the model's general knowledge.

### Workflow

```text
User Support Question
        ↓
Sentence Transformer
        ↓
Semantic Similarity Search
        ↓
Top-3 Relevant Knowledge Chunks
        ↓
RAG Prompt
        ↓
Qwen 3 4B
        ↓
Grounded Support Answer
        ↓
Sources
```

## Example

### User Question

> The application has become very slow and database requests are timing out. What could be causing this?

### Retrieved Knowledge

The system retrieves relevant sections from `database-timeout.md`, including:

* Initial Checks
* Possible Causes
* Symptoms

### Generated Response

The LLM provides troubleshooting guidance based on the retrieved support knowledge and distinguishes possible causes from confirmed root causes.

The response also identifies the knowledge sections used as sources.

## Key Features

* Semantic search using Sentence Transformers
* Knowledge retrieval based on meaning rather than exact keywords
* Top-3 relevant knowledge chunks
* Local LLM inference using Qwen 3 4B
* Retrieval-Augmented Generation (RAG)
* Source-aware responses
* Grounded troubleshooting recommendations
* Explicit protection against unsupported root-cause claims
* Application Support / Production Support use case
* Runs locally without a paid LLM API

## Technology Stack

* Python
* Sentence Transformers
* `all-MiniLM-L6-v2`
* Ollama
* Qwen 3 4B
* Semantic similarity search
* Markdown-based support knowledge

## Project Structure

```text
rag-support-knowledge-assistant/
│
├── rag.py
├── retriever.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── support-knowledge/
    └── database-timeout.md
```

## How It Works

### 1. User Question

The user enters an application-support question.

Example:

```text
Database timeouts started immediately after a deployment.
How should I investigate?
```

### 2. Semantic Embedding

The Sentence Transformer converts the question into a numerical vector representation.

This allows the system to compare the meaning of the question with the meaning of knowledge-base content.

### 3. Knowledge Retrieval

The support documentation is divided into sections and converted into embeddings.

The system calculates semantic similarity between the user question and each knowledge chunk.

The highest-scoring chunks are returned.

### 4. RAG Prompt

The retrieved knowledge is added to a prompt together with the user's question and instructions for the LLM.

The prompt instructs the model to:

* use the provided support knowledge
* avoid inventing root causes
* distinguish symptoms from possible causes
* provide practical troubleshooting steps
* recommend escalation where appropriate
* identify the knowledge sources used

### 5. Local LLM

The prompt is sent to Qwen 3 4B running locally through Ollama.

The model generates the final support response.

### 6. Grounded Answer

The final response is based primarily on the retrieved support knowledge rather than unrestricted model generation.

## Retrieval Testing

The retriever was tested using several realistic Application Support questions.

### Test 1

**Question:**

> The application cannot reach the database after a network change. What should I check?

**Top result:**

```text
Initial Checks
Similarity: 0.6498
```

Relevant retrieved information included:

* database reachability
* network connectivity
* connection pool usage
* recent configuration changes
* other applications using the database

### Test 2

**Question:**

> The application has become very slow and database requests are timing out. What could be causing this?

**Top results included:**

```text
Initial Checks
Similarity: 0.7075

Possible Causes
Similarity: 0.6343

Symptoms
Similarity: 0.6328
```

The retrieved Possible Causes section included:

* database availability problems
* network connectivity issues
* connection pool exhaustion
* database performance degradation
* application resource pressure
* configuration changes
* increased application traffic

### Test 3

**Question:**

> Database timeouts started immediately after a deployment. How should I investigate?

**Top results included:**

```text
Initial Checks
Similarity: 0.7365

Troubleshooting Approach
Similarity: 0.6982
```

The retrieved troubleshooting guidance specifically recommends comparing the incident timeline with deployments or configuration changes.

## Why RAG?

A general-purpose LLM may provide a technically reasonable answer, but an enterprise support environment requires answers aligned with the organization's own documentation and procedures.

RAG provides a mechanism to:

* connect an LLM to internal knowledge
* retrieve relevant operational information
* reduce reliance on generic model knowledge
* provide source context
* make support responses more consistent
* create a foundation for enterprise AI assistants

## Application Support Use Case

This project is designed around real Application Support workflows.

Potential future integrations include:

```text
Application Logs
      ↓
Monitoring Systems
      ↓
Incident / Ticketing Systems
      ↓
Support Knowledge
      ↓
RAG Support Agent
      ↓
AI Investigation
      ↓
Evidence-Based Recommendation
```

This creates a foundation for an AI-powered Application Support platform.

## Current Limitations

The current implementation is intentionally simple and runs locally.

Current limitations include:

* Markdown knowledge base
* embeddings are generated during search
* no persistent vector database
* local CPU-based LLM inference
* no live monitoring integration
* no ticketing-system integration
* no authentication or authorization layer
* limited evaluation dataset

These limitations provide opportunities for future improvements.

## Future Improvements

Planned improvements include:

* Persistent vector database
* Embedding caching
* Improved chunking and ranking
* Retrieval evaluation framework
* RAG evaluation metrics
* MCP-based support tools
* Log analysis integration
* Monitoring integration
* Incident/ticket integration
* Agentic troubleshooting workflows
* Cloud deployment
* Observability and latency monitoring
* Enterprise security controls

## Skills Demonstrated

This project demonstrates practical experience with:

* Python
* LLM integration
* Local AI inference
* Retrieval-Augmented Generation
* Semantic search
* Embeddings
* Prompt engineering
* Knowledge retrieval
* Application Support automation
* Production troubleshooting workflows
* Grounded AI responses

## Portfolio Context

This project is part of a hands-on AI learning path focused on combining Application Support experience with modern AI engineering techniques.

The goal is to build practical AI systems that can assist with:

* Incident investigation
* Log analysis
* Troubleshooting
* Knowledge retrieval
* Production support
* Operational automation

## Author

Vaishnavi LK

Application Support Engineer | AI / RAG / Agentic AI
