# Tree-based Methods

## TL;DR (30 Sekunden)

**Tree-based Methods** sind Machine-Learning-Verfahren, die Entscheidungen hierarchisch in Form eines Baumes treffen.

Die zentrale Idee:

> Teile den Datenraum schrittweise durch Regeln auf, bis möglichst homogene Gruppen entstehen.

Beispiele:

- Decision Trees
- Random Forests
- Gradient Boosted Trees (GBDT)
- XGBoost
- LightGBM

---

**Praktische Bedeutung:**

Tree-based Methods erklären:

- Wie nichtlineare Zusammenhänge ohne Feature Engineering gelernt werden können
- Warum Ensemble-Methoden sehr leistungsfähig sind
- Wie komplexe Modelle durch Kombination vieler einfacher Modelle entstehen
- Eine der wichtigsten Modellklassen für tabellarische Daten

---

# Motivation & Intuition

Ein Entscheidungsbaum trifft Entscheidungen ähnlich wie ein Mensch.

Beispiel:

Vorhersage, ob ein Kunde ein Produkt kauft:
      Einkommen > 50k?
         /       \
       Ja         Nein
      /             \
Alter < 30? Nein
/ 
Ja Nein
|
Kauf

---

Der Baum zerlegt den Datenraum durch einfache Regeln:

$$
x_j < threshold
$$

bis eine Entscheidung möglich ist.

---

# Decision Trees

Ein **Decision Tree** besteht aus:

- Knoten
- Kanten
- Blättern

---

## Aufbau

## Root Node

Startpunkt des Baums.

Enthält alle Trainingsdaten.

---

## Internal Nodes

Entscheidungsregeln:

Beispiel:

$$
x_1 < 5
$$

---

## Leaf Nodes

Endgültige Vorhersage:

- Klasse
- numerischer Wert

---

# Training eines Entscheidungsbaums

Das Training besteht darin:

> Finde die besten Splits, um die Daten möglichst gut aufzuteilen.

---

Beispiel:

Feature:

$$
x=\text{Alter}
$$

Mögliche Splits:

$$
x<20
$$

oder:

$$
x<40
$$

Der beste Split wird ausgewählt.

---

# Split-Kriterien

Ein Split soll die Unreinheit reduzieren.

---

## Gini Impurity

Häufig bei Klassifikation:

$$
Gini
=
1-\sum_i p_i^2
$$

Dabei:

- $p_i$ = Anteil einer Klasse

---

Perfekte Trennung:

$$
Gini=0
$$

---

## Entropy

Alternative:

$$
H(X)
=
-\sum_i p_i\log(p_i)
$$

---

Der Baum maximiert typischerweise:

$$
Information Gain
$$

also die Reduktion der Unsicherheit.

---

# Regression Trees

Bei Regression sagt ein Blatt einen Wert vorher.

Beispiel:

Hauspreise:
Wohnfläche > 100m²?
   |
   ↓
Preis = 600000€

---

Der Split minimiert typischerweise:

$$
MSE
=
\frac1n
\sum_i(y_i-\hat y_i)^2
$$

---

# Overfitting bei Entscheidungsbäumen

Ein Baum kann immer weiter wachsen:
Tiefe 1
|
Tiefe 5
|
Tiefe 20
|
Ein Blatt pro Datenpunkt

---

Ein sehr tiefer Baum:

- passt perfekt auf Trainingsdaten
- lernt Rauschen
- generalisiert schlecht

---

Das ist:

**Overfitting**

---

# Regularisierung von Trees

Man begrenzt die Komplexität durch:

## Maximale Tiefe

$$
depth \leq d
$$

---

## Mindestanzahl Samples pro Blatt

Verhindert sehr spezifische Regeln.

---

## Pruning

Entfernt unnötige Äste nach dem Training.

---

# Random Forest

Ein **Random Forest** kombiniert viele Entscheidungsbäume.

Die Idee:

> Viele schwache, unterschiedliche Modelle ergeben zusammen ein starkes Modell.

---

Aufbau:
Tree 1

Tree 2 ---> Durchschnitt / Mehrheit
/
Tree 3

---

# Bagging

Random Forest verwendet:

**Bootstrap Aggregating**

Für jeden Baum:

1. Ziehe zufällige Trainingsstichprobe
2. Trainiere Baum
3. Kombiniere Ergebnisse

---

Bei Klassifikation:

Mehrheitsentscheidung:

$$
\hat y=
\text{majority vote}
$$

---

Bei Regression:

Mittelwert:

$$
\hat y=
\frac1T
\sum_t h_t(x)
$$

---

# Random Feature Selection

Zusätzlich wird bei jedem Split nur eine zufällige Feature-Auswahl betrachtet.

Dadurch:

- werden Bäume unterschiedlicher
- sinkt die Korrelation zwischen Modellen

---

Weniger Korrelation:

↓

bessere Ensemble-Leistung

---

# Gradient Boosted Trees

Gradient Boosting kombiniert viele kleine Bäume sequenziell.

Die Idee:

> Jeder neue Baum korrigiert die Fehler der bisherigen Modelle.

---

Beispiel:

Erster Baum:
Vorhersage grob

Zweiter Baum:
lernt Fehler des ersten

Dritter Baum:
verbessert Restfehler

---

# Boosting-Formulierung

Ein Modell wird schrittweise aufgebaut:

$$
F_m(x)
=
F_{m-1}(x)+\eta h_m(x)
$$

Dabei:

- $h_m$ = neuer Baum
- $\eta$ = Learning Rate

---

# XGBoost

**XGBoost** ist eine optimierte Variante von Gradient Boosting.

