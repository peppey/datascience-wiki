# Quality Metrics for LLM Evaluation

## Definition

Quality metrics in LLM evaluation are quantitative measures used to assess whether a Large Language Model (LLM) produces outputs that satisfy predefined quality requirements.

Unlike traditional machine learning, LLM outputs are often open-ended natural language rather than fixed class labels or numerical predictions. Therefore, evaluating an LLM usually requires measuring several different quality dimensions.

Typical questions include:

- Is the answer factually correct?
- Does it answer the user's question?
- Is it complete?
- Is it supported by the provided context?
- Does it follow the instructions?
- Does it contain hallucinations?
- Is the retrieved context relevant?
- Is the response safe?
- Does the model behave consistently across similar inputs?

«LLM quality metrics are measurable indicators used to evaluate specific dimensions of an LLM system's output quality.»

A single metric is rarely sufficient to describe the quality of an LLM application.

---

## Why Quality Metrics Matter

LLMs can produce outputs that are:

Fluent
  +
Plausible
  +
Well-written
  ≠
Correct

For example:

Question:
When was Company X founded?

Retrieved context:
Company X was founded in 1998.

LLM answer:
Company X was founded in 2001 in Munich.

The answer may sound perfectly plausible, but it contains information that is not supported by the available context.

A good evaluation framework should therefore distinguish between different failure modes.

For example:

                    LLM Evaluation
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
   Retrieval          Generation         System
        │                 │                 │
   Is the context    Is the answer      Is the system
   relevant?         correct?           reliable?

---

## Quality Dimensions

Common quality dimensions for LLM evaluation include:

Dimension| Question
Correctness| Is the answer factually correct?
Relevance| Does the answer address the question?
Completeness| Does it contain all important information?
Faithfulness| Is it supported by the provided context?
Groundedness| Are claims grounded in available evidence?
Context relevance| Is the retrieved context useful?
Instruction following| Did the model follow the requested instructions?
Coherence| Is the response logically structured?
Fluency| Is the language natural and understandable?
Safety| Does the response avoid harmful or prohibited content?
Citation correctness| Do citations actually support the claims?

The relevant dimensions depend on the application.

---

@# Reference-Based vs. Reference-Free Evaluation

A fundamental distinction is whether a reference answer is available.

                 Evaluation
                     │
          ┌──────────┴──────────┐
          │                     │
   Reference available     No reference
          │                     │
          ▼                     ▼
 Reference-based          Reference-free
 evaluation               evaluation

Reference-Based Evaluation

The model output is compared with a known reference.

Example:

Question:
What is the capital of Germany?

Reference:
Berlin

Model:
Berlin

This makes evaluation relatively straightforward.

However, there can be many valid ways of answering an open-ended question. A reference-based metric can therefore incorrectly penalize a valid answer simply because it differs from the reference wording.

---

## Reference-Free Evaluation

The output is evaluated without requiring an exact reference answer.

For example:

Question
   +
Retrieved context
   +
LLM answer
        │
        ▼
   Evaluation model
        │
        ▼
Quality score

This is particularly useful for open-ended generation and RAG systems.

---

## Exact Match

Exact Match (EM) checks whether the generated answer exactly matches the reference answer.

Example:

Reference:
Berlin

Prediction:
Berlin

→ Match

But:

Reference:
Berlin

Prediction:
The capital of Germany is Berlin.

→ No exact match

Exact Match is therefore most useful when answers have a well-defined canonical form.

Typical use cases include:

- Structured extraction
- Short factual answers
- Classification-like tasks
- Mathematical answers
- Entity extraction

It is usually too strict for general conversational responses.

---

## Lexical Similarity Metrics

Traditional NLP metrics can compare generated text with reference text based on word or phrase overlap.

Examples include:

- BLEU
- ROUGE

BLEU

BLEU evaluates n-gram overlap between a generated answer and one or more reference texts.

It has historically been widely used for machine translation.

However:

Reference:
The meeting takes place on Monday.

Prediction:
The meeting is scheduled for Monday.

The two sentences have essentially the same meaning but do not have identical wording.

Lexical overlap therefore does not necessarily correspond to semantic correctness.

