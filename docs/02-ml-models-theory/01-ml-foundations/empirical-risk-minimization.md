# Empirical Risk Minimization (ERM)

## TL;DR (30 Sekunden)

**Empirical Risk Minimization (ERM)** ist das grundlegende Prinzip, nach dem viele Machine-Learning-Algorithmen trainiert werden.

**Kernidee:**

Wir wählen das Modell, das den Fehler auf den Trainingsdaten minimiert:

$$
\hat{h}
=
\arg\min_{h \in \mathcal{H}}
\hat{R}(h)
$$

Dabei gilt:

- $\hat{h}$ = gelerntes Modell
- $\mathcal{H}$ = Hypothesenklasse (alle möglichen Modelle)
- $\hat{R}(h)$ = empirischer Fehler (Trainingsfehler)

Die Hoffnung:

> Ein Modell mit kleinem Trainingsfehler besitzt auch einen kleinen Fehler auf neuen Daten.

---

**Praktische Bedeutung:**

ERM erklärt:

- Warum Training auf einem Datensatz funktioniert
- Wie Machine Learning mathematisch formuliert wird
- Warum Generalisierung nicht automatisch garantiert ist
- Warum Regularisierung und Modellkomplexität wichtig sind

---

# Motivation & Intuition

Beim Machine Learning haben wir:

- Trainingsdaten
- eine Menge möglicher Modelle
- eine Loss-Funktion

Beispiel:

Wir möchten Bilder klassifizieren.

Dazu betrachten wir viele mögliche Modelle:

$$
h_1, h_2, h_3, ..., h_n
$$

Jedes Modell macht Vorhersagen und erhält einen Fehlerwert.

Das Ziel:

> Finde das Modell mit dem kleinsten Fehler auf den vorhandenen Daten.

---

# Empirical Risk Minimization

ERM bedeutet:

> Wähle das Modell, das den durchschnittlichen Fehler auf den Trainingsdaten minimiert.

Formal:

$$
\hat{h}
=
\arg\min_{h \in \mathcal{H}}
\hat{R}(h)
$$

Dabei ist:

$$
\hat{R}(h)
=
\frac{1}{n}
\sum_{i=1}^{n}
L(h(x_i),y_i)
$$

---

## Bedeutung der Terme

| Begriff | Bedeutung |
|---|---|
| $h$ | Modell/Hypothese |
| $\mathcal{H}$ | Menge aller erlaubten Modelle |
| $n$ | Anzahl Trainingsbeispiele |
| $L$ | Loss-Funktion |
| $\hat{R}(h)$ | durchschnittlicher Trainingsfehler |

---

# Empirical Risk vs. True Risk

ERM optimiert nur den Trainingsfehler.

Aber eigentlich interessiert uns:

> Wie gut ist das Modell auf unbekannten Daten?

---

## Empirical Risk

Der Fehler auf bekannten Trainingsdaten:

$$
\hat{R}(h)
=
\frac{1}{n}
\sum_{i=1}^{n}
L(h(x_i),y_i)
$$

Dieser Wert kann berechnet werden.

---

## True Risk

Der erwartete Fehler auf neuen Daten:

$$
R(h)
=
E[L(h(X),Y)]
$$

Dieser Wert ist normalerweise unbekannt.

---

## Das eigentliche Ziel

Eigentlich möchten wir:

$$
\hat{h}
=
\arg\min_h R(h)
$$

also das Modell mit minimalem echten Fehler.

Das Problem:

Die Datenverteilung ist unbekannt.

Deshalb verwenden wir ERM:

$$
\arg\min_h \hat{R}(h)
$$

und hoffen:

$$
\hat{R}(h)
\approx
R(h)
$$

---

# Warum funktioniert Training auf einem Datensatz?

Die zentrale Frage:

> Warum darf man anhand weniger Beispiele ein Modell für unbekannte Daten lernen?

Die Antwort:

Durch statistische Annahmen und genügend Daten.

---

## Annahme: Daten sind repräsentativ

Die Trainingsdaten stammen aus derselben Verteilung wie zukünftige Daten:

$$
(x_i,y_i)
\sim P(X,Y)
$$

Dann enthält der Trainingsdatensatz Informationen über die zugrunde liegende Aufgabe.

---

## Gesetz der großen Zahlen

Mit mehr Daten nähert sich der Durchschnitt dem Erwartungswert:

Viele Beispiele:

$$
\frac{1}{n}
\sum_i L(h(x_i),y_i)
$$

wird ähnlich wie:

$$
E[L(h(X),Y)]
$$

Also:

$$
\hat{R}(h)
\rightarrow
R(h)
$$

---

# Problem: ERM alleine reicht nicht

ERM minimiert nur den Trainingsfehler.

Das kann zu Overfitting führen.

---

Beispiel:

Ein neuronales Netz mit Millionen Parametern kann Trainingsdaten auswendig lernen.

Dann:

$$
\hat{R}(h)=0
$$

aber:

$$
R(h)>0
$$

Das Modell generalisiert schlecht.

---

# Zusammenhang mit Uniform Convergence

Damit ERM funktioniert, benötigen wir:

$$
\sup_{h\in\mathcal{H}}
|
R(h)-\hat{R}(h)
|
\rightarrow 0
$$

Das bedeutet:

Der Trainingsfehler approximiert den Testfehler für alle Modelle.

Dann gilt:

Kleiner Trainingsfehler

↓

kleiner Testfehler

---

# Generalisierungsgrenzen für ERM

Eine typische Generalisierungsschranke lautet:

