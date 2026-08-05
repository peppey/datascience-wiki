# Hilberträume

## TL;DR (30 Sekunden)

Ein **Hilbertraum** ist eine Verallgemeinerung des euklidischen Raums auf möglicherweise unendlich viele Dimensionen.

Die zentrale Idee:

> Ein Hilbertraum ist ein Raum, in dem man Längen, Winkel und Abstände definieren kann.

Dafür benötigt man ein **inneres Produkt**:

$$
\langle x,y\rangle
$$

Aus diesem entstehen:

Länge:

$$
||x||
=
\sqrt{\langle x,x\rangle}
$$

Abstand:

$$
d(x,y)
=
||x-y||
$$

---

**Praktische Bedeutung:**

Hilberträume sind wichtig für:

- Kernel Methods
- Support Vector Machines
- Funktionalanalysis
- Quantenmechanik
- mathematische Grundlagen von Machine Learning

---

# Motivation & Intuition

In der linearen Algebra arbeitet man meistens mit:

$$
\mathbb{R}^2
$$

oder:

$$
\mathbb{R}^3
$$

Dort kennen wir:

- Punkte
- Vektoren
- Winkel
- Längen

Beispiel:

Zwei Vektoren:

$$
x=(1,0)
$$

und

$$
y=(0,1)
$$

stehen senkrecht aufeinander, weil:

$$
x^Ty=0
$$

---

Ein Hilbertraum erweitert diese Idee:

Nicht nur endlichdimensionale Vektoren, sondern auch:

- Funktionen
- Folgen
- unendlichdimensionale Vektoren

können betrachtet werden.

---

# Inneres Produkt

Das zentrale Konzept eines Hilbertraums ist das **innere Produkt**.

Ein inneres Produkt ordnet zwei Elementen eine Zahl zu:

$$
\langle x,y\rangle
$$

und beschreibt deren Ähnlichkeit.

---

Beispiel im normalen Vektorraum:

$$
\langle x,y\rangle
=
x^Ty
$$

also:

$$
x_1y_1+x_2y_2+...+x_ny_n
$$

---

Aus dem inneren Produkt entstehen:

## Länge eines Vektors

$$
||x||
=
\sqrt{\langle x,x\rangle}
$$

---

## Winkel zwischen Vektoren

$$
\cos(\theta)
=
\frac{\langle x,y\rangle}
{||x||||y||}
$$

---

## Orthogonalität

Zwei Vektoren sind orthogonal, wenn:

$$
\langle x,y\rangle=0
$$

---

# Definition eines Hilbertraums

Ein Hilbertraum ist ein:

1. Vektorraum
2. mit einem inneren Produkt
3. der vollständig bezüglich der induzierten Norm ist

Formal:

Ein Raum $\mathcal{H}$ ist ein Hilbertraum, wenn:

$$
(\mathcal{H},\langle\cdot,\cdot\rangle)
$$

ein vollständiger innerer Produktraum ist.

---

# Was bedeutet Vollständigkeit?

Vollständigkeit bedeutet:

> Jede Folge, die immer weiter zusammenrückt, besitzt einen Grenzwert innerhalb des Raums.

---

Beispiel:

Eine Folge von Punkten:

$$
x_1,x_2,x_3,...
$$

wird immer ähnlicher:

$$
||x_n-x_m||\rightarrow0
$$

Dann existiert ein Grenzwert:

$$
x_n\rightarrow x
$$

und dieser Grenzwert liegt ebenfalls im Raum.

---

Warum ist das wichtig?

Ohne Vollständigkeit könnten Berechnungen "aus dem Raum herauslaufen".

---

# Beispiele für Hilberträume

## Euklidischer Raum

Der klassische Raum:

$$
\mathbb{R}^n
$$

mit:

$$
\langle x,y\rangle=x^Ty
$$

ist ein Hilbertraum.

---

## Folgenraum $\ell^2$

Ein Element ist eine unendliche Folge:

$$
x=(x_1,x_2,x_3,...)
$$

mit:

$$
\sum_i x_i^2 < \infty
$$

Das innere Produkt:

$$
\langle x,y\rangle
=
\sum_i x_i y_i
$$

---

## Funktionenraum $L^2$

Elemente sind Funktionen:

$$
f(x)
$$

mit:

$$
\int |f(x)|^2 dx < \infty
$$

Das innere Produkt:

$$
\langle f,g\rangle
=
\int f(x)g(x)dx
$$

---

# Hilberträume in Machine Learning

Viele ML-Methoden arbeiten nicht direkt mit Datenpunkten:

$$
x\in\mathbb{R}^n
$$

sondern mit Funktionen oder transformierten Features:

$$
\phi(x)
$$

Diese können in sehr großen oder unendlichdimensionalen Räumen liegen.

---

Beispiel:

Kernel Mapping:

$$
x
\rightarrow
\phi(x)
$$

wobei:

$$
\phi(x)\in\mathcal{H}
$$

Der Feature Space ist ein Hilbertraum.

