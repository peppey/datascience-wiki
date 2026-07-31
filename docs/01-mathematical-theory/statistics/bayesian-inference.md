# Bayesian Inference

## TL;DR (30 Sekunden)

**Bayesian Inference** beschreibt, wie man vorhandenes Wissen mit neuen Daten kombiniert, um Wahrscheinlichkeiten zu aktualisieren.

Die zentrale Idee:

> Neue Beobachtungen verändern unsere Überzeugung über ein Modell oder einen Parameter.

Die Grundlage ist der **Satz von Bayes**:

$$
P(\theta|D)
=
\frac{P(D|\theta)P(\theta)}
{P(D)}
$$

Dabei:

- $\theta$ = unbekannter Parameter / Modell
- $D$ = beobachtete Daten
- $P(\theta)$ = Prior (Vorwissen)
- $P(D|\theta)$ = Likelihood (Wahrscheinlichkeit der Daten)
- $P(\theta|D)$ = Posterior (aktualisiertes Wissen)

---

**Praktische Bedeutung:**

Bayesian Inference erklärt:

- Wie Unsicherheit in ML berücksichtigt werden kann
- Warum Vorwissen hilfreich sein kann
- Wie Parameterverteilungen statt einzelne Werte gelernt werden
- Grundlagen von Bayesian Neural Networks und Gaussian Processes

---

# Motivation & Intuition

In klassischem Machine Learning lernen wir meistens einen festen Parameter:

Beispiel:

$$
\theta = 5
$$

Ein Bayesianischer Ansatz sagt:

> Wir kennen den Parameter nicht exakt, sondern haben eine Verteilung darüber.

Beispiel:

$$
\theta \sim P(\theta)
$$

Nach neuen Daten aktualisieren wir diese Verteilung.

---

Vor Daten:
Unsicherheit über θ
|
|
breite Verteilung

Nach Daten:
mehr Information
|
|
konzentriertere Verteilung

---

# Der Satz von Bayes

Die zentrale Gleichung:

$$
P(\theta|D)
=
\frac{P(D|\theta)P(\theta)}
{P(D)}
$$

beschreibt:

$$
\text{Posterior}
=
\frac{\text{Likelihood}\cdot\text{Prior}}
{\text{Evidence}}
$$

---

## Prior

Der Prior beschreibt unser Wissen vor Beobachtung der Daten.

Beispiel:

Wir wissen aus Erfahrung:

> Eine Münze ist wahrscheinlich ungefähr fair.

Dann:

$$
P(\theta)
$$

beschreibt diese Annahme.

---

## Likelihood

Die Likelihood beschreibt:

> Wie wahrscheinlich sind die beobachteten Daten für ein bestimmtes Modell?

Beispiel:

Wir werfen eine Münze 100-mal.

Für verschiedene Werte von $\theta$:

- $\theta=0.5$ passt gut
- $\theta=0.1$ passt schlecht

---

## Posterior

Der Posterior kombiniert:

- Vorwissen
- neue Daten

und ergibt:

$$
P(\theta|D)
$$

---

# Beispiel: Münzwurf

Wir möchten die Wahrscheinlichkeit $\theta$ für Kopf bestimmen.

Vorwissen:

$$
P(\theta)
$$

Wir werfen die Münze:
K K Z K K K Z ...

Die Daten liefern:

$$
P(D|\theta)
$$

Bayes kombiniert beides:

$$
P(\theta|D)
\propto
P(D|\theta)P(\theta)
$$

Nach vielen Würfen wird der Posterior immer konzentrierter.

---

# Bayesian Learning vs. Klassisches ML

## Maximum Likelihood Estimation (MLE)

Klassisches ML sucht den wahrscheinlichsten Parameter:

$$
\hat{\theta}
=
\arg\max_\theta P(D|\theta)
$$

Es wird nur die Likelihood betrachtet.

---

## Maximum A Posteriori (MAP)

Bayesianischer Ansatz mit Prior:

$$
\hat{\theta}
=
\arg\max_\theta
P(\theta|D)
$$

Durch Bayes:

$$
=
\arg\max_\theta
P(D|\theta)P(\theta)
$$

---

Unterschied:

| Methode | Verwendet |
|-|-|
| MLE | nur Daten |
| MAP | Daten + Vorwissen |
| Bayesian Inference | gesamte Posterior-Verteilung |

---

# Zusammenhang mit Regularisierung

MAP-Schätzung ist eng mit Regularisierung verbunden.

Beispiel:

L2-Regularisierung:

$$
\min
Loss
+
\lambda ||w||^2
$$

entspricht einer Annahme:

$$
w\sim N(0,\sigma^2)
$$

also einem Gaussian Prior.

---

Intuition:

Regularisierung bedeutet:

> Wir bevorzugen bestimmte Parameter, bevor wir Daten sehen.

Das ist genau ein Bayesianischer Prior.

---

# Bayesian Inference in Machine Learning

## Bayesian Regression

Normale Regression:

Wir lernen:

$$
w
$$

Bayesian Regression:

Wir lernen:

$$
P(w|D)
$$

also eine Verteilung über mögliche Gewichte.

---

Vorteil:

Wir erhalten:

- Vorhersage
- Unsicherheit der Vorhersage

---

# Predictive Distribution

Bei Bayesian Prediction betrachten wir nicht nur einen Punktwert.

Wir berechnen:

$$
P(y|x,D)
$$

also:

> Welche Ausgaben sind für diese Eingabe wahrscheinlich?

---

Die Vorhersage berücksichtigt Unsicherheit:

- Modellunsicherheit
- Datenrauschen

---

# Bayesian Neural Networks

Normale neuronale Netze:

$$
w=\text{fester Parameter}
$$

Bayesian Neural Networks:

$$
w\sim P(w)
$$

Die Gewichte werden als Wahrscheinlichkeitsverteilungen modelliert.

---

Vorteile:

- Unsicherheit über Vorhersagen
- robustere Entscheidungen
- wichtig bei sicherheitskritischen Anwendungen

---

Nachteile:

- mathematisch und rechnerisch aufwendiger
- Posterior oft schwer direkt berechenbar

---

# Zusammenhang mit Gaussian Processes

Gaussian Processes sind ein weiteres Bayesianisches Modell.

Statt Parameter zu lernen:

$$
\theta
$$

betrachtet man direkt eine Verteilung über Funktionen:

$$
f(x)
$$

---

Ein Gaussian Process definiert:

- Mittelwertfunktion
- Kovarianzstruktur

und erzeugt eine Verteilung über mögliche Funktionen.

---

Anwendung:

- Regression
- kleine Datensätze
- Unsicherheitsabschätzung

---

# Approximate Bayesian Inference

In vielen Modellen ist der echte Posterior schwer zu berechnen.

Grund:

$$
P(\theta|D)
$$

kann sehr komplex sein.

Daher verwendet man Näherungen:

---

## Markov Chain Monte Carlo (MCMC)

Idee:

Ziehe viele Stichproben aus dem Posterior.

---

## Variational Inference

Idee:

Approximieren den Posterior durch eine einfachere Verteilung.

Beispiel:

$$
q(\theta)\approx P(\theta|D)
$$

---

# Zusammenhang mit Generalisierung

Bayesianische Methoden können Generalisierung verbessern durch:

- Einbeziehen von Vorwissen
- Begrenzung plausibler Modelle
- Modellierung von Unsicherheit

---

Der Prior wirkt ähnlich wie Regularisierung:

Zu viele mögliche Modelle:

↓

höheres Overfitting-Risiko

Prior:

↓

kleinerer effektiver Suchraum

↓

bessere Generalisierung

---

# Häufige Fehler & Missverständnisse

## ❌ Bayesian bedeutet subjektiv und ungenau

Nein.

Bayesian Inference ist eine mathematische Methode.

Der Prior muss nur explizit angegeben werden.

---

## ❌ Der Posterior ist immer besser als MLE

Nicht unbedingt.

Ein schlechter Prior kann Ergebnisse verschlechtern.

---

## ❌ Bayesian Models brauchen immer kleine Datenmengen

Nein.

Sie können auch bei großen Problemen verwendet werden, aber oft mit Approximationen.

---

# Praktische Implikationen

## Unsicherheit ist ein zusätzliches Ergebnis

Normale ML-Modelle:
Input → Vorhersage

Bayesian Modelle:
Input → Vorhersage + Unsicherheit

---

## Vorwissen kann genutzt werden

Besonders hilfreich bei:

- wenigen Daten
- teuren Experimenten
- medizinischen Anwendungen

---

## Regularisierung hat Bayesianische Interpretation

Viele klassische ML-Techniken können als Bayesianische Annahmen interpretiert werden.

---

# Zusammenfassung

| Begriff | Bedeutung |
|---|---|
| Bayesian Inference | Aktualisierung von Wissen durch Daten |
| Prior | Vorwissen über Parameter |
| Likelihood | Wahrscheinlichkeit der Daten |
| Posterior | Aktualisiertes Wissen nach Daten |
| MLE | Parameter nur aus Daten schätzen |
| MAP | Daten + Prior verwenden |
| Bayesian Neural Network | Wahrscheinlichkeitsverteilungen über Gewichte |
| Unsicherheit | Teil der Vorhersage |

---

# Siehe auch

- Empirical Risk Minimization (ERM)
- Regularisierung
- Maximum Likelihood Estimation
- Gaussian Processes
- Bayesian Neural Networks
- Probabilistic Machine Learning

---

# Ressourcen & Referenzen

**Bücher**

- Pattern Recognition and Machine Learning – Christopher Bishop
- Probabilistic Machine Learning – Kevin Murphy

**Konzepte**

- Bayes (1763) – An Essay towards solving a Problem in the Doctrine of Chances
- Bayesian Neural Networks
- Variational Inference

---

# Übungsaufgaben

**Aufgabe 1**

Welche Rolle spielt der Prior in Bayesian Inference?

---

**Aufgabe 2**

Was ist der Unterschied zwischen MLE und MAP?

---

**Aufgabe 3**

Warum liefern Bayesianische Modelle Unsicherheitsinformationen?

---

**Aufgabe 4**

Wie hängt Regularisierung mit Bayesianischen Priors zusammen?
