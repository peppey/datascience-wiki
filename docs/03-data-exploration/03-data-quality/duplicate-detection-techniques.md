# Duplicate Detection Techniques

**Duplicate detection** is the process of identifying records, documents, or observations that represent the same underlying entity or information.

Duplicate detection is a common data-cleaning task, but "duplicate" can mean several different things.

For example:

```text
"Max Mustermann"
"Max Mustermann"
```

is an obvious exact duplicate.

But:

```text
"Max Mustermann"
"M. Mustermann"
```

may refer to the same person without being identical strings.

Similarly:

```text
"Apple iPhone 15 Pro 128GB"
"Apple iPhone 15 Pro - 128 GB"
```

may describe the same product even though the texts differ.

The appropriate duplicate-detection technique therefore depends on **what constitutes equivalence in the application**.

---

## 1. Types of Duplicates

A useful first step is to distinguish several types of duplicates.

### 1.1 Exact duplicates

Two records are exactly identical.

For example:

```text
id | name          | age
---|---------------|----
1  | Alice Smith   | 32
2  | Bob Jones     | 41
3  | Alice Smith   | 32
```

Rows 1 and 3 are exact duplicates if the complete record is considered.

These are the easiest duplicates to detect.

---

### 1.2 Duplicate records with different IDs

Two records can contain identical information but have different identifiers:

```text
customer_id | name
------------|-------------
1024        | Alice Smith
8741        | Alice Smith
```

The different IDs do not necessarily imply different people.

This situation occurs frequently after:

* merging databases
* importing data from multiple systems
* migrating databases
* repeated customer registration
* combining historical datasets

---

### 1.3 Near-duplicates

Near-duplicates differ in one or more fields but are likely to represent the same entity.

For example:

```text
Alice Smith
Alice Smyth
```

or:

```text
+49 89 123456
089 / 123456
```

The records are not identical, but they may represent the same person or organization.

---

### 1.4 Semantic duplicates

Two records may express the same meaning while sharing few literal tokens.

For example:

```text
"Car won't start"
"Vehicle fails to start"
```

Traditional string similarity may consider these relatively different.

Semantic methods such as embeddings can recognize that the two texts are closely related.

---

### 1.5 Entity duplicates

In **entity resolution**, the goal is to determine whether two records refer to the same real-world entity.

For example:

```text
Record A:
Name: Maria Schmidt
Address: Hauptstr. 12, Munich

Record B:
Name: M. Schmidt
Address: Hauptstraße 12, München
```

The task is not merely to determine whether the records are similar.

The question is:

> **Do these records refer to the same entity?**

This is also called:

* entity resolution
* record linkage
* deduplication
* identity resolution

depending on the context.

---

# 2. Exact Duplicate Detection

Exact duplicate detection should usually be the first step because it is simple, fast, and deterministic.

In pandas:

```python
duplicates = df[df.duplicated()]
```

To remove exact duplicate rows:

```python
df = df.drop_duplicates()
```

You can also define which columns determine uniqueness:

```python
df = df.drop_duplicates(
    subset=["name", "date_of_birth", "address"]
)
```

This is useful when some columns, such as database IDs or timestamps, are expected to differ.

---

## 3. Hash-Based Duplicate Detection

For large datasets, records can be represented by a hash.

For example:

```text
record
   ↓
canonical representation
   ↓
hash function
   ↓
hash value
```

Identical records produce identical hashes.

A simplified example:

```python
import hashlib

def hash_record(values):
    text = "|".join(str(value) for value in values)
    return hashlib.sha256(text.encode()).hexdigest()
```

Hashing is useful when:

* datasets are large
* exact equality is sufficient
* records need to be compared efficiently
* files or documents need to be checked for identical content

However, ordinary hashing does **not** detect near-duplicates.

A tiny change produces a completely different cryptographic hash.

---

# 4. Canonicalization

Before comparing records, it is often useful to transform equivalent representations into a common format.

This is called **canonicalization** or **normalization**.

For example:

```text
"Max Mustermann"
" max mustermann "
"MAX MUSTERMANN"
```

can be normalized to:

```text
max mustermann
```

A simple normalization function might be:

```python
def normalize_text(text):
    return " ".join(text.lower().split())
```

Depending on the application, normalization can include:

* lowercasing
* trimming whitespace
* Unicode normalization
* removing punctuation
* standardizing abbreviations
* standardizing phone numbers
* standardizing addresses
* converting units
* normalizing dates
* transliteration

