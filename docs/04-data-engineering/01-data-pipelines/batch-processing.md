# Batch Processing

## TL;DR

**Batch Processing** processes data in **groups (batches)** instead of processing each record individually or continuously.

For example, instead of processing 1 million records one by one:

$$
\text{Data}
\rightarrow
\boxed{\text{Batch 1}}
\rightarrow
\boxed{\text{Batch 2}}
\rightarrow
\boxed{\text{Batch 3}}
\rightarrow
\ldots
$$

Batch processing is commonly used in **ETL pipelines**, data engineering, and large-scale data processing.

---

## Basic Workflow

A typical batch pipeline looks like:

$$
\boxed{
\text{Read}
\rightarrow
\text{Process}
\rightarrow
\text{Write}
}
$$

For example:

```text
Input Data
    ↓
Split into batches
    ↓
Batch 1 → Transform → Load
Batch 2 → Transform → Load
Batch 3 → Transform → Load
```

Batches can often be processed independently and in parallel.

---

## Batch Size

The **batch size** determines how many records are processed at once.

A larger batch:

* reduces overhead
* can improve throughput
* requires more memory

A smaller batch:

* uses less memory
* allows finer-grained error handling
* may increase processing overhead

The optimal batch size depends on the data and processing system.

---

## Error Handling

A major advantage of batching is that **an error in one batch does not necessarily require the entire pipeline to fail**.

For example:

```text
Batch 1 → ✓
Batch 2 → ✓
Batch 3 → ✗
Batch 4 → ✓
```

The failed batch can be:

* retried
* logged
* written to a separate error location
* skipped while processing continues

For example:

$$
\text{Batch}
\rightarrow
\begin{cases}
\text{Success} &\rightarrow \text{Load}\
\text{Failure} &\rightarrow \text{Retry / Error Handling}
\end{cases}
$$

It is useful to store information such as:

* batch ID
* processing status
* error message
* timestamp
* number of records

This makes failed batches **reproducible and retryable**.

---

## Idempotency

Batch processing should ideally be **idempotent**.

Processing the same batch twice should not create duplicate or inconsistent results.

For example, instead of blindly inserting records:

```text
Batch 42 → INSERT
Batch 42 → INSERT again
```

the pipeline can use a unique batch ID or an upsert mechanism.

This is especially important when a batch is automatically retried after a failure.

---

## Parallel Processing

Independent batches can often be processed concurrently:

```text
              ┌→ Batch 1 → Process ─┐
Input Data ───┼→ Batch 2 → Process ─┼→ Output
              └→ Batch 3 → Process ─┘
```

This can significantly increase throughput.

However, parallel processing requires consideration of:

* memory
* CPU
* database load
* ordering requirements
* concurrency limits

---

## Batch Processing vs. Streaming

**Batch Processing**:

* processes data periodically
* works on finite datasets
* focuses on throughput

**Stream Processing**:

* processes data continuously
* handles events as they arrive
* focuses on low latency

For example:

$$
\text{Batch:}
\quad
\text{Process every hour}
$$

$$
\text{Streaming:}
\quad
\text{Process immediately}
$$

---

## Key Takeaway

Batch processing divides large datasets into manageable units that can be processed independently.

A robust batch pipeline should support:

* appropriate batch sizes
* retries
* logging
* failure isolation
* idempotent processing
* parallel execution

The important principle is:

$$
\boxed{
\text{Process}
\rightarrow
\text{Track}
\rightarrow
\text{Retry Failed Batches}
}
$$
