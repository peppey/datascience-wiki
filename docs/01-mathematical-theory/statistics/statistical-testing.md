# Statistical Testing

## TL;DR (30 Sekunden)

**Statistical Testing** (statistisches Testen) ist eine Methode, um anhand von Daten Entscheidungen über Hypothesen zu treffen.

Die zentrale Idee:

> Wir prüfen, ob beobachtete Daten ausreichend starke Evidenz gegen eine Annahme liefern.

Ein statistischer Test besteht aus:

1. **Nullhypothese** $H_0$
2. **Alternativhypothese** $H_1$
3. Teststatistik
4. Entscheidung anhand eines Signifikanzniveaus

---

**Praktische Bedeutung:**

Statistical Testing erklärt:

- Wie man Aussagen aus Daten ableitet
- Wie man Unsicherheit quantifiziert
- Warum Ergebnisse statistisch signifikant sein können
- Grundlagen von A/B-Tests und Modellvergleichen im ML

---

# Motivation & Intuition

Beim Machine Learning arbeiten wir mit Stichproben.

Beispiel:

Wir trainieren ein Modell und erhalten:

Modell A:

$$
Accuracy = 92\%
$$

Modell B:

$$
Accuracy = 93\%
$$

Die Frage:

> Ist Modell B wirklich besser oder ist der Unterschied nur Zufall?

Statistische Tests helfen, diese Frage zu beantworten.

---

# Grundidee statistischer Tests

Wir formulieren eine Annahme:

$$
H_0
$$

und prüfen, ob die Daten mit dieser Annahme vereinbar sind.

---

Beispiel:

Wir testen:

> Ein neues Modell ist nicht besser als das alte.

Nullhypothese:

$$
H_0:
\mu_A=\mu_B
$$

Alternativhypothese:

$$
H_1:
\mu_A>\mu_B
$$

---

Wenn die Daten sehr unwahrscheinlich unter $H_0$ wären:

↓

wir verwerfen $H_0$

---

# Nullhypothese und Alternativhypothese

## Nullhypothese ($H_0$)

Die Standardannahme:

> Es gibt keinen Effekt.

Beispiele:

- Modelle sind gleich gut
- Medikament wirkt nicht
- Variable hat keinen Einfluss

---

## Alternativhypothese ($H_1$)

Die Behauptung, die wir zeigen möchten:

> Es gibt einen Effekt.

Beispiele:

- Modell A ist besser
- Variable beeinflusst Ergebnis

---

# Fehlerarten beim Testen

Statistische Tests können Fehler machen.

---

## Typ-I-Fehler

Wir verwerfen $H_0$, obwohl sie wahr ist.

Beispiel:

Wir glauben:

> Modell B ist besser

obwohl der Unterschied nur Zufall ist.

Wahrscheinlichkeit:

$$
P(\text{Typ-I-Fehler})=\alpha
$$

$\alpha$ nennt man Signifikanzniveau.

Typische Werte:

- 0.05
- 0.01

---

## Typ-II-Fehler

Wir behalten $H_0$, obwohl sie falsch ist.

Beispiel:

Ein besseres Modell wird nicht erkannt.

Wahrscheinlichkeit:

$$
P(\text{Typ-II-Fehler})=\beta
$$

---

# p-Wert

Der **p-Wert** beschreibt:

> Wie wahrscheinlich wären die beobachteten Daten (oder extremere Daten), wenn $H_0$ wahr wäre?

Formal:

$$
p=P(D\geq D_{obs}|H_0)
$$

---

Interpretation:

Kleiner p-Wert:

↓

Daten passen schlecht zu $H_0$

↓

Evidenz gegen $H_0$

---

Typische Entscheidung:

Wenn:

$$
p<\alpha
$$

dann:

$$
\text{Verwerfe }H_0
$$

---

# Signifikanzniveau

Das Signifikanzniveau:

$$
\alpha
$$

bestimmt, wie streng der Test ist.

Beispiel:

$$
\alpha=0.05
$$

bedeutet:

Wir akzeptieren maximal 5% Wahrscheinlichkeit für einen Typ-I-Fehler.

---

Kleineres $\alpha$:

- weniger False Positives
- aber mehr False Negatives

---

# Häufige statistische Tests

## t-Test

Vergleicht Mittelwerte.

Beispiel:

Sind zwei Modelle unterschiedlich gut?

$$
\mu_1=\mu_2
$$

---

## Chi-Quadrat-Test

Untersucht Zusammenhänge zwischen kategorialen Variablen.

Beispiel:

Hängt Feature A mit Klasse B zusammen?

---

## ANOVA

Vergleicht mehrere Gruppen.

Beispiel:

Sind drei Modelle unterschiedlich gut?

---

## Kolmogorov-Smirnov-Test