Canonicalization is often one of the highest-value steps in duplicate detection.

It can turn many apparent near-duplicates into exact matches.

---

# 5. Field-Specific Normalization

Different fields require different normalization strategies.

### Names

```text
"Dr. Maria Schmidt"
"Maria Schmidt"
```

Possible transformations:

* lowercase
* remove titles
* normalize whitespace
* normalize punctuation

### Phone numbers

```text
+49 89 123456
089 123456
```

A phone-number-specific parser can convert both into a standardized representation.

### Email addresses

```text
Alice@example.com
alice@example.com
```

Case normalization may be appropriate depending on the application.

### Addresses

Addresses are considerably more difficult:

```text
Hauptstraße 12
Hauptstr. 12
Hauptstrasse 12
```

Domain-specific address normalization can be useful.

The key principle is:

> **Normalize according to the semantics of the field, not using one generic string transformation for everything.**

---

# 6. String Similarity

When normalization is not sufficient, records can be compared using string-similarity measures.

Common approaches include:

* Levenshtein distance
* Damerau-Levenshtein distance
* Jaro similarity
* Jaro-Winkler similarity
* cosine similarity
* Jaccard similarity

These methods measure different notions of similarity.

---

## 7. Levenshtein Distance

**Levenshtein distance** is the minimum number of single-character operations required to transform one string into another.

The allowed operations are:

* insertion
* deletion
* substitution

For example:

```text
kitten
sitten
```

requires one substitution:

```text
k → s
```

so the distance is:

$$
d(\text{kitten},\text{sitten})=1
$$

For:

```text
kitten
sitting
```

the distance is:

$$
d(\text{kitten},\text{sitting})=3
$$

Levenshtein distance is useful for detecting:

* typos
* spelling variations
* OCR errors
* small transcription differences

---

# 8. Jaro and Jaro-Winkler Similarity

**Jaro similarity** is particularly useful for comparing short strings such as names.

**Jaro-Winkler similarity** extends Jaro similarity by giving additional weight to common prefixes.

This can be useful for names such as:

```text
Martha
Marhta
```

or:

```text
Smith
Smit
```

These measures are often useful in record linkage because names and other short identifiers can contain small transcription errors.

---

# 9. Token-Based Similarity

Character-level similarity is not always appropriate.

Consider:

```text
"Apple iPhone 15 Pro 128 GB"
"iPhone 15 Pro Apple 128GB"
```

The strings differ in ordering even though they contain essentially the same information.

Token-based methods treat the text as a collection of tokens rather than as one character sequence.

For example:

```text
Apple iPhone 15 Pro 128 GB
```

becomes approximately:

```text
{apple, iphone, 15, pro, 128, gb}
```

This allows similarity measures to be less sensitive to word order.

---

# 10. Jaccard Similarity

Jaccard similarity compares two sets:

$$
J(A,B)
=
\frac{|A\cap B|}
{|A\cup B|}
$$

For example:

```text
A = {apple, iphone, 15, pro}
B = {apple, iphone, 15, max}
```

The intersection contains three elements:

```text
{apple, iphone, 15}
```

and the union contains five:

```text
{apple, iphone, 15, pro, max}
```

Therefore:

$$
J(A,B)=\frac{3}{5}=0.6
$$

Jaccard similarity is useful when the presence of tokens matters more than their exact order.

---

# 11. TF-IDF and Cosine Similarity

Documents or records can be represented using **TF-IDF vectors**.

The cosine similarity between two vectors is:

$$
\cos(\theta)
=
\frac{\mathbf{x}\cdot\mathbf{y}}
{\|\mathbf{x}\|\|\mathbf{y}\|}
$$

A value close to \(1\) indicates that the vectors point in similar directions.

TF-IDF plus cosine similarity can be useful for detecting textual near-duplicates.

However, it is based primarily on lexical overlap.

Two texts with different wording can therefore still have low similarity.

---

# 12. Embedding-Based Duplicate Detection

For semantic duplicate detection, records can be represented using **embeddings**.

An embedding model maps text to a vector:

```text
"Car won't start"
        ↓
[0.12, -0.44, 0.73, ...]
```

Another text:

```text
"Vehicle fails to start"
        ↓
[0.10, -0.41, 0.75, ...]
```

The vectors can then be compared using cosine similarity.

```python
similarity = cosine_similarity(
    embedding_a,
    embedding_b,
)
```

This allows duplicate detection based on **semantic similarity** rather than exact wording.

