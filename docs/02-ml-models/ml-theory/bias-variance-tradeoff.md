# Bias-Variance Trade-off

## TL;DR (30 Sekunden)

Der **Bias-Variance Trade-off** beschreibt den Zusammenhang zwischen Modellkomplexität und Generalisierung.

Die zentrale Idee:

> Ein Modell muss komplex genug sein, um die Struktur der Daten zu lernen, aber einfach genug bleiben, um nicht nur Zufälligkeiten auswendig zu lernen.

Der erwartete Fehler eines Modells lässt sich vereinfacht zerlegen:

$$
Error
=
Bias^2
+
Variance
+
Noise
$$

Dabei gilt:

- **Bias** = Fehler durch zu starke Vereinfachung
- **Variance** = Fehler durch zu starke Anpassung an Trainingsdaten
- **Noise** = unvermeidbares Rauschen in den Daten

---

**Praktische Bedeutung:**

Der Bias-Variance Trade-off erklärt:

- Warum einfache Modelle underfitten
- Warum komplexe Modelle overfitten
- Warum Regularisierung die Generalisierung verbessern kann
- Warum die optimale Modellgröße von den Daten abhängt

---

# Motivation & Intuition

Beim Machine Learning möchten wir ein Modell finden, das auf unbekannten Daten gut funktioniert.

Wir optimieren aber nur auf einem endlichen Trainingsdatensatz:

$$
\hat{R}(h)
$$

und hoffen:

$$
\hat{R}(h)\approx R(h)
$$

Das Problem:

Die Wahl der Modellkomplexität beeinflusst diese Annäherung.

---

# Zusammenhang zwischen Modellkomplexität und Fehler

Wenn ein Modell komplexer wird:

- kann es mehr Muster lernen
- kann aber auch mehr Zufälligkeiten lernen

Typischer Verlauf:
Fehler
^
|
|
| 
| \ Test Error
| ______/
| 
| 
|
|---------------------> Modellkomplexität

  Bias     Variance

---

# Bias

## Definition

**Bias** beschreibt den Fehler, der entsteht, weil ein Modell zu starke Vereinfachungen macht.

Ein Modell mit hohem Bias besitzt starke Annahmen über die Daten und kann wichtige Zusammenhänge nicht darstellen.

---

Formal:

$$
Bias(x)
=
E[\hat{f}(x)]-f(x)
$$

---

## Beispiel

Angenommen, die echte Beziehung ist:

$$
y=x^2
$$

Wir verwenden aber ein lineares Modell:

$$
y=ax+b
$$

Das Modell kann die quadratische Struktur niemals perfekt darstellen.

Es entsteht ein systematischer Fehler.

---

## Ursachen für hohen Bias

- Modell ist zu einfach
- zu wenige Features
- zu starke Regularisierung
- falsche Modellannahmen

---

## Symptome

Ein Modell mit hohem Bias:

- hat hohen Trainingsfehler
- hat hohen Testfehler

Dies nennt man:

**Underfitting**

---

# Variance

## Definition

**Variance** beschreibt, wie stark ein Modell auf Änderungen im Trainingsdatensatz reagiert.

Ein Modell mit hoher Variance lernt Details des Trainingsdatensatzes, inklusive Zufälligkeiten.

---

Intuition:

Trainingsdaten A:

$$
h_A
$$

Trainingsdaten B:

$$
h_B
$$

Bei hoher Variance gilt:

$$
h_A \neq h_B
$$

Das Modell verändert sich stark, obwohl die Daten nur leicht anders sind.

---

## Beispiel

Ein Entscheidungsbaum mit sehr großer Tiefe:

- lernt jeden einzelnen Trainingspunkt
- erzeugt sehr spezifische Regeln

Er funktioniert gut auf Trainingsdaten, aber schlecht auf neuen Daten.

---

## Ursachen für hohe Variance

- Modell zu komplex
- zu wenige Trainingsdaten
- zu viele Parameter

---

## Symptome

Ein Modell mit hoher Variance:

- hat sehr kleinen Trainingsfehler
- hat großen Testfehler

Dies nennt man:

**Overfitting**

---

# Bias und Variance im Vergleich

| | Hoher Bias | Hohe Variance |
|-|-|-|
| Modell | zu einfach | zu komplex |
| Training Error | hoch | niedrig |
| Test Error | hoch | hoch |
| Problem | Underfitting | Overfitting |
| Lösung | komplexeres Modell | Regularisierung / mehr Daten |

---

# Bias-Variance Zerlegung

Der erwartete quadratische Fehler kann zerlegt werden:

$$
E[(y-\hat{f}(x))^2]
=
Bias^2
+
Variance
+
Noise
$$

---

## Bias²

Beschreibt:

> Wie weit liegt das durchschnittliche Modell vom echten Zusammenhang entfernt?

---

## Variance

Beschreibt:

> Wie stark verändert sich das Modell bei neuen Trainingsdaten?

---

## Noise

Beschreibt:

> Fehler, der unabhängig vom Modell nicht entfernt werden kann.

Beispiele:

- Messfehler
- zufällige Schwankungen

