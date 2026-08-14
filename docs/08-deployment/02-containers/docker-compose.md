# Docker Compose

## TL;DR

**Docker Compose** is a tool for defining and running applications that consist of multiple Docker containers.

Instead of starting containers individually with `docker run`, Compose allows the complete application stack to be described in a single YAML file.

The basic workflow is:

$$
\boxed{
\text{Compose File}
\rightarrow
\text{Services}
\rightarrow
\text{Containers}
}
$$

---

## Compose File

A Compose application is defined in a YAML file, typically named:

```text
compose.yaml
```

A simple example:

```yaml
services:
  app:
    build: .
    ports:
      - "8080:8080"

  database:
    image: postgres:16
```

The file describes the services that make up the application.

---

## Services

A **service** represents a container or a group of containers with the same configuration.

For example:

```yaml
services:
  app:
    image: my-app

  database:
    image: postgres:16
```

Here, the application consists of two services:

```text
        Application
             │
       ┌─────┴─────┐
       ▼           ▼
      app       database
       │           │
    Container   Container
```

Compose creates and manages the corresponding containers.

---

## Images

A service can use an existing Docker image:

```yaml
services:
  database:
    image: postgres:16
```

The image is pulled from a container registry if it is not already available locally.

A service can also build an image from a Dockerfile:

```yaml
services:
  app:
    build: .
```

The `build` context specifies the directory containing the Dockerfile and application files.

---

## Ports

Ports can be mapped from the host to a container:

```yaml
services:
  app:
    image: my-app
    ports:
      - "8080:8080"
```

The general format is:

```text
HOST_PORT:CONTAINER_PORT
```

For example:

```text
localhost:8080
      │
      ▼
┌──────────────┐
│  Container   │
│    :8080     │
└──────────────┘
```

---

## Environment Variables

Environment variables can be passed to services:

```yaml
services:
  app:
    image: my-app
    environment:
      DATABASE_URL: postgresql://database:5432/app
```

A `.env` file can also be used for configuration values:

```text
DATABASE_USER=postgres
DATABASE_PASSWORD=secret
```

This allows configuration to be separated from the Compose file.

---

## Volumes

Volumes can be used to persist data:

```yaml
services:
  database:
    image: postgres:16
    volumes:
      - postgres-data:/var/lib/postgresql/data

volumes:
  postgres-data:
```

The volume exists independently of the container.

```text
Database Container
       │
       ▼
/var/lib/postgresql/data
       │
       ▼
   Docker Volume
```

---

## Networks

Compose automatically creates a network for the application.

Services on the same Compose network can communicate using their service names.

For example:

```yaml
services:
  app:
    image: my-app

  database:
    image: postgres:16
```

The application can connect to the database using:

```text
database
```

rather than an IP address.

The resulting architecture is:

```text
┌──────────────┐
│     app      │
└──────┬───────┘
       │
       │ database:5432
       ▼
┌──────────────┐
│   database   │
└──────────────┘
```

---

## Starting an Application

The complete application can be started with:

```text
docker compose up
```

To run it in the background:

```text
docker compose up -d
```

Compose creates the required networks, volumes, images, and containers.

---

## Stopping an Application

The application can be stopped with:

```text
docker compose stop
```

This stops the containers but does not remove them.

To stop and remove the application's containers and networks:

```text
docker compose down
```

Volumes are normally preserved unless explicitly requested:

```text
docker compose down -v
```

---

## Building Services

If a service uses a Dockerfile, its image can be built with:

```text
docker compose build
```

The application can also be rebuilt and started with:

```text
docker compose up --build
```

This is useful after changing the Dockerfile or application dependencies.

---

## Logs

Logs from all services can be viewed with:

```text
docker compose logs
```

Logs can be followed continuously:

```text
docker compose logs -f
```

Logs for a specific service can be displayed with:

```text
docker compose logs app
```

---

## Service Dependencies

Services can declare dependencies on other services:

```yaml
services:
  app:
    image: my-app
    depends_on:
      - database

  database:
    image: postgres:16
```

This expresses that `app` depends on `database`.

However, `depends_on` does not necessarily mean that the database is fully ready to accept connections. Health checks can be used when readiness matters.

---

## Health Checks

A service can define a health check:

```yaml
services:
  database:
    image: postgres:16
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
```

Health checks allow Compose to determine whether a service is healthy.

---

## Scaling

A service can be started with multiple container instances:

```text
docker compose up --scale app=3
```

This results in:

```text
             ┌───────────┐
             │   app     │
             │ instance 1│
             └─────┬─────┘
                   │
             ┌─────▼─────┐
             │   app     │
             │ instance 2│
             └─────┬─────┘
                   │
             ┌─────▼─────┐
             │   app     │
             │ instance 3│
             └───────────┘
```

Compose is primarily intended for local development and smaller deployment environments rather than large-scale orchestration.

---

## Common Commands

Useful Docker Compose commands include:

```text
docker compose up
docker compose up -d
docker compose down
docker compose build
docker compose ps
docker compose logs
docker compose stop
docker compose restart
```

A typical development workflow is:

```text
Edit Code
   │
   ▼
docker compose up --build
   │
   ▼
Run Services
   │
   ▼
Inspect Logs
   │
   ▼
docker compose down
```

---

## Docker Compose vs. Docker

Docker provides the underlying container technology:

```text
Docker
├── Images
├── Containers
├── Networks
└── Volumes
```

Docker Compose provides a declarative way to manage several of these resources together:

```text
Docker Compose
       │
       ▼
   compose.yaml
       │
   ┌───┼───────────┐
   ▼   ▼           ▼
  App Database   Redis
```

Compose therefore does not replace Docker. It builds on Docker to simplify multi-container applications.

---

## Docker Compose in Machine Learning

Docker Compose is useful for local ML and data-science systems consisting of multiple services.

For example:

```text
┌──────────────────┐
│   ML Application │
└────────┬─────────┘
         │
    ┌────┴────┐
    ▼         ▼
 Database   MLflow
```

A Compose file might define:

```yaml
services:
  app:
    build: .

  mlflow:
    image: mlflow/mlflow

  database:
    image: postgres:16
```

This makes it possible to start the complete local environment with:

```text
docker compose up
```

---

## Key Idea

Docker Compose describes a **multi-container application declaratively**.

Instead of manually creating containers, networks, and volumes, the desired application architecture is defined in a Compose file:

```text
compose.yaml
     │
     ├── Services
     ├── Networks
     ├── Volumes
     └── Configuration
             │
             ▼
      Docker Compose
             │
             ▼
    Running Containers
```

The main advantage is that the complete application environment can be defined, reproduced, and started with a small number of commands.