---

## ROUGE

ROUGE measures overlap between generated text and reference text.

Common variants include:

- ROUGE-1
- ROUGE-2
- ROUGE-L

ROUGE is particularly associated with summarization evaluation.

However, like BLEU, it primarily measures textual overlap rather than factual correctness.

---

## Semantic Similarity

Embedding-based metrics compare the semantic representation of the generated answer and a reference answer.

For example:

Reference:
The meeting takes place on Monday.

Prediction:
The meeting is scheduled for Monday.

The two texts may have high semantic similarity even though their exact wording differs.

A typical approach is:

Reference
    │
    ▼
Embedding Model
    │
    ▼
Vector ─────────┐
                │
                ▼
          Similarity Score
                ▲
                │
Vector ─────────┘
    ▲
    │
Embedding Model
    ▲
    │
Prediction

Common similarity measures include cosine similarity.

However:

«Semantic similarity does not necessarily imply factual correctness.»

Two statements can be semantically similar while both being factually wrong.

---

## LLM-as-a-Judge

One of the most important approaches for modern LLM evaluation is LLM-as-a-Judge.

An LLM is used to evaluate another model's output.

Input
  │
  ├──────────────┐
  ▼              │
LLM              │
  │              │
  ▼              │
Answer           │
                 ▼
             Judge LLM
                 │
                 ▼
          Evaluation result

The judge can evaluate dimensions such as:

Correctness:       1–5
Relevance:         1–5
Completeness:      1–5
Faithfulness:      1–5
Instruction-following: 1–5

The judge can also provide structured output:

{
  "correct": true,
  "score": 4,
  "reason": "The answer is correct but omits one relevant detail."
}

---

#€ Rubric-Based Evaluation

LLM-as-a-Judge works particularly well when the evaluation criteria are explicitly defined in a rubric.

Example:

Correctness

5 = Completely correct
4 = Mostly correct, minor omission
3 = Partially correct
2 = Contains significant errors
1 = Fundamentally incorrect

The evaluator receives:

Question
Reference / Context
Model Answer
Evaluation Rubric

and produces a score.

This makes the evaluation criteria more explicit and reproducible.

---

## Pairwise Evaluation

Instead of assigning an absolute score, a judge can compare two model outputs.

Question
   │
   ├── Model A → Answer A
   │
   └── Model B → Answer B
                 │
                 ▼
             Judge LLM
                 │
                 ▼
        A / B / Tie

Example:

Which answer is better?

Answer A:
...

Answer B:
...

Pairwise evaluation can be useful when comparing:

- Model versions
- Prompt versions
- RAG configurations
- Different LLM providers
- Different retrieval strategies

It can be easier for a judge to determine which of two responses is better than to assign an absolute quality score.

---

## LLM Judge Biases

LLM-as-a-Judge is powerful but not objective.

Potential problems include:

Position Bias

The judge may favor the first or second answer depending on presentation order.

Verbosity Bias

Longer answers may sometimes be judged as better simply because they contain more information.

Style Bias

The judge may prefer a particular writing style independently of factual quality.

Self-Preference

A model may prefer outputs that resemble its own style or behavior.

Evaluation Instability

Small changes in prompts or formatting can sometimes affect the judge's decision.

Therefore, LLM-as-a-Judge should itself be validated.

---

## Human Evaluation

Human evaluation remains important, particularly when:

- No reliable reference exists.
- The task is highly subjective.
- Safety is critical.
- Evaluation criteria are difficult to formalize.
- The cost of an incorrect answer is high.

A common approach is to combine:

Automated evaluation
        +
LLM-as-a-Judge
        +
Human evaluation

Human evaluation can also be used to validate whether automated metrics correlate with actual human judgments.

---

## RAG Evaluation

Retrieval-Augmented Generation (RAG) systems require evaluating both retrieval and generation.

A typical RAG pipeline is:

User Query
    │
    ▼
Retriever
    │
    ▼
Retrieved Documents
    │
    ▼
LLM
    │
    ▼
Generated Answer

This means there are at least two major evaluation areas:

Retrieval Quality
        +
Generation Quality

---

