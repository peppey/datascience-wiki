# Uniform Convergence

## TL;DR (30 Sekunden)

**Uniform Convergence** beschreibt, wann der Trainingsfehler eines Modells zuverlässig den tatsächlichen Testfehler approximiert.

**Kernidee:**

Wenn genügend Daten vorhanden sind, soll gelten:

> Der Fehler auf den Trainingsdaten ist für alle Modelle ungefähr gleich dem erwarteten Fehler auf neuen Daten.

Formal:

$$
\sup_{h \in \mathcal{H}}
|R(h)-\hat{R}(h)|
\rightarrow 0
$$

Dabei gilt:

- $R(h)$ = echter Fehler (Test Error)
- $\hat{R}(h)$ = Trainingsfehler (Empirical Risk)
- $\mathcal{H}$ = Hypothesenklasse

**Praktische Bedeutung:**

Uniform Convergence erklärt:

- Wann generalisiert ein Modell?
- Warum reicht ein kleiner Trainingsfehler alleine nicht aus?
- Warum brauchen komplexe Modelle mehr Daten?

---

# Motivation & Intuition

Angenommen, wir trainieren ein Modell zur Bilderkennung.

Wir haben:

- Trainingsdaten
- eine große Menge möglicher Modelle

Das Training sucht das Modell mit dem kleinsten Trainingsfehler:

$$
\hat{h}
=
\arg\min_h \hat{R}(h)
$$

Die Hoffnung:

> Das Modell mit dem kleinsten Trainingsfehler hat auch einen kleinen Testfehler.

Aber das funktioniert nicht immer.

---

## Problem: Overfitting

Ein sehr komplexes Modell kann den Trainingsdatensatz perfekt auswendig lernen.

Beispiel:

Ein neuronales Netz merkt sich jedes Trainingsbild.

Dann gilt:

$$
\hat{R}(h)=0
$$

aber:

$$
R(h) \gg 0
$$

Der Trainingsfehler sagt also alleine nichts über die Generalisierung aus.

---

# Was bedeutet Uniform Convergence?

Die zentrale Frage der Lerntheorie lautet:

> Wie ähnlich sind Trainingsfehler und Testfehler?

Für ein einzelnes Modell ist das relativ einfach.

Wir betrachten:

$$
|R(h)-\hat{R}(h)|
$$

Uniform Convergence fordert aber mehr:

Die Abweichung soll für **alle Modelle gleichzeitig** klein sein.

Also:

$$
\forall h \in \mathcal{H}:
|R(h)-\hat{R}(h)| < \epsilon
$$

---

## Warum "uniform"?

Das Wort bedeutet:

> Die Schranke gilt überall gleichmäßig.

Nicht nur für ein einzelnes Modell:
Modell A:
Train Error ≈ Test Error ✓
Modell B:
Train Error ≈ Test Error ✓
Modell C:
Train Error ≈ Test Error ✓

sondern für die gesamte Hypothesenklasse:
Alle möglichen Modelle:
Train Error ≈ Test Error ✓

---

# Empirical Risk vs. True Risk

## Empirical Risk (Trainingsfehler)

Der Fehler auf den vorhandenen Daten:

$$
\hat{R}(h)
=
\frac{1}{n}
\sum_{i=1}^{n}
L(h(x_i),y_i)
$$

Dabei:

- $n$ = Anzahl Trainingsbeispiele
- $L$ = Loss Function


---

## True Risk (Testfehler)

Der erwartete Fehler auf neuen Daten:

$$
R(h)
=
E[L(h(X),Y)]
$$

Dieser Wert ist unbekannt, weil wir die gesamte Datenverteilung nicht kennen.

---

## Ziel des Lernens

Wir möchten:

$$
\hat{R}(h)
\approx
R(h)
$$

Wenn dies für alle Modelle gilt, können wir sicher sein:

Ein Modell mit kleinem Trainingsfehler besitzt auch einen kleinen Testfehler.

---

# Konzentrationsungleichungen

Uniform Convergence basiert auf sogenannten **Konzentrationsungleichungen**.

Sie beschreiben:

> Wie wahrscheinlich ist es, dass eine Zufallsvariable stark von ihrem Erwartungswert abweicht?

