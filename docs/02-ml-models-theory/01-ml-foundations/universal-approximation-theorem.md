# Universal Approximation Theorem

## TL;DR (30 Sekunden)

Das **Universal Approximation Theorem** beschreibt die Ausdruckskraft neuronaler Netze.

Die zentrale Aussage:

> Ein ausreichend großes neuronales Netz mit mindestens einer versteckten Schicht kann jede stetige Funktion auf einer kompakten Menge beliebig genau approximieren.

Formal:

Für eine geeignete Aktivierungsfunktion existiert ein neuronales Netz $f_\theta$, sodass:

$$
|f_\theta(x)-f(x)|<\epsilon
$$

für beliebig kleines:

$$
\epsilon>0
$$

---

**Praktische Bedeutung:**

Das Theorem erklärt:

- Warum neuronale Netze sehr flexible Funktionen lernen können
- Warum Neural Networks theoretisch sehr allgemeine Probleme approximieren können
- Warum Ausdruckskraft alleine nicht ausreicht für gutes Machine Learning

---

# Motivation & Intuition

Viele Machine-Learning-Probleme können als Funktionsapproximation betrachtet werden.

Wir möchten eine unbekannte Funktion lernen:

$$
y=f(x)
$$

Beispiele:

- Bilderkennung
- Sprachverarbeitung
- Zeitreihenprognosen
- Steuerungsprobleme

Das neuronale Netz soll eine Approximation finden:

$$
\hat{f}(x)\approx f(x)
$$

---

Die Frage:

> Sind neuronale Netze überhaupt flexibel genug, um beliebige Funktionen darzustellen?

Das Universal Approximation Theorem beantwortet diese Frage mit:

**Ja, unter bestimmten Bedingungen.**

---

# Was bedeutet Approximation?

Approximation bedeutet:

Eine Funktion wird durch eine andere Funktion angenähert.

Beispiel:

Eine komplizierte Funktion:

$$
f(x)
$$

wird angenähert durch:

$$
\hat{f}(x)
$$

Der Fehler:

$$
|f(x)-\hat{f}(x)|
$$

soll klein sein.

---

# Aussage des Theorems

Ein Feedforward-Neural-Network mit:

- einer versteckten Schicht
- genügend Neuronen
- geeigneter Aktivierungsfunktion

kann jede stetige Funktion beliebig genau approximieren.

---

Vereinfacht:
Input
↓

Hidden Layer

↓

Output


kann theoretisch jede ausreichend glatte Funktion darstellen.

---

# Mathematische Formulierung

Ein neuronales Netz mit einer Hidden Layer kann dargestellt werden als:

$$
f(x)
=
\sum_{i=1}^{m}
a_i\sigma(w_i^Tx+b_i)
$$

Dabei:

- $\sigma$ = Aktivierungsfunktion
- $w_i$ = Gewichte
- $b_i$ = Bias
- $a_i$ = Ausgangsgewichte
- $m$ = Anzahl Neuronen

Das Theorem sagt:

Für jede stetige Funktion $f$ und jedes:

$$
\epsilon>0
$$

existiert ein Netz, sodass:

$$
||f-\hat{f}||<\epsilon
$$

---

# Rolle der Aktivierungsfunktion

Ohne Aktivierungsfunktion wäre ein neuronales Netz nur eine lineare Transformation.

Beispiel:

Schicht 1:

$$
Wx+b
$$

Schicht 2:

$$
W_2(W_1x+b_1)+b_2
$$

ergibt wieder:

$$
Ax+b
$$

also nur ein lineares Modell.

---

Aktivierungsfunktionen machen nichtlineare Approximation möglich.

Beispiele:

- Sigmoid
- ReLU
- Tanh

---

# Intuition: Neuronen als Bausteine

Ein einzelnes Neuron:

$$
\sigma(w^Tx+b)
$$

stellt eine einfache Funktion dar.

Viele Neuronen:

$$
\sum_i a_i\sigma(w_i^Tx+b_i)
$$

können viele einfache Funktionen kombinieren.

Ähnlich wie:

- Polynome komplexe Funktionen approximieren
- Fourier-Reihen Signale approximieren

---

# Was sagt das Theorem NICHT?

Das Universal Approximation Theorem wird häufig falsch interpretiert.

Es sagt nicht:

> Ein neuronales Netz findet automatisch die richtige Funktion.

Es sagt nur:

> Eine passende Netzwerkarchitektur besitzt die Fähigkeit, die Funktion darzustellen.

---

# Ausdruckskraft vs. Lernen

Es gibt einen wichtigen Unterschied:

## Ausdruckskraft

Kann das Modell eine Funktion darstellen?

↓

Universal Approximation Theorem beantwortet diese Frage.

---

## Lernen

Kann der Trainingsalgorithmus diese Funktion finden?

↓

Abhängig von:

- Datenmenge
- Optimierung
- Initialisierung
- Regularisierung

---

Ein Netzwerk kann theoretisch alles darstellen, aber praktisch schwierig zu trainieren sein.

---

# Zusammenhang mit Overfitting

Mehr Ausdruckskraft bedeutet:

- mehr mögliche Funktionen
- höhere Modellkomplexität

Das kann zu Overfitting führen.

Ein großes Netzwerk kann:

Trainingsdaten perfekt lernen:

$$
\hat{R}(h)\approx0
$$

aber schlecht generalisieren:

$$
R(h)\gg0
$$

---

Deshalb benötigt man:

- Regularisierung
- ausreichend Daten
- geeignete Modellarchitektur

---

# Zusammenhang mit Bias-Variance Trade-off

Das Theorem erklärt, warum neuronale Netze einen niedrigen Bias besitzen können.

Große Netzwerke:

- können komplexe Muster darstellen
- haben hohe Ausdruckskraft

Aber:

- können hohe Variance besitzen

Daher entsteht ein Trade-off:

Mehr Kapazität:

↓

weniger Bias

aber:

↓

höheres Overfitting-Risiko

---

# Zusammenhang mit Deep Learning

Das ursprüngliche Theorem betrachtet oft nur eine versteckte Schicht.

Moderne Deep Learning Modelle nutzen:

- viele Schichten
- Millionen Parameter
- spezielle Architekturen

Beispiele:

- CNNs für Bilder
- Transformer für Sprache

---

Tiefe Netzwerke bieten zusätzliche Vorteile:

- hierarchische Feature-Lernen
- effizientere Darstellung bestimmter Funktionen

---

# Grenzen des Theorems

## 1. Keine Aussage über Effizienz

Das Theorem sagt nicht:

Wie viele Neuronen benötigt werden.

Eine Funktion kann theoretisch darstellbar sein, aber extrem viele Parameter benötigen.

---

## 2. Keine Garantie für Generalisierung

Ein Netzwerk kann jede Funktion approximieren, aber trotzdem schlecht generalisieren.

---

## 3. Nur theoretische Existenz

Das Theorem sagt:

> Ein solches Netzwerk existiert.

Nicht:

> Gradient Descent findet es automatisch.

---

# Beispiel

Angenommen:

Eine Funktion beschreibt die Klassifikation von Bildern.

Das Universal Approximation Theorem sagt:

Ein ausreichend großes Netzwerk könnte diese Funktion darstellen.

Aber praktisch benötigen wir:

- Millionen Bilder
- passende Architektur
- Training
- Regularisierung

---

# Praktische Implikationen

## Große Netzwerke sind flexibel

Sie können:

- komplexe Muster lernen
- viele verschiedene Aufgaben lösen

---

## Architektur ist entscheidend

Nicht jedes Netzwerk nutzt seine Kapazität gleich gut.

Beispiele:

CNNs nutzen:

- lokale Bildstrukturen

Transformer nutzen:

- Attention-Strukturen

---

## Mehr Parameter sind nicht automatisch besser

Ein größeres Modell kann:

- bessere Approximation ermöglichen
- aber auch stärker overfitten

---

# Zusammenfassung

| Begriff | Bedeutung |
|---|---|
| Universal Approximation Theorem | Neuronale Netze können beliebige stetige Funktionen approximieren |
| Approximation | Annäherung einer Funktion |
| Ausdruckskraft | Welche Funktionen ein Modell darstellen kann |
| Aktivierungsfunktion | Ermöglicht Nichtlinearität |
| Hidden Layer | Macht komplexe Transformationen möglich |
| Overfitting | Zu starke Anpassung an Trainingsdaten |
| Generalisierung | Leistung auf neuen Daten |

---

# Siehe auch

- Bias-Variance Trade-off
- Regularisierung
- Gradient Descent
- Deep Learning
- Empirical Risk Minimization (ERM)

---

# Ressourcen & Referenzen

**Bücher**

- Deep Learning – Goodfellow, Bengio & Courville
- Understanding Machine Learning – Shalev-Shwartz & Ben-David

**Originalarbeiten**

- Cybenko (1989) – Approximation by Superpositions of a Sigmoidal Function
- Hornik (1991) – Approximation Capabilities of Multilayer Feedforward Networks

---

# Übungsaufgaben

**Aufgabe 1**

Was besagt das Universal Approximation Theorem intuitiv?

---

**Aufgabe 2**

Warum bedeutet das Theorem nicht, dass neuronale Netze automatisch gute Modelle erzeugen?

---

**Aufgabe 3**

Warum benötigt ein neuronales Netz Aktivierungsfunktionen?

---

**Aufgabe 4**

Wie hängt Ausdruckskraft mit Overfitting zusammen?