## Context Relevance

Context relevance measures whether the retrieved documents contain information that is relevant to the user's question.

Example:

Question:
When was Company X founded?

Retrieved document:
Company X was founded in 1998.

→ Highly relevant

Compared with:

Question:
When was Company X founded?

Retrieved document:
Company X currently employs 5,000 people.

→ Low relevance

A system can therefore fail even if the LLM itself is highly capable:

Bad retrieval
     ↓
Missing information
     ↓
Poor answer

---

## Context Recall

Context recall measures whether the retrieved context contains the information required to answer the question.

Suppose the relevant information is distributed across three documents:

Document A → Relevant information
Document B → Relevant information
Document C → Relevant information

If the retriever returns only:

Document A

then the retrieval process has incomplete coverage.

Context recall is therefore concerned with:

«Did retrieval find the information that was needed?»

---

## Context Precision

Context precision measures how much of the retrieved context is actually relevant.

Example:

Top 5 retrieved documents:

1. Relevant
2. Relevant
3. Irrelevant
4. Irrelevant
5. Irrelevant

Only 2 of the 5 documents are useful.

This indicates low context precision.

The distinction is:

Context Recall
→ Did we retrieve the necessary information?

Context Precision
→ Did we retrieve mostly useful information?

---

## Faithfulness

Faithfulness evaluates whether the generated answer is supported by the provided context.

Example:

Context:
The company was founded in 1998.

Answer:
The company was founded in 1998.

The answer is faithful.

But:

Context:
The company was founded in 1998.

Answer:
The company was founded in 1998 in Munich.

The claim about Munich is not supported by the context.

The answer may therefore have low faithfulness despite sounding plausible.

---

## Groundedness

Groundedness is closely related to faithfulness.

It measures whether claims in the generated answer are grounded in the available evidence.

A useful conceptual model is:

Generated Answer
       │
       ▼
Extract Claims
       │
       ▼
Check Claims Against Context
       │
       ▼
Supported / Unsupported

For example:

Answer:

1. Company X was founded in 1998.   ✓
2. It was founded in Munich.        ✗
3. It has 5,000 employees.          ✓

A claim-level groundedness metric can therefore be more informative than simply evaluating the entire answer.

---

## Answer Correctness

Answer correctness evaluates whether the final answer actually answers the question correctly.

It can be assessed using:

Question
   +
Reference answer
   +
Generated answer

or, depending on the application:

Question
   +
Evidence / Context
   +
Generated answer

Correctness is broader than semantic similarity.

For example:

Reference:
The product was launched in 2020.

Prediction:
The product was launched in 2021.

The wording is perfectly clear and relevant, but the answer is factually incorrect.

---

#€ Answer Relevance

Answer relevance measures whether the response actually addresses the user's question.

Example:

Question:
What is the refund period?

Answer:
The company was founded in 1998 and currently has 500 employees.

The answer may be factually correct but completely irrelevant.

Therefore:

Correct ≠ Relevant

A good evaluation framework should measure both.

---

## Completeness

An answer can be correct but incomplete.

Example:

Question:
What are the three steps required to terminate the contract?

Answer:
You need to send written notice.

The answer contains correct information but omits two required steps.

Completeness therefore measures whether the answer covers all important aspects of the question.

---

## Citation Correctness

For RAG and research-oriented applications, citations can be evaluated separately.

Important questions include:

1. Does the citation actually support the claim?
2. Is the citation attached to the correct claim?
3. Is the cited source relevant?
4. Are important claims missing citations?

Example:

Claim:
Company X was founded in 1998.

Citation:
Document A

Document A:
"Company X was founded in 1998."

→ Citation supported

Whereas:

Claim:
Company X was founded in Munich.

Citation:
Document A

Document A:
"Company X was founded in 1998."

→ Citation does not support the claim

Citation correctness is particularly important for enterprise RAG and research applications.

---

## Safety Metrics

LLM evaluation can also include safety-related metrics.

Depending on the application, these may include:

- Harmful content rate
- Toxicity rate
- Refusal correctness
- Prompt injection resistance
- Sensitive information leakage
- Policy violation rate