Die zentrale Idee:

Mit mehr Daten wird die Unsicherheit kleiner.

---

# Hoeffding's Inequality

Die wichtigste Konzentrationsungleichung im Machine Learning ist die **Hoeffding-Ungleichung**.

Sie sagt:

Wenn wir viele unabhängige Datenpunkte haben,

dann liegt der empirische Mittelwert mit hoher Wahrscheinlichkeit nahe am echten Mittelwert.

Formal:

$$
P(
|\hat{R}(h)-R(h)|>\epsilon
)
\leq
2e^{-2n\epsilon^2}
$$

---

## Interpretation

Die Wahrscheinlichkeit für eine große Abweichung fällt exponentiell:
Mehr Daten
↓
kleinere Unsicherheit
↓
Train Error ≈ Test Error

---

Beispiel:

Ein Modell wird auf

- 100 Datenpunkten
- 10.000 Datenpunkten

trainiert.

Bei 10.000 Datenpunkten ist es viel wahrscheinlicher, dass:

$$
\hat{R}(h)
\approx
R(h)
$$

---

# Chernoff Bounds

Die **Chernoff Bounds** sind eine allgemeinere Klasse von Konzentrationsungleichungen.

Sie verwenden die sogenannte Moment-generating Function:

$$
E[e^{\lambda X}]
$$

um Wahrscheinlichkeitsabschätzungen herzuleiten.

Die Idee:

> Extreme Abweichungen vom Erwartungswert sind sehr unwahrscheinlich.

---

## Zusammenhang zu Hoeffding

Hoeffding ist eine spezielle Konzentrationsungleichung.

Chernoff Bounds sind allgemeiner:
Konzentrationsungleichungen
    |
    |
    +-- Chernoff Bounds
    |
    +-- Hoeffding Inequality
    |
    +-- Bernstein Inequality

---

# Von einem Modell zu einer Hypothesenklasse

Die Hoeffding-Ungleichung gilt zunächst nur für ein fixes Modell.

Also:
Modell h auswählen
↓
Train Error ≈ Test Error

Beim Machine Learning wählen wir aber das beste Modell aus vielen Möglichkeiten:
Viele Modelle
↓
Training sucht bestes Modell
↓
Welches Modell gewinnt?

Wir brauchen daher eine Schranke für:

$$
\sup_{h\in\mathcal{H}}
|R(h)-\hat{R}(h)|
$$

---

# Union Bound

Eine einfache Möglichkeit ist die **Union Bound**.

Sie sagt:

Wenn viele Ereignisse jeweils unwahrscheinlich sind,

dann ist die Wahrscheinlichkeit, dass mindestens eines passiert:

höchstens die Summe der Einzelwahrscheinlichkeiten.

Formal:

$$
P(A_1 \cup ... \cup A_n)
\leq
\sum_i P(A_i)
$$

---

## Bedeutung für Machine Learning

Bei einer endlichen Hypothesenklasse:
Modell 1 → kleine Abweichung
Modell 2 → kleine Abweichung
Modell 3 → kleine Abweichung
...

können wir die Wahrscheinlichkeiten addieren.

Dadurch erhalten wir:

$$
P(
\exists h:
|R(h)-\hat{R}(h)|>\epsilon
)
$$

---

# Zusammenhang mit Modellkomplexität

Bei unendlich großen Hypothesenklassen funktioniert die einfache Union Bound nicht mehr.

Wir brauchen Komplexitätsmaße:

- VC-Dimension
- Rademacher Complexity

Diese beschreiben:

> Wie viele verschiedene Modelle effektiv betrachtet werden müssen.

---

# Generalisierungsschranke

Eine typische Generalisierungsschranke sieht so aus:

$$
R(h)
\leq
\hat{R}(h)
+
\text{Komplexität}
+
\text{Datenunsicherheit}
$$

Die zusätzlichen Terme beschreiben:

- wie groß die Hypothesenklasse ist
- wie viele Daten vorhanden sind

---

# Warum ist Uniform Convergence wichtig?

Wenn Uniform Convergence gilt:

$$
\sup_h |R(h)-\hat{R}(h)| < \epsilon
$$

