# PAC-Learning (Probably Approximately Correct)

## TL;DR (30 Sekunden)

**PAC-Learning** ist ein theoretisches Modell, das beschreibt, wann und unter welchen Bedingungen ein Algorithmus aus Beispieldaten zuverlässig lernen kann.

Die zentrale Idee:

> Ein Lernalgorithmus soll mit hoher Wahrscheinlichkeit eine Hypothese finden, deren Fehler nur geringfügig größer als der optimale Fehler ist.

PAC steht für:

- **Probably**: Mit hoher Wahrscheinlichkeit
- **Approximately**: Ungefähr korrekt
- **Correct**: Geringer Fehler

---

Formal:

Ein Algorithmus lernt eine Hypothesenklasse $\mathcal{H}$ PAC, wenn er mit Wahrscheinlichkeit mindestens:

$$
1-\delta
$$

eine Hypothese $h$ findet mit:

$$
R(h)\leq \epsilon
$$

Dabei:

- $\epsilon$ = erlaubter Fehler
- $\delta$ = Wahrscheinlichkeit, dass das Lernen fehlschlägt
- $R(h)$ = echter Fehler (True Risk)

---

**Praktische Bedeutung:**

PAC-Learning erklärt:

- Warum Lernen aus endlich vielen Daten möglich ist
- Wie viele Trainingsdaten benötigt werden
- Zusammenhang zwischen Modellkomplexität und Generalisierung
- Theoretische Grundlagen von Machine Learning

---

# Motivation & Intuition

Machine Learning versucht, aus Beispielen eine Regel zu lernen.

Wir erhalten:

Trainingsdaten:

$$
D=\{(x_1,y_1),...,(x_n,y_n)\}
$$

und suchen:

$$
h\in\mathcal{H}
$$

mit möglichst kleinem Fehler.

---

Das zentrale Problem:

Wir sehen nur endlich viele Beispiele.

Die Frage:

> Wann können wir sicher sein, dass unser Modell auch auf neuen Daten funktioniert?

PAC-Learning formalisiert genau diese Frage.

---

# Das PAC-Learning-Modell

Ein Lernproblem besteht aus:

## Eingaberaum

$$
X
$$

Mögliche Datenpunkte.

Beispiel:

- Bilder
- Texte
- Messwerte

---

## Labelraum

$$
Y
$$

Mögliche Ausgaben.

Beispiel:

$$
Y=\{0,1\}
$$

für Klassifikation.

---

## Hypothesenklasse

$$
\mathcal{H}
$$

Menge möglicher Modelle.

Beispiele:

- lineare Klassifikatoren
- Entscheidungsbäume
- neuronale Netze

---

## Datenverteilung

Die Daten stammen aus einer unbekannten Verteilung:

$$
D\sim P(X,Y)
$$

Der Lernalgorithmus kennt diese Verteilung nicht.

---

# Probably

"Probably" bedeutet:

Das Modell muss nicht immer perfekt lernen.

Es darf mit kleiner Wahrscheinlichkeit scheitern.

---

Diese Wahrscheinlichkeit wird durch:

$$
\delta
$$

beschrieben.

Beispiel:

$$
\delta=0.05
$$

bedeutet:

Mit 95% Wahrscheinlichkeit funktioniert die Garantie.

---

# Approximately

"Approximately" bedeutet:

Das Modell muss nicht perfekt sein.

Es genügt:

$$
R(h)\leq\epsilon
$$

---

Beispiel:

Perfekter Klassifikator:

$$
R(h)=0
$$

PAC-Lernen erlaubt:

$$
R(h)<0.01
$$

also 1% Fehler.

---

# Correct

"Correct" bezieht sich auf die Genauigkeit der gelernten Hypothese bezüglich der unbekannten Datenverteilung.

Nicht:

> Perfekte Anpassung an Trainingsdaten

sondern:

> Gute Leistung auf neuen Daten.

---

# Sample Complexity

Eine zentrale Frage:

> Wie viele Trainingsbeispiele benötigen wir?

Die benötigte Datenmenge heißt:

**Sample Complexity**

---

Sie hängt ab von:

- gewünschtem Fehler $\epsilon$
- gewünschter Sicherheit $\delta$
- Komplexität der Hypothesenklasse

---

Typische Form:

$$
n
\propto
\frac{1}{\epsilon}
\left(
\log\frac{1}{\delta}
+
Complexity(\mathcal{H})
\right)
$$

---

Interpretation:

Kleinere Fehlergrenze:

$$
\epsilon \downarrow
$$

benötigt:

$$
n\uparrow
$$

mehr Daten.

---

# Zusammenhang mit VC-Dimension

Die VC-Dimension misst die Komplexität einer Hypothesenklasse.

Für eine Klasse mit VC-Dimension:

$$
d
$$

gilt ungefähr:

$$
n
\propto
\frac{d+\log(1/\delta)}
{\epsilon}
$$

---

Bedeutung:

Größere Hypothesenklasse:

↓

höhere VC-Dimension

↓

mehr Daten notwendig

---

# PAC-Learning und ERM

Empirical Risk Minimization (ERM) sucht:

$$
\hat{h}
=
\arg\min_{h\in\mathcal{H}}
\hat{R}(h)
$$

also die Hypothese mit kleinstem Trainingsfehler.

---

Die PAC-Theorie untersucht:

Wann gilt:

$$
\hat{R}(h)\approx R(h)
$$

?

---

Wenn Uniform Convergence gilt:

$$
\sup_h
|R(h)-\hat{R}(h)|
<\epsilon
$$

dann kann ERM erfolgreich lernen.

---

# Agnostic PAC-Learning

Das klassische PAC-Modell nimmt oft an:

Es existiert eine perfekte Hypothese:

$$
h^*
$$

mit:

$$
R(h^*)=0
$$

---

In der Praxis ist das unrealistisch.

Beim **agnostic PAC-Learning** gibt es keine perfekte Lösung.

Der Algorithmus sucht:

$$
R(h)
\leq
\min_{h\in\mathcal{H}}R(h)+\epsilon
$$

---

Bedeutung:

Das Modell findet fast die beste mögliche Hypothese innerhalb der Klasse.

---

# PAC-Learning und Overfitting

PAC-Learning erklärt, warum ein kleiner Trainingsfehler nicht ausreicht.

Ein Modell kann:

Trainingsdaten perfekt lernen:

$$
\hat{R}(h)=0
$$

aber trotzdem schlecht generalisieren.

---

Die PAC-Theorie berücksichtigt:

- Modellkomplexität
- Datenmenge
- Generalisierungsfehler

---

# Beispiel

Angenommen:

Wir lernen einen Spam-Filter.

Hypothesenklasse:

- einfache Regeln

oder:

- extrem komplexe Regeln

---

Komplexes Modell:

- kann alle Trainingsmails perfekt klassifizieren
- benötigt aber viele Daten

---

Einfaches Modell:

- macht mehr Trainingsfehler
- generalisiert möglicherweise besser

---

PAC-Learning beschreibt den Zusammenhang:
Modellkomplexität
|
↓
benötigte Datenmenge
|
↓
Generalisierung

---

# Zusammenhang mit anderen Konzepten

## Uniform Convergence

Uniform Convergence liefert die theoretische Grundlage:

Train Error ≈ Test Error

---

## VC-Dimension

Misst:

Wie komplex ist eine Hypothesenklasse?

---

## Rademacher Complexity

Alternative Komplexitätsmessung für moderne ML-Modelle.

---

## Structural Risk Minimization

Idee:

Wähle nicht nur den kleinsten Trainingsfehler, sondern berücksichtige Modellkomplexität.

---

# PAC vs. klassisches Machine Learning

| | Klassisches ML | PAC-Learning |
|-|-|-|
| Ziel | gutes Modell finden | Lernbarkeit beweisen |
| Daten | praktisch | theoretisch modelliert |
| Fokus | Performance | Garantien |
| Fehler | empirisch | mathematisch beschränkt |

---

# Häufige Fehler & Missverständnisse

## ❌ PAC bedeutet, dass das Modell perfekt lernt

Nein.

Es garantiert nur:

- kleinen Fehler
- hohe Wahrscheinlichkeit

---

## ❌ Mehr Daten lösen jedes Problem

Nein.

Wenn die Hypothesenklasse ungeeignet ist, hilft mehr Daten wenig.

---

## ❌ PAC-Learning sagt, welches Modell man verwenden soll

Nein.

Es beschreibt Bedingungen für erfolgreiches Lernen.

---

# Praktische Implikationen

## Modellgröße und Datenmenge müssen zusammenpassen

Große Modelle benötigen typischerweise:

- mehr Daten
- stärkere Regularisierung

---

## Generalisierung ist messbar

PAC liefert eine theoretische Erklärung:

Warum Training auf Stichproben funktionieren kann.

---

## Komplexität kontrollieren

Methoden wie:

- Regularisierung
- Feature Selection
- Modellbeschränkungen

reduzieren effektive Komplexität.

---

# Zusammenfassung

| Begriff | Bedeutung |
|---|---|
| PAC-Learning | Theorie des Lernens aus Beispieldaten |
| Probably | Erfolg mit hoher Wahrscheinlichkeit |
| Approximately | kleiner erlaubter Fehler |
| Correct | gute Generalisierung |
| $\epsilon$ | Fehlertoleranz |
| $\delta$ | Fehlerwahrscheinlichkeit |
| Sample Complexity | benötigte Datenmenge |
| VC-Dimension | Komplexität der Hypothesenklasse |
| Agnostic PAC | Lernen ohne perfekte Hypothese |

---

# Siehe auch

- Empirical Risk Minimization (ERM)
- Uniform Convergence
- VC-Dimension
- Rademacher Complexity
- Structural Risk Minimization
- Bias-Variance Trade-off

---

# Ressourcen & Referenzen

**Bücher**

- Understanding Machine Learning – Shalev-Shwartz & Ben-David
- Foundations of Machine Learning – Mohri, Rostamizadeh & Talwalkar

**Originalarbeiten**

- Valiant (1984) – A Theory of the Learnable
- Vapnik & Chervonenkis – Statistical Learning Theory

---

# Übungsaufgaben

**Aufgabe 1**

Was bedeuten die Begriffe "Probably" und "Approximately" im PAC-Modell?

---

**Aufgabe 2**

Warum benötigt eine Hypothesenklasse mit hoher VC-Dimension mehr Daten?

---

**Aufgabe 3**

Wie hängt PAC-Learning mit ERM zusammen?

---

**Aufgabe 4**

Warum garantiert ein kleiner Trainingsfehler nicht automatisch PAC-Lernen?
