# Regularisierung aus theoretischer Perspektive

## TL;DR (30 Sekunden)

**Regularisierung** verhindert, dass ein Modell die Trainingsdaten zu stark auswendig lernt.

Die Grundidee:

> Ein gutes Modell soll nicht nur einen kleinen Trainingsfehler haben, sondern auch möglichst einfach sein.

Statt nur den Trainingsfehler zu minimieren:

$$
\min_h \hat{R}(h)
$$

optimiert man:

$$
\min_h
\left(
\hat{R}(h)
+
\lambda \Omega(h)
\right)
$$

Dabei gilt:

- $\hat{R}(h)$ = Fehler auf Trainingsdaten
- $\Omega(h)$ = Komplexität des Modells
- $\lambda$ = Stärke der Regularisierung

---

**Praktische Bedeutung:**

Regularisierung erklärt:

- Warum einfachere Modelle oft besser generalisieren
- Warum L1/L2-Regularisierung Overfitting reduziert
- Wie Structural Risk Minimization funktioniert

---

# Motivation & Intuition

Beim Training möchte ein Modell den Trainingsfehler minimieren.

Ohne Regularisierung:

$$
\hat{h}
=
\arg\min_h \hat{R}(h)
$$

Problem:

Ein sehr komplexes Modell kann die Trainingsdaten perfekt anpassen.

Beispiel:

Ein neuronales Netz kann:

- echte Muster lernen ✓
- Zufälligkeiten im Datensatz lernen ✗

Dann gilt:

$$
\hat{R}(h) \approx 0
$$

aber:

$$
R(h) \gg 0
$$

Das Modell generalisiert schlecht.

---

# Grundidee der Regularisierung

Regularisierung fügt eine Strafe für komplexe Modelle hinzu.

Die Optimierung wird:

$$
\hat{h}
=
\arg\min_h
(
\hat{R}(h)
+
\lambda\Omega(h)
)
$$

Das Modell muss also zwei Ziele erfüllen:

1. Trainingsdaten gut erklären
2. Einfach bleiben

---

# Zusammenhang mit Generalisierung

Die zentrale Idee der Lerntheorie:

> Komplexere Modelle können mehr Funktionen darstellen und benötigen daher mehr Daten.

Eine typische Generalisierungsschranke:

$$
R(h)
\leq
\hat{R}(h)
+
\text{Komplexität}
$$

Regularisierung reduziert den Komplexitätsterm.

---

Beispiel:

Ohne Regularisierung:

Kleiner Trainingsfehler

+

hohe Komplexität

=

schlechte Generalisierung


Mit Regularisierung:

Etwas größerer Trainingsfehler

+

kleinere Komplexität

=

bessere Generalisierung

---

# L2-Regularisierung

Die häufigste Form der Regularisierung ist L2-Regularisierung.

Dabei wird die Größe der Gewichte bestraft:

$$
\Omega(w)
=
||w||_2^2
=
\sum_i w_i^2
$$

Die Optimierung lautet:

$$
\min_w
(
\hat{R}(w)
+
\lambda
\sum_i w_i^2
)
$$

---

## Intuition

Große Gewichte werden bestraft.

Ohne Regularisierung:
w1 = 20
w2 = -15
w3 = 30

Mit L2:
w1 = 2
w2 = -1.5
w3 = 3

Das Modell wird weniger empfindlich gegenüber einzelnen Merkmalen.

---

## Warum hilft L2 bei Generalisierung?

Große Gewichte können dazu führen, dass kleine Änderungen in den Eingaben große Änderungen in der Ausgabe erzeugen.

Kleinere Gewichte:

- stabileres Modell
- weniger empfindlich gegenüber Rauschen
- kleinere effektive Komplexität

Dadurch:

$$
R(h)
\approx
\hat{R}(h)
$$

---

# L1-Regularisierung

Bei L1-Regularisierung wird die absolute Größe der Gewichte bestraft:

$$
\Omega(w)
=
||w||_1
=
\sum_i |w_i|
$$

Die Optimierung:

$$
\min_w
(
\hat{R}(w)
+
\lambda
\sum_i |w_i|
)
$$

---

## Intuition

L1 führt häufig dazu, dass viele Gewichte exakt null werden.

Beispiel:

Vorher:
Feature A: 0.8
Feature B: 0.03
Feature C: 0.5
Feature D: 0.01

Nach L1:
Feature A: 0.8
Feature B: 0
Feature C: 0.5
Feature D: 0

Das Modell nutzt nur wichtige Features.

---

## Warum hilft L1 bei Generalisierung?

L1 reduziert die Anzahl effektiv verwendeter Features.

Dadurch:

- einfacheres Modell
- weniger Overfitting
- bessere Interpretierbarkeit

---

# L1 vs. L2 Regularisierung

