# Source Separation

## TL;DR

**Source separation** separates a mixed audio signal into its underlying sound sources.

For example:

```text
Mixed Audio
     │
     ▼
Source Separation
     │
 ┌───┼────────┐
 ▼   ▼        ▼
Speech  Music  Noise
```

The goal is to estimate the individual sources from their mixture.

---

## Problem Formulation

A recorded signal can often be modeled as a mixture of several sources:

$$
x(t) = \sum_{i=1}^{N} s_i(t),
$$

where:

* $x(t)$ is the observed mixture,
* $s_i(t)$ are the individual sources.

The task is to estimate:

$$
\hat{s}_1(t), \hat{s}_2(t), \ldots, \hat{s}_N(t)
$$

from only the mixture $x(t)$.

---

## Common Approaches

### 1. Spectrogram-Based Separation

The audio is transformed into a time-frequency representation such as a spectrogram or mel-spectrogram.

```text
Audio
  │
  ▼
STFT
  │
  ▼
Spectrogram
  │
  ▼
Separation Model
  │
  ├──→ Source 1
  ├──→ Source 2
  └──→ Source 3
```

A model can learn to determine which parts of the spectrogram belong to each source.

Common techniques include **time-frequency masks**:

$$
\hat{S}_i(f,t) = M_i(f,t)X(f,t),
$$

where $M_i$ is a learned mask for source $i$.

---

### 2. Waveform-Based Separation

Instead of operating on spectrograms, neural networks can work directly on the audio waveform.

```text
Mixed Waveform
      │
      ▼
Neural Network
      │
 ┌────┼────┐
 ▼    ▼    ▼
Speech Music Noise
```

This avoids explicitly constructing a spectrogram.

Common architectures include:

* CNNs
* Temporal convolutional networks
* Transformers

---

### 3. Deep Learning

Modern source separation is often formulated as a supervised learning problem.

During training, the model receives mixtures together with their corresponding sources:

```text
Source 1 ──┐
           ├──→ Mixture ──→ Model ──→ Estimated sources
Source 2 ──┘
```

The model learns to minimize a separation loss between the estimated and true sources.

---

## Applications

Source separation is used for:

* **Speech enhancement**
* **Noise reduction**
* **Music source separation**
* **Speaker separation**
* **Meeting transcription**
* **Karaoke / vocal removal**
* **Audio preprocessing**

For example, a music recording can be separated into:

```text
Mixture
  │
  ├──→ Vocals
  ├──→ Drums
  ├──→ Bass
  └──→ Other instruments
```

---

## Blind Source Separation

In **blind source separation (BSS)**, the individual sources are not directly known during separation.

A classical example is the **cocktail party problem**:

> Several people speak simultaneously, and the goal is to recover the individual speakers from microphone recordings.

Classical approaches include:

* Independent Component Analysis (ICA)
* Non-negative Matrix Factorization (NMF)

Modern approaches often use neural networks.

---

## Key Idea

Source separation attempts to solve:

$$
\text{mixture}
\rightarrow
\text{individual sources}.
$$

It is therefore fundamentally different from **audio classification**, where the goal is only to identify what is present, and **sound event detection**, where the goal is to determine what occurs and when.