For example, a system may be tested with a set of adversarial prompts:

100 safety test cases
        │
        ▼
       LLM
        │
        ▼
Correctly handled: 97
Incorrectly handled: 3

Safety pass rate = 97%

Safety metrics should be defined specifically for the risks relevant to the application.

---

## Task-Specific Metrics

Not every LLM application should use the same metrics.

For example:

Application| Important Metrics
RAG chatbot| Faithfulness, context recall, context precision, answer correctness
Enterprise search| Recall@K, Precision@K, NDCG, MRR
Summarization| Completeness, factual correctness, semantic similarity
Information extraction| Exact Match, precision, recall, F1
Code generation| Test pass rate, correctness, security
Classification| Accuracy, precision, recall, F1
Agentic system| Task success rate, tool-call correctness, execution success
Customer support| Correctness, relevance, completeness, safety
Research assistant| Correctness, groundedness, citation correctness

These metrics should be selected based on the actual requirements of the application.

---

## Composite Quality Metrics

Sometimes several dimensions are combined into an overall score.

For example:

Overall Quality
    =
0.40 × Correctness
+ 0.25 × Faithfulness
+ 0.20 × Relevance
+ 0.15 × Completeness

However, composite scores should be used carefully.

A single number can hide important failures.

For example:

Overall score = 0.92

might conceal:

Correctness   = 0.97
Faithfulness  = 0.99
Safety        = 0.70

If safety is critical, averaging these metrics may be inappropriate.

For critical dimensions, hard thresholds can be preferable to weighted averages.

---

## Threshold-Based Evaluation

Instead of optimizing a single score, quality requirements can be defined as minimum thresholds.

Example:

Requirements:

Faithfulness       ≥ 0.95
Answer correctness ≥ 0.90
Context recall     ≥ 0.90
Safety pass rate   = 100%

A system passes only if all critical requirements are satisfied.

This is particularly useful for production systems.

---

## Evaluation Datasets

Quality metrics require a suitable evaluation dataset.

A typical LLM evaluation dataset contains:

Input
Expected behavior
Reference answer / context
Metadata
Evaluation criteria

For RAG:

Question
Relevant documents
Reference answer
Expected citations

The dataset should contain realistic examples as well as important edge cases.

---

## Golden Datasets

A Golden Dataset is a curated and stable set of high-quality evaluation examples.

It can be used to compare different versions of an LLM application.

Golden Dataset v1
        │
        ├── Model v1 → Metrics
        │
        ├── Model v2 → Metrics
        │
        └── Model v3 → Metrics

This allows teams to detect regressions when changing:

- LLMs
- Prompts
- Retrieval models
- Chunking strategies
- Embedding models
- Rerankers
- System instructions

---

## Error Analysis

Metrics alone are not sufficient.

Suppose:

Faithfulness = 94%

This tells us that approximately 6% of evaluated cases have a problem, but not why.

Error analysis investigates the individual failures.

For example:

100 evaluation cases
       │
       ▼
6 failures
       │
       ├── 2 retrieval failures
       ├── 2 hallucinations
       ├── 1 incomplete answer
       └── 1 instruction-following failure

This provides much more actionable information than the aggregate metric alone.

---

## Evaluation by Subgroup

Aggregate metrics can hide problems in specific categories.

For example:

Overall faithfulness: 95%

By document type:

Policies:       99%
Contracts:      97%
Technical docs: 96%
Scanned PDFs:   81%

The overall metric looks strong, but the system performs substantially worse on scanned PDFs.

Evaluation should therefore often be segmented by relevant dimensions such as:

- Query type
- Document type
- Language
- User group
- Difficulty
- Topic
- Data source

---

## Regression Testing

LLM applications should be evaluated whenever an important component changes.

For example:

Prompt changed
      │
      ▼
Run evaluation suite
      │
      ▼
Calculate metrics
      │
      ▼
Compare against baseline
      │
      ▼
Pass / Fail

A regression test might require:

Faithfulness       ≥ 0.95
Answer correctness ≥ 0.90
Safety             = 100%

This prevents changes that improve one aspect of the system from silently degrading another.

---

## Evaluation in CI/CD