Embeddings are particularly useful for:

* documents
* product descriptions
* support tickets
* customer messages
* articles
* legal documents

However, semantic similarity is not equivalent to identity.

Two documents can be semantically similar while referring to different entities or events.

---

# 13. Exact Matching vs. Fuzzy Matching vs. Semantic Matching

These approaches solve different problems.

| Technique         | Detects                    | Typical use              |
| ----------------- | -------------------------- | ------------------------ |
| Exact matching    | identical values           | database duplicates      |
| Hashing           | identical records          | large datasets/files     |
| Canonicalization  | equivalent representations | names, addresses         |
| Edit distance     | small textual changes      | typos                    |
| Token similarity  | similar token sets         | product descriptions     |
| TF-IDF            | lexical similarity         | documents                |
| Embeddings        | semantic similarity        | text/document duplicates |
| Entity resolution | same real-world entity     | customer databases       |

A robust system often combines several of these techniques.

---

# 14. Blocking

Comparing every record with every other record can be extremely expensive.

Suppose a dataset contains \(n\) records.

Naively comparing every pair requires approximately:

$$
\frac{n(n-1)}{2}
$$

comparisons.

This is:

$$
O(n^2)
$$

For \(1,000,000\) records, this would mean roughly \(5\times10^{11}\) pairs.

This is usually impractical.

**Blocking** reduces the number of candidate pairs.

For example, instead of comparing every customer with every other customer, first restrict comparisons to records sharing:

```text
country
```

or:

```text
first letter of surname
```

or:

```text
postal code
```

Only records in the same block are then compared using more expensive similarity measures.

---

# 15. Blocking Strategies

Possible blocking keys include:

* country
* postal code
* city
* birth year
* email domain
* first letter of surname
* phonetic encoding
* normalized phone number
* product category

Multiple blocking passes can be combined.

For example:

```text
Pass 1:
same postal code

Pass 2:
same first letter of surname

Pass 3:
same email domain
```

The goal is to reduce the number of candidate pairs without excluding too many true duplicates.

There is therefore a trade-off:

```text
more restrictive blocking
        ↓
fewer comparisons
        ↓
higher risk of missing duplicates
```

---

# 16. Record Linkage

**Record linkage** attempts to determine whether two records represent the same entity.

Suppose we have:

```text
Record A
Name: Maria Schmidt
Address: Hauptstraße 12
City: Munich
```

and:

```text
Record B
Name: M. Schmidt
Address: Hauptstr. 12
City: München
```

Instead of comparing the records as one string, we can compare individual fields:

| Field   | Similarity |
| ------- | ---------: |
| Name    |       0.85 |
| Address |       0.92 |
| City    |       0.95 |

These scores can then be combined.

---

# 17. Weighted Similarity

A simple approach is a weighted similarity score:

$$
S
=
w_1s_1+
w_2s_2+
\cdots+
w_ks_k
$$

where:

* \(s_i\) is the similarity of field \(i\)
* \(w_i\) is its importance

For example:

$$
S=
0.5S_{\text{name}}
+
0.3S_{\text{address}}
+
0.2S_{\text{city}}
$$

A threshold can then be used:

```text
S ≥ 0.90 → duplicate
S < 0.70 → different
otherwise → review
```

The exact thresholds must be determined empirically.

---

# 18. Probabilistic Record Linkage

A more principled approach is **probabilistic record linkage**.

Instead of using a single deterministic threshold, the system estimates:

$$
P(\text{same entity}\mid\text{observed similarities})
$$

A classic framework is the **Fellegi-Sunter model**.

The basic idea is to compare the evidence for two hypotheses:

```text
M = records refer to the same entity
U = records refer to different entities
```

Field comparisons provide evidence for one hypothesis or the other.

This approach is useful when:

* data is noisy
* multiple fields are available
* some fields are much more informative than others
* false matches are costly

---

# 19. Classification-Based Duplicate Detection

Duplicate detection can also be formulated as a binary classification problem.

Each candidate pair becomes one training example:

```text
name_similarity
address_similarity
email_similarity
phone_similarity
...
        ↓
classifier
        ↓
duplicate / not duplicate
```

Possible models include:

* logistic regression
* decision trees
* random forests
* gradient boosting
* neural networks

The training data requires labeled pairs:

```text
pair A → duplicate
pair B → not duplicate
pair C → duplicate
```

This approach can capture complex interactions between fields.