$$
R(h)
\leq
\hat{R}(h)
+
\text{Komplexitätsterm}
+
\text{Fehlerterm}
$$


Die Differenz:

$$
R(h)-\hat{R}(h)
$$

nennt man Generalisierungsfehler.

---

## Interpretation

Der Testfehler besteht aus:

### Trainingsfehler

Wie gut passt das Modell die Daten?

$$
\hat{R}(h)
$$

+

### Komplexitätsstrafe

Wie mächtig ist die Hypothesenklasse?

Beispiele:

- VC-Dimension
- Rademacher Complexity

+

### Datenunsicherheit

Wie viele Beispiele haben wir?

Mehr Daten:

↓

kleinere Unsicherheit

---

# ERM und Modellkomplexität

ERM sucht immer das beste Modell innerhalb einer Hypothesenklasse.

Die Wahl von $\mathcal{H}$ ist daher entscheidend.

---

## Kleine Hypothesenklasse

Beispiel:

Lineare Modelle

Vorteile:

- wenig Overfitting
- wenige Daten notwendig

Nachteile:

- eventuell zu wenig flexibel

---

## Große Hypothesenklasse

Beispiel:

Tiefe neuronale Netze

Vorteile:

- sehr flexibel
- können komplexe Muster lernen

Nachteile:

- mehr Daten notwendig
- höheres Overfitting-Risiko

---

# Regularized Empirical Risk Minimization

In der Praxis verwendet man häufig eine Erweiterung:

$$
\hat{h}
=
\arg\min_h
(
\hat{R}(h)
+
\lambda \Omega(h)
)
$$

Dabei:

- $\hat{R}(h)$ = Trainingsfehler
- $\Omega(h)$ = Komplexitätsstrafe
- $\lambda$ = Stärke der Regularisierung

---

Beispiele:

- L2-Regularisierung
- Weight Decay
- Dropout
- Early Stopping

---

Die Idee:

Nicht nur:

> Passe die Trainingsdaten möglichst gut an.

sondern:

> Passe die Trainingsdaten gut an, aber bleibe möglichst einfach.

---

# Beispiel

Angenommen wir haben zwei Modelle:

## Modell A

Train Error:

$$
\hat{R}(A)=1\%
$$

Komplexität:

niedrig

---

## Modell B

Train Error:

$$
\hat{R}(B)=0\%
$$

Komplexität:

sehr hoch

---

ERM würde Modell B wählen.

Aber mit Generalisierungsbetrachtung kann Modell A besser sein:

$$
R(A)<R(B)
$$

weil Modell B überangepasst ist.

---

# Zusammenhang mit PAC Learning

PAC Learning beschreibt, wann Lernen theoretisch möglich ist.

PAC bedeutet:

**Probably Approximately Correct**

Ein Algorithmus soll mit hoher Wahrscheinlichkeit ein fast optimales Modell finden.

ERM ist einer der wichtigsten Ansätze dafür:

Daten

↓

ERM

↓

Modell mit kleinem empirischen Fehler

↓

kleiner echter Fehler (wenn Generalisierung gilt)

---

# Häufige Fehler & Missverständnisse

## ❌ ERM minimiert automatisch den Testfehler

Nein.

ERM minimiert nur:

$$
\hat{R}(h)
$$

nicht:

$$
R(h)
$$

---

## ❌ Das Modell mit dem kleinsten Trainingsfehler ist immer das beste

Nein.

Ein komplexes Modell kann overfitten.

---

## ❌ Mehr Parameter sind immer besser

Nein.

Mehr Parameter erhöhen oft die Modellkomplexität.

---

# Praktische Implikationen

## Training ist eine Approximation

Man kann den echten Fehler nicht direkt optimieren.

Deshalb:

Trainingsdaten

↓

Empirical Risk

↓

Approximation des True Risk

---

## Datenmenge bestimmt Lernfähigkeit

Mehr Daten helfen, weil:

- empirischer Fehler stabiler wird
- Generalisierungsfehler sinkt

---

## Validation Sets sind notwendig

Da ERM nur Trainingsdaten betrachtet, nutzt man:

- Validation Set
- Cross Validation
- Test Set

um Generalisierung zu prüfen.

---

# Zusammenfassung

| Begriff | Bedeutung |
|---|---|
| ERM | Minimierung des Trainingsfehlers |
| Empirical Risk | Fehler auf Trainingsdaten |
| True Risk | Erwarteter Fehler auf neuen Daten |
| Hypothesenklasse | Menge möglicher Modelle |
| Generalisierung | Leistung auf unbekannten Daten |
| Overfitting | Trainingsfehler klein, Testfehler groß |
| Regularisierung | Kontrolle der Modellkomplexität |

---

# Siehe auch

- Uniform Convergence
- VC-Dimension & Rademacher Complexity
- PAC Learning
- Structural Risk Minimization
- Regularisierung

---

# Ressourcen & Referenzen

**Bücher**

- Understanding Machine Learning – Shalev-Shwartz & Ben-David
- Foundations of Machine Learning – Mohri, Rostamizadeh & Talwalkar

**Konzepte**

- Vapnik – Statistical Learning Theory
- Vapnik & Chervonenkis – Theory of Pattern Recognition

---

# Übungsaufgaben

**Aufgabe 1**

Was optimiert ERM direkt: True Risk oder Empirical Risk?

---

**Aufgabe 2**

Warum kann ein Modell mit perfektem Trainingsfehler trotzdem schlecht generalisieren?

---

**Aufgabe 3**

Welche Rolle spielt die Hypothesenklasse bei ERM?

---

**Aufgabe 4**

Warum benötigt ERM Generalisierungsgrenzen?