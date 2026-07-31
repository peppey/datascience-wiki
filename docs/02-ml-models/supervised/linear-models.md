# Linear Models

## TL;DR (30 Sekunden)

**Lineare Modelle** gehören zu den grundlegendsten und wichtigsten Modellen im Machine Learning.

Die zentrale Idee:

> Eine Zielvariable wird als lineare Kombination der Eingabefeatures modelliert.

Allgemeine Form:

$$
f(x)=w^Tx+b
$$

Dabei:

- $x$ = Eingabevektor
- $w$ = Gewichte
- $b$ = Bias-Term

---

**Praktische Bedeutung:**

Lineare Modelle erklären:

- Grundlagen von Regression und Klassifikation
- Wie Features gewichtet werden
- Zusammenhang zwischen Optimierung und Machine Learning
- Basis vieler komplexerer Modelle

---

# Motivation & Intuition

Angenommen, wir möchten einen Hauspreis vorhersagen.

Features:

- Wohnfläche
- Anzahl Zimmer
- Lage

Ein lineares Modell nimmt an:

$$
Preis
=
w_1\cdot Fläche
+
w_2\cdot Zimmer
+
w_3\cdot Lage
+
b
$$

---

Das Modell lernt also:

> Welchen Einfluss hat jedes Feature auf die Vorhersage?

---

# Lineare Regression

Die **lineare Regression** ist eines der ältesten ML-Verfahren.

Ziel:

Eine kontinuierliche Variable vorhersagen.

Beispiele:

- Preisvorhersage
- Temperatur
- Umsatz
- Nachfrage

---

Das Modell:

$$
y=w^Tx+b
$$

---

Beispiel:

$$
Preis=
5000\cdot m^2+20000
$$

---

# Trainingsziel

Das Modell soll die Vorhersagefehler minimieren.

Typischer Loss:

**Mean Squared Error (MSE)**

$$
MSE=
\frac1n
\sum_{i=1}^{n}
(y_i-\hat y_i)^2
$$

---

Das Training sucht:

$$
\min_w
MSE
$$

---

# Optimierung

Die Parameter werden so angepasst, dass der Fehler kleiner wird.

Möglichkeiten:

- analytische Lösung
- Gradient Descent

---

## Normal Equation

Für kleine Probleme existiert eine geschlossene Lösung:

$$
w=(X^TX)^{-1}X^Ty
$$

---

## Gradient Descent

Bei großen Datenmengen verwendet man iterative Optimierung:

$$
w_{neu}
=
w-\eta\nabla L(w)
$$

---

# Lineare Klassifikation

Lineare Modelle können auch Klassifikation durchführen.

Die Entscheidung basiert auf:

$$
w^Tx+b
$$

---

Beispiel:

Binäre Klassifikation:

$$
y\in\{0,1\}
$$

Entscheidung:

Wenn:

$$
w^Tx+b>0
$$

dann:

Klasse 1

sonst:

Klasse 0

---

# Logistic Regression

Obwohl der Name "Regression" enthält, ist Logistic Regression ein Klassifikator.

Die Idee:

> Die lineare Ausgabe wird in eine Wahrscheinlichkeit umgewandelt.

---

Lineare Funktion:

$$
z=w^Tx+b
$$

Sigmoid-Funktion:

$$
\sigma(z)=\frac1{1+e^{-z}}
$$

---

Ergebnis:

$$
P(y=1|x)=\sigma(w^Tx+b)
$$

---

# Loss Functions

Lineare Modelle verwenden unterschiedliche Loss-Funktionen.

---

## Regression

Typisch:

### Mean Squared Error

$$
L=(y-\hat y)^2
$$

---

## Klassifikation

Typisch:

### Cross Entropy Loss

$$
L=
-y\log(\hat y)
-(1-y)\log(1-\hat y)
$$

---

# Regularisierung

Lineare Modelle können ebenfalls overfitten.

Eine Lösung:

> Beschränke die Größe der Gewichte.

---

# L2-Regularisierung (Ridge Regression)

Zusätzlicher Term:

$$
\lambda ||w||^2
$$

Optimierung:

$$
Loss+\lambda||w||^2
$$

---

Effekt:

- kleinere Gewichte
- weniger komplexes Modell
- bessere Generalisierung

---

# L1-Regularisierung (Lasso)

Penalty:

$$
\lambda||w||_1
$$

also:

$$
\lambda\sum_i |w_i|
$$

---

Effekt:

Einige Gewichte werden exakt:

$$
w_i=0
$$

---

Dadurch:

- Feature Selection
- sparsames Modell

---

# Bias-Variance Trade-off

Lineare Modelle haben typischerweise:

## Niedrige Varianz

Sie ändern sich wenig bei neuen Trainingsdaten.

---

## Höheren Bias

Wenn die Realität nicht linear ist, können sie zu einfach sein.

---

Beispiel:

Einfache lineare Grenze:

kann komplexe Muster nicht darstellen.

---

