# Support Vector Machines (SVM)

## TL;DR (30 Sekunden)

**Support Vector Machines (SVMs)** sind überwachte Lernverfahren, die eine optimale Trennfläche zwischen Klassen suchen.

Die zentrale Idee:

> Finde die Entscheidungsgrenze, die den größtmöglichen Abstand zu den Datenpunkten beider Klassen besitzt.

Dieser Abstand heißt **Margin**.

---

Für eine lineare Klassifikation:

$$
f(x)=w^Tx+b
$$

Die Vorhersage erfolgt über:

$$
sign(w^Tx+b)
$$

---

**Praktische Bedeutung:**

SVMs erklären:

- Wie Klassifikation geometrisch betrachtet werden kann
- Warum große Margins die Generalisierung verbessern
- Wie Kernel Methoden nichtlineare Probleme lösen
- Grundlagen von Maximum Margin Learning

---

# Motivation & Intuition

Angenommen, wir haben zwei Klassen:
   -
 -
?

Es gibt viele mögliche Trennlinien.

Die Frage:

> Welche Trennlinie ist die beste?

---

Eine einfache Idee:

Wähle die Linie mit maximalem Abstand zu beiden Klassen.

Diese Grenze ist robuster gegenüber neuen Daten.

---

# Lineare Klassifikation

Ein linearer Klassifikator trennt Daten durch eine Hyperebene:

$$
w^Tx+b=0
$$

Dabei:

- $w$ = Gewichtsvektor
- $b$ = Bias
- $x$ = Eingabe

---

Für zwei Klassen:

$$
y_i\in\{-1,+1\}
$$

gilt:

$$
y_i(w^Tx_i+b)>0
$$

wenn der Punkt korrekt klassifiziert wird.

---

# Die Margin-Idee

Die Margin beschreibt den Abstand zwischen Entscheidungsgrenze und nächstem Datenpunkt.

Eine größere Margin bedeutet:

- stabilere Entscheidung
- weniger empfindlich gegenüber Rauschen
- bessere Generalisierung

---

Die Support Vector Machine maximiert:

$$
\text{Margin}
$$

---

# Support Vectors

Die wichtigsten Datenpunkte heißen:

**Support Vectors**

Sie bestimmen die Position der Entscheidungsgrenze.

---

Intuition:
  ← Support Vector
  ← Support Vector

---

Andere Punkte sind weniger wichtig.

Wenn sie entfernt werden, verändert sich die Grenze kaum.

---

# Mathematische Formulierung

Die SVM löst ein Optimierungsproblem:

$$
\min_w
\frac{1}{2}||w||^2
$$

unter:

$$
y_i(w^Tx_i+b)\geq1
$$

---

Warum:

Die Margin ist:

$$
\frac{2}{||w||}
$$

Also:

Margin maximieren

entspricht:

$$
||w||
\text{ minimieren}
$$

---

# Soft Margin SVM

Perfekte Trennung ist in realen Daten oft nicht möglich.

Daher erlaubt man Fehler.

Neue Variable:

$$
\xi_i
$$

heißt:

**Slack Variable**

---

Optimierung:

$$
\min_w
\frac{1}{2}||w||^2
+
C\sum_i\xi_i
$$

---

Parameter $C$ kontrolliert den Trade-off:

## Großes $C$

- wenige Klassifikationsfehler erlaubt
- komplexere Grenze
- höheres Overfitting-Risiko

---

## Kleines $C$

- mehr Fehler erlaubt
- größere Margin
- bessere Robustheit

---

# Zusammenhang mit Regularisierung

Die SVM enthält bereits eine Form der Regularisierung.

Der Term:

$$
||w||^2
$$

beschränkt die Komplexität des Modells.

---

Interpretation:

Kleine Gewichte:

↓

einfacheres Modell

↓

bessere Generalisierung

---

Dies entspricht einer L2-Regularisierung.

---

# Kernel Trick

Lineare SVMs können nur lineare Grenzen lernen.

Viele Probleme sind aber nicht linear:
+
+
-

---

Die Idee:

Transformiere Daten in einen höherdimensionalen Raum:

$$
\phi(x)
$$

Dort wird eine lineare Trennung möglich.

---

Problem:

Die explizite Berechnung von:

$$
\phi(x)
$$

kann sehr teuer sein.

---

# Kernel Trick

Stattdessen verwendet man direkt:

$$
K(x,z)=\phi(x)^T\phi(z)
$$

Der Kernel berechnet die Ähnlichkeit im neuen Raum.

---

Beliebte Kernel:

## Linear Kernel

$$
K(x,z)=x^Tz
$$

---

## Polynomial Kernel

$$
K(x,z)=(x^Tz+c)^d
$$

---

## Radial Basis Function (RBF)

$$
K(x,z)=e^{-\gamma||x-z||^2}
$$

---

# SVM und RKHS

Kernel Methoden basieren auf **Reproducing Kernel Hilbert Spaces (RKHS)**.

Ein Kernel definiert einen Feature Space:

$$
\phi(x)
$$

ohne ihn explizit berechnen zu müssen.

