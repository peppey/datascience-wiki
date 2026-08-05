# Kernel Methods & Reproducing Kernel Hilbert Space (RKHS)

## TL;DR (30 Sekunden)

**Kernel Methods** ermöglichen es, komplexe nichtlineare Zusammenhänge zu lernen, ohne explizit in einen hochdimensionalen Feature Space zu transformieren.

Die Kernidee:

> Berechne Ähnlichkeiten zwischen Datenpunkten, anstatt die expliziten Features zu berechnen.

Ein Kernel beschreibt:

$$
K(x,x')
=
\langle \phi(x),\phi(x')\rangle
$$

Dabei:

- $\phi(x)$ = Transformation in einen Feature Space
- $K(x,x')$ = Ähnlichkeit zwischen zwei Datenpunkten

---

**Praktische Bedeutung:**

Kernel Methods erklären:

- Warum SVMs auch nichtlineare Grenzen lernen können
- Wie komplexe Feature Spaces entstehen
- Warum man hochdimensionale Transformationen nicht explizit berechnen muss

---

# Motivation & Intuition

Viele Machine-Learning-Modelle suchen eine Trennlinie zwischen Daten.

Beispiel:

## Linear trennbare Daten
○ ○ ○
────────

● ● ●


Eine Gerade reicht aus.

---

## Nichtlinear trennbare Daten

Beispiel:
○ ○ ● ○
○ ● ● ○
● ○ ○ ●

Eine einfache Gerade funktioniert nicht.

---

Die Idee:

Transformiere die Daten in einen anderen Raum:

Originalraum:

$$
x
$$

↓

Feature Space:

$$
\phi(x)
$$

Dort kann eine lineare Trennung möglich sein.

---

# Feature Spaces

Ein Feature Space ist ein Raum, in dem Daten durch Merkmale dargestellt werden.

Beispiel:

Ein Punkt:

$$
x=(x_1,x_2)
$$

kann transformiert werden zu:

$$
\phi(x)
=
(x_1,x_2,x_1^2,x_2^2,x_1x_2)
$$

Der neue Raum enthält zusätzliche Informationen.

---

## Problem der expliziten Transformation

Diese Transformation kann sehr teuer werden.

Beispiel:

Ein Modell mit vielen Eingabefeatures kann einen Feature Space mit Millionen oder unendlich vielen Dimensionen erzeugen.

Wir möchten trotzdem darin rechnen.

Die Lösung:

**Kernel Trick**

---

# Der Kernel Trick

Der Kernel Trick ersetzt das Skalarprodukt im Feature Space:

Statt:

$$
\langle\phi(x),\phi(x')\rangle
$$

berechnen wir direkt:

$$
K(x,x')
$$

---

Die Transformation wird also nie explizit berechnet.

Original:

$$
x
\rightarrow
\phi(x)
\rightarrow
\langle\phi(x),\phi(x')\rangle
$$

Mit Kernel:

$$
x,x'
\rightarrow
K(x,x')
$$

---

# Beispiel: Polynomial Kernel

Ein möglicher Kernel:

$$
K(x,x')
=
(x^Tx'+c)^d
$$

Er entspricht einer Transformation in einen polynomialen Feature Space.

Zum Beispiel:

$$
x=(x_1,x_2)
$$

kann Features enthalten wie:

- $x_1^2$
- $x_2^2$
- $x_1x_2$

ohne dass diese explizit berechnet werden.

---

# Häufige Kernel

## Linear Kernel

$$
K(x,x')
=
x^Tx'
$$

Entspricht:

Keine Transformation.

Gut für:

- viele Features
- lineare Probleme

---

## Polynomial Kernel

$$
K(x,x')
=
(x^Tx'+c)^d
$$

Erzeugt polynomial komplexere Entscheidungsgrenzen.

---

## Radial Basis Function Kernel (RBF)

Der häufigste nichtlineare Kernel:

$$
K(x,x')
=
e^{-\gamma ||x-x'||^2}
$$

Intuition:

Ähnliche Punkte erhalten hohe Werte.

Unähnliche Punkte erhalten niedrige Werte.

---

# Support Vector Machines (SVMs)

SVMs suchen eine Trennfläche mit maximalem Abstand zu den Datenpunkten.

Die Entscheidungsgrenze:

$$
w^Tx+b=0
$$

---

Die Punkte, die der Grenze am nächsten sind, heißen:

**Support Vectors**

Sie bestimmen die Position der Entscheidungsgrenze.

---

# Warum funktionieren Kernel-SVMs?

Eine SVM benötigt nur Skalarprodukte zwischen Datenpunkten.

Die Optimierung verwendet Terme wie:

$$
x_i^Tx_j
$$

Mit Kernel Methods ersetzt man diese durch:

$$
K(x_i,x_j)
$$

Dadurch kann die SVM im Feature Space arbeiten.

---

Ablauf:

Daten

↓

Kernel berechnet Ähnlichkeiten

↓

SVM findet optimale Trennfläche im Feature Space

↓

Nichtlineare Grenze im ursprünglichen Raum

---

# Reproducing Kernel Hilbert Space (RKHS)

Ein **Reproducing Kernel Hilbert Space (RKHS)** ist ein mathematischer Raum von Funktionen, der durch einen Kernel definiert wird.

Die zentrale Idee:

> Jeder gültige Kernel entspricht einem inneren Produkt in einem bestimmten Funktionsraum.

---

Formal:

Ein Kernel:

$$
K(x,x')
$$

definiert einen Hilbertraum:

$$
\mathcal{H}
$$

mit Funktionen:

$$
f:\mathcal{X}\rightarrow\mathbb{R}
$$

---

Dabei gilt die Reproducing Property:

$$
f(x)
=
\langle f,K(x,\cdot)\rangle_{\mathcal{H}}
$$

---

## Intuition

Der Kernel enthält alle Informationen darüber:

- wie Funktionen verglichen werden
- welche Funktionen im Modell möglich sind
- welche Komplexität der Lernraum besitzt

---

# Zusammenhang zwischen Kernel und Modellkomplexität

Der Kernel bestimmt den Feature Space.

Ein komplexerer Kernel:

- ermöglicht komplexere Modelle
- kann feinere Muster lernen
- erhöht aber Overfitting-Risiko

---

Beispiel:

## Linear Kernel

Einfacher Feature Space:

- geringe Komplexität
- weniger Overfitting

---

## RBF Kernel

Sehr flexibler Feature Space:

- komplexe Muster möglich
- mehr Daten notwendig

---

# Zusammenhang mit Regularisierung

SVMs verwenden ebenfalls eine Form von Regularisierung.

Die Optimierung:

$$
\min
\frac{1}{2}||w||^2
+
C
\sum_i \xi_i
$$

Dabei:

- $||w||^2$ kontrolliert die Modellkomplexität
- $C$ bestimmt den Einfluss von Fehlern

---

Großes $C$:

- weniger Fehler erlaubt
- komplexeres Modell

Kleines $C$:

- stärkere Regularisierung
- einfacheres Modell

---

# Kernel Methods und Generalisierung

Kernel Methods funktionieren gut, weil sie:

1. einen geeigneten Feature Space wählen
2. Komplexität kontrollieren
3. Regularisierung verwenden

Die Generalisierung hängt ab von:

- Wahl des Kernels
- Kernel-Parametern
- Datenmenge

---

# Häufige Fehler & Missverständnisse

## ❌ Kernel erzeugen einfach neue Features

Nicht direkt.

Der Kernel berechnet nur Ähnlichkeiten, ohne die Features explizit zu erzeugen.

---

## ❌ Ein komplexerer Kernel ist immer besser

Nein.

Ein zu flexibler Kernel kann overfitten.

---

## ❌ SVMs sind immer linear

Nein.

Mit Kernel Methods können SVMs nichtlineare Entscheidungsgrenzen lernen.

---

# Praktische Implikationen

## Kernelwahl ist entscheidend

Typische Wahl:

- Linear: viele Features, große Datenmengen
- Polynomial: strukturierte nichtlineare Muster
- RBF: allgemeine nichtlineare Probleme

---

## Feature Engineering vs. Kernel

Kernel Methods übernehmen teilweise die Feature-Erzeugung.

Statt:

Manuell Features bauen

↓

Kernel definiert impliziten Feature Space

---

## Grenzen von Kernel Methods

Bei sehr großen Datensätzen:

- Kernel-Matrix wächst quadratisch:

$$
O(n^2)
$$

- hoher Speicherbedarf

Deshalb werden bei großen Datenmengen oft neuronale Netze bevorzugt.

---

# Zusammenfassung

| Begriff | Bedeutung |
|---|---|
| Kernel | Berechnet Ähnlichkeit im Feature Space |
| Kernel Trick | Nutzung von Feature Spaces ohne explizite Transformation |
| Feature Space | Raum mit transformierten Merkmalen |
| SVM | Modell mit maximalem Abstand zur Trennfläche |
| Support Vector | Datenpunkt, der die Grenze bestimmt |
| RKHS | Funktionsraum, der durch einen Kernel definiert wird |
| Regularisierung | Kontrolliert Modellkomplexität |

---

# Siehe auch

- Support Vector Machines
- Empirical Risk Minimization (ERM)
- Structural Risk Minimization
- Regularisierung
- VC-Dimension & Rademacher Complexity

---

# Ressourcen & Referenzen

**Bücher**

- Understanding Machine Learning – Shalev-Shwartz & Ben-David
- The Elements of Statistical Learning – Hastie, Tibshirani & Friedman

**Konzepte**

- Mercer (1909) – Positive Definite Functions
- Vapnik – Statistical Learning Theory

---

# Übungsaufgaben

**Aufgabe 1**

Warum muss ein Kernel den Feature Space nicht explizit berechnen?

---

**Aufgabe 2**

Was beschreibt ein Kernel intuitiv?

---

**Aufgabe 3**

Warum können Kernel-SVMs nichtlineare Entscheidungsgrenzen lernen?

---

**Aufgabe 4**

Welche Rolle spielt Regularisierung bei SVMs?
