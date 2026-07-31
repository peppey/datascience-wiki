# VC-Dimension & Rademacher Complexity

## TL;DR (30 Sekunden)

Die **VC-Dimension** und die **Rademacher Complexity** sind Maße für die Komplexität einer Hypothesenklasse.

**Kernidee:** Je komplexer ein Modell ist, desto mehr Daten benötigt es, um zuverlässig zu generalisieren. Beide Maße helfen dabei, diesen Zusammenhang mathematisch zu beschreiben.

- **VC-Dimension:** Misst, wie viele Punkte eine Hypothesenklasse beliebig klassifizieren kann.
- **Rademacher Complexity:** Misst, wie gut eine Hypothesenklasse zufälliges Rauschen anpassen kann.

**Praktische Bedeutung:**
- Warum overfitten große Modelle leichter?
- Warum benötigen komplexere Modelle mehr Trainingsdaten?
- Wie entstehen Generalisierungsgarantien?

---

# Motivation & Intuition

Angenommen, du möchtest zwischen Katzen und Hunden unterscheiden.

Du hast zwei mögliche Modelle:

- eine lineare Entscheidungsgrenze
- ein sehr tiefes neuronales Netz

Beide können den Trainingsdatensatz perfekt lernen.

**Frage:** Welches Modell wird auf neuen Daten besser funktionieren?

Die Trainingsgenauigkeit beantwortet diese Frage nicht.

Stattdessen müssen wir wissen, **wie flexibel die jeweilige Hypothesenklasse ist.**

Eine sehr flexible Hypothesenklasse kann nahezu jede beliebige Zuordnung der Trainingsdaten lernen – sogar zufälliges Rauschen.

Die Lern-theorie versucht deshalb nicht nur den Trainingsfehler zu betrachten, sondern auch die **Komplexität des Modells**.

---

# Kernkonzepte

## Was ist eine Hypothesenklasse?

Eine Hypothesenklasse $\mathcal{H}$ ist die Menge aller Modelle, die ein Lernalgorithmus auswählen kann.

Beispiele:

| Modell | Hypothesenklasse |
|---------|------------------|
| Lineare Regression | Alle Geraden |
| Entscheidungsbaum | Alle möglichen Bäume |
| Neuronales Netz | Alle möglichen Gewichte |
| SVM | Alle Hyperplanes |

Nicht ein einzelnes Modell ist entscheidend, sondern die gesamte Menge möglicher Modelle.

---

## Warum spielt Komplexität eine Rolle?

Je größer die Hypothesenklasse,

- desto leichter findet man ein Modell mit kleinem Trainingsfehler,
- desto größer wird aber auch die Gefahr des Overfittings.

Ein extremes Beispiel:

Eine Hypothesenklasse, die **jede beliebige Zuordnung** lernen kann, erreicht immer 100 % Trainingsgenauigkeit.

Sie generalisiert deshalb aber nicht zwangsläufig gut.

Die Lern-theorie versucht deshalb einen Kompromiss zwischen

- Trainingsfehler
- Modellkomplexität

zu finden.

---

# Die VC-Dimension

Die **VC-Dimension (Vapnik-Chervonenkis-Dimension)** ist das klassische Maß für die Komplexität einer Hypothesenklasse.

## Shattering

Die zentrale Idee lautet:

> Wie viele Punkte kann eine Hypothesenklasse beliebig klassifizieren?

Kann für jede mögliche Label-Zuordnung ein Modell gefunden werden, sagt man:

> Die Punkte werden **geshattered**.

---

## Formale Definition

Die VC-Dimension einer Hypothesenklasse ist die maximale Anzahl von Punkten, die vollständig geshattered werden können.

Kurz:

> VC-Dimension = maximale Anzahl beliebig klassifizierbarer Punkte.

---

# Beispiele

## Beispiel 1: Schwellenwert auf einer Zahlengeraden

Betrachte die Funktion

```
x < t  → Klasse A
x ≥ t → Klasse B
```

Mit einem Schwellenwert lassen sich

- ein Punkt
- zwei Punkte

beliebig klassifizieren.

Drei Punkte funktionieren jedoch nicht mehr.

⇒ **VC-Dimension = 2**

---

## Beispiel 2: Lineare Klassifikation in 2D

Eine Gerade kann

drei beliebige Punkte trennen.

Vier beliebige Punkte jedoch nicht.

⇒ VC-Dimension = 3

---

## Beispiel 3: Hyperplanes

Für lineare Klassifikatoren im d-dimensionalen Raum gilt

$$
VC = d+1
$$

Beispiele:

| Dimension | VC-Dimension |
|------------|--------------|
| 1D | 2 |
| 2D | 3 |
| 10D | 11 |

---

# Zusammenhang zur Sample Complexity

Die VC-Dimension ersetzt bei unendlichen Hypothesenklassen deren Größe.

Für viele Lernverfahren gilt näherungsweise

$$
m =
O\left(
\frac{VC}{\epsilon^2}
\log\frac1\delta
\right)
$$

Dabei gilt:

- größere VC-Dimension
- ⇒ mehr Trainingsdaten nötig

---

# Intuition

Man kann sich die VC-Dimension wie den Freiheitsgrad eines Modells vorstellen.

Ein Modell mit

- kleiner VC-Dimension

kann nur einfache Zusammenhänge lernen.

Ein Modell mit

- großer VC-Dimension

kann sehr komplexe Muster darstellen.

Mehr Flexibilität bedeutet gleichzeitig mehr Risiko für Overfitting.

