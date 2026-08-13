# Docker

## TL;DR

**Docker** is a platform for packaging and running applications in isolated **containers**.

A Docker container contains an application together with its dependencies and runtime environment, making it easier to run the same application consistently across different systems.

The basic workflow is:

$$
\boxed{
\text{Dockerfile}
\rightarrow
\text{Image}
\rightarrow
\text{Container}
}
$$

---

## Containers

A **container** is an isolated process that runs from a Docker image.

Unlike virtual machines, containers share the host system's kernel and are therefore generally more lightweight.

A container has its own:

- filesystem
- processes
- network interfaces
- environment variables
- resource limits

---

## Docker Images

A **Docker image** is an immutable template used to create containers.

Images consist of layers. Each layer represents a change to the filesystem.

For example:

```text
Base Python Image
       │
       ▼
Install Dependencies
       │
       ▼
Copy Application
       │
       ▼
Final Image
```

Images can be stored in and retrieved from container registries.
Dockerfile
A Dockerfile defines how an image is built.

Example:

```text
FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

Common instructions include:
- FROM — selects a base image
- WORKDIR — sets the working directory
- COPY — copies files into the image
- RUN — executes commands during the build
- ENV — defines environment variables
- EXPOSE — documents a container port
- CMD — defines the default command

## Building an Image

An image can be built from a Dockerfile:

```text
docker build -t my-app .
```

The result is an image named:
```text
my-app
```

The build process executes the Dockerfile instructions and creates the corresponding image layers.

## Running a Container

A container can be created from an image:
```text
docker run my-app
```

For example, to map a host port to a container port:
```text
docker run -p 8080:8080 my-app
```

The general relationship is:
```text
Image
  │
  │ docker run
  ▼
Container
```

Multiple containers can be created from the same image.

## Container Lifecycle

A container typically goes through states such as:
```text
Created
   │
   ▼
Running
   │
   ├──► Stopped
   │
   └──► Restarted
   ```

Useful commands include:
```text
docker ps
docker start <container>
docker stop <container>
docker rm <container>
```

## Volumes
Containers are usually ephemeral: data written inside a container can disappear when the container is removed.
Volumes provide persistent storage outside the container's writable layer.

```text
docker volume create my-data
```
A volume can then be mounted into a container:
```text
docker run -v my-data:/data my-app
```
## Networking

Docker provides virtual networks that allow containers to communicate with each other.
For example:
```text
┌──────────────┐
│   Frontend   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   Backend    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   Database   │
└──────────────┘
```

Containers connected to the same Docker network can communicate using container or service names.

## Environment Variables
Configuration can be passed to containers using environment variables:
```text
docker run -e DATABASE_URL=... my-app
```

This allows configuration to be separated from the application image.

## Docker Compose
Docker Compose is used to define and manage applications consisting of multiple containers.
A compose.yaml might define:
```text
services:
  app:
    build: .
    ports:
      - "8080:8080"

  database:
    image: postgres:16
```

The application can then be started with:
```text
docker compose up
```
Compose is particularly useful for local development and testing of multi-container applications.

## Registries
A container registry stores and distributes Docker images.
The workflow is typically:
```text
Dockerfile
    │
    ▼
Build Image
    │
    ▼
Push to Registry
    │
    ▼
Pull Image
    │
    ▼
Run Container
```

Examples of registries include:
- Docker Hub
- GitHub Container Registry
- cloud provider registries
- private enterprise registries

## Docker vs. Virtual Machines
Docker containers and virtual machines provide isolation in different ways.
```text
Virtual Machines

Application
     │
Guest OS
     │
Hypervisor
     │
Host OS
     │
Hardware
```

Compared with:
```text
Containers

Application
     │
Container
     │
Container Runtime
     │
Host OS Kernel
     │
Hardware
```
Containers are generally lighter because they share the host kernel.

## Docker in Machine Learning
Docker is commonly used in ML systems to package:
- Python environments
- ML frameworks
- system libraries
- model-serving applications
- data-processing pipelines

For example:
```text
Docker Image
├── Python
├── PyTorch
├── NumPy
├── Application Code
└── Model Serving Code
```
This helps ensure that the same environment can be reproduced across development, testing, and deployment.

## Key Idea
Docker separates an application's environment from the underlying machine:
```text
Application+Dependencies+Runtime→Container Image
```
 
The image provides a reproducible environment, while containers are the running instances of that image.
