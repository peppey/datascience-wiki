# GitHub Actions

## TL;DR

**GitHub Actions** is a CI/CD platform integrated directly into GitHub.

It allows workflows to automatically **build, test, and deploy** applications when events occur in a repository.

The basic workflow is:

$$
\boxed{
\text{Git Event}
\rightarrow
\text{Workflow}
\rightarrow
\text{Jobs}
\rightarrow
\text{Steps}
}
$$

---

## Workflow

A **workflow** defines an automated process and is stored as a YAML file in:

```text
.github/workflows/
```

For example:

```yaml
name: CI

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
      - run: pytest
```

---

## Jobs

A **job** is a collection of steps executed on a runner.

```text
Workflow
   │
   ├── Build Job
   │
   └── Test Job
```

Jobs can run sequentially or in parallel.

---

## Steps

A **step** is an individual action within a job.

For example:

```yaml
steps:
  - uses: actions/checkout@v4
  - run: pip install -r requirements.txt
  - run: pytest
```

Steps can execute shell commands or use reusable **Actions**.

---

## Events

Workflows can be triggered by events such as:

```text
push
pull_request
workflow_dispatch
schedule
```

For example:

```yaml
on:
  pull_request:
```

This runs the workflow whenever a pull request is created or updated.

---

## Runners

A **runner** is the machine that executes a job.

Common environments include:

```text
ubuntu-latest
windows-latest
macos-latest
```

The basic architecture is:

```text
GitHub Repository
       │
       ▼
 GitHub Actions
       │
       ▼
    Runner
       │
       ▼
Build / Test / Deploy
```

---

## CI/CD

GitHub Actions is commonly used for CI/CD:

```text
Push Code
    │
    ▼
Build
    │
    ▼
Test
    │
    ▼
Docker Build
    │
    ▼
Deploy
```

---

## Key Idea

GitHub Actions provides **automation directly inside GitHub repositories**.

Workflows are defined as YAML files and consist of:

```text
Workflow
   │
   └── Jobs
        │
        └── Steps
```

It is commonly used for **Continuous Integration and Continuous Deployment (CI/CD)**.
