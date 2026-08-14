# Jenkins

## TL;DR

**Jenkins** is an open-source automation server used to automate software development processes such as **building, testing, and deploying applications**.

Jenkins executes automated workflows called **Pipelines**. These workflows can be triggered by events such as Git commits, pull requests, schedules, or manual actions.

The basic workflow is:

$$
\boxed{
\text{Source Code}
\rightarrow
\text{Build}
\rightarrow
\text{Test}
\rightarrow
\text{Deploy}
}
$$

---

## Jenkins Server

A Jenkins installation consists of a central **Jenkins controller** that manages jobs and coordinates their execution.

```text
                 Jenkins
                    │
              ┌─────▼─────┐
              │ Controller │
              └─────┬─────┘
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
       Agent 1              Agent 2
```

The controller manages:

* Jobs and Pipelines
* Credentials
* Plugins
* Build history
* Agents
* Scheduling

---

## Jobs

A **Job** is a task that Jenkins can execute.

Examples include:

```text
Build Application
Run Unit Tests
Build Docker Image
Deploy Application
Run Integration Tests
```

A job can be triggered manually or automatically.

```text
Trigger
   │
   ▼
 Jenkins Job
   │
   ├── Build
   ├── Test
   └── Deploy
```

---

## Pipelines

A **Pipeline** describes an automated workflow as code.

Jenkins Pipelines are commonly defined in a file called:

```text
Jenkinsfile
```

A simple Pipeline looks like:

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'make build'
            }
        }

        stage('Test') {
            steps {
                sh 'make test'
            }
        }

        stage('Deploy') {
            steps {
                sh './deploy.sh'
            }
        }
    }
}
```

The Pipeline consists of several **stages**.

```text
Jenkinsfile
     │
     ▼
┌─────────┐
│  Build  │
└────┬────┘
     ▼
┌─────────┐
│  Test   │
└────┬────┘
     ▼
┌─────────┐
│ Deploy  │
└─────────┘
```

---

## Stages

A **stage** represents a logical part of a Pipeline.

Typical stages include:

```text
Checkout
   │
   ▼
Build
   │
   ▼
Test
   │
   ▼
Package
   │
   ▼
Deploy
```

Stages make Pipelines easier to understand and allow Jenkins to display progress and results for individual parts of the workflow.

---

## Steps

A stage contains one or more **steps**.

For example:

```groovy
stage('Test') {
    steps {
        sh 'pytest'
    }
}
```

A step is an individual action executed by Jenkins.

Common steps include:

```groovy
sh 'python test.py'
```

```groovy
bat 'build.bat'
```

```groovy
echo 'Running tests'
```

```groovy
checkout scm
```

---

## Agents

An **agent** is a machine on which Jenkins executes Pipeline steps.

For example:

```groovy
pipeline {
    agent any
}
```

This allows Jenkins to select an available agent.

The architecture can look like:

```text
              Jenkins Controller
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
      Linux Agent           Windows Agent
          │                     │
          ▼                     ▼
       Build                 Build
```

Agents can be physical machines, virtual machines, containers, or Kubernetes pods.

---

## Controller and Agents

The Jenkins controller is responsible for coordinating work, while agents perform the actual builds and tests.

```text
              Controller
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
      Agent     Agent     Agent
        │         │         │
        ▼         ▼         ▼
      Build     Tests    Deploy
```

This allows Jenkins to distribute workloads across multiple machines.

---

## Triggers

A Pipeline can be triggered in different ways.

### Manual Trigger

A user can start a Jenkins job manually.

```text
User
 │
 ▼
Jenkins
 │
 ▼
Pipeline
```

### Git Trigger

A Git repository can trigger Jenkins after a change.

```text
Git Commit
    │
    ▼
Webhook
    │
    ▼
 Jenkins
    │
    ▼
Pipeline
```

### Scheduled Trigger

Jenkins can execute jobs according to a schedule.

For example:

```text
H 2 * * *
```

This can be used to run a job periodically.

---

## Source Code Checkout

Jenkins can retrieve source code from Git repositories.

For example:

```groovy
stage('Checkout') {
    steps {
        checkout scm
    }
}
```

The typical workflow is:

```text
Git Repository
      │
      ▼
   Jenkins
      │
      ▼
   Workspace
```

The **workspace** is the directory in which Jenkins executes the build.

---

## Build

A build transforms source code into an executable or deployable artifact.

For example:

```groovy
stage('Build') {
    steps {
        sh 'mvn package'
    }
}
```

The build process might produce:

```text
Source Code
     │
     ▼
  Compiler
     │
     ▼
  Artifact
