# Diffusion Models

## TL;DR (30 Sekunden)

**Diffusion Models** sind generative Modelle, die neue Daten erzeugen, indem sie einen schrittweisen Prozess des Entrauschens lernen.

Die zentrale Idee:

> Lerne, aus reinem Rauschen wieder realistische Daten zu erzeugen.

Beispiele:

- Bildgenerierung
- Text-zu-Bild Modelle
- Audio-Synthese
- Molekülgenerierung

Bekannte Modelle:

- Stable Diffusion
- DALL·E
- Imagen

---

**Praktische Bedeutung:**

Diffusion Models erklären:

- Wie moderne generative KI-Systeme funktionieren
- Warum Rauschen schrittweise entfernt werden kann
- Zusammenhang zwischen Wahrscheinlichkeit, neuronalen Netzen und Sampling
- Grundlagen aktueller Bildgeneratoren

---

# Motivation & Intuition

Generative Modelle möchten neue Daten erzeugen, die ähnlich wie Trainingsdaten aussehen.

Beispiel:

Trainingsdaten:
Viele Bilder von Katzen

Ziel:
Neues realistisches Katzenbild erzeugen

---

Die Frage:

> Wie kann ein Modell lernen, die Datenverteilung zu verstehen?

Formal:

Gegeben:

$$
x\sim p_{data}(x)
$$

soll ein Modell lernen:

$$
p_\theta(x)
$$

---

# Grundidee von Diffusion Models

Diffusion Models bestehen aus zwei Prozessen:

1. **Forward Process**
   - Daten werden schrittweise verrauscht

2. **Reverse Process**
   - Das Modell lernt, das Rauschen wieder zu entfernen

---

Visualisierung:
Bild
|
↓
mehr Rauschen
|
↓
reines Rauschen
reines Rauschen
|
↓
Entrauschen
|
↓
neues Bild


---

# Forward Diffusion Process

Der Forward Process ist fest definiert.

Zu einem Datenpunkt:

$$
x_0
$$

wird schrittweise Rauschen hinzugefügt.

Nach vielen Schritten:

$$
x_T
$$

ist fast reines Rauschen.

---

Mathematisch:

$$
q(x_t|x_{t-1})
=
N(
\sqrt{1-\beta_t}x_{t-1},
\beta_t I
)
$$

---

Dabei:

- $t$ = Zeitschritt
- $\beta_t$ = Rauschstärke

---

Je größer $t$:

mehr Rauschen

↓

weniger Information über ursprüngliche Daten

---

# Warum funktioniert der Forward Process?

Der Rauschprozess ist einfach.

Nach genügend Schritten gilt ungefähr:

$$
x_T\sim N(0,I)
$$

also:

Standard-Gaussian Noise.

---

Das Modell muss daher nur lernen:

> Wie kommt man von Rauschen zurück zu Daten?

---

# Reverse Diffusion Process

Der eigentliche Lernprozess.

Das Modell approximiert:

$$
p_\theta(x_{t-1}|x_t)
$$

---

Also:

Gegeben:

verrauschter Zustand

$$
x_t
$$

Vorhersage:

weniger verrauschter Zustand

$$
x_{t-1}
$$

---

Ein neuronales Netzwerk lernt:

- welches Rauschen entfernt werden muss
- wie Datenstrukturen aussehen

---

# Noise Prediction

In vielen modernen Diffusion Models sagt das Netzwerk nicht direkt das Bild vorher.

Es sagt das hinzugefügte Rauschen voraus:

$$
\epsilon_\theta(x_t,t)
$$

---

Training:

Das Modell bekommt:

- verrauschtes Bild
- Zeitschritt $t$

und lernt:

$$
\epsilon
$$

zurückzugeben.

---

Loss:

$$
L=
||\epsilon-\epsilon_\theta(x_t,t)||^2
$$

---

# Sampling

Nach dem Training:

Start:

$$
x_T
$$

mit zufälligem Rauschen.

---

Dann wiederholt:

1. Netzwerk schätzt Rauschen
2. Rauschen entfernen
3. nächsten Zustand berechnen

---

Nach vielen Schritten:

$$
x_T\rightarrow x_0
$$

---

Ergebnis:

Ein neues künstliches Beispiel.

---

# Zusammenhang mit Wahrscheinlichkeitsmodellen

Diffusion Models modellieren eine Datenverteilung:

$$
p(x)
$$

---

Das Ziel:

Nicht nur einzelne Beispiele lernen.

Sondern:

> Die Struktur der gesamten Datenverteilung verstehen.

---

Damit gehören sie zu:

**Generative Models**

---

# Vergleich mit anderen generativen Modellen

| Modell | Idee | Vorteil |
|-|-|-|
| GAN | Generator gegen Diskriminator | schnelle Generierung |
| VAE | Latenter Raum | probabilistische Darstellung |
| Diffusion | iteratives Entrauschen | sehr hohe Qualität |

---

# Diffusion Models vs. GANs

## GAN

Besteht aus:

Generator:

$$
z\rightarrow x
$$

und

Discriminator:

$$
x\rightarrow real/fake
$$

