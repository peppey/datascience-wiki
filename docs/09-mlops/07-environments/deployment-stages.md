# Deployment Stages

## TL;DR

**Deployment stages** describe the different environments through which an application or ML model typically moves before reaching production.

A common workflow is:

```text
Development → QA/Staging → Pre-Production → Production
```

Not every project requires all stages.

---

## Development

The **Development** environment is used for implementing and testing new changes.

```text
Developer
    │
    ▼
Development
```

Changes can be tested quickly without affecting users.

---

## QA / Staging

**QA (Quality Assurance)** or **Staging** is used for more systematic testing in an environment that resembles production.

Typical activities include:

* Integration testing
* End-to-end testing
* Performance testing
* Manual testing

```text
Development
     │
     ▼
QA / Staging
     │
     ▼
Production
```

---

## Pre-Production

**Pre-production (Pre-Prod)** is an optional environment that is very close to the production setup.

It can be used for final validation before deployment:

```text
Development
     │
     ▼
QA / Staging
     │
     ▼
Pre-Production
     │
     ▼
Production
```

Pre-prod is particularly useful when production deployments are sensitive or complex.

---

## Production

The **Production** environment runs the application or model for real users or consumers.

```text
Pre-Production
      │
      ▼
  Production
      │
      ▼
    Users
```

Changes deployed here should have passed the required validation stages.

---

## Typical Workflow

A deployment pipeline can therefore look like:

```text
Code / Model Change
        │
        ▼
   Development
        │
        ▼
    QA / Staging
        │
        ▼
   Pre-Production
        │
        ▼
    Production
```

The exact stages depend on the project. Smaller projects may use only **Development → Production**, while larger systems may use separate QA, Staging, and Pre-Production environments.

---

## Key Idea

Deployment stages provide **progressively stricter environments for validating changes** before they reach production.

$$
\boxed{
\text{Development}
\rightarrow
\text{Testing}
\rightarrow
\text{Pre-Production}
\rightarrow
\text{Production}
}
$$