```

Examples of artifacts include:

```text
.jar
.whl
.exe
Docker Image
```

---

## Testing

Jenkins can automatically execute tests.

For example:

```groovy
stage('Test') {
    steps {
        sh 'pytest'
    }
}
```

A typical Pipeline is:

```text
       Build
         │
         ▼
       Tests
         │
    ┌────┴────┐
    ▼         ▼
  Passed    Failed
    │
    ▼
  Deploy
```

If a required stage fails, later stages can be prevented from running.

---

## Artifacts

Build artifacts can be stored by Jenkins.

For example:

```groovy
post {
    success {
        archiveArtifacts artifacts: 'target/*.jar'
    }
}
```

Artifacts allow files generated during a build to be retained and downloaded later.

```text
Build
  │
  ▼
Artifact
  │
  ▼
Jenkins
  │
  ▼
Artifact Storage
```

---

## Credentials

Jenkins provides a **Credentials** system for securely storing secrets.

Examples include:

```text
Username / Password
SSH Keys
API Tokens
Cloud Credentials
Certificates
```

Credentials should not be written directly into a Jenkinsfile.

Instead, Jenkins can inject them into a Pipeline when needed.

```groovy
withCredentials([
    usernamePassword(
        credentialsId: 'docker',
        usernameVariable: 'USER',
        passwordVariable: 'PASSWORD'
    )
]) {
    sh 'docker login'
}
```

This keeps sensitive values out of the source code.

---

## Environment Variables

Jenkins can provide environment variables to Pipeline steps.

For example:

```groovy
pipeline {
    agent any

    environment {
        APP_NAME = 'my-app'
    }

    stages {
        stage('Build') {
            steps {
                sh 'echo $APP_NAME'
            }
        }
    }
}
```

Environment variables can be used to configure different environments.

---

## Docker

Jenkins can build and publish Docker images.

For example:

```groovy
stage('Build Docker Image') {
    steps {
        sh 'docker build -t my-app:latest .'
    }
}
```

A typical workflow is:

```text
Git
 │
 ▼
Jenkins
 │
 ▼
Docker Build
 │
 ▼
Docker Image
 │
 ▼
Container Registry
```

Jenkins therefore integrates well with container-based development.

---

## Continuous Integration

Jenkins is commonly used for **Continuous Integration (CI)**.

The idea is to automatically validate changes whenever developers push code.

```text
Developer
    │
    ▼
Git Commit
    │
    ▼
Jenkins
    │
    ├── Build
    ├── Test
    └── Quality Checks
            │
            ▼
         Result
```

This helps detect problems early.

---

## Continuous Delivery

Jenkins can also automate **Continuous Delivery**.

After successful tests, an application can be packaged and prepared for deployment.

```text
Commit
  │
  ▼
Build
  │
  ▼
Test
  │
  ▼
Package
  │
  ▼
Deployable Artifact
```

Deployment may still require manual approval.

---

## Continuous Deployment

With **Continuous Deployment**, successful builds are automatically deployed.

```text
Commit
  │
  ▼
Build
  │
  ▼
Test
  │
  ▼
Deploy
  │
  ▼
Production
```

This removes the need for a manual deployment step.

---

## Declarative Pipeline

Jenkins supports a **Declarative Pipeline** syntax.

For example:

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'make build'
            }
        }

        stage('Test') {
            steps {
                sh 'make test'
            }
        }
    }
}
```

Declarative Pipelines provide a structured way to describe CI/CD workflows.

---

## Scripted Pipeline

Jenkins also supports **Scripted Pipelines**.

They use Groovy more freely:

```groovy
node {
    stage('Build') {
        sh 'make build'
    }

    stage('Test') {
        sh 'make test'
    }
}
```

Scripted Pipelines provide more programming flexibility, while Declarative Pipelines are generally easier to structure and maintain.

---

## Plugins

Jenkins is highly extensible through **plugins**.

Plugins add integrations and functionality for technologies such as:

```text
Git
Docker
Kubernetes
Maven
Gradle
Slack
SonarQube
AWS
Azure
```

For example, a Jenkins installation can use Git plugins to interact with Git repositories and Docker plugins to build container images.

---

## Parallel Execution

Independent tasks can be executed in parallel.

For example:

```groovy
stage('Tests') {
    parallel {
        stage('Unit Tests') {
            steps {
                sh 'pytest tests/unit'
            }
        }

        stage('Integration Tests') {
            steps {
                sh 'pytest tests/integration'
            }
        }
    }
}
```

The architecture becomes:

```text
             Tests
               │
       ┌───────┴───────┐
       ▼               ▼
 Unit Tests      Integration Tests
       │               │
       └───────┬───────┘
               ▼
             Deploy
```

Parallel execution can reduce Pipeline runtime.

---

## Build Status

Jenkins records the result of each build.

Common statuses include:

```text
SUCCESS
FAILURE
UNSTABLE
ABORTED
```

The build history allows developers to inspect previous executions.

```text
Build #105  SUCCESS
Build #104  SUCCESS
Build #103  FAILURE
Build #102  SUCCESS
```

---

## Workspace

Each Jenkins build can use a **workspace** on its agent.

For example:

```text
Agent
 │
 └── Workspace
       ├── source/
       ├── build/
       └── test-results/
```

The workspace contains the files required to execute the Pipeline.

---

## Jenkinsfile

The `Jenkinsfile` is normally stored together with the application source code.

```text
Git Repository
├── src/
├── tests/
├── Dockerfile
└── Jenkinsfile
```

This approach is called **Pipeline as Code**.

The CI/CD configuration is version-controlled alongside the application.

---

## Jenkins with Kubernetes

Jenkins can use Kubernetes to dynamically create build agents.

```text
             Jenkins
                │
                ▼
           Kubernetes
                │
       ┌────────┼────────┐
       ▼        ▼        ▼
     Pod      Pod       Pod
       │        │        │
     Build    Test     Deploy
```

This allows build environments to be created dynamically and removed after use.

---

## Jenkins in Machine Learning

Jenkins can automate ML workflows such as:

```text
Git Commit
    │
    ▼
Run Tests
    │
    ▼
Build Docker Image
    │
    ▼
Train / Validate
    │
    ▼
Register Model
    │
    ▼
Deploy Model
```

For example, Jenkins can trigger:

* Data validation
* Unit and integration tests
* Docker image builds
* ML training jobs
* Model validation
* Model deployment
* Kubernetes or KServe deployments

Jenkins is therefore often used as the CI/CD component around an ML platform.

---

## Jenkins vs. GitHub Actions

Both Jenkins and GitHub Actions can be used for CI/CD.

```text
Jenkins
├── Self-hosted
├── Highly extensible
├── Plugin ecosystem
└── Pipeline as Code

GitHub Actions
├── Integrated into GitHub
├── Hosted runners
├── Workflow as Code
└── GitHub-native integrations
```

Jenkins is particularly useful when an organization wants extensive control over its CI/CD infrastructure or needs integrations provided by the Jenkins ecosystem.

---

## Typical CI/CD Workflow

A typical Jenkins workflow looks like:

```text
              Developer
                  │
                  ▼
             Git Commit
                  │
                  ▼
              Jenkins
                  │
                  ▼
              Checkout
                  │
                  ▼
                Build
                  │
                  ▼
                Test
                  │
             ┌────┴────┐
             │         │
           Failed    Passed
             │         │
             ▼         ▼
           Stop      Package
                       │
                       ▼
                    Deploy
                       │
                       ▼
                  Production
```

---

## Common Jenkins Concepts

| Concept         | Description                            |
| --------------- | -------------------------------------- |
| **Controller**  | Manages Jenkins and coordinates builds |
| **Agent**       | Executes Pipeline steps                |
| **Job**         | A task executed by Jenkins             |
| **Pipeline**    | Automated workflow                     |
| **Jenkinsfile** | Pipeline definition stored as code     |
| **Stage**       | Logical section of a Pipeline          |
| **Step**        | Individual action within a stage       |
| **Workspace**   | Directory used during a build          |
| **Artifact**    | File produced by a build               |
| **Credential**  | Securely stored secret                 |
| **Plugin**      | Extension adding functionality         |

---

## Common Commands

Jenkins is primarily managed through its web UI and Pipeline definitions, but Jenkins can also be accessed through its CLI and HTTP API.

Typical Pipeline steps include:

```text
checkout scm
sh
bat
echo
archiveArtifacts
junit
withCredentials
```

For example:

```groovy
stage('Test') {
    steps {
        sh 'pytest'
    }
}
```

---

## Key Idea

Jenkins is an **automation server for building, testing, and deploying software**.

The central concept is a Pipeline:

```text
              Jenkins
                  │
                  ▼
             Jenkinsfile
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
      Build      Test      Deploy
        │         │         │
        └─────────┴─────────┘
                  │
                  ▼
              Application
```

The main advantage of Jenkins is that repetitive software-development processes can be automated and executed consistently.

A Jenkins Pipeline turns a sequence of manual development and deployment steps into a **reproducible, version-controlled workflow**.
