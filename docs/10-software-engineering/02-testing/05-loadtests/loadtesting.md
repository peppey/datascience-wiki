# Load Testing

## TL;DR

**Load testing** evaluates how a system behaves under a specified amount of expected or increasing **load**.

The main goals are to determine:

* whether the system can handle the expected number of users or requests
* how **response time** changes under load
* the maximum sustainable **throughput**
* whether resources such as CPU, memory or database connections become bottlenecks
* whether the system remains stable under sustained load

A typical load test gradually sends requests to a system while measuring metrics such as:

$$
\boxed{
\text{Load}
\rightarrow
\text{Requests}
\rightarrow
\text{System Metrics}
\rightarrow
\text{Performance Analysis}
}
$$

---

## What Is Load Testing?

Load testing is a type of **performance testing** in which a system is exposed to a predefined workload.

For example, an API might normally receive:

$$
100 \text{ requests/second}
$$

A load test can simulate this traffic and measure whether the API satisfies its performance requirements.

Typical requirements could be:

* response time $< 200,\text{ms}$
* throughput $\geq 100$ requests/second
* error rate $< 1%$
* CPU utilization $< 80%$

The objective is not necessarily to break the system, but to determine whether it performs adequately under realistic conditions.

---

## Load

The **load** describes the work imposed on the system.

Depending on the application, load can be expressed as:

* concurrent users
* requests per second
* transactions per second
* messages per second
* data volume
* concurrent jobs

For an HTTP API, a common measure is:

$$
\text{Throughput}
=

\frac{\text{Number of Requests}}{\text{Time}}
$$

For example:

$$
\frac{10,000\text{ requests}}{100\text{ s}}
=

100\text{ requests/s}
$$

---

## Important Metrics

### Response Time

The time required to process a request.

Instead of only considering the average, percentiles are commonly used:

* **p50** — median response time
* **p95** — 95% of requests are faster than this value
* **p99** — 99% of requests are faster than this value

For example:

$$
p95 = 180,\text{ms}
$$

means that 95% of requests completed within 180 ms.

---

### Throughput

Throughput measures how much work the system can process per unit of time.

For an API:

$$
\text{Throughput} =
\text{requests per second}
$$

A system might initially scale approximately linearly with increasing load, but eventually reach a bottleneck where additional load primarily increases response times.

---

### Error Rate

The proportion of requests that fail:

$$
\text{Error Rate}
=

\frac{\text{Failed Requests}}
{\text{Total Requests}}
$$

A system may therefore appear fast while still being unable to handle the workload if many requests fail.

---

### Resource Utilization

Load tests should also monitor infrastructure resources such as:

* CPU
* memory
* network bandwidth
* disk I/O
* database connections
* connection pools
* GPU utilization

This helps identify the component responsible for performance degradation.

---

## Typical Load Test

A load test often follows several phases:

### 1. Baseline

Measure the system with little or no load.

This provides a reference for later measurements.

### 2. Ramp-Up

Gradually increase the load.

For example:

$$
10
\rightarrow
50
\rightarrow
100
\rightarrow
200
\text{ requests/s}
$$

### 3. Sustained Load

Maintain the target load for a defined period.

This tests whether the system can operate reliably under normal expected conditions.

### 4. Analysis

Compare the observed metrics with the system's requirements.

---

## Load Testing vs. Stress Testing

These concepts are related but have different goals.

| Test                  | Goal                                                  |
| --------------------- | ----------------------------------------------------- |
| **Load Testing**      | Test expected or specified workloads                  |
| **Stress Testing**    | Exceed normal capacity and determine system limits    |
| **Spike Testing**     | Test sudden increases or decreases in load            |
| **Endurance Testing** | Test stability over a long period                     |
| **Capacity Testing**  | Determine the maximum workload the system can support |

Load testing therefore usually focuses on **realistic expected load**, while stress testing intentionally pushes the system beyond its expected capacity.

---

## Example

Suppose an inference API is expected to support:

$$
100 \text{ requests/s}
$$

with a maximum p95 latency of:

$$
200,\text{ms}
$$

A load test could gradually increase traffic:

```text
10 req/s
    ↓
25 req/s
    ↓
50 req/s
    ↓
75 req/s
    ↓
100 req/s
```

At each stage, response times, errors and resource utilization are measured.

A result could look like:

|      Load | p95 latency | Error rate |
| --------: | ----------: | ---------: |
|  25 req/s |       80 ms |         0% |
|  50 req/s |       95 ms |         0% |
|  75 req/s |      130 ms |         0% |
| 100 req/s |      185 ms |       0.1% |
| 125 req/s |      420 ms |       4.2% |

The system satisfies the specified requirement at **100 requests/s**, but performance deteriorates significantly above this level.

---

## Bottlenecks

Load testing can reveal bottlenecks in different parts of a system.

For example:

```text
Client
  ↓
API
  ↓
Application
  ↓
Database
  ↓
External Service
```

A database with insufficient connection capacity might cause increasing response times even though the application itself has sufficient CPU and memory.

Therefore, load testing should ideally be combined with **monitoring** to identify the source of performance degradation.

---

## Tools

Common tools for load testing include:

* **k6**
* **JMeter**
* **Locust**
* **Gatling**
* **Apache Bench (ab)**

The tool generates the workload while application and infrastructure monitoring systems collect performance metrics.

---

## Key Idea

Load testing answers the question:

> **Can the system handle the workload it is expected to receive while satisfying its performance requirements?**

The important relationship is:

$$
\boxed{
\text{Load}
\rightarrow
\text{System Behavior}
\rightarrow
\text{Performance Metrics}
\rightarrow
\text{Capacity}
}
$$

A good load test therefore does not only measure how fast a system is under light load. It determines **how performance changes as the workload increases** and where the system's practical capacity lies.
