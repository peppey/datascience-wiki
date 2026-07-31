# Clustering

## TL;DR (30 Sekunden)

**Clustering** ist ein Verfahren des **unüberwachten Lernens**, bei dem Datenpunkte ohne vorgegebene Labels in Gruppen eingeteilt werden.

Die zentrale Idee:

> Datenpunkte innerhalb einer Gruppe sollen möglichst ähnlich sein, während verschiedene Gruppen möglichst unterschiedlich sind.

Beispiele:

- Kundensegmentierung
- Gruppierung von Dokumenten
- Bildanalyse
- Anomalieerkennung

---

**Praktische Bedeutung:**

Clustering erklärt:

- Wie Muster ohne Labels gefunden werden können
- Wie Ähnlichkeit mathematisch definiert wird
- Warum verschiedene Cluster-Methoden unterschiedliche Ergebnisse liefern
- Grundlagen vieler unsupervised Learning Verfahren

---

# Motivation & Intuition

Beim überwachten Lernen kennen wir die Zielvariable:

$$
(x,y)
$$

Beispiel:
Bild → Katze / Hund

---

Beim Clustering haben wir nur Daten:

$$
x
$$

und suchen selbst nach Strukturen.

Beispiel:

Kundendaten:

- Alter
- Kaufverhalten
- Einkommen

Die Frage:

> Gibt es natürliche Gruppen von Kunden?

---

# Formale Definition

Gegeben:

$$
X=\{x_1,x_2,...,x_n\}
$$

soll eine Partition gefunden werden:

$$
C_1,C_2,...,C_k
$$

mit:

$$
X=C_1\cup C_2\cup...\cup C_k
$$

---

Dabei sollen gelten:

## Innerhalb eines Clusters

Punkte sind ähnlich:

$$
d(x_i,x_j)
\text{ klein}
$$

---

## Zwischen Clustern

Punkte sind unterschiedlich:

$$
d(x_i,x_j)
\text{ groß}
$$

---

# Ähnlichkeit und Distanz

Clustering benötigt eine Definition von Ähnlichkeit.

Häufige Distanzmaße:

---

## Euklidische Distanz

$$
d(x,y)=
\sqrt{\sum_i(x_i-y_i)^2}
$$

Geeignet für:

- numerische Features
- geometrische Daten

---

## Manhattan Distanz

$$
d(x,y)=
\sum_i|x_i-y_i|
$$

---

## Cosine Similarity

Misst den Winkel zwischen Vektoren.

Besonders häufig bei:

- Textdaten
- Embeddings

---

# K-Means Clustering

Der bekannteste Clustering-Algorithmus ist **K-Means**.

Die Idee:

> Finde $k$ Gruppen mit möglichst kleinen Abständen zu ihren Zentren.

---

Jeder Cluster besitzt einen Mittelpunkt:

$$
\mu_k
$$

genannt:

**Centroid**

---

# K-Means Algorithmus

Der Algorithmus läuft iterativ.

---

## Schritt 1: Initialisierung

Wähle:

$$
k
$$

zufällige Clusterzentren.

---

## Schritt 2: Zuordnung

Jeder Datenpunkt wird dem nächsten Zentrum zugeordnet:

$$
C_i=
\arg\min_k ||x_i-\mu_k||
$$

---

## Schritt 3: Zentren aktualisieren

Berechne neue Mittelpunkte:

$$
\mu_k=
\frac1{|C_k|}
\sum_{x_i\in C_k}x_i
$$

---

## Schritt 4

Wiederhole:

Zuordnung → Aktualisierung

bis sich nichts mehr ändert.

---

# Optimierungsziel von K-Means

K-Means minimiert:

$$
\sum_{k=1}^{K}
\sum_{x_i\in C_k}
||x_i-\mu_k||^2
$$

Dies nennt man:

**Within-Cluster Sum of Squares (WCSS)**

---

Ziel:

Innerhalb eines Clusters:

kleine Abstände

---

# Wahl von K

Ein Problem:

Wie viele Cluster gibt es?

---

## Elbow Method

Man betrachtet:

$$
WCSS
$$

für verschiedene Werte von:

$$
k
$$

---

Man sucht den Punkt:

> Ab dort bringt ein weiterer Cluster wenig Verbesserung.

---

# Hierarchisches Clustering

Hierarchisches Clustering erzeugt eine Baumstruktur:

**Dendrogramm**

---

Es gibt zwei Ansätze:

## Agglomerativ

Start:
Jeder Punkt = eigener Cluster

Dann:
ähnliche Cluster zusammenführen

---

## Divisiv

Start:
Alle Punkte in einem Cluster

Dann:
aufteilen

---

Vorteil:

Die Anzahl der Cluster muss nicht vorher bekannt sein.

---

# DBSCAN

**Density-Based Spatial Clustering of Applications with Noise**

Die Idee:

> Cluster sind dichte Regionen im Datenraum.

---

Parameter:

## $\epsilon$

Radius der Nachbarschaft.

---

## MinPts

Mindestanzahl Punkte für einen Cluster.

---

DBSCAN erkennt:

- Cluster beliebiger Form
- Ausreißer

---

Beispiel:
    x
  Noise

---

# Gaussian Mixture Models (GMM)

GMM nimmt an:

Daten entstehen aus einer Mischung von Wahrscheinlichkeitsverteilungen.