LLM evaluation can become part of the software development lifecycle.

Code / Prompt Change
        │
        ▼
Build
        │
        ▼
Evaluation Dataset
        │
        ▼
LLM Evaluation
        │
        ▼
Quality Metrics
        │
        ▼
Threshold Check
        │
   ┌────┴────┐
   │         │
 PASS       FAIL
   │         │
Deploy     Reject

This makes LLM quality a measurable engineering property rather than something checked manually before release.

---

## Metric Limitations

Every LLM quality metric has limitations.

For example:

Metric| Typical Limitation
Exact Match| Too strict for natural language
BLEU| Mostly lexical overlap
ROUGE| Does not directly measure factual correctness
Semantic similarity| Similarity does not guarantee correctness
LLM-as-a-Judge| Judge bias and instability
Faithfulness| Requires reliable evidence/context
Context recall| Depends on reference information
Context precision| Requires relevance judgments
Human evaluation| Expensive and slower
Composite score| Can hide critical failures

Therefore:

«Metrics should be treated as measurement instruments, not as perfect representations of quality.»

---

## Designing an LLM Evaluation Framework

A practical evaluation framework can follow these steps:

1. Define the task
        │
        ▼
2. Define quality dimensions
        │
        ▼
3. Create evaluation dataset
        │
        ▼
4. Select metrics
        │
        ▼
5. Establish baseline
        │
        ▼
6. Evaluate system
        │
        ▼
7. Analyze failures
        │
        ▼
8. Define thresholds
        │
        ▼
9. Automate regression testing
        │
        ▼
10. Monitor production

The most important step is usually defining what "good" means before selecting the metric.

---

Example: Evaluating a RAG System

Consider an enterprise chatbot answering questions about internal documents.

A useful evaluation setup could be:

                    RAG Evaluation
                         │
          ┌──────────────┴──────────────┐
          │                             │
      Retrieval                     Generation
          │                             │
          ▼                             ▼
  Context Recall                 Faithfulness
  Context Precision              Correctness
  Context Relevance              Relevance
                                  Completeness
                                  Citation correctness

For example:

Evaluation Dataset: 500 questions

Context Recall:       0.94
Context Precision:    0.88
Faithfulness:         0.96
Answer Correctness:   0.91
Answer Relevance:     0.95

The metrics can then be compared against a previous system version:

                    v1       v2

Context Recall      0.91     0.94
Context Precision   0.92     0.88
Faithfulness        0.94     0.96
Correctness         0.89     0.91

This reveals an important trade-off:

Retrieval recall ↑
Retrieval precision ↓

The new system retrieves more relevant information but also introduces more irrelevant context.

Looking only at answer correctness would hide this retrieval regression.

---

## A Good Evaluation Strategy

A robust LLM evaluation system typically combines several layers:

                  LLM Evaluation
                        │
        ┌───────────────┼────────────────┐
        │               │                │
     Automated       LLM Judge         Human
      Metrics        Evaluation       Evaluation
        │               │                │
        └───────────────┼────────────────┘
                        │
                        ▼
                  Error Analysis
                        │
                        ▼
                  Quality Decision

A practical combination might be:

Automated

- Exact Match
- Precision / Recall / F1
- Recall@K
- NDCG
- Semantic similarity

LLM-based

- Correctness
- Relevance
- Completeness
- Faithfulness
- Instruction following

Human

- Expert correctness
- Subjective quality
- Safety
- Validation of automated metrics

---

Key Takeaway

«LLM quality cannot usually be represented by a single metric. A good evaluation framework measures the specific dimensions that matter for the application and combines automated metrics, model-based evaluation, and human validation where appropriate.»

For a typical RAG application, the most important distinction is:

                 RAG Quality
                     │
          ┌──────────┴──────────┐
          │                     │
      Retrieval              Generation
          │                     │
          ▼                     ▼
 Context Recall          Answer Correctness
 Context Precision       Faithfulness
 Context Relevance       Relevance
                         Completeness
                         Citation Correctness

The goal is not simply to maximize one score.

The goal is to establish measurable quality requirements, detect regressions, understand failure modes, and continuously improve the complete LLM system.