For example, a moderately similar name combined with an identical phone number may be strong evidence of a match.

---

# 20. Threshold Selection

Duplicate detection is often not simply:

```text
similarity > 0.8
```

The threshold determines a trade-off between two types of errors.

### False positive

Two different records are incorrectly classified as duplicates.

```text
different entities → duplicate
```

### False negative

Two duplicate records are incorrectly classified as different.

```text
same entity → not duplicate
```

The relative cost of these errors depends on the application.

For example, incorrectly merging two patients may be much more serious than failing to merge two duplicate marketing records.

---

# 21. Precision and Recall

Duplicate detection can therefore be evaluated using standard classification metrics.

### Precision

$$
\text{Precision}
=
\frac{TP}{TP+FP}
$$

Of the pairs classified as duplicates, how many are actually duplicates?

### Recall

$$
\text{Recall}
=
\frac{TP}{TP+FN}
$$

Of all actual duplicate pairs, how many were detected?

### F1 score

$$
F_1
=
2
\frac{\text{Precision}\cdot\text{Recall}}
{\text{Precision}+\text{Recall}}
$$

The appropriate metric depends on the consequences of false matches and missed matches.

---

# 22. Human Review

For ambiguous cases, it can be better to involve a human rather than forcing an automatic decision.

For example:

```text
similarity < 0.60
    → different

0.60 ≤ similarity < 0.90
    → human review

similarity ≥ 0.90
    → duplicate
```

This creates a **three-way decision system**:

```text
match
non-match
possible match → review
```

Human review can also generate labeled examples that can later be used to improve the duplicate-detection model.

---

# 23. Clustering-Based Deduplication

Instead of comparing pairs independently, records can sometimes be grouped into clusters.

For example:

```text
Alice Smith
A. Smith
Alice Smyth
Bob Jones
Robert Jones
```

A clustering algorithm can group records that are sufficiently similar.

Possible approaches include:

* hierarchical clustering
* DBSCAN
* connected components on a similarity graph

For entity resolution, clustering should be used carefully.

Pairwise similarity is not necessarily transitive.

For example:

```text
A ≈ B
B ≈ C
A ≠ C
```

This can produce unexpected clusters if similarity thresholds are applied naively.

---

# 24. Duplicate Detection for Files and Documents

Duplicate detection is also useful for documents.

### Exact document duplicates

Cryptographic hashes such as SHA-256 can detect byte-for-byte identical files.

### Near-duplicate documents

Possible techniques include:

* normalized text comparison
* shingling
* MinHash
* locality-sensitive hashing
* TF-IDF similarity
* embedding similarity

These methods are useful when documents differ only slightly.

For example:

```text
Document A:
original article

Document B:
same article with formatting changes

Document C:
same article with a few sentences modified
```

Different techniques can detect different levels of similarity.

---

# 25. MinHash and Locality-Sensitive Hashing

For very large collections of documents, comparing every pair is expensive.

**MinHash** provides a compact representation of a set that can approximately preserve **Jaccard similarity**.

**Locality-sensitive hashing (LSH)** can then be used to efficiently retrieve likely similar items.

The general workflow is:

```text
documents
    ↓
tokenization / shingles
    ↓
MinHash signatures
    ↓
LSH
    ↓
candidate pairs
    ↓
exact similarity calculation
```

This is particularly useful when searching for near-duplicate documents in large collections.

---

# 26. Semantic Duplicate Detection with Embeddings

For modern NLP systems, a common architecture is:

```text
documents
    ↓
embedding model
    ↓
vector representations
    ↓
nearest-neighbor search
    ↓
similarity threshold
    ↓
candidate duplicates
```

A vector database or approximate nearest-neighbor index can make this efficient for large collections.

For example, embeddings can identify documents such as:

```text
"How do I terminate my employment contract?"

and

"What are the requirements for ending an employment relationship?"
```

as semantically similar even though they use different words.

However, semantic similarity should usually be treated as a **candidate-generation mechanism**, not as proof that two documents are duplicates.

---

# 27. A Multi-Stage Duplicate Detection Pipeline

A robust production system often combines several techniques.

For example:

```text
                    Raw records
                         │
                         ▼
                  Canonicalization
                         │
                         ▼
                  Exact matching
                         │
             ┌───────────┴───────────┐
             │                       │
        exact match             unmatched
                                     │
                                     ▼
                                  Blocking
                                     │
                                     ▼
                              Candidate pairs
                                     │
                                     ▼
                            Fuzzy / semantic
                               similarity
                                     │
                                     ▼
                              Classification
                                     │
                    ┌────────────────┼────────────────┐
                    │                │                │
                 duplicate       uncertain        different
                    │                │
                    ▼                ▼
                merge             review
```