Typischerweise:

$$
x\sim
\sum_k
\pi_k
N(\mu_k,\Sigma_k)
$$

---

Unterschied zu K-Means:

K-Means:

> Jeder Punkt gehört genau zu einem Cluster.

GMM:

> Jeder Punkt hat eine Wahrscheinlichkeit für jedes Cluster.

---

# Soft vs. Hard Clustering

## Hard Clustering

Jeder Punkt:

genau ein Cluster.

Beispiel:

K-Means

---

## Soft Clustering

Jeder Punkt:

Wahrscheinlichkeiten über Cluster.

Beispiel:

Gaussian Mixture Models

---

# Clustering und Dimensionsreduktion

In hohen Dimensionen wird Clustering schwierig.

Problem:

**Curse of Dimensionality**

---

Daher kombiniert man oft:

1. Dimensionsreduktion

zum Beispiel:

- PCA
- Autoencoder

2. Clustering

---

# Zusammenhang mit Machine Learning

Clustering wird genutzt für:

## Unsupervised Learning

Keine Labels notwendig.

---

## Feature Learning

Cluster können neue Features erzeugen.

---

## Datenexploration

Strukturen in Daten entdecken.

---

# Zusammenhang mit Statistik

Viele Clustering-Verfahren basieren auf probabilistischen Modellen.

Beispiele:

- Gaussian Mixture Models
- Bayesian Clustering

---

# Zusammenhang mit Anomaly Detection

Cluster können helfen, ungewöhnliche Punkte zu finden.

Beispiel:
Cluster:
         x
    Anomalie

---

Punkte weit entfernt von allen Clustern sind verdächtig.

---

# Herausforderungen

## Wahl der Distanz

Die falsche Distanz kann falsche Cluster erzeugen.

---

## Skalierung der Features

Features mit großen Werten dominieren.

Beispiel:

- Einkommen: 100000
- Alter: 30

Lösung:

Normalisierung.

---

## Anzahl der Cluster

Oft unbekannt.

---

## Interpretation

Cluster müssen fachlich interpretiert werden.

---

# Clustering vs. Klassifikation

| | Clustering | Klassifikation |
|-|-|-|
| Lernen | Unsupervised | Supervised |
| Labels | Nein | Ja |
| Ziel | Gruppen finden | Klassen vorhersagen |
| Beispiel | Kundensegmente | Spam erkennen |

---

# Vor- und Nachteile

## Vorteile

- Keine Labels notwendig
- Musterentdeckung
- Datenexploration

---

## Nachteile

- Ergebnisse abhängig von Methode
- Cluster nicht immer eindeutig
- Interpretation schwierig

---

# Häufige Fehler & Missverständnisse

## ❌ Clustering findet automatisch echte Gruppen

Nein.

Cluster hängen ab von:

- Distanzmaß
- Algorithmus
- Parametern

---

## ❌ Jeder Datensatz besitzt natürliche Cluster

Nicht unbedingt.

Manche Daten enthalten keine sinnvolle Gruppenstruktur.

---

## ❌ Cluster bedeuten Ursachen

Nein.

Clustering findet Zusammenhänge, keine Kausalität.

---

# Praktische Implikationen

## Standardisiere Features

Vor allem bei:

- K-Means
- Distanz-basierten Methoden

---

## Wähle Methode passend zum Problem

| Situation | Methode |
|-|-|
| Runde Cluster | K-Means |
| Ausreißer vorhanden | DBSCAN |
| Unbekannte Clusterzahl | Hierarchisch |
| Unsicherheit wichtig | GMM |

---

## Evaluation von Clustering

Da Labels fehlen, verwendet man interne Kriterien:

### Silhouette Score

Misst:

- Zusammenhalt innerhalb eines Clusters
- Abstand zu anderen Clustern

---

# Zusammenfassung

| Begriff | Bedeutung |
|---|---|
| Clustering | Gruppierung ähnlicher Datenpunkte |
| Unsupervised Learning | Lernen ohne Labels |
| K-Means | Zentroid-basiertes Clustering |
| Hierarchisches Clustering | Baumartige Clusterstruktur |
| DBSCAN | Dichte-basiertes Clustering |
| GMM | Probabilistisches Clustering |
| Hard Clustering | Ein Cluster pro Punkt |
| Soft Clustering | Wahrscheinlichkeiten über Cluster |

---

# Siehe auch

- PCA & Dimensionality Reduction
- Gaussian Mixture Models
- Anomaly Detection
- Representation Learning
- Unsupervised Learning
- Bayesian Inference

---

# Ressourcen & Referenzen

**Bücher**

- The Elements of Statistical Learning – Hastie, Tibshirani & Friedman
- Pattern Recognition and Machine Learning – Christopher Bishop

**Konzepte**

- Lloyd (1982) – Least Squares Quantization in PCM
- Ester et al. (1996) – DBSCAN
- Dempster et al. (1977) – EM Algorithm

---

# Übungsaufgaben

**Aufgabe 1**

Warum benötigt Clustering keine Labels?

---

**Aufgabe 2**

Wie unterscheidet sich K-Means von Gaussian Mixture Models?

---

**Aufgabe 3**

Warum müssen Features vor K-Means oft skaliert werden?

---

**Aufgabe 4**

Warum bedeutet ein gefundenes Cluster nicht automatisch eine kausale Gruppe?