---

Problem:

- Training instabil
- Mode Collapse möglich

---

## Diffusion

Vorteile:

- stabileres Training
- sehr gute Bildqualität
- vielfältige Samples

Nachteil:

- langsameres Sampling

---

# Latenter Raum

Viele moderne Diffusion Models arbeiten nicht direkt im Bildraum.

Beispiel:

Stable Diffusion:

Bild:

$$
x
$$

↓

Encoder

↓

Latenter Raum:

$$
z
$$

↓

Diffusion

---

Vorteil:

- weniger Berechnung
- größere Bilder möglich

---

# Conditional Diffusion Models

Diffusion Models können gesteuert werden.

Beispiel:

Text:

"Ein Hund im Schnee"

wird als Bedingung verwendet.

---

Das Modell lernt:

$$
p(x|c)
$$

---

Dabei:

- $x$ = generiertes Objekt
- $c$ = Bedingung

---

Beispiele:

- Text-to-Image
- Image-to-Image
- Inpainting

---

# Zusammenhang mit Transformer-Modellen

Viele moderne Diffusion-Systeme verwenden:

- Transformer
- Attention Mechanismen

---

Beispiel:

Text Encoder:
Text
|
↓
Embedding
|
↓
Diffusion Model
|
↓
Bild

---

# Anwendungen

## Bildgenerierung

Beispiele:

- Kunst
- Produktbilder
- Design

---

## Medizin

- Bildrekonstruktion
- Simulation von Daten

---

## Wissenschaft

- Moleküldesign
- Materialforschung

---

## Datenaugmentation

Neue Trainingsdaten erzeugen.

---

# Herausforderungen

## Langsames Sampling

Viele Schritte notwendig:

$$
x_T\rightarrow x_0
$$

---

## Kontrolle

Es ist schwierig, exakt gewünschte Ergebnisse zu erzeugen.

---

## Trainingsdaten

Modelle können:

- Bias übernehmen
- Trainingsdaten imitieren

---

# Zusammenhang mit Machine Learning Theorie

Diffusion Models verbinden viele theoretische Konzepte:

## Wahrscheinlichkeitstheorie

Modellierung von:

$$
p(x)
$$

---

## Stochastische Prozesse

Der Forward Process ist ein Markov-Prozess.

---

## Variational Inference

Die Herleitung basiert auf probabilistischen Approximationen.

---

## Deep Learning

Neuronale Netze approximieren:

$$
\epsilon_\theta(x_t,t)
$$

---

# Häufige Fehler & Missverständnisse

## ❌ Diffusion Models speichern einfach Trainingsbilder

Nein.

Sie lernen eine statistische Verteilung.

---

## ❌ Der Forward Process wird gelernt

Nein.

Der Prozess des Rauschens ist vorgegeben.

Das Modell lernt nur den Rückweg.

---

## ❌ Mehr Rauschen macht das Modell schlechter

Nein.

Das Rauschen ermöglicht überhaupt erst das Lernen einer stabilen Generierung.

---

# Praktische Implikationen

## Qualität gegen Geschwindigkeit

Mehr Sampling-Schritte:

- bessere Qualität
- längere Laufzeit

---

## Gute Repräsentationen sind entscheidend

Text- und Bildrepräsentationen beeinflussen stark:

- Kontrolle
- Qualität

---

## Große Modelle benötigen viele Daten

Wie bei anderen Deep-Learning-Modellen:

mehr Daten

↓

bessere Modellierung komplexer Verteilungen

---

# Zusammenfassung

| Begriff | Bedeutung |
|---|---|
| Diffusion Model | Generatives Modell durch Entrauschen |
| Forward Process | Hinzufügen von Rauschen |
| Reverse Process | Entfernen von Rauschen |
| Noise Prediction | Vorhersage des hinzugefügten Rauschens |
| Sampling | Erzeugen neuer Daten |
| Conditional Diffusion | Steuerung durch zusätzliche Information |
| Latent Diffusion | Diffusion im komprimierten Raum |

---

# Siehe auch

- Generative Models
- Variational Autoencoders (VAE)
- GANs
- Transformer
- Representation Learning
- Bayesian Inference
- Probabilistic Models

---

# Ressourcen & Referenzen

**Bücher**

- Deep Learning – Goodfellow, Bengio & Courville
- Probabilistic Machine Learning – Kevin Murphy

**Originalarbeiten**

- Sohl-Dickstein et al. (2015) – Deep Unsupervised Learning using Nonequilibrium Thermodynamics
- Ho et al. (2020) – Denoising Diffusion Probabilistic Models
- Rombach et al. (2022) – High-Resolution Image Synthesis with Latent Diffusion Models

---

# Übungsaufgaben

**Aufgabe 1**

Warum fügt man im Forward Process zunächst Rauschen hinzu?

---

**Aufgabe 2**

Was lernt ein Diffusion Model während des Trainings?

---

**Aufgabe 3**

Warum starten Diffusion Models beim Sampling mit zufälligem Rauschen?

---

**Aufgabe 4**

Was ist der Unterschied zwischen einem GAN und einem Diffusion Model?
