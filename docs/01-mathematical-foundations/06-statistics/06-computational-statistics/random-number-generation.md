# Random Number Generation

## TL;DR

**Random number generation** is the process of producing values that behave unpredictably or statistically like random samples.

There are two fundamentally different approaches:

```text
Random Number Generation
        │
        ├── True Randomness
        │      └── Physical processes
        │
        └── Pseudo-Randomness
               └── Deterministic algorithms
```

---

## True Random Numbers

**True random number generators (TRNGs)** use physical processes that are considered inherently unpredictable.

Examples include:

* Thermal noise
* Electronic noise
* Radioactive decay
* Quantum phenomena

The physical process is measured and converted into random bits:

```text
Physical Process
      │
      ▼
Measurement
      │
      ▼
Random Bits
```

True randomness is useful for applications such as cryptography.

---

## Pseudo-Random Numbers

Most computer programs use a **Pseudo-Random Number Generator (PRNG)**.

A PRNG is deterministic:

$$
x_{n+1}=f(x_n)
$$

The initial state $x_0$ determines the complete sequence.

```text
Initial State
     │
     ▼
    PRNG
     │
     ├── x₁
     ├── x₂
     ├── x₃
     └── ...
```

The numbers are called *pseudo-random* because they are generated deterministically but are designed to have properties similar to random numbers.

---

## Linear Congruential Generator

A simple PRNG is the **Linear Congruential Generator (LCG)**:

$$
x_{n+1}=(ax_n+c)\bmod m
$$

where:

* $x_n$ is the current state
* $a$ is the multiplier
* $c$ is the increment
* $m$ is the modulus

The state can be converted to a number in $[0,1)$:

$$
u_n=\frac{x_n}{m}
$$

For example:

$$
x_0=7,\quad a=5,\quad c=3,\quad m=16
$$

gives:

$$
7\rightarrow6\rightarrow1\rightarrow8\rightarrow11\rightarrow\dots
$$

The sequence is deterministic.

---

## Period

A PRNG has a finite internal state space.

Eventually, a state must repeat:

$$
x_i=x_j
$$

After this happens, the sequence repeats:

$$
x_{i+k}=x_{j+k}
$$

The number of generated values before repetition is called the **period**.

Modern PRNGs are designed to have very long periods.

---

## Seed

The **seed** determines the initial state of a PRNG:

$$
x_0=\text{seed}
$$

Therefore:

$$
\text{Same Seed}
\Rightarrow
\text{Same Sequence}
$$

This is important for reproducible simulations and machine learning experiments.

---

## Uniform Random Numbers

A common goal is to generate values uniformly distributed in an interval.

For:

$$
U\sim\operatorname{Uniform}(0,1)
$$

every subinterval of equal length has the same probability.

For example:

$$
P(0.2\leq U<0.3)=0.1
$$

A uniform random number can then be transformed into other distributions.

---

## Sampling from Other Distributions

Random numbers from a uniform distribution can be transformed into samples from other probability distributions.

For example, the **inverse transform method** uses the cumulative distribution function $F$:

$$
U\sim\operatorname{Uniform}(0,1)
$$

and

$$
X=F^{-1}(U)
$$

Then $X$ follows the desired distribution.

For an exponential distribution with rate $\lambda$:

$$
X=-\frac{1}{\lambda}\ln(1-U)
$$

---

## Random Number Generation in Machine Learning

Random numbers are used extensively in ML:

```text
Random Number Generation
          │
          ├── Weight Initialization
          ├── Data Shuffling
          ├── Sampling
          ├── Train/Test Splitting
          ├── Dropout
          └── Data Augmentation
```

For example:

```python
import numpy as np

rng = np.random.default_rng(42)

x = rng.random(5)
```

The seed makes the generated sequence reproducible.

---

## Cryptographic Randomness

Ordinary PRNGs are not necessarily suitable for security.

Cryptographic applications require **cryptographically secure pseudo-random number generators (CSPRNGs)**.

A CSPRNG is designed so that observing generated values does not allow an attacker to feasibly predict future values.

```text
PRNG
└── General simulations, ML, numerical computing

CSPRNG
└── Cryptography, tokens, keys, security
```

---

## Key Idea

Random number generation usually does not mean that a computer creates fundamentally random numbers.

For most numerical applications, a deterministic algorithm produces **pseudo-random numbers** with desirable statistical properties:

$$
\boxed{
\text{Seed}
\rightarrow
\text{PRNG}
\rightarrow
\text{Uniform Samples}
\rightarrow
\text{Other Distributions}
}
$$

True random number generators instead obtain randomness from physical processes.