# Erweiterungen linearer Modelle

## Polynomial Regression

Man erweitert die Features:

Beispiel:

statt:

$$
x
$$

verwendet man:

$$
x,x^2,x^3
$$

---

Das Modell bleibt linear in den Parametern:

$$
y=w_1x+w_2x^2+b
$$

---

## Generalized Linear Models (GLMs)

Erweitern lineare Modelle durch:

- andere Verteilungen
- Link-Funktionen

Beispiele:

- Logistic Regression
- Poisson Regression

---

# Lineare Modelle und neuronale Netze

Eine einzelne Neurone berechnet:

$$
y=\sigma(w^Tx+b)
$$

Ohne Aktivierungsfunktion ist ein neuronales Netz nur ein lineares Modell.

---

Mehrere Schichten mit Aktivierungen ermöglichen:

- Nichtlinearität
- komplexe Funktionen

---

# Zusammenhang mit Optimierung

Lineare Modelle sind ein wichtiges Beispiel für mathematische Optimierung.

Training:

$$
\min_w L(w)
$$

---

Viele ML-Methoden basieren auf ähnlichen Prinzipien:

- Gradient Descent
- Konvexe Optimierung
- Regularisierung

---

# Zusammenhang mit Generalisierung

Lineare Modelle generalisieren oft gut, weil ihre Komplexität begrenzt ist.

---

Theoretisch:

kleinere Hypothesenklasse

↓

geringere Generalisierungsfehler

↓

weniger Daten notwendig

---

Zusammenhang mit:

- VC-Dimension
- Regularisierung
- Structural Risk Minimization

---

# Vorteile linearer Modelle

## Einfach und schnell

Training ist sehr effizient.

---

## Interpretierbar

Gewichte zeigen:

Welche Features wichtig sind.

---

## Gute Baseline

Viele ML-Projekte starten mit:

- Linear Regression
- Logistic Regression

---

# Nachteile linearer Modelle

## Nur lineare Zusammenhänge

Sie können komplexe Muster schlecht erfassen.

---

## Feature Engineering notwendig

Nichtlineare Beziehungen müssen oft manuell erzeugt werden.

---

## Ausreißer können problematisch sein

Besonders bei MSE-Loss.

---

# Vergleich mit anderen Modellen

| Modell | Stärke |
|-|-|
| Lineare Modelle | Einfachheit, Interpretierbarkeit |
| Trees | Nichtlineare Muster |
| SVM | Maximale Margin |
| Neural Networks | Sehr flexible Funktionen |
| Boosting | Hohe Performance auf Tabellendaten |

---

# Häufige Fehler & Missverständnisse

## ❌ Linear bedeutet nur eine Gerade

Nein.

Lineare Modelle können viele Features besitzen:

$$
w^Tx+b
$$

---

## ❌ Lineare Modelle sind zu einfach für ML

Nein.

Viele reale Probleme sind ausreichend linear.

---

## ❌ Logistic Regression ist ein Regressionsmodell

Nein.

Sie wird hauptsächlich zur Klassifikation verwendet.

---

# Praktische Implikationen

## Gute erste Wahl

Lineare Modelle sind oft der erste Vergleichspunkt.

---

## Interpretierbarkeit

Besonders wichtig in:

- Medizin
- Finanzen
- Wissenschaft

---

## Skalierung

Features sollten oft normalisiert werden:

$$
x'=\frac{x-\mu}{\sigma}
$$

besonders bei Regularisierung.

---

# Zusammenfassung

| Begriff | Bedeutung |
|---|---|
| Lineares Modell | Ausgabe als gewichtete Summe von Features |
| Linear Regression | Vorhersage kontinuierlicher Werte |
| Logistic Regression | Wahrscheinlichkeitsbasierte Klassifikation |
| Gewicht | Einfluss eines Features |
| Bias | Verschiebung der Funktion |
| L1-Regularisierung | Erzeugt Sparse Modelle |
| L2-Regularisierung | Verkleinert Gewichte |
| Gradient Descent | Optimierungsverfahren |

---

# Siehe auch

- Logistic Regression
- Regularisierung
- Gradient Descent
- Convex Optimization
- SVM
- Bias-Variance Trade-off
- Empirical Risk Minimization

---

# Ressourcen & Referenzen

**Bücher**

- Introduction to Statistical Learning – James et al.
- The Elements of Statistical Learning – Hastie, Tibshirani & Friedman

**Konzepte**

- Linear Regression
- Generalized Linear Models
- Ridge Regression
- Lasso Regression

---

# Übungsaufgaben

**Aufgabe 1**

Warum können lineare Modelle trotz ihrer Einfachheit sehr leistungsfähig sein?

---

**Aufgabe 2**

Was ist der Unterschied zwischen Ridge und Lasso Regression?

---

**Aufgabe 3**

Warum wird Logistic Regression für Klassifikation verwendet?

---

**Aufgabe 4**

Wie beeinflusst Regularisierung die Generalisierung eines linearen Modells?
