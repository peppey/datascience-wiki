# Audio Classification

## TL;DR

**Audio classification** assigns an audio signal to one or more predefined classes.

Examples include:

* Speech vs. music
* Speaker identification
* Environmental sound classification
* Emotion recognition
* Machine fault detection from sound

Common approaches include working with the **raw waveform**, transforming audio into **time-frequency representations**, using **hand-crafted features with classical ML**, or using **pretrained audio models**.

## Common Approaches

### Classification on Raw Audio

The model receives the audio waveform directly:

$$
x(t) \rightarrow \text{model} \rightarrow y
$$

Deep learning models can learn useful representations directly from the waveform.

Common approaches include:

* 1D CNNs
* Temporal convolutional networks
* Transformers
* Self-supervised audio models

Examples of pretrained models include Wav2Vec 2.0 and HuBERT.

### Spectrogram-Based Classification

A common approach is to transform the audio signal into a **time-frequency representation**, such as a spectrogram or Mel spectrogram.

For example:

$$
\text{Audio}
\rightarrow
\text{STFT}
\rightarrow
\text{Spectrogram}
\rightarrow
\text{Classifier}
$$

Common representations include:

* Spectrograms
* Mel spectrograms
* Log-Mel spectrograms
* MFCCs

Spectrograms can be interpreted as images:

* $x$-axis = time
* $y$-axis = frequency
* intensity = signal energy

This makes it possible to treat audio classification partly as a **computer vision problem** and apply image-based architectures such as 2D CNNs.

A typical pipeline is:

$$
\text{Audio}
\rightarrow
\text{Mel Spectrogram}
\rightarrow
\text{2D CNN}
\rightarrow
\text{Class}
$$

### Feature Extraction + Classical ML

Instead of training a deep neural network, manually designed audio features can be extracted first.

Typical features include:

* MFCCs
* Spectral centroid
* Spectral bandwidth
* Spectral contrast
* Zero-crossing rate
* Chroma features

The resulting feature vector can then be used with classical ML models:

$$
\text{Audio}
\rightarrow
\text{Features}
\rightarrow
\text{ML Model}
\rightarrow
\text{Class}
$$

Common models include:

* Logistic Regression
* SVM
* Random Forest
* Gradient Boosting

### Pretrained Audio Embeddings

A pretrained audio model can be used as a **feature extractor**:

$$
\text{Audio}
\rightarrow
\text{Pretrained Encoder}
\rightarrow
\text{Embedding}
\rightarrow
\text{Classifier}
$$

The extracted embedding can then be classified using a simple model or a neural network.

This is useful when the available labeled dataset is relatively small.

### Transfer Learning

A pretrained audio model can be fine-tuned on the target classification task:

$$
\text{Pretrained Audio Model}
\rightarrow
\text{Fine-tuning}
\rightarrow
\text{Audio Classifier}
$$

This can reduce the amount of labeled data required compared with training a model from scratch.

## Problem Variants

Audio classification can use different classification settings:

* **Binary classification** — two classes
* **Multiclass classification** — exactly one class among several
* **Multilabel classification** — multiple classes can be present simultaneously

For example, an environmental recording could contain:

$$
{\text{car},\text{speech},\text{rain}}
$$

which makes it a multilabel classification problem.

## Typical Pipeline

```text
Audio
  │
  ▼
Preprocessing
  │
  ├── Resampling
  ├── Normalization
  └── Segmentation
  │
  ▼
Representation
  │
  ├── Raw waveform
  ├── Spectrogram
  ├── Mel spectrogram
  └── Audio features
  │
  ▼
Model
  │
  ├── CNN
  ├── Transformer
  ├── SVM
  └── Random Forest
  │
  ▼
Class
```

## Key Idea

Audio classification can be approached directly on the waveform or by transforming the audio into a more useful representation.

A particularly common strategy is to use **spectrograms**, which allow audio to be processed with architectures originally developed for computer vision.