| | L1 | L2 |
|-|-|-|
| Strafe | $||w||_1$ | $||w||_2^2$ |
| Effekt | viele Gewichte werden 0 | Gewichte werden kleiner |
| Ergebnis | sparsames Modell | stabiles Modell |
| Vorteil | Feature Selection | robuste Anpassung |

---

# Structural Risk Minimization (SRM)

**Structural Risk Minimization** erweitert die Idee der Regularisierung.

Die zentrale Idee:

> Wähle nicht nur das Modell mit dem kleinsten Trainingsfehler, sondern das Modell mit dem besten Verhältnis aus Fehler und Komplexität.

---

Anstatt eine einzige Hypothesenklasse zu betrachten:

$$
\mathcal{H}
$$

betrachtet man eine Folge verschachtelter Klassen:

$$
\mathcal{H}_1
\subset
\mathcal{H}_2
\subset
...
\subset
\mathcal{H}_n
$$

---

Beispiel:

$$
\mathcal{H}_1
$$

Lineare Modelle

↓

$$
\mathcal{H}_2
$$

kleine neuronale Netze

↓

$$
\mathcal{H}_3
$$

große neuronale Netze

---

# Idee von SRM

Eine größere Hypothesenklasse:

Vorteil:

- kleiner Trainingsfehler möglich

Nachteil:

- höhere Komplexität

---

SRM sucht den besten Kompromiss:

$$
\text{True Risk}
\approx
\text{Train Error}
+
\text{Komplexitätsstrafe}
$$

---

# Zusammenhang zwischen Regularisierung und SRM

Regularisierung ist eine praktische Umsetzung von SRM.

Beide verfolgen dieselbe Idee:

> Vermeide unnötig komplexe Modelle.

---

Beispiele:

| Methode | Theoretische Interpretation |
|-|-|
| L2-Regularisierung | Begrenze Gewichtskomplexität |
| L1-Regularisierung | Begrenze Anzahl aktiver Features |
| Dropout | Reduziere effektive Modellkomplexität |
| Early Stopping | Verhindere zu lange Anpassung |

---

# Beispiel

Zwei Modelle:

## Modell A

Train Error:

$$
1\%
$$

Komplexität:

hoch


## Modell B

Train Error:

$$
3\%
$$

Komplexität:

niedrig


Ohne Regularisierung gewinnt A.

Mit Generalisierungsbetrachtung kann B besser sein:

$$
R(B)<R(A)
$$

weil B weniger overfitten kann.

---

# Häufige Fehler & Missverständnisse

## ❌ Regularisierung macht das Modell immer besser

Nein.

Zu starke Regularisierung kann zu Underfitting führen.

---

## ❌ Regularisierung reduziert immer den Trainingsfehler

Nein.

Sie akzeptiert bewusst einen höheren Trainingsfehler, um besser zu generalisieren.

---

## ❌ Ein komplexeres Modell ist immer schlechter

Nein.

Komplexe Modelle können sehr gut funktionieren, wenn genug Daten vorhanden sind.

---

# Praktische Implikationen

## Regularisierung kontrolliert Modellkomplexität

Besonders wichtig bei:

- kleinen Datensätzen
- vielen Features
- verrauschten Daten

---

## Hyperparameter $\lambda$

Die Stärke der Regularisierung wird über $\lambda$ gesteuert.

Kleines $\lambda$:

- wenig Regularisierung
- flexibleres Modell

Großes $\lambda$:

- stärker eingeschränkt
- einfacheres Modell

---

## Cross Validation hilft bei der Wahl

Da die optimale Regularisierung datenabhängig ist:

- verschiedene $\lambda$ testen
- Validierungsdaten verwenden

---

# Zusammenfassung

| Begriff | Bedeutung |
|---|---|
| Regularisierung | Bestraft komplexe Modelle |
| L1-Regularisierung | Erzeugt sparse Modelle |
| L2-Regularisierung | Verkleinert Gewichte |
| Structural Risk Minimization | Optimiert Fehler + Komplexität |
| Overfitting | Modell lernt Trainingsdaten zu genau |
| Generalisierung | Gute Leistung auf neuen Daten |

---

# Siehe auch

- Empirical Risk Minimization (ERM)
- Uniform Convergence
- VC-Dimension & Rademacher Complexity
- Bias-Variance Trade-off
- Overfitting

---

# Ressourcen & Referenzen

**Bücher**

- Understanding Machine Learning – Shalev-Shwartz & Ben-David
- The Elements of Statistical Learning – Hastie, Tibshirani & Friedman

**Konzepte**

- Vapnik – Statistical Learning Theory
- Structural Risk Minimization (SRM)

---

# Übungsaufgaben

**Aufgabe 1**

Warum kann ein Modell mit höherem Trainingsfehler besser generalisieren?

---

**Aufgabe 2**

Was ist der Unterschied zwischen L1- und L2-Regularisierung?

---

**Aufgabe 3**

Warum kann Regularisierung Overfitting reduzieren?

---

**Aufgabe 4**

Wie hängt Structural Risk Minimization mit Regularisierung zusammen?
