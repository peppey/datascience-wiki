# Retrieval-Augmented Generation (RAG)

## TL;DR

Retrieval-Augmented Generation (RAG) combines information retrieval with a large language model (LLM). Instead of relying only on its training data, the model retrieves relevant information from external documents and uses it to generate an answer.

## How RAG Works

A typical RAG pipeline consists of two phases:

**Indexing**
- Load documents from files, databases, or other sources.
- Split documents into smaller chunks.
- Convert chunks into vector embeddings.
- Store embeddings and document metadata in a vector database or search index.

**Retrieval and generation**
- Convert the user's query into an embedding.
- Retrieve the most relevant document chunks.
- Add the retrieved context to the LLM prompt.
- Generate an answer based on the provided context.

```text
Documents → Chunking → Embeddings → Vector Database
                                         ↑
User Query → Query Embedding → Retrieval
                                         ↓
                                  Context + Prompt
                                         ↓
                                        LLM
                                         ↓
                                      Answer
```

## Embeddings and Similarity Search

Embeddings represent text as numerical vectors. Semantically similar texts tend to have similar vector representations.

Cosine similarity measures the angle between two vectors:

$$
\text{cosine similarity}(A,B)
=
\frac{A \cdot B}{\|A\|\|B\|}
$$

A higher value generally indicates greater similarity. The interpretation depends on the embedding model and data.

## Important Design Choices

- **Chunking:** Chunk size, overlap, and document structure influence retrieval quality.
- **Retrieval:** Dense search uses embeddings; keyword search matches terms. Hybrid search combines both.
- **Top-k:** Determines how many chunks are retrieved.
- **Reranking:** Reorders retrieved chunks according to their relevance to the query.
- **Prompt design:** Instructions should define how the model uses context and handles missing information.
- **Evaluation:** Retrieval and answer quality should be evaluated separately.

## Common Challenges

- Relevant information is missing from retrieved chunks.
- Chunks lack context because documents were split poorly.
- The model generates unsupported claims despite having retrieved evidence.
- Access controls are not correctly enforced for individual documents.
- Prompt injection attacks in retrieved documents influence model behavior.

RAG reduces reliance on the model's internal knowledge but does not guarantee factual answers. Source citations, access controls, retrieval evaluation, and appropriate fallback behavior are important for reliable applications.

## RAG vs. Fine-Tuning

| RAG | Fine-tuning |
|---|---|
| Supplies external information at inference time | Changes model behavior through additional training |
| Well suited to frequently updated knowledge | Well suited to adapting style, format, or task behavior |
| Retrieved sources can be cited | Knowledge is not automatically traceable to a source |
| Requires a retrieval pipeline | Requires training data and a training process |

The approaches can also be combined.