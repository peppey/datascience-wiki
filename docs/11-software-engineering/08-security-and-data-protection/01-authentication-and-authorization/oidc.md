# OpenID Connect (OIDC)

## Definition

**OpenID Connect (OIDC)** ist ein Authentifizierungsprotokoll, das auf OAuth 2.0 aufbaut. Es ermöglicht Anwendungen, die Identität eines Benutzers oder einer anderen Identität über einen zentralen Identity Provider (IdP) zu überprüfen.

OIDC wird häufig für Single Sign-on (SSO), Webanwendungen, APIs und Cloud-native Infrastrukturen eingesetzt. Nutzer können sich damit beispielsweise über einen zentralen Unternehmens-Login bei mehreren Anwendungen anmelden, ohne für jede Anwendung eigene Zugangsdaten zu benötigen.

**Abgrenzung zu OAuth 2.0:**

* **OAuth 2.0** regelt die Autorisierung: Welche Ressourcen darf ein Client im Namen eines Benutzers oder einer anderen Identität verwenden?
* **OIDC** ergänzt OAuth 2.0 um Authentifizierung: Wer ist der Benutzer?

OIDC stellt dazu unter anderem ein standardisiertes ID Token bereit.

## Zentrale Komponenten

| Komponente               | Beschreibung                                                                                       |
| ------------------------ | -------------------------------------------------------------------------------------------------- |
| **End User**             | Benutzer, dessen Identität überprüft werden soll.                                                  |
| **Relying Party (RP)**   | Anwendung, die OIDC zur Authentifizierung verwendet.                                               |
| **OpenID Provider (OP)** | Dienst, der Benutzer authentifiziert und ID Tokens ausstellt.                                      |
| **Client**               | Anwendung, die einen OIDC-Flow ausführt; bei OIDC ist sie typischerweise die Relying Party.        |
| **ID Token**             | Signiertes Token mit Informationen über die authentifizierte Identität.                            |
| **Access Token**         | Token, mit dem auf geschützte Ressourcen zugegriffen werden kann.                                  |
| **Authorization Server** | Stellt im OAuth-2.0-Kontext Tokens aus; diese Funktion kann vom OpenID Provider übernommen werden. |

Beispiele für Identity Provider sind Keycloak, Microsoft Entra ID und Auth0.

## Ablauf der Authentifizierung

Für interaktive Webanwendungen ist der Authorization Code Flow mit PKCE ein verbreitetes Verfahren.

1. **Login initiieren:** Die Anwendung leitet den Benutzer zum Authorization Endpoint des Identity Providers weiter.
2. **Benutzer authentifizieren:** Der Identity Provider prüft die Identität, beispielsweise mittels Passwort, Single Sign-on oder Multi-Faktor-Authentifizierung.
3. **Authorization Code erhalten:** Nach erfolgreicher Authentifizierung leitet der Identity Provider den Benutzer mit einem kurzlebigen Authorization Code zurück zur Anwendung.
4. **Tokens anfordern:** Die Anwendung tauscht den Code am Token Endpoint gegen Tokens aus. PKCE schützt den Code-Austausch vor bestimmten Angriffen.
5. **ID Token validieren:** Die Anwendung prüft unter anderem Signatur, Aussteller (`iss`), Zielgruppe (`aud`), Ablaufzeit (`exp`) und gegebenenfalls die Nonce.
6. **Sitzung aufbauen:** Die Anwendung verwendet die verifizierte Identität, um eine lokale Sitzung einzurichten und gegebenenfalls Berechtigungen zu bestimmen.

Die Anmeldung selbst erfolgt beim Identity Provider. Die Anwendung vertraut der Identität erst, nachdem sie die zurückgegebenen Tokens korrekt validiert hat.

## Wichtige Tokens und Claims

### ID Token

Ein ID Token ist üblicherweise ein JSON Web Token (JWT), das Aussagen über eine authentifizierte Identität enthält.

Typische Claims sind:

* `iss`: Aussteller des Tokens, also der Identity Provider.
* `sub`: Eindeutiger Bezeichner des Benutzers innerhalb des Ausstellerkontexts.
* `aud`: Zielgruppe, für die das Token bestimmt ist.
* `exp`: Zeitpunkt, ab dem das Token nicht mehr gültig ist.
* `iat`: Zeitpunkt der Ausstellung.
* `nonce`: Wert zur Bindung der Authentifizierungsantwort an die ursprüngliche Anfrage, sofern verwendet.

Das ID Token ist für die Relying Party bestimmt. Es sollte nicht als allgemeines Zugriffstoken für beliebige APIs verwendet werden.

### Access Token

Das Access Token dient dem Zugriff auf geschützte Ressourcen, beispielsweise eine API. Es kann ein JWT oder ein opakes Token sein.

Eine API muss das Access Token gemäß ihrem vorgesehenen Sicherheitsmodell validieren. Insbesondere müssen Zielgruppe, Gültigkeit und erforderliche Berechtigungen zum Zugriff passen.

### Refresh Token

Ein Refresh Token kann dazu verwendet werden, neue Access Tokens anzufordern, ohne dass sich der Benutzer erneut anmelden muss. Seine Verwendung hängt vom jeweiligen Flow, Client-Typ und der Konfiguration des Identity Providers ab.

