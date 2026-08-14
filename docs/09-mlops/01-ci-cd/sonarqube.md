# SonarQube

## TL;DR

**SonarQube** is a platform for continuously inspecting source code to detect **bugs, vulnerabilities, code smells, and maintainability problems**.

The basic workflow is:

$$
\boxed{
\text{Source Code}
\rightarrow
\text{SonarQube Analysis}
\rightarrow
\text{Quality Gate}
}
$$

---

## Code Analysis

SonarQube analyzes source code using language-specific rules.

It can detect:

* Bugs
* Vulnerabilities
* Code smells
* Duplicated code
* Low test coverage

The analysis produces a report:

```text
Source Code
     │
     ▼
SonarQube Scanner
     │
     ▼
SonarQube Server
     │
     ▼
Analysis Report
```

---

## SonarQube Scanner

The **SonarQube Scanner** analyzes the project and sends the results to the SonarQube server.

For example:

```text
sonar-scanner
```

It can also be integrated into build tools such as Maven or Gradle.

---

## Quality Gate

A **Quality Gate** defines conditions that code must satisfy.

For example:

```text
Coverage          ≥ 80%
Bugs              = 0
Vulnerabilities   = 0
```

The result is:

```text
             Analysis
                │
        ┌───────┴───────┐
        ▼               ▼
    Quality Gate      Quality Gate
      Passed            Failed
        │                 │
        ▼                 ▼
     Continue             Stop
```

Quality Gates are commonly used in CI/CD pipelines.

---

## Code Smells

A **code smell** is code that is not necessarily incorrect but may be difficult to maintain.

Examples include:

```text
Duplicated Code
Very Long Methods
Unused Variables
Complex Conditions
```

SonarQube identifies such patterns and provides suggestions for improvement.

---

## Test Coverage

SonarQube can display how much of the source code is covered by automated tests.

For example:

```text
Lines to Cover: 100
Covered Lines: 85

Coverage: 85%
```

Coverage itself does not guarantee good tests, but it provides a useful quality indicator.

---

## Security

SonarQube can detect potential security vulnerabilities in source code.

For example:

```text
Source Code
     │
     ▼
Security Analysis
     │
     ├── Vulnerabilities
     └── Security Hotspots
```

This allows security problems to be identified earlier in the development process.

---

## CI/CD Integration

SonarQube is commonly integrated into CI/CD systems such as Jenkins or GitHub Actions.

```text
Git Push
   │
   ▼
CI Pipeline
   │
   ▼
Build & Test
   │
   ▼
SonarQube Analysis
   │
   ▼
Quality Gate
   │
   ├── Passed → Continue
   └── Failed → Stop
```

This prevents code that does not meet defined quality requirements from progressing through the pipeline.

---

## Key Idea

SonarQube provides **automated code quality and security analysis**.

Its main purpose is to detect problems early and enforce minimum quality standards:

```text
Code
 │
 ▼
SonarQube
 │
 ├── Bugs
 ├── Vulnerabilities
 ├── Code Smells
 ├── Coverage
 └── Duplications
       │
       ▼
  Quality Gate
```

SonarQube is therefore commonly used as a **quality-control step in CI/CD pipelines**.
