# Profiling

## TL;DR (30 seconds)

**Profiling** measures how a program uses **time, CPU, memory, and other resources** to identify performance bottlenecks.

```text
Application
     │
     ▼
  Profiler
     │
     ├── Execution time
     ├── CPU usage
     └── Memory usage
          │
          ▼
   Find bottlenecks
          │
          ▼
      Optimize
```

---

## 1. CPU Profiling

CPU profiling measures how much time is spent in different parts of a program.

Python provides the built-in `cProfile`:

```bash
python -m cProfile script.py
```

It reports metrics such as:

* **`ncalls`** – number of calls
* **`tottime`** – time spent inside the function
* **`cumtime`** – time including called functions

---

## 2. Line Profiling

**Line profiling** measures execution time for individual lines of code.

This is useful when a function is known to be slow but the specific bottleneck is unclear.

A common tool is `line_profiler`.

---

## 3. Memory Profiling

Memory profiling identifies where a program consumes or allocates memory.

This is particularly useful for:

* large datasets
* pandas DataFrames
* NumPy arrays
* ML models
* large batches

A common tool is `memory_profiler`.

---

## 4. Sampling Profilers

A **sampling profiler** periodically observes what the program is executing.

```text
Program running
│
├── sample → function A
├── sample → function A
├── sample → function B
├── sample → function A
└── sample → function A

A ≈ 80% of observed execution
B ≈ 20%
```

Sampling profilers generally have lower overhead than detailed tracing.

Examples include **py-spy** and **Scalene**.

---

## 5. Profiling ML Workloads

Profiling is useful for analyzing:

* data loading
* preprocessing
* feature engineering
* model inference
* CPU/GPU usage
* memory consumption

For PyTorch, `torch.profiler` can profile CPU and GPU operations:

```python
with torch.profiler.profile(
    activities=[
        torch.profiler.ProfilerActivity.CPU,
        torch.profiler.ProfilerActivity.CUDA,
    ]
) as prof:
    model(input_data)
```

---

## 6. Profiling vs Monitoring

**Profiling** is typically used to investigate performance problems.

**Monitoring** continuously observes a running system.

```text
Profiling                  Monitoring
    │                          │
    ▼                          ▼
Find bottleneck          Observe production
    │                          │
    ▼                          ▼
Optimize                  Detect problems
```

For example:

* **Profiling:** Why does this function take 800 ms?
* **Monitoring:** What is the current p95 latency?

---

## Key Takeaways

1. **Profiling** identifies performance bottlenecks.
2. **CPU profiling** finds expensive functions and operations.
3. **Line profiling** identifies expensive lines of code.
4. **Memory profiling** identifies memory-intensive code.
5. **Sampling profilers** provide low-overhead performance analysis.
6. Profiling is especially useful for **data pipelines and ML workloads**.
7. A typical workflow is **profile → identify bottleneck → optimize**.