---

# Zusammenhang mit Kernel Methods

Ein Kernel ist ein inneres Produkt in einem Hilbertraum:

$$
K(x,x')
=
\langle\phi(x),\phi(x')\rangle_{\mathcal{H}}
$$

Das bedeutet:

Der Kernel definiert einen Hilbertraum.

---

Beispiel:

RBF-Kernel:

$$
K(x,x')
=
e^{-\gamma||x-x'||^2}
$$

entspricht einem bestimmten (unendlichdimensionalen) Feature Space.

---

# Reproducing Kernel Hilbert Space (RKHS)

Ein RKHS ist ein spezieller Hilbertraum von Funktionen.

Die Besonderheit:

Der Wert einer Funktion kann durch das innere Produkt mit dem Kernel berechnet werden:

$$
f(x)
=
\langle f,K(x,\cdot)\rangle_{\mathcal{H}}
$$

---

Intuition:

Der Kernel enthält die Information darüber:

- wie Funktionen verglichen werden
- welche Funktionen einfach oder komplex sind
- welcher Feature Space verwendet wird

---

# Warum sind Hilberträume nützlich?

## Geometrische Interpretation

Viele ML-Algorithmen beruhen auf:

- Abständen
- Winkeln
- Projektionen

Diese benötigen ein inneres Produkt.

---

## Lineare Modelle in großen Räumen

Ein Modell:

$$
f(x)=w^Tx
$$

wird im Hilbertraum:

$$
f(x)=\langle w,x\rangle_{\mathcal{H}}
$$

Dadurch können lineare Methoden auf komplexen Daten angewendet werden.

---

## Optimierung

Viele Lernverfahren suchen:

- minimale Norm
- optimale Projektion
- kleinsten Abstand

Diese Konzepte existieren natürlich in Hilberträumen.

---

# Zusammenhang mit SVMs

SVMs suchen eine optimale Trennfläche:

$$
w^Tx+b=0
$$

Im Feature Space:

$$
\langle w,\phi(x)\rangle+b=0
$$

Der Kernel ermöglicht:

$$
\langle\phi(x),\phi(x')\rangle
$$

ohne $\phi$ explizit zu berechnen.

---

# Häufige Fehler & Missverständnisse

## ❌ Ein Hilbertraum ist nur ein Raum mit vielen Dimensionen

Nicht ganz.

Ein Hilbertraum benötigt zusätzlich:

- inneres Produkt
- Vollständigkeit

---

## ❌ Jeder Vektorraum ist ein Hilbertraum

Nein.

Nicht jeder Vektorraum besitzt ein geeignetes inneres Produkt.

---

## ❌ Hilberträume sind nur theoretische Mathematik

Nein.

Sie bilden die Grundlage vieler Methoden:

- SVMs
- Kernel Regression
- Gaussian Processes
- Signalverarbeitung

---

# Praktische Implikationen

## Feature Spaces können sehr groß sein

Kernel Methods erlauben:

- unendlichdimensionale Räume
- ohne explizite Berechnung

---

## Geometrie bleibt erhalten

Auch in unendlichdimensionalen Räumen bleiben Konzepte wie:

- Abstand
- Winkel
- Projektion

erhalten.

---

## Komplexität wird kontrolliert

Die Norm im Hilbertraum kann als Maß für Modellkomplexität dienen.

Beispiel:

$$
||w||_{\mathcal{H}}
$$

kleinere Norm:

↓

einfacheres Modell

↓

bessere Generalisierung

---

# Zusammenfassung

| Begriff | Bedeutung |
|---|---|
| Hilbertraum | Vollständiger Raum mit innerem Produkt |
| Inneres Produkt | Definiert Winkel und Ähnlichkeit |
| Norm | Beschreibt Länge eines Elements |
| Vollständigkeit | Grenzwerte bleiben im Raum |
| Feature Space | Raum transformierter Daten |
| RKHS | Hilbertraum von Funktionen mit Kernel |
| Kernel | Inneres Produkt im Feature Space |

---

# Siehe auch

- Kernel Methods & RKHS
- Support Vector Machines
- Regularisierung
- Structural Risk Minimization
- Funktionalanalysis

---

# Ressourcen & Referenzen

**Bücher**

- Understanding Machine Learning – Shalev-Shwartz & Ben-David
- Functional Analysis – Walter Rudin

**Konzepte**

- Hilbert (1912) – Grundlegung der Theorie der Hilberträume
- Mercer’s Theorem
- Reproducing Kernel Hilbert Spaces (Aronszajn, 1950)

---

# Übungsaufgaben

**Aufgabe 1**

Welche Rolle spielt das innere Produkt in einem Hilbertraum?

---

**Aufgabe 2**

Warum sind Hilberträume für Kernel Methods wichtig?

---

**Aufgabe 3**

Was bedeutet Vollständigkeit eines Hilbertraums?

---

**Aufgabe 4**

Warum kann ein Feature Space in Machine Learning unendlichdimensional sein?