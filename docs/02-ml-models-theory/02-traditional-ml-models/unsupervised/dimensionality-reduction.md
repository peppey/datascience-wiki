# Dimensionality Reduction

## TL;DR (30 Sekunden)

**Dimensionality Reduction** beschreibt Methoden, die die Anzahl der Features eines Datensatzes reduzieren, während möglichst viele relevante Informationen erhalten bleiben.

Die zentrale Idee:

> Finde eine niedrigdimensionale Darstellung der Daten, die die wichtigsten Strukturen bewahrt.

Beispiele:

- Visualisierung hochdimensionaler Daten
- Rauschreduktion
- Beschleunigung von Machine Learning Modellen
- Feature Compression

---

**Praktische Bedeutung:**

Dimensionality Reduction erklärt:

- Warum hohe Dimensionen problematisch sind
- Wie Daten in kompakter Form dargestellt werden können
- Grundlagen von PCA und Manifold Learning
- Zusammenhang zwischen Datenrepräsentation und Modellleistung

---

# Motivation & Intuition

Moderne Datensätze haben oft sehr viele Features.

Beispiele:

- Bilder: Millionen Pixel
- Text: Tausende Dimensionen durch Embeddings
- Genomdaten: viele tausend Messwerte

---

Problem:

Viele Features enthalten:

- Redundanz
- Rauschen
- irrelevante Informationen

---

Ziel:

Aus:

$$
x\in\mathbb{R}^d
$$

wird:

$$
z\in\mathbb{R}^k
$$

mit:

$$
k<d
$$

---

Beispiel:

Ein Bild mit:

$$
10000
$$

Pixeln

wird dargestellt durch:

$$
50
$$

wichtige Komponenten.

---

# Warum ist hohe Dimension problematisch?

Dieses Problem nennt man:

**Curse of Dimensionality**

---

Mit steigender Dimension:

- werden Datenpunkte dünner verteilt
- Distanzen verlieren Bedeutung
- Modelle benötigen mehr Daten

---

Beispiel:

In 2 Dimensionen:

Daten sind relativ dicht.

---

In 1000 Dimensionen:

Datenpunkte sind weit voneinander entfernt.

---

# Ziele der Dimensionsreduktion

## 1. Kompression

Weniger Speicher und Berechnung.

---

## 2. Visualisierung

Daten mit vielen Dimensionen werden auf:

- 2D
- 3D

reduziert.

---

## 3. Rauschreduktion

Unwichtige Variationen werden entfernt.

---

## 4. Bessere Generalisierung

Weniger Features können:

- Overfitting reduzieren
- Modelle vereinfachen

---

# Lineare vs. Nichtlineare Dimensionsreduktion

Es gibt zwei große Kategorien.

---

## Lineare Methoden

Annahme:

Die wichtige Struktur liegt in einem linearen Unterraum.

Beispiele:

- PCA
- Linear Discriminant Analysis

---

## Nichtlineare Methoden

Annahme:

Daten liegen auf einer gekrümmten Struktur (Manifold).

Beispiele:

- t-SNE
- UMAP
- Autoencoder

---

# Principal Component Analysis (PCA)

Die bekannteste Methode zur Dimensionsreduktion.

Die Idee:

> Finde neue Achsen, die möglichst viel Varianz der Daten erklären.

---

Die neuen Achsen heißen:

**Principal Components**

---

Beispiel:

Originaldaten:

PCA findet die Richtung:

mit maximaler Streuung.

---

# Mathematische Idee von PCA

Gegeben:

$$
X\in\mathbb{R}^{n\times d}
$$

---

PCA sucht Richtungen:

$$
w_1,w_2,...,w_k
$$

sodass:

$$
Var(Xw_i)
$$

maximal wird.

---

Die Projektion:

$$
z=Xw
$$

liefert die neue Darstellung.

---

# Kovarianzmatrix

PCA basiert auf der Kovarianzmatrix:

$$
\Sigma=
\frac1nX^TX
$$

---

Die Eigenvektoren von:

$$
\Sigma
$$

sind die Principal Components.

---

Die Eigenwerte zeigen:

Wie viel Varianz eine Komponente erklärt.

---

# Explained Variance

Jede Hauptkomponente erklärt einen Anteil der Information.

Beispiel:

| Komponente | erklärte Varianz |
|-|-|
| PC1 | 60% |
| PC2 | 25% |
| PC3 | 10% |
| Rest | 5% |

---

Man kann nur die wichtigsten Komponenten behalten.

---

# PCA Beispiel

Datensatz:

100 Features

PCA:

↓

10 Komponenten

↓

95% der Varianz erhalten

---

Vorteile:

- schnelleres Training
- weniger Speicher
- weniger Rauschen

---

# t-SNE

**t-distributed Stochastic Neighbor Embedding**

Eine Methode zur Visualisierung hochdimensionaler Daten.

---

Die Idee:

> Erhalte lokale Nachbarschaften.

---

Beispiel:

Wenn zwei Punkte im Originalraum ähnlich sind:

↓

sollen sie auch im 2D-Raum nahe liegen.

---

Typische Anwendungen:

- Visualisierung von Embeddings
- Bilddaten
- Genexpressionsdaten

---

# Eigenschaften von t-SNE

Vorteile:

- Sehr gute Visualisierung
- Erkennen von Gruppen

Nachteile:

- Keine globale Strukturgarantie
- Langsam bei großen Datenmengen
- Ergebnis abhängig von Parametern