---

# Beispiel

Angenommen, wir trainieren drei Modelle:

## Modell A: Lineares Modell

Train Error:

$$
10\%
$$

Test Error:

$$
12\%
$$

Eigenschaft:

- stabil
- aber zu einfach

→ hoher Bias

---

## Modell B: Mittlere Komplexität

Train Error:

$$
3\%
$$

Test Error:

$$
4\%
$$

Eigenschaft:

- lernt Muster
- generalisiert gut

→ guter Trade-off

---

## Modell C: Sehr komplexes Modell

Train Error:

$$
0\%
$$

Test Error:

$$
20\%
$$

Eigenschaft:

- merkt sich Trainingsdaten

→ hohe Variance

---

# Zusammenhang mit Regularisierung

Regularisierung verändert die Modellkomplexität.

Ohne Regularisierung:

$$
\min_h \hat{R}(h)
$$

Mit Regularisierung:

$$
\min_h
(
\hat{R}(h)
+
\lambda\Omega(h)
)
$$

---

Die Regularisierung erhöht leicht den Bias, reduziert aber die Variance.

Ziel:

> Einen besseren Gesamtfehler erreichen.

---

Beispiel:

L2-Regularisierung:

- kleinere Gewichte
- einfacheres Modell
- weniger empfindlich gegenüber Trainingsdaten

---

# Zusammenhang mit Trainingsdaten

Mehr Daten reduzieren typischerweise die Variance.

Warum?

Ein komplexes Modell sieht mehr Beispiele und kann besser zwischen:

- echten Mustern
- Zufälligkeiten

unterscheiden.

---

Bei kleinen Datensätzen:

- hohe Variance wahrscheinlicher

Bei großen Datensätzen:

- komplexere Modelle möglich

---

# Zusammenhang mit Modellwahl

Der Bias-Variance Trade-off erklärt, warum es kein universell bestes Modell gibt.

Ein Modell muss zur Aufgabe passen.

Beispiele:

| Situation | Geeigneter Ansatz |
|-|-|
| Wenige Daten | einfachere Modelle |
| Viele Daten | komplexere Modelle |
| Viele Features | Regularisierung |
| Sehr komplexe Muster | flexible Modelle |

---

# Zusammenhang mit Deep Learning

Tiefe neuronale Netze besitzen:

- sehr viele Parameter
- hohe Ausdruckskraft

Nach klassischer Theorie müssten sie stark overfitten.

In der Praxis funktioniert Training trotzdem oft gut durch:

- große Datenmengen
- Regularisierung
- Optimierungsverfahren
- spezielle Eigenschaften neuronaler Netze

---

# Häufige Fehler & Missverständnisse

## ❌ Ein kleiner Trainingsfehler bedeutet ein gutes Modell

Nein.

Ein Modell kann Trainingsdaten auswendig lernen.

---

## ❌ Ein einfaches Modell ist immer besser

Nein.

Ein zu einfaches Modell kann wichtige Muster verpassen.

---

## ❌ Komplexe Modelle sind grundsätzlich schlecht

Nein.

Mit genügend Daten können komplexe Modelle sehr gut generalisieren.

---

# Praktische Implikationen

## Modellkomplexität wählen

Man sollte Modelle vergleichen:

- Trainingsfehler
- Validierungsfehler
- Testfehler

---

## Regularisierung verwenden

Hilft besonders bei:

- kleinen Datensätzen
- vielen Features
- komplexen Modellen

---

## Mehr Daten helfen gegen Variance

Mehr Trainingsdaten:

↓

weniger abhängig von einzelnen Beispielen

↓

bessere Generalisierung

---

# Zusammenfassung

| Begriff | Bedeutung |
|---|---|
| Bias | Fehler durch zu einfache Annahmen |
| Variance | Empfindlichkeit gegenüber Trainingsdaten |
| Bias-Variance Trade-off | Balance zwischen Einfachheit und Flexibilität |
| Underfitting | hoher Bias |
| Overfitting | hohe Variance |
| Regularisierung | reduziert Variance durch Komplexitätskontrolle |
| Noise | unvermeidbarer Datenfehler |

---

# Siehe auch

- Empirical Risk Minimization (ERM)
- Uniform Convergence
- Regularisierung
- Structural Risk Minimization
- VC-Dimension & Rademacher Complexity

---

# Ressourcen & Referenzen

**Bücher**

- The Elements of Statistical Learning – Hastie, Tibshirani & Friedman
- Understanding Machine Learning – Shalev-Shwartz & Ben-David

**Konzepte**

- Bias-Variance Decomposition
- Statistical Learning Theory

---

# Übungsaufgaben

**Aufgabe 1**

Warum besitzt ein sehr komplexes Modell häufig eine hohe Variance?

---

**Aufgabe 2**

Warum kann Regularisierung helfen, obwohl der Trainingsfehler steigt?

---

**Aufgabe 3**

Was ist der Unterschied zwischen Underfitting und Overfitting?

---

**Aufgabe 4**

Warum können mehr Trainingsdaten die Generalisierung verbessern?
