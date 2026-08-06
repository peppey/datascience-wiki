│   │   │   └── causal-inference.md
# Causal Inference

## TL;DR (30 Sekunden)

**Causal Inference** beschäftigt sich mit der Frage:

> Verursacht eine Variable eine Änderung in einer anderen Variable?

Der zentrale Unterschied:

- **Korrelation:** Zwei Dinge treten gemeinsam auf.
- **Kausalität:** Eine Änderung von A verursacht eine Änderung von B.

Beispiel:

Korrelation:

> Menschen mit mehr Eisverkauf sehen mehr Badeunfälle.

Kausalität?

Nein. Eine dritte Variable beeinflusst beide:

> Temperatur → Eisverkauf und Badeunfälle

---

**Praktische Bedeutung:**

Causal Inference erklärt:

- Warum Korrelation nicht automatisch Ursache bedeutet
- Wie man Interventionen bewertet
- Wie Machine Learning für Entscheidungsprobleme genutzt werden kann
- Grundlagen von A/B-Tests und Treatment Effects

---

# Motivation & Intuition

Machine Learning beantwortet häufig:

> Kann ich eine Variable vorhersagen?

Beispiel:

$$
P(Y|X)
$$

Also:

> Wenn ich $X$ beobachte, was passiert mit $Y$?

---

Causal Inference fragt:

> Was passiert mit $Y$, wenn ich $X$ aktiv verändere?

Also:

$$
P(Y|do(X))
$$

---

Der Unterschied:

Beobachtung:

$$
P(Y|X)
$$

Intervention:

$$
P(Y|do(X))
$$

---

# Korrelation vs. Kausalität

## Korrelation

Zwei Variablen hängen statistisch zusammen.

Beispiel:

$$
X=\text{Sport}
$$

$$
Y=\text{Gesundheit}
$$

Menschen, die mehr Sport machen, sind häufig gesünder.

---

Aber warum?

Mögliche Erklärungen:

1. Sport verbessert Gesundheit.
2. Gesündere Menschen treiben mehr Sport.
3. Eine dritte Variable beeinflusst beide.

---

# Confounder

Ein **Confounder** ist eine Variable, die sowohl Ursache für die Einflussvariable als auch für das Ergebnis ist.

Beispiel:
   Wetter
   /    \
  ↓      ↓
Eisverkauf Badeunfälle

Wetter beeinflusst:

- Eisverkauf
- Badeunfälle

Dadurch entsteht eine scheinbare Beziehung.

---

# Kausale Fragestellung

Eine typische kausale Frage:

> Was wäre passiert, wenn eine Person eine andere Behandlung erhalten hätte?

Beispiel:

Medizin:

> Senkt ein Medikament den Blutdruck?

Machine Learning:

> Erhöht eine Empfehlung die Kaufwahrscheinlichkeit?

---

# Counterfactuals

Ein wichtiges Konzept:

**Was wäre passiert, wenn etwas anders gewesen wäre?**

Beispiel:

Eine Person erhält ein Medikament.

Wir beobachten:

$$
Y(1)
$$

also:

> Ergebnis mit Behandlung.

Aber wir kennen nicht:

$$
Y(0)
$$

also:

> Ergebnis ohne Behandlung.

---

Dieses Problem nennt man:

**Fundamental Problem of Causal Inference**

---

Wir können niemals gleichzeitig beobachten:

- Behandlung
- keine Behandlung

für dieselbe Person.

---

# Potential Outcomes Framework

Das Potential-Outcome-Modell beschreibt mögliche Ergebnisse.

Für eine Person:

$$
Y(1)
$$

= Ergebnis mit Treatment

$$
Y(0)
$$

= Ergebnis ohne Treatment

---

Der individuelle Treatment Effect:

$$
\tau_i
=
Y_i(1)-Y_i(0)
$$

ist theoretisch interessant.

Aber nicht direkt beobachtbar.

---

# Average Treatment Effect (ATE)

Da individuelle Effekte nicht beobachtet werden können, betrachtet man oft den Durchschnitt:

$$
ATE
=
E[Y(1)-Y(0)]
$$

---

Interpretation:

> Wie stark verändert eine Intervention durchschnittlich das Ergebnis?

---

Beispiel:

Eine Kampagne erhöht durchschnittlich die Conversion Rate um:

$$
+5\%
$$

---

# Randomized Controlled Trials (RCTs)

Der Goldstandard für kausale Analyse:

## Idee:

Menschen werden zufällig Gruppen zugeordnet.
Population
|
↓
Randomisierung
/ \

Treatment Control


---

Warum funktioniert das?

Durch Zufall sind Gruppen im Durchschnitt vergleichbar.

Unterschiede können auf die Intervention zurückgeführt werden.

---

Beispiel:

A/B-Test:

Gruppe A:

- alte Webseite

Gruppe B:

- neue Webseite

Unterschied:

→ Effekt der Änderung

---

# Kausale Graphen (DAGs)

Kausale Beziehungen können als gerichtete Graphen dargestellt werden.

DAG:

**Directed Acyclic Graph**