Vergleicht Verteilungen.

Beispiel:

Haben Trainings- und Testdaten dieselbe Verteilung?

---

# Statistical Testing im Machine Learning

Statistische Tests werden verwendet für:

- Feature Selection
- Modellvergleich
- Datenanalyse
- Experimentbewertung

---

## Beispiel: Modellvergleich

Wir vergleichen zwei Klassifikatoren.

Ergebnisse über mehrere Testläufe:

Modell A:

$$
90,91,89,92
$$

Modell B:

$$
92,93,91,94
$$

Die Frage:

Ist B signifikant besser?

Ein Test prüft:

$$
H_0:
\mu_A=\mu_B
$$

---

# Zusammenhang mit Generalisierung

Ein Modell kann auf einem Testset besser aussehen, ohne wirklich besser zu sein.

Grund:

Zufällige Schwankungen.

Statistische Tests helfen abzuschätzen:

> Ist der Unterschied wahrscheinlich echt?

---

# Zusammenhang mit Overfitting

Wenn man sehr viele Modelle ausprobiert:

- viele Tests durchführen
- bestes Ergebnis auswählen

entsteht ein Problem:

**Multiple Testing**

---

Beispiel:

100 Modelle werden getestet.

Auch schlechte Modelle können zufällig sehr gut aussehen.

---

Lösung:

- Korrektur für Mehrfachtests
- separates Testset
- Cross Validation

---

# Multiple Testing

Wenn viele Hypothesen getestet werden:

$$
H_1,H_2,...,H_n
$$

steigt die Wahrscheinlichkeit für falsche positive Ergebnisse.

---

Methoden zur Kontrolle:

## Bonferroni-Korrektur

Signifikanzniveau:

$$
\alpha'=\frac{\alpha}{n}
$$

---

## False Discovery Rate (FDR)

Kontrolliert den Anteil falscher Entdeckungen.

---

# Zusammenhang mit Bayesian Inference

Statistical Testing und Bayesian Inference beantworten ähnliche Fragen:

> Was können wir aus Daten schließen?

Unterschied:

| | Frequentistisch | Bayesianisch |
|-|-|-|
| Parameter | fest | zufällige Variable |
| Ergebnis | Testentscheidung | Posterior-Verteilung |
| Vorwissen | nicht direkt | Prior |

---

# Häufige Fehler & Missverständnisse

## ❌ Ein kleiner p-Wert beweist die Hypothese

Nein.

Er zeigt nur:

Die Daten sind unwahrscheinlich unter $H_0$.

---

## ❌ Nicht signifikant bedeutet kein Effekt

Nein.

Vielleicht sind die Datenmengen zu klein.

---

## ❌ Statistische Signifikanz bedeutet praktische Relevanz

Nein.

Ein winziger Unterschied kann statistisch signifikant sein, aber praktisch unwichtig.

---

# Praktische Implikationen

## Ergebnisse nicht nur vergleichen

Nicht nur:

"Modell A hat höhere Accuracy"

sondern:

"Der Unterschied ist statistisch abgesichert."

---

## Testdaten nicht mehrfach verwenden

Das Testset sollte erst am Ende verwendet werden.

---

## Unsicherheit berichten

Zusätzlich zu Metriken:

- Konfidenzintervalle
- Standardabweichungen
- statistische Tests

angeben.

---

# Zusammenfassung

| Begriff | Bedeutung |
|---|---|
| Hypothesentest | Entscheidung anhand von Daten |
| Nullhypothese | Annahme ohne Effekt |
| Alternativhypothese | Annahme mit Effekt |
| p-Wert | Evidenz gegen $H_0$ |
| Signifikanzniveau | erlaubte Fehlerwahrscheinlichkeit |
| Typ-I-Fehler | False Positive |
| Typ-II-Fehler | False Negative |
| Multiple Testing | Problem vieler Tests |

---

# Siehe auch

- Bayesian Inference
- Empirical Risk Minimization (ERM)
- Confidence Intervals
- Generalization Theory
- A/B Testing

---

# Ressourcen & Referenzen

**Bücher**

- Introduction to Statistical Learning – James, Witten, Hastie, Tibshirani
- All of Statistics – Larry Wasserman

**Konzepte**

- Fisher – Statistical Hypothesis Testing
- Neyman-Pearson Lemma
- Multiple Testing Theory

---

# Übungsaufgaben

**Aufgabe 1**

Was beschreibt die Nullhypothese in einem statistischen Test?

---

**Aufgabe 2**

Was bedeutet ein kleiner p-Wert?

---

**Aufgabe 3**

Warum kann häufiges Testen von vielen Modellen zu falschen Ergebnissen führen?

---

**Aufgabe 4**

Was ist der Unterschied zwischen Typ-I- und Typ-II-Fehler?