This is generally more scalable and reliable than applying an expensive similarity measure to every possible pair.

---

# 28. Choosing a Technique

A practical decision process is:

| Situation                 | Suitable first approach            |
| ------------------------- | ---------------------------------- |
| Completely identical rows | exact matching                     |
| Identical files           | cryptographic hash                 |
| Formatting differences    | canonicalization                   |
| Typos in names            | edit distance                      |
| Similar short names       | Jaro-Winkler                       |
| Similar token sets        | Jaccard                            |
| Similar documents         | TF-IDF + cosine                    |
| Semantically similar text | embeddings                         |
| Same real-world entity    | record linkage                     |
| Millions of records       | blocking / approximate search      |
| Very high-stakes matching | probabilistic model + human review |

Often the best solution combines several of these.

---

# 29. Important Considerations

### Duplicate detection is domain-specific

What counts as a duplicate depends on the application.

For example, two orders from the same customer are not duplicates merely because they have the same customer information.

### Do not use IDs blindly

A unique database ID does not guarantee that the underlying entity is unique.

### Be careful when merging records

Automatically merging records can destroy information if two different entities are incorrectly treated as one.

### Preserve provenance

When deduplicating data, it can be useful to retain:

* original IDs
* source systems
* timestamps
* matching scores
* matching rules
* merge decisions

This makes the process auditable.

### Validate after deduplication

After merging duplicates, check whether:

* record counts are plausible
* important fields were lost
* contradictory values exist
* duplicate groups were merged correctly

---

# 30. Example: Customer Deduplication

Suppose two systems contain:

```text
System A

customer_id: 123
name: Maria Schmidt
email: maria.schmidt@example.com
phone: +49 89 123456
```

and:

```text
System B

customer_id: 9841
name: Maria Schmidt
email: maria.schmidt@example.com
phone: 089 123456
```

A possible pipeline is:

### Step 1: Normalize

```text
name  → maria schmidt
email → maria.schmidt@example.com
phone → +4989123456
```

### Step 2: Exact matching

The normalized email matches exactly.

### Step 3: Compare additional fields

The normalized phone also matches.

### Step 4: Decide

The evidence strongly suggests that both records refer to the same customer.

### Step 5: Preserve provenance

Rather than simply deleting one record, retain the relationship:

```text
canonical_customer_id: 123
source_ids: [123, 9841]
```

This makes the deduplication process traceable.

---

# 31. Common Mistakes

### Mistake 1: Using exact equality for everything

Real-world data often contains formatting differences and errors.

### Mistake 2: Using fuzzy matching without normalization

Many superficial differences can be eliminated more reliably through canonicalization.

### Mistake 3: Comparing every record with every other record

This quickly becomes computationally infeasible.

### Mistake 4: Treating similarity as identity

Two records can be very similar while representing different entities.

### Mistake 5: Using one threshold for every field

A 95% name similarity and a 95% email similarity do not necessarily have the same meaning.

### Mistake 6: Automatically merging uncertain matches

Ambiguous matches should often be reviewed rather than forced into a binary decision.

### Mistake 7: Ignoring the cost of errors

False positives and false negatives can have very different consequences.

---

# 32. Summary

Duplicate detection ranges from simple exact matching to sophisticated entity-resolution systems.

The main approaches are:

* **exact matching** for identical records
* **hashing** for identical files or records
* **canonicalization** for equivalent representations
* **edit distance** for small textual differences
* **token-based similarity** for reordered or partially overlapping text
* **TF-IDF and cosine similarity** for lexical document similarity
* **embeddings** for semantic similarity
* **blocking** for reducing the number of candidate comparisons
* **record linkage** for determining whether records represent the same entity
* **classification and probabilistic models** for combining multiple signals
* **human review** for ambiguous cases

A scalable duplicate-detection system often follows the pattern:

$$
\text{normalize}
\rightarrow
\text{exact match}
\rightarrow
\text{blocking}
\rightarrow
\text{candidate generation}
\rightarrow
\text{similarity}
\rightarrow
\text{decision}
$$

The most important principle is:

> **Duplicate detection is not simply a search for similar records. It is the definition and detection of equivalence under the semantics of a particular problem.**
