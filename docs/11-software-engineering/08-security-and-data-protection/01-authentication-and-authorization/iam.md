# Identity and Access Management (IAM)

## TL;DR

- **Identity and Access Management (IAM)** manages digital identities and controls their access to systems and resources.
- IAM combines identity management, authentication, authorization, and access lifecycle management.
- **Authentication** verifies who you are; **authorization** determines what you can do.
- Common IAM concepts include users, groups, roles, permissions, service accounts, and policies.
- Follow the principle of least privilege and regularly review access rights.

## What Is IAM?

IAM is the framework of technologies, processes, and policies used to manage identities and control access to applications, infrastructure, data, and services.

Typical goals include:

- **Security:** Prevent unauthorized access.
- **Least privilege:** Grant only the permissions necessary for a task.
- **Centralized management:** Manage identities and access consistently.
- **Compliance:** Support auditing and regulatory requirements.
- **Lifecycle management:** Provision, update, and revoke access as responsibilities change.

## Core Components

| Component | Purpose | Example |
|---|---|---|
| Identity | Represents a user or workload | Employee account or application identity |
| Authentication | Verifies an identity | Password, MFA, SSH key |
| Authorization | Determines permitted actions | Permission to read a dataset |
| Role | Groups permissions | Developer or administrator |
| Policy | Defines access rules | Allow read access to a specific resource |
| Identity lifecycle | Manages access over time | Create, update, or disable an account |
| Audit logging | Records security-relevant events | Log changes to permissions |

## IAM vs. Authentication vs. Authorization

IAM is the broader framework that encompasses identity management and access control.

- **Authentication:** Who or what is making the request?
- **Authorization:** Is this identity allowed to perform the requested action?
- **IAM:** How are identities, credentials, permissions, and access policies managed throughout their lifecycle?

For example, an employee authenticates using single sign-on (SSO). IAM provides the identity and access framework, while authorization determines whether the employee can access a particular application or dataset.

## IAM in Cloud Platforms

Cloud providers use IAM to control access to resources such as storage buckets, virtual machines, databases, and machine learning services.

Examples include:

- **Google Cloud IAM:** Grants principals roles containing permissions on Google Cloud resources.
- **AWS IAM:** Manages identities, roles, policies, and access to AWS services.
- **Microsoft Entra ID and Azure RBAC:** Manage identities and access to Microsoft services and Azure resources.

Cloud IAM often distinguishes between human users and workloads. Applications should generally use managed identities, workload identity federation, or service accounts rather than long-lived personal credentials.

## IAM in Kubernetes and OpenShift

Kubernetes has its own authorization mechanisms, including RBAC, while authentication can integrate with external identity providers.

Important concepts include:

- **Users and groups:** Represent human identities.
- **Service accounts:** Provide identities for workloads.
- **Roles and bindings:** Define and grant Kubernetes API permissions.
- **External identity providers:** Integrate cluster access with organizational identity systems.

In OpenShift, authentication can be integrated with identity providers, while OpenShift RBAC determines what authenticated users and service accounts can do.

Kubernetes RBAC and cloud IAM are related but distinct: permission to create a pod does not automatically grant that pod permission to access a cloud storage bucket.

## Best Practices

- **Apply least privilege:** Grant only the access required.
- **Use MFA:** Protect human accounts with multi-factor authentication.
- **Prefer SSO:** Centralize authentication and simplify account management.
- **Use workload identities:** Avoid embedding long-lived credentials in source code.
- **Separate environments:** Keep development, testing, and production permissions distinct.
- **Automate the access lifecycle:** Revoke access when it is no longer needed.
- **Audit permissions:** Regularly review roles, policies, and access logs.
- **Separate duties:** Avoid giving every user administrative privileges.

## Related Topics

- Authentication
- Authorization
- Role-Based Access Control (RBAC)
- Policy Management
- Secrets Management
- Kubernetes and OpenShift
- Zero Trust Security