Beispiel:
Alter
|
↓
Medikament → Gesundheit

---

DAGs helfen:

- Confounder zu erkennen
- notwendige Kontrollvariablen zu finden
- falsche Schlussfolgerungen zu vermeiden

---

# Backdoor-Kriterium

Ein wichtiger Begriff in der Kausalanalyse.

Die Idee:

> Blockiere alle nicht-kausalen Wege zwischen Ursache und Ergebnis.

Beispiel:
Alter → Medikament
Alter → Gesundheit

Alter muss kontrolliert werden.

---

# Causal Inference und Machine Learning

Machine Learning wird häufig für kausale Aufgaben eingesetzt.

Beispiele:

- personalisierte Medizin
- Empfehlungssysteme
- Marketing
- Policy Evaluation
- Preisoptimierung

---

ML kann helfen:

- Confounder zu modellieren
- Treatment Effects zu schätzen
- komplexe Zusammenhänge zu analysieren

---

# Causal Machine Learning

Causal ML kombiniert:

- Machine Learning
- Statistik
- Kausale Modelle

Ziel:

Nicht nur:

$$
P(Y|X)
$$

sondern:

$$
P(Y|do(X))
$$

zu schätzen.

---

Beispiele:

## Double Machine Learning

Verwendet ML-Modelle, um:

- Treatment
- Outcome

zu modellieren und daraus kausale Effekte zu schätzen.

---

## Causal Forests

Erweitern Random Forests zur Schätzung individueller Treatment Effects.

---

# Unterschied zwischen Prediction und Causation

| | Prediction | Causal Inference |
|-|-|-|
| Frage | Was passiert? | Was passiert bei Änderung? |
| Ziel | Vorhersage | Ursache-Wirkung |
| Daten | Beobachtungen ausreichend | Intervention wichtig |
| Beispiel | Wer kauft? | Wie erhöht man Käufe? |

---

# Zusammenhang mit Statistical Testing

Statistische Tests können zeigen:

> Gibt es einen Unterschied?

Causal Inference fragt zusätzlich:

> Ist dieser Unterschied durch eine Intervention verursacht?

---

Beispiel:

Statistical Testing:

"Gruppe A und B unterscheiden sich."

Causal Inference:

"Die Behandlung verursacht diesen Unterschied."

---

# Zusammenhang mit Bayesian Inference

Bayesianische Methoden können genutzt werden, um:

- Unsicherheit über kausale Effekte zu modellieren
- Vorwissen einzubeziehen

Beispiel:

Posterior über Treatment Effect:

$$
P(\tau|D)
$$

---

# Häufige Fehler & Missverständnisse

## ❌ Korrelation bedeutet Kausalität

Nein.

Eine dritte Variable kann die Ursache sein.

---

## ❌ Mehr Daten lösen automatisch Kausalitätsprobleme

Nein.

Mehr Beobachtungen beseitigen keine Confounder.

---

## ❌ Ein gutes Vorhersagemodell versteht Ursachen

Nein.

Ein Modell kann sehr gut vorhersagen, ohne kausale Zusammenhänge zu kennen.

---

# Praktische Implikationen

## Experimente sind besonders wertvoll

Randomisierte Experimente ermöglichen starke kausale Aussagen.

---

## Beobachtungsdaten benötigen zusätzliche Annahmen

Methoden:

- Matching
- Instrumental Variables
- Regression Adjustment
- Propensity Scores

---

## Kausalität ist wichtig für Entscheidungen

Besonders bei:

- Medizin
- Wirtschaft
- Politik
- automatisierten Entscheidungen

---

# Zusammenfassung

| Begriff | Bedeutung |
|---|---|
| Causal Inference | Analyse von Ursache-Wirkungs-Beziehungen |
| Korrelation | statistischer Zusammenhang |
| Kausalität | Ursache erzeugt Wirkung |
| Confounder | gemeinsame Ursache zweier Variablen |
| Treatment Effect | Effekt einer Intervention |
| ATE | durchschnittlicher Behandlungseffekt |
| Counterfactual | alternatives mögliches Ergebnis |
| DAG | Graph für kausale Beziehungen |

---

# Siehe auch

- Statistical Testing
- Bayesian Inference
- Reinforcement Learning
- Experimental Design
- Probabilistic Graphical Models

---

# Ressourcen & Referenzen

**Bücher**

- Causality – Judea Pearl
- The Book of Why – Judea Pearl & Dana Mackenzie
- Causal Inference: The Mixtape – Scott Cunningham

**Konzepte**

- Rubin Causal Model
- Potential Outcomes Framework
- Directed Acyclic Graphs (DAGs)

---

# Übungsaufgaben

**Aufgabe 1**

Warum bedeutet Korrelation nicht automatisch Kausalität?

---

**Aufgabe 2**

Was ist der Unterschied zwischen $P(Y|X)$ und $P(Y|do(X))$?

---

**Aufgabe 3**

Warum kann man den individuellen Treatment Effect normalerweise nicht direkt messen?

---

**Aufgabe 4**

Warum helfen randomisierte Experimente bei kausalen Aussagen?