---

Die SVM sucht dann die optimale Trennebene in diesem Hilbertraum.

---

Zusammenhang:
Kernel
↓
Feature Space
↓
Hilbertraum
↓
Lineare SVM

---

# Dualproblem der SVM

Die SVM kann auch als duales Optimierungsproblem formuliert werden.

Die Lösung hängt nur von Skalarprodukten ab:

$$
x_i^Tx_j
$$

oder mit Kernel:

$$
K(x_i,x_j)
$$

---

Dadurch wird der Kernel Trick möglich.

---

Die Dualvariablen:

$$
\alpha_i
$$

bestimmen die Bedeutung der Datenpunkte.

Nur Punkte mit:

$$
\alpha_i>0
$$

sind Support Vectors.

---

# Zusammenhang mit Generalisierung

Die SVM basiert auf dem Prinzip:

> Eine größere Margin führt zu besserer Generalisierung.

---

Theoretisch:

Größere Margin:

↓

kleinere effektive Modellkomplexität

↓

bessere Generalisierung

---

Dies steht im Zusammenhang mit:

- VC-Dimension
- Structural Risk Minimization
- Uniform Convergence

---

# SVM vs. andere Modelle

| Modell | Idee |
|-|-|
| Logistic Regression | Wahrscheinlichkeitsmodellierung |
| Decision Tree | Regelbasierte Splits |
| Neural Network | Flexible Funktionsapproximation |
| SVM | Maximale Trennmargin |

---

# Vorteile von SVMs

## Gute Generalisierung

Durch:

- Margin Maximierung
- Regularisierung

---

## Effektiv bei kleinen Datensätzen

Besonders wenn:

- viele Features
- wenige Beispiele

---

## Kernel ermöglichen komplexe Muster

Nichtlineare Probleme können gelöst werden.

---

# Nachteile von SVMs

## Schlechte Skalierung

Training kann teuer sein bei:

- sehr großen Datensätzen

---

## Kernel-Auswahl

Die Wahl von:

- Kernel
- $C$
- $\gamma$

ist entscheidend.

---

## Keine natürliche Wahrscheinlichkeitsausgabe

SVM liefert zunächst nur:

$$
f(x)
$$

nicht:

$$
P(y|x)
$$

---

# Beispiel

Spam-Erkennung:

Features:

- Wortanzahl
- bestimmte Begriffe
- E-Mail-Struktur

SVM sucht:

Eine Grenze zwischen:
Spam
|
|
|----------- Grenze
|
|
Nicht Spam

---

Die wichtigsten E-Mails nahe an der Grenze werden zu Support Vectors.

---

# Häufige Fehler & Missverständnisse

## ❌ SVM sucht einfach irgendeine Trennlinie

Nein.

Sie maximiert die Margin.

---

## ❌ Support Vectors sind die wichtigsten positiven Beispiele

Nein.

Es sind die Punkte, die die Entscheidungsgrenze bestimmen.

---

## ❌ Kernel erzeugen immer bessere Modelle

Nein.

Ein zu komplexer Kernel kann Overfitting verursachen.

---

# Praktische Implikationen

## Gute Anwendungsszenarien

SVMs funktionieren besonders gut bei:

- mittleren Datensätzen
- vielen Features
- klaren Klassenstrukturen

---

## Hyperparameter

Wichtige Parameter:

| Parameter | Bedeutung |
|-|-|
| $C$ | Strafe für Fehler |
| Kernel | Form des Feature Spaces |
| $\gamma$ | Einfluss einzelner Punkte beim RBF-Kernel |

---

# Zusammenfassung

| Begriff | Bedeutung |
|-|-|
| SVM | Klassifikator mit maximaler Margin |
| Hyperplane | Entscheidungsgrenze |
| Margin | Abstand zur nächsten Datenklasse |
| Support Vector | Punkt, der Grenze bestimmt |
| Soft Margin | Erlaubt Klassifikationsfehler |
| Kernel Trick | Implizite Projektion in Feature Space |
| RKHS | Mathematischer Raum hinter Kernel Methoden |

---

# Siehe auch

- Kernel Methods & RKHS
- Hilberträume
- VC-Dimension
- Regularisierung
- Structural Risk Minimization
- Konvexe Optimierung
- Lagrange-Dualität

---

# Ressourcen & Referenzen

**Bücher**

- Understanding Machine Learning – Shalev-Shwartz & Ben-David
- The Elements of Statistical Learning – Hastie, Tibshirani & Friedman

**Originalarbeiten**

- Vapnik & Cortes (1995) – Support-Vector Networks
- Boser, Guyon & Vapnik (1992) – A Training Algorithm for Optimal Margin Classifiers

---

# Übungsaufgaben

**Aufgabe 1**

Warum maximiert eine SVM die Margin?

---

**Aufgabe 2**

Welche Rolle spielen Support Vectors?

---

**Aufgabe 3**

Warum benötigt man Kernel Methoden?

---

**Aufgabe 4**

Wie hängt SVM-Regularisierung mit Generalisierung zusammen?