## OIDC Discovery

OIDC definiert einen Discovery-Mechanismus, über den Clients die Endpunkte und Fähigkeiten eines OpenID Providers automatisch ermitteln können.

Das standardisierte Discovery-Dokument liegt üblicherweise unter:

`https://<issuer>/.well-known/openid-configuration`

Es enthält unter anderem:

* `issuer`: die kanonische Kennung des Identity Providers,
* `authorization_endpoint`: Endpunkt für Authentifizierungsanfragen,
* `token_endpoint`: Endpunkt für den Code- und Token-Austausch,
* `jwks_uri`: URL der öffentlichen Schlüssel zur Token-Signaturprüfung,
* `userinfo_endpoint`: optionaler Endpunkt für zusätzliche Benutzerinformationen.

Die konkreten URLs hängen vom Anbieter und dessen Konfiguration ab.

## OIDC, JWT und OAuth 2.0

Die Begriffe beschreiben unterschiedliche Aspekte:

* **OAuth 2.0:** Autorisierungsframework für delegierten Zugriff.
* **OIDC:** Authentifizierungsschicht auf OAuth 2.0.
* **JWT:** Tokenformat, das unter anderem für ID Tokens und Access Tokens verwendet werden kann.

Nicht jedes OAuth-Access-Token ist ein JWT, und nicht jedes JWT ist ein OIDC-Token.

## Einsatz in Data Science und ML Engineering

OIDC ist besonders in verteilten Systemen relevant, in denen Benutzer, Services und APIs sicher miteinander kommunizieren müssen.

### Geschützte ML-APIs

Ein bereitgestelltes ML-Modell kann über eine API erreichbar sein, beispielsweise mit FastAPI. Ein API-Gateway oder die Anwendung prüft das Access Token, bevor eine Inferenzanfrage verarbeitet wird.

So lässt sich der Zugriff auf Modelle und Daten anhand der Identität und der vorgesehenen Berechtigungen kontrollieren.

### Kubernetes und OpenShift

In Kubernetes- und OpenShift-Umgebungen kann OIDC zur Benutzeranmeldung und Integration mit einem zentralen Identity Provider eingesetzt werden. Je nach Plattform und Konfiguration können auch Workload-Identitäten oder kurzlebige Tokens für automatisierte Zugriffe relevant sein.

Dabei ist zu unterscheiden zwischen:

* der Anmeldung von Menschen an einer Plattform,
* der Authentifizierung eines Services gegenüber einer anderen Komponente,
* der Autorisierung für konkrete Aktionen und Ressourcen.

OIDC allein definiert nicht die vollständigen Rollen und Berechtigungen eines Systems.

### ML-Pipelines und automatisierte Workloads

Trainingsjobs, Deployments und CI/CD-Pipelines benötigen oft Zugriff auf Modellregister, Objektspeicher oder APIs. Eine OIDC-basierte föderierte Identität kann es ermöglichen, kurzlebige Zugangsdaten auszustellen, anstatt langfristige Zugangsschlüssel als Secrets zu speichern.

Ob das funktioniert, hängt davon ab, ob der jeweilige Zieldienst OIDC-basierte Federation unterstützt und welche Vertrauensbeziehungen konfiguriert sind.

## Sicherheitsaspekte

* **Tokens validieren:** Signatur, Aussteller, Zielgruppe und Ablaufzeit müssen gemäß dem jeweiligen Token-Typ geprüft werden.
* **HTTPS verwenden:** Authentifizierungsdaten und Tokens müssen während der Übertragung geschützt sein.
* **Authorization Code Flow mit PKCE bevorzugen:** PKCE schützt den Code-Austausch insbesondere bei öffentlichen Clients.
* **Tokens nicht verwechseln:** ID Tokens sind für den Client bestimmt; Access Tokens sind für geschützte Ressourcen vorgesehen.
* **Secrets schützen:** Client-Secrets, Refresh Tokens und andere vertrauliche Zugangsdaten dürfen nicht in Quellcode, Logs oder Git-Repositories gelangen.
* **Minimal erforderliche Berechtigungen vergeben:** Erfolgreiche Authentifizierung bedeutet nicht automatisch, dass eine Identität auf jede Ressource zugreifen darf.
* **Token-Lebensdauer begrenzen:** Kurze Gültigkeitszeiten und geeignete Erneuerungs- und Widerrufsmechanismen reduzieren Risiken.

## Zusammenfassung

OpenID Connect erweitert OAuth 2.0 um standardisierte Authentifizierung. Es ermöglicht Anwendungen, Identitäten über einen zentralen Identity Provider zu verifizieren. Für Data-Science-Systeme ist OIDC vor allem bei Single Sign-on, dem Schutz von ML-APIs, der Integration von Kubernetes-/OpenShift-Plattformen und der föderierten Authentifizierung automatisierter Workloads relevant.

Die zentrale Unterscheidung lautet: **Authentifizierung beantwortet, wer eine Identität ist; Autorisierung bestimmt, was diese Identität tun darf.** OIDC unterstützt die erste Aufgabe und kann als Grundlage für die zweite dienen, ersetzt aber keine Berechtigungsprüfung.