Verbesserungen:

- Regularisierung
- effiziente Berechnung
- bessere Split-Suche
- Umgang mit Missing Values

---

Besonders erfolgreich bei:

- Tabellendaten
- Wettbewerben
- Business-Anwendungen

---

# LightGBM und CatBoost

Weitere moderne Tree-Methoden:

## LightGBM

Eigenschaften:

- sehr schnell
- geeignet für große Datenmengen

---

## CatBoost

Eigenschaften:

- besonders gut für kategoriale Features
- benötigt weniger Feature Engineering

---

# Vergleich der Tree-Methoden

| Methode | Idee | Vorteil |
|-|-|-|
| Decision Tree | einzelner Baum | interpretierbar |
| Random Forest | viele unabhängige Bäume | robust |
| Gradient Boosting | sequenzielle Verbesserung | sehr hohe Genauigkeit |
| XGBoost | optimiertes Boosting | Standard für Tabellendaten |
| LightGBM | effizientes Boosting | große Datenmengen |
| CatBoost | kategoriale Features | wenig Vorverarbeitung |

---

# Zusammenhang mit Bias-Variance Trade-off

Tree-basierte Modelle zeigen den Trade-off sehr deutlich.

## Einzelner Baum

Hohe Varianz:

- empfindlich gegenüber Datenänderungen
- Overfitting möglich

---

## Random Forest

Reduziert Varianz:

- viele unterschiedliche Bäume
- Mittelwertbildung

---

## Boosting

Reduziert Bias:

- lernt schrittweise komplexere Muster

---

# Zusammenhang mit Ensemble Learning

Tree-basierte Methoden nutzen:

## Bagging

Viele Modelle parallel:

↓

reduziert Variance

Beispiel:

Random Forest

---

## Boosting

Modelle hintereinander:

↓

reduziert Bias

Beispiel:

XGBoost

---

# Vorteile von Tree-based Methods

## Keine Skalierung notwendig

Anders als:

- SVM
- neuronale Netze

benötigen Bäume meistens keine Normalisierung.

---

## Nichtlineare Zusammenhänge

Bäume lernen automatisch:

- Interaktionen
- Schwellenwerte
- komplexe Beziehungen

---

## Interpretierbarkeit

Einzelne Bäume können als Regeln gelesen werden.

---

# Nachteile

## Schlechte Extrapolation

Trees können schlecht Werte außerhalb des Trainingsbereichs vorhersagen.

---

## Einzelne Trees sind instabil

Kleine Datenänderungen können große Änderungen verursachen.

---

## Große Ensembles schwer interpretierbar

Random Forest und Boosting verlieren Transparenz.

---

# Zusammenhang mit Machine Learning Theorie

Tree-based Methods verbinden mehrere theoretische Konzepte:

## Modellkomplexität

Tiefe Bäume:

↓

höhere Komplexität

---

## Regularisierung

Beschränkung der Baumgröße:

↓

bessere Generalisierung

---

## Ensemble Learning

Kombination vieler Modelle:

↓

bessere Performance

---

# Häufige Fehler & Missverständnisse

## ❌ Mehr Bäume sind immer besser

Nein.

Zu viele oder zu komplexe Modelle können weiterhin overfitten.

---

## ❌ Entscheidungsbäume brauchen kein Tuning

Doch.

Wichtige Parameter:

- Tiefe
- Anzahl Bäume
- Learning Rate
- Regularisierung

---

## ❌ Tree-Modelle verstehen automatisch Kausalität

Nein.

Sie lernen Zusammenhänge, keine Ursachen.

---

# Praktische Implikationen

## Gute Wahl für Tabellendaten

Tree-based Methods gehören häufig zu den besten Methoden für:

- strukturierte Daten
- Business-Daten
- Kaggle-Probleme

---

## Feature Importance

Viele Tree-Modelle liefern:

- Feature Importance
- Split-Häufigkeiten

Aber:

Diese sind nicht automatisch kausale Aussagen.

---

## Hyperparameter sind entscheidend

Besonders:

- Baumtiefe
- Anzahl Bäume
- Learning Rate
- Regularisierung

---

# Zusammenfassung

| Begriff | Bedeutung |
|---|---|
| Decision Tree | hierarchische Entscheidungsregeln |
| Split | Aufteilung des Datenraums |
| Leaf | Endentscheidung |
| Random Forest | Ensemble vieler Trees |
| Bagging | parallele Kombination von Modellen |
| Boosting | sequenzielle Fehlerkorrektur |
| XGBoost | optimiertes Gradient Boosting |
| Overfitting | zu komplexe Baumstruktur |

---

# Siehe auch

- Bias-Variance Trade-off
- Ensemble Learning
- Regularisierung
- Gradient Descent
- Feature Engineering
- Statistical Learning Theory

---

# Ressourcen & Referenzen

**Bücher**

- The Elements of Statistical Learning – Hastie, Tibshirani & Friedman
- Introduction to Statistical Learning – James et al.

**Originalarbeiten**

- Breiman (2001) – Random Forests
- Friedman (2001) – Greedy Function Approximation: A Gradient Boosting Machine
- Chen & Guestrin (2016) – XGBoost: A Scalable Tree Boosting System

---

# Übungsaufgaben

**Aufgabe 1**

Warum neigen einzelne Entscheidungsbäume zu Overfitting?

---

**Aufgabe 2**

Wie reduziert ein Random Forest die Varianz?

---

**Aufgabe 3**

Was ist der Unterschied zwischen Bagging und Boosting?

---

**Aufgabe 4**

Warum sind Gradient Boosted Trees häufig sehr erfolgreich auf Tabellendaten?
