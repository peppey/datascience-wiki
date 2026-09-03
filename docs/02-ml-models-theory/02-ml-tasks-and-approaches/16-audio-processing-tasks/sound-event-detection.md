# Sound Event Detection

## TL;DR

**Sound Event Detection (SED)** identifies **which sound events occur and when they occur** in an audio signal.

Unlike **audio classification**, which typically assigns a label to an entire audio recording, SED produces **time-localized events**.

Example:

```text
Audio
│
├── 0–2 s:   silence
├── 2–4 s:   dog barking
├── 4–6 s:   speech
└── 6–8 s:   dog barking
```

The output can therefore be represented as:

```text
Event          Start      End
dog_bark       2.0 s      4.0 s
speech         4.0 s      6.0 s
dog_bark       6.0 s      8.0 s
```

---

## Problem Formulation

Given an audio signal

$$
x(t),
$$

the goal is to detect events

$$
e_i = (c_i, t_i^{start}, t_i^{end}),
$$

where:

* $c_i$ is the event class,
* $t_i^{start}$ is the start time,
* $t_i^{end}$ is the end time.

Multiple events can occur simultaneously.

Therefore, SED is often a **multi-label, temporal detection problem**.

---

## Common Approaches

### Frame-Level Classification

The audio is divided into short frames:

```text
Audio
│
├── Frame 1 ──→ classifier
├── Frame 2 ──→ classifier
├── Frame 3 ──→ classifier
└── ...
```

Each frame receives one or more event probabilities.

For example:

```text
Time     Dog    Speech    Car
0–1 s    0.01   0.02      0.01
1–2 s    0.85   0.03      0.02
2–3 s    0.92   0.04      0.01
3–4 s    0.10   0.80      0.05
```

Thresholding and post-processing can then turn frame-level predictions into event intervals.

---

### Spectrogram + Neural Network

The audio can be transformed into a **spectrogram** or **mel-spectrogram**.

This converts the problem into a representation similar to an image:

```text
Audio
  │
  ▼
Spectrogram
  │
  ▼
Neural Network
  │
  ▼
Time-localized predictions
```

Common architectures include:

* CNNs
* CRNNs
* Transformers

A CNN can learn local time-frequency patterns, while recurrent or attention-based layers can model temporal context.

---

### Sequence Models

SED is naturally a **sequence prediction problem**.

Models can process a sequence of acoustic features and predict events over time.

Common approaches include:

* RNNs
* LSTMs
* GRUs
* Transformers

These models can capture temporal dependencies such as:

```text
sound onset → sound continues → sound stops
```

---

## Weakly Labeled Data

A common challenge is that precise start and end times are expensive to annotate.

Instead of:

```text
dog barking: 12.3–15.7 s
```

the training data may only contain:

```text
dog barking: present
```

for the entire recording.

This leads to **weakly supervised SED**, where the model must learn temporal localization from recording-level labels.

---

## Evaluation

SED evaluation considers both:

1. **What event was detected?**
2. **When was it detected?**

Typical metrics include:

* Event-based precision and recall
* Event-based F1-score
* Segment-based F1-score
* Error rate

Temporal overlap between predicted and reference events is usually taken into account.

---

## Audio Classification vs. Sound Event Detection

| Task                      | Output                               |
| ------------------------- | ------------------------------------ |
| Audio Classification      | Labels for an entire recording       |
| Sound Event Detection     | Labels + temporal locations          |
| Audio Tagging             | Events present in an audio recording |
| Sound Source Localization | Spatial location of sound sources    |

For example:

**Audio Classification**

```text
Audio → "dog barking"
```

**Sound Event Detection**

```text
2.1–4.3 s → "dog barking"
7.0–8.2 s → "dog barking"
```

---

## Key Idea

Sound Event Detection extends audio classification with **temporal localization**:

$$
\text{SED}
=

\text{classification}
+
\text{temporal localization}.
$$