---

Wichtig:

t-SNE ist hauptsächlich ein Visualisierungstool, kein Feature-Extractor für Modelle.

---

# UMAP

**Uniform Manifold Approximation and Projection**

Eine moderne Alternative zu t-SNE.

---

Ziel:

Lokale und globale Strukturen besser erhalten.

---

Vorteile:

- schneller
- oft bessere globale Struktur
- geeignet für größere Datensätze

---

# Manifold Learning

Viele hochdimensionale Daten liegen eigentlich auf einer niedrigdimensionalen Struktur.

Beispiel:

Ein Bild besitzt tausende Pixel.

Aber:

Die tatsächlichen Variationen können durch wenige Faktoren entstehen:

- Rotation
- Beleuchtung
- Objektposition

---

Diese Struktur nennt man:

**Manifold**

---

# Autoencoder

Eine neuronale Methode zur Dimensionsreduktion.

Ein Autoencoder besteht aus:

## Encoder

Komprimiert:

$$
x\rightarrow z
$$

---

## Decoder

Rekonstruiert:

$$
z\rightarrow x'
$$

---

Training:

Minimiere:

$$
||x-x'||^2
$$

---

Der versteckte Raum:

$$
z
$$

ist die reduzierte Darstellung.

---

# Zusammenhang mit Machine Learning

Dimensionsreduktion wird genutzt für:

## Clustering

Weniger Dimensionen:

↓

bessere Cluster-Struktur

---

## Klassifikation

Weniger Features:

↓

weniger Overfitting

---

## Visualisierung

Komplexe Modelle besser verstehen.

---

# Zusammenhang mit Regularisierung

Dimensionsreduktion wirkt ähnlich wie Regularisierung.

Weniger Dimensionen:

↓

kleinere Hypothesenklasse

↓

geringeres Overfitting-Risiko

---

# Zusammenhang mit Feature Selection

## Feature Selection

Entfernt komplette Features.

Beispiel:

Entferne:

- Feature 10
- Feature 20

---

## Dimensionality Reduction

Erzeugt neue Features.

Beispiel:

$$
z_1=0.3x_1+0.7x_2
$$

---

Vergleich:

| | Feature Selection | Dimensionality Reduction |
|-|-|-|
| Features | Original | Neu |
| Interpretierbarkeit | höher | niedriger |
| Kompression | geringer | höher |

---

# Herausforderungen

## Informationsverlust

Nicht jede Information bleibt erhalten.

---

## Interpretierbarkeit

Neue Dimensionen sind oft schwer verständlich.

---

## Skalierung

Viele Methoden benötigen standardisierte Daten.

---

# Vor- und Nachteile

## Vorteile

- Weniger Rechenaufwand
- Visualisierung möglich
- Rauschreduktion
- Weniger Overfitting

---

## Nachteile

- Informationsverlust
- Neue Features schwer interpretierbar
- Methode muss passend gewählt werden

---

# Häufige Fehler & Missverständnisse

## ❌ Weniger Dimensionen sind immer besser

Nein.

Zu starke Reduktion kann wichtige Informationen entfernen.

---

## ❌ PCA findet automatisch die besten Features

Nein.

PCA maximiert Varianz, nicht unbedingt Vorhersagequalität.

---

## ❌ t-SNE zeigt echte Cluster

Nicht unbedingt.

Die Darstellung kann Strukturen verstärken, die im Originalraum weniger ausgeprägt sind.

---

# Praktische Implikationen

## Vor PCA

Oft:

1. Features standardisieren
2. PCA anwenden
3. Modell trainieren

---

## Wahl der Methode

| Ziel | Methode |
|-|-|
| Kompression | PCA |
| Visualisierung | t-SNE / UMAP |
| Nichtlineare Repräsentation | Autoencoder |
| Klassifikation verbessern | PCA / Feature Learning |

---

# Zusammenfassung

| Begriff | Bedeutung |
|---|---|
| Dimensionality Reduction | Reduktion der Feature-Anzahl |
| Curse of Dimensionality | Probleme hoher Dimensionen |
| PCA | Lineare Varianz-basierte Reduktion |
| Principal Component | Neue Koordinatenachse |
| Explained Variance | Erhaltener Informationsanteil |
| t-SNE | Lokale Struktur für Visualisierung |
| UMAP | Moderne Manifold-Methode |
| Autoencoder | Neuronale Dimensionsreduktion |

---

# Siehe auch

- Clustering
- Representation Learning
- Autoencoder
- PCA
- Feature Engineering
- Regularisierung
- Manifold Learning

---

# Ressourcen & Referenzen

**Bücher**

- The Elements of Statistical Learning – Hastie, Tibshirani & Friedman
- Pattern Recognition and Machine Learning – Christopher Bishop

**Originalarbeiten**

- Pearson (1901) – On Lines and Planes of Closest Fit to Systems of Points
- van der Maaten & Hinton (2008) – Visualizing Data using t-SNE
- McInnes et al. (2018) – UMAP: Uniform Manifold Approximation and Projection

---

# Übungsaufgaben

**Aufgabe 1**

Warum ist die Curse of Dimensionality ein Problem für Machine Learning?

---

**Aufgabe 2**

Was maximiert PCA?

---

**Aufgabe 3**

Was ist der Unterschied zwischen Feature Selection und Dimensionality Reduction?

---

**Aufgabe 4**

Warum sollte t-SNE hauptsächlich zur Visualisierung verwendet werden?