dann folgt:

Das empirisch beste Modell ist fast genauso gut wie das theoretisch beste Modell.

Also:

$$
\hat{h}
=
\arg\min_h \hat{R}(h)
$$

liefert ungefähr:

$$
R(\hat{h})
\approx
\min_h R(h)
$$

---

# Beispiel

Vergleich zweier Hypothesenklassen:

## Kleine Hypothesenklasse
10 mögliche Modelle

Vorteile:

- wenig Overfitting
- schnelle Konvergenz

Nachteile:

- eventuell zu einfach

---

## Große Hypothesenklasse
Millionen mögliche Modelle

Vorteile:

- sehr flexibel

Nachteile:

- mehr Daten nötig
- größere Gefahr für Overfitting

---

# Zusammenhang mit VC-Dimension

Die VC-Dimension gibt eine obere Schranke für die notwendige Datenmenge.

Typisch:

$$
n
\propto
\frac{VC(\mathcal{H})}{\epsilon^2}
$$

Größere VC-Dimension bedeutet:

- größere Hypothesenklasse
- langsamere Konvergenz
- mehr Trainingsdaten benötigt

---

# Häufige Fehler & Missverständnisse

## ❌ Kleiner Trainingsfehler bedeutet automatisch gute Generalisierung

Nein.

Ein Modell kann Trainingsdaten auswendig lernen.

---

## ❌ Uniform Convergence bedeutet perfekte Vorhersagen

Nein.

Sie sagt nur:

Trainingsfehler und Testfehler sind ähnlich.

Beide können trotzdem schlecht sein.

---

## ❌ Mehr Daten lösen jedes Problem

Nicht immer.

Wenn die Hypothesenklasse ungeeignet ist, hilft mehr Daten nur begrenzt.

---

# Praktische Implikationen

## Große Modelle brauchen viele Daten

Große neuronale Netze besitzen hohe Komplexität.

Damit Uniform Convergence ungefähr gilt, benötigen sie viele Beispiele.

---

## Regularisierung reduziert effektive Komplexität

Methoden wie:

- Weight Decay
- Dropout
- Early Stopping

reduzieren die Menge effektiv möglicher Modelle.

---

## Validierung ist eine praktische Approximation

Da der echte Testfehler unbekannt ist, verwendet man:

- Validation Sets
- Cross Validation

um Generalisierung abzuschätzen.

---

# Zusammenfassung

| Begriff | Bedeutung |
|---|---|
| Uniform Convergence | Trainingsfehler nähert sich Testfehler für alle Modelle |
| True Risk | Erwarteter Fehler auf neuen Daten |
| Empirical Risk | Fehler auf Trainingsdaten |
| Hoeffding Inequality | Wahrscheinlichkeit großer Abweichungen |
| Chernoff Bounds | Allgemeine Konzentrationsabschätzungen |
| Union Bound | Kombination vieler Wahrscheinlichkeiten |
| VC-Dimension | Maß für Hypothesenklassen-Komplexität |
| Generalisierung | Gute Leistung auf unbekannten Daten |

---

# Siehe auch

- VC-Dimension & Rademacher Complexity
- PAC Learning
- Empirical Risk Minimization
- Structural Risk Minimization
- Regularisierung

---

# Ressourcen & Referenzen

**Bücher**

- Understanding Machine Learning – Shalev-Shwartz & Ben-David
- Foundations of Machine Learning – Mohri, Rostamizadeh & Talwalkar

**Konzepte**

- Hoeffding (1963) – Probability Inequalities for Sums of Bounded Random Variables
- Chernoff (1952) – A Measure of Asymptotic Efficiency for Tests of a Hypothesis

---

# Übungsaufgaben

**Aufgabe 1**

Warum reicht es nicht aus, nur den Trainingsfehler eines Modells zu betrachten?

---

**Aufgabe 2**

Was beschreibt die Hoeffding-Ungleichung intuitiv?

---

**Aufgabe 3**

Warum benötigt eine große Hypothesenklasse mehr Daten, damit Uniform Convergence gilt?

---

**Aufgabe 4**

Wie hängen Uniform Convergence und Overfitting zusammen?
