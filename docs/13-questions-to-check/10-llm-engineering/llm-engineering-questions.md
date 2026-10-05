## Pretraining & Tokenization

### Question 1

What is the pretraining objective of a decoder-only LLM, and why does it scale well without labeled data?

---

### Question 2

Why is next-token prediction sufficient to learn such a broad range of capabilities?

---

### Question 3

Why do LLMs use subword tokenization instead of word-level or character-level tokenization? 

A: To have a smaller vocabulary with less unique tokens than at word-level and avoid unknown words. And because character-level tokens are often not meaningful enough and computationally to ineffient. 

---

### Question 4

How can tokenization explain weaknesses of LLMs in arithmetic, spelling or non-English text?

---

## Self-Attention & Multi-Head Attention

### Question 5

What is the intuitive role of queries, keys and values in self-attention?

---

### Question 6

Why is the dot product in self-attention scaled by the square root of the key dimension?

---

### Question 7

Why does multi-head attention often work better than a single attention head with the same total dimension?

---

### Question 8

Why does self-attention scale quadratically with sequence length, and why is this a problem for long contexts?

---

## Positional Encoding

### Question 9

Why does a Transformer need explicit positional information?

---

### Question 10

What is the difference between absolute and relative positional encodings?

---

### Question 11

How does Rotary Position Embedding (RoPE) encode relative positions?

---

### Question 12

Why do models often perform poorly on sequences longer than those seen during training?

---

## Decoder-Only Models & Inference

### Question 13

Why is causal masking required in decoder-only models?

---

### Question 14

Why have decoder-only models become dominant for LLMs compared to encoder-decoder architectures?

---

### Question 15

What is the KV cache, and why does it speed up autoregressive generation?

---

### Question 16

Why can training be parallelized over all tokens while inference is inherently sequential?

---

## Model Architectures (GPT, LLaMA, MoE, Multimodal)

### Question 17

How does a Mixture of Experts model increase the number of parameters without proportionally increasing compute per token?

---

### Question 18

What is the role of the router in Mixture of Experts, and why is load balancing a problem?

---

### Question 19

Why does a Mixture of Experts model still require a lot of memory at inference time?

---

### Question 20

How can images be integrated into an LLM in a multimodal architecture?

---

## Quantization

### Question 21

What is quantization, and why does it reduce memory consumption and latency?

---

### Question 22

What is the difference between post-training quantization and quantization-aware training?

---

### Question 23

Why is LLM inference often memory-bandwidth-bound rather than compute-bound?

---

### Question 24

Why do activation outliers make quantization of LLMs difficult?

---

## Instruction Tuning & Alignment

### Question 25

What is the difference between pretraining, instruction tuning and preference tuning (e.g. RLHF or DPO)?

---

### Question 26

Why does instruction tuning make a model more useful even though it hardly adds new knowledge?

---

### Question 27

Why is the quality of instruction data often more important than its quantity?

---

### Question 28

What is catastrophic forgetting, and how can it occur during finetuning?

---

## Parameter-Efficient Finetuning (PEFT & LoRA)

### Question 29

Why is full finetuning of large LLMs expensive in terms of memory?

---

### Question 30

How does LoRA work, and why does it drastically reduce the number of trainable parameters?

---

### Question 31

Why can LoRA adapters be merged into the base weights without additional inference latency?

---

### Question 32

When would you prefer RAG over finetuning, and when finetuning over RAG?

---

## Prompt Engineering & Structured Output

### Question 33

What is the difference between zero-shot, few-shot and chain-of-thought prompting?

---

### Question 34

Why can in-context examples change model behavior without any weight updates?

---

### Question 35

What is the difference between asking for JSON in the prompt and using constrained decoding?

---

### Question 36

How do temperature and top-p influence the output, and when should you use a low temperature?

---

## Function Calling, Tool Use & Agents

### Question 37

Does the LLM execute a function itself during function calling? Explain the actual flow.

---

### Question 38

Why are precise tool names and descriptions critical for reliable tool use?

---

### Question 39

What distinguishes an agent from a simple LLM call or a fixed chain?

---

### Question 40

What are typical failure modes of agents (e.g. loops, error accumulation), and how can they be mitigated?

---

## Retrieval-Augmented Generation (RAG)

### Question 41

Which problems of plain LLMs does RAG address?

---

### Question 42

Why are documents split into chunks, and how does chunk size affect retrieval quality?

---

### Question 43

Why can a RAG system still hallucinate even if the relevant document was retrieved?

---

### Question 44

What is the "lost in the middle" problem, and how does it affect the way retrieved context should be arranged?

---

## Vector Search & Retrieval

### Question 45

What is the difference between sparse retrieval (e.g. BM25) and dense retrieval?

---

### Question 46

Why is hybrid search often better than using only dense retrieval?

---

### Question 47

Why is approximate nearest neighbor search used instead of exact search?

---

### Question 48

Why does a re-ranker improve results after the initial retrieval step?

---

## LLM Evaluation

### Question 49

Why is evaluating LLMs fundamentally harder than evaluating a classification model?

---

### Question 50

Why are n-gram metrics like BLEU and ROUGE often insufficient for generative tasks?

---

### Question 51

What are typical biases of LLM-as-a-judge (e.g. position, verbosity, self-preference), and how can they be reduced?

---

### Question 52

Why should retrieval and generation be evaluated separately in a RAG system?

---

### Question 53

When is human evaluation still necessary despite its cost?

---

## Safety & Reliability

### Question 54

Why do LLMs hallucinate, and why are the outputs often still fluent and confident?

---

### Question 55

What is the difference between prompt injection and jailbreaking?

---

### Question 56

Why is indirect prompt injection especially dangerous in systems with RAG or tool access?

---

### Question 57

Which measures help to secure LLM applications (e.g. least privilege, output validation, guardrails)?
