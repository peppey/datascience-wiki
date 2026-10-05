# GCP Foundations

Google Cloud Platform (GCP) is Google's public cloud. It provides infrastructure (compute, storage, networking) and managed services (data warehouses, ML platforms, container orchestration) that are billed by usage. This article covers the core concepts needed before using any specific GCP service.

---

## 1. Resource Hierarchy

Everything in GCP lives inside a hierarchy. Permissions and policies set at a higher level are **inherited** by everything below.

```
Organization          (company, e.g. example.com)
 └── Folder           (team, department, environment)
      └── Project     (container for resources)
           └── Resource  (bucket, VM, dataset, endpoint, ...)
```

| Level | Purpose | Typical use |
|---|---|---|
| **Organization** | Root node, tied to a Google Workspace / Cloud Identity domain | Company-wide policies |
| **Folder** | Optional grouping of projects | Separate teams or `dev` / `prod` |
| **Project** | Basic unit for resources, billing, APIs and permissions | One project per application and environment |
| **Resource** | The actual service instance | Bucket, GKE cluster, BigQuery dataset |

### Projects

A project is the central working unit. Every resource belongs to exactly one project. A project has three identifiers:

| Identifier | Description | Changeable |
|---|---|---|
| **Project name** | Human-readable label | Yes |
| **Project ID** | Globally unique string, used in CLI and APIs | No |
| **Project number** | Numeric ID assigned by GCP | No |

> **Note:** Separate projects per environment (`myapp-dev`, `myapp-prod`) give clean isolation of permissions, quotas and costs.

---

## 2. Regions and Zones

| Term | Meaning | Example |
|---|---|---|
| **Region** | Geographic location with several data centers | `europe-west3` (Frankfurt) |
| **Zone** | Isolated deployment area within a region | `europe-west3-a` |
| **Multi-region** | Spans several regions (e.g. for storage or BigQuery) | `EU`, `US` |

Choosing a region affects:

- **Latency**: place resources close to users and to each other.
- **Cost**: prices differ between regions.
- **Compliance**: data residency requirements (e.g. GDPR) may restrict the choice.
- **Availability**: spreading across zones protects against zone failures.

Transferring data between regions or out of GCP (**egress**) is usually billed, so keep data and compute in the same region.

---

## 3. APIs and Services

Most GCP services are disabled by default and must be **enabled per project** before use.

```bash
gcloud services enable storage.googleapis.com
gcloud services enable aiplatform.googleapis.com
gcloud services list --enabled
```

A common error such as `API has not been used in project ... before or it is disabled` simply means the API still needs to be enabled.

---

## 4. Identity and Access (Overview)

Access is controlled by **IAM** (Identity and Access Management). Each permission is granted as:

> **Who** (principal) gets **which role** on **which resource**.

| Principal | Description |
|---|---|
| **User account** | A person (Google account) |
| **Group** | Collection of users, preferred for managing access |
| **Service account** | Identity for applications and automation, not for humans |

Roles are collections of permissions. Prefer **predefined** or **custom** roles over the broad primitive roles (`Owner`, `Editor`, `Viewer`) and follow the principle of least privilege.

Details are covered in the IAM and Service Accounts articles.

---

## 5. Billing and Costs

- A **billing account** pays for one or more projects. A project without a linked billing account cannot use paid services.
- Costs are **usage-based** (e.g. per compute hour, per GB stored, per GB scanned).
- **Budgets and alerts** notify when spending crosses a threshold. They do **not** stop spending by default.
- **Labels** (key-value tags on resources) allow cost attribution, e.g. `team=ml`, `env=prod`.

Typical cost traps for data science and ML work:

| Trap | Cause |
|---|---|
| Idle notebooks / VMs | Instances keep running and billing |
| GPUs | Expensive per hour, often left allocated |
| Egress | Moving data out of a region or out of GCP |
| Unfiltered BigQuery queries | Billing depends on bytes scanned |
| Forgotten disks and snapshots | Storage costs continue after deleting the VM |

---

## 6. Interacting with GCP

| Method | Use |
|---|---|
| **Console** | Web UI, good for exploring |
| **gcloud CLI** | Scripting and daily work |
| **Client libraries** | Access from code (e.g. `google-cloud-storage` for Python) |
| **Terraform / IaC** | Reproducible infrastructure |
| **REST APIs** | Underlying interface for all of the above |

### gcloud basics

```bash
# Initial setup and login
gcloud init
gcloud auth login

# Select the active project and default region
gcloud config set project my-project-id
gcloud config set compute/region europe-west3

# Inspect the current configuration
gcloud config list

# Named configurations for switching between projects/accounts
gcloud config configurations create dev
gcloud config configurations activate dev
```

### Two kinds of authentication

| Command | Used by |
|---|---|
| `gcloud auth login` | The `gcloud` CLI itself |
| `gcloud auth application-default login` | **Application Default Credentials (ADC)**, picked up automatically by client libraries in your code |

> **Note:** In production, code should use an attached service account (e.g. on GKE or Cloud Run) instead of personal credentials or downloaded key files.

---

## 7. Service Landscape for Data Science

| Category | Service | Role |
|---|---|---|
| **Compute** | Compute Engine | Virtual machines |
| | GKE | Managed Kubernetes |
| | Cloud Run | Serverless containers |
| **Storage** | Cloud Storage (GCS) | Object storage, data lake foundation |
| **Data** | BigQuery | Serverless data warehouse |
| **ML** | Vertex AI | Training, pipelines, model registry, endpoints |
| **DevOps** | Artifact Registry, Cloud Build | Images, packages, CI/CD |
| **Operations** | Cloud Logging, Cloud Monitoring | Logs, metrics, alerting |

---

## 8. Shared Responsibility

In a managed cloud, responsibility is split:

| Provider (Google) | Customer (you) |
|---|---|
| Physical data centers, hardware, network | IAM and access configuration |
| Managed service availability | Data and its classification |
| Underlying platform security | Application code and configuration |
| | Cost control |

The more managed a service is, the more the provider handles. Misconfigured permissions and publicly exposed data remain the customer's responsibility.

---

## Key Takeaways

- Resources live in **projects**, projects live in **folders** and an **organization**; IAM is inherited downwards.
- Use **separate projects** per environment for isolation and clear costs.
- Pick the **region** deliberately: latency, price, compliance and egress all depend on it.
- **APIs must be enabled** per project.
- Access follows **who / which role / which resource**; use service accounts for automation and least privilege.
- **Budgets alert but do not stop** spending; watch idle compute, GPUs and egress.
- Use **ADC** for local development and attached service accounts in production.

---

## Related Topics

- IAM and Service Accounts
- Cloud Storage
- BigQuery
- Vertex AI
- GKE (compared to Kubernetes and OpenShift)
- Cloud Native