---

# Grenzen der VC-Dimension

Die VC-Dimension erklärt viele klassische Lernalgorithmen sehr gut.

Bei modernen Deep-Learning-Modellen stößt sie jedoch an Grenzen.

Neuronale Netze besitzen häufig

- Millionen Parameter
- extrem hohe VC-Dimension

und generalisieren trotzdem überraschend gut.

Die VC-Dimension liefert deshalb oft sehr pessimistische Schranken.

Moderne Lern-theorie verwendet daher häufig feinere Komplexitätsmaße.

---

# Rademacher Complexity

Die wichtigste Alternative ist die **Rademacher Complexity**.

Statt zu fragen

> "Wie viele Punkte können beliebig klassifiziert werden?"

fragt sie

> "Wie gut kann die Hypothesenklasse zufälliges Rauschen anpassen?"

---

## Die Idee

Man versieht Trainingsdaten zufällig mit Labels

```
+1
-1
+1
-1
...
```

Ein gutes Modell sollte dieses reine Rauschen **nicht** perfekt lernen können.

Kann eine Hypothesenklasse selbst zufällige Labels sehr gut erklären,

ist sie vermutlich zu komplex.

---

## Interpretation

- kleine Rademacher Complexity
    - geringe Modellkomplexität
    - gute Generalisierung

- große Rademacher Complexity
    - hohe Flexibilität
    - erhöhtes Overfitting-Risiko

Sie misst also direkt die Fähigkeit zum Overfitting.

---

# VC-Dimension vs. Rademacher Complexity

| VC-Dimension | Rademacher Complexity |
|---------------|----------------------|
| rein kombinatorisch | datenabhängig |
| betrachtet schlimmsten Fall | berücksichtigt den konkreten Datensatz |
| klassische Lerntheorie | moderne Lerntheorie |
| oft pessimistisch | meist deutlich schärfere Schranken |

Die VC-Dimension beschreibt die maximale Komplexität einer Hypothesenklasse.

Die Rademacher Complexity beschreibt die tatsächlich genutzte Komplexität auf einem bestimmten Datensatz.

---

# Zusammenhang mit Generalisierung

Für fast alle Generalisierungsschranken gilt vereinfacht:

```
Testfehler

≤ Trainingsfehler
+ Komplexität
+ Unsicherheit durch endliche Daten
```

Die Komplexität wird dabei beispielsweise durch

- VC-Dimension
- Rademacher Complexity

beschrieben.

Je größer dieser Term wird,

desto stärker können Trainings- und Testfehler voneinander abweichen.

---

# Häufige Fehler & Missverständnisse

## ❌ Große VC-Dimension bedeutet schlechtes Modell

Nein.

Sie bedeutet lediglich,

dass mehr Daten benötigt werden.

Große Modelle können hervorragend generalisieren, wenn ausreichend Daten vorhanden sind.

---

## ❌ Kleine VC-Dimension ist immer besser

Nicht unbedingt.

Eine zu kleine Hypothesenklasse kann wichtige Zusammenhänge gar nicht darstellen.

Es entsteht **Underfitting**.

---

## ❌ Rademacher Complexity ersetzt die VC-Dimension

Nein.

Beide messen Modellkomplexität,

jedoch auf unterschiedliche Weise.

Die VC-Dimension bleibt ein zentrales theoretisches Werkzeug.

---

# Praktische Implikationen

## Mehr Daten helfen komplexen Modellen

Je komplexer ein Modell,

desto mehr Trainingsdaten werden benötigt.

---

## Regularisierung reduziert die effektive Komplexität

L1-, L2-Regularisierung oder Early Stopping beschränken die tatsächlich genutzte Modellkomplexität.

Dadurch verbessert sich häufig die Generalisierung.

---

## Modellwahl ist ein Kompromiss

Ein zu einfaches Modell

→ Underfitting

Ein zu komplexes Modell

→ Overfitting

Die optimale Komplexität liegt meist zwischen beiden Extremen.

---

# Zusammenfassung

| Begriff | Bedeutung |
|-----------|-----------|
| VC-Dimension | Maximale Anzahl geshatterter Punkte |
| Shattering | Alle möglichen Labelings sind realisierbar |
| Rademacher Complexity | Fähigkeit, zufällige Labels anzupassen |
| Hohe Komplexität | Mehr Flexibilität, aber mehr Overfitting |
| Niedrige Komplexität | Weniger Overfitting, aber Gefahr von Underfitting |

---

# Siehe auch

- PAC Learning
- Uniform Convergence
- Empirical Risk Minimization
- Structural Risk Minimization
- Regularisierung

---

# Ressourcen & Referenzen

**Bücher**

- Understanding Machine Learning – Shalev-Shwartz & Ben-David
- Foundations of Machine Learning – Mohri, Rostamizadeh & Talwalkar

**Paper**

- Vapnik & Chervonenkis (1971)
- Bartlett & Mendelson (2002) – Rademacher and Gaussian Complexities

---

# Übungsaufgaben

**Aufgabe 1**

Warum besitzt ein linearer Klassifikator im zweidimensionalen Raum eine VC-Dimension von 3?

---

**Aufgabe 2**

Warum benötigt eine Hypothesenklasse mit größerer VC-Dimension im Allgemeinen mehr Trainingsdaten?

---

**Aufgabe 3**

Welche Vorteile besitzt die Rademacher Complexity gegenüber der VC-Dimension bei modernen Machine-Learning-Modellen?