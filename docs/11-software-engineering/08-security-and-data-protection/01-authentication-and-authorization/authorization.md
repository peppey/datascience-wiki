# Authorization

## TL;DR

- **Authorization** determines what an authenticated user, service, or application is allowed to do.
- **Authentication** verifies identity; authorization determines permissions.
- Common models include Role-Based Access Control (RBAC), Attribute-Based Access Control (ABAC), and Access Control Lists (ACLs).
- Follow the principle of least privilege: grant only the permissions required.
- In Kubernetes and OpenShift, RBAC controls access to API resources and operations.

## Authentication vs. Authorization

| Concept | Question | Example |
|---|---|---|
| Authentication | Who are you? | Logging in with a password or SSH key |
| Authorization | What are you allowed to do? | Permission to deploy an application |
| Auditing | What happened? | Recording who changed a deployment |

Authentication usually precedes authorization, although the exact flow depends on the system.

## Common Authorization Models

**Role-Based Access Control (RBAC)**

Permissions are assigned to roles, which are then granted to users or service accounts.

Example: A developer can view and update deployments but cannot manage cluster-wide permissions.

**Attribute-Based Access Control (ABAC)**

Access decisions depend on attributes such as user identity, resource classification, environment, or time.

Example: A user may access a document only if they belong to the relevant department and have the required clearance.

**Access Control Lists (ACLs)**

Permissions are defined for individual resources and their associated users or groups.

Example: A file grants read access to one group and write access to another.

## Authorization in Kubernetes and OpenShift

Kubernetes uses RBAC to control access to its API.

The main resources are:

- **Role:** Defines permissions within a namespace.
- **ClusterRole:** Defines permissions that can apply across a cluster or be reused in namespace bindings.
- **RoleBinding:** Grants a Role or ClusterRole to users, groups, or service accounts within a namespace.
- **ClusterRoleBinding:** Grants a ClusterRole across the cluster.

Example: Allow a service account to read pods in a specific namespace.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: development
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "list", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: pod-reader-binding
  namespace: development
subjects:
  - kind: ServiceAccount
    name: application
    namespace: development
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: pod-reader
```

This grants the `application` service account read access to pods in the `development` namespace. It does not grant permission to create or delete pods.

Check permissions using:

```bash
kubectl auth can-i list pods -n development
kubectl auth can-i create deployments -n development
```

For OpenShift, the equivalent command is `oc auth can-i`.

## Best Practices

- **Least privilege:** Grant only the permissions needed for a task.
- **Use groups and roles:** Avoid managing permissions individually for every user.
- **Separate duties:** Limit who can deploy, administer, and change access controls.
- **Avoid excessive privileges:** Do not grant `cluster-admin` or wildcard permissions without a clear need.
- **Review permissions regularly:** Remove obsolete accounts, roles, and bindings.
- **Use service accounts for workloads:** Avoid embedding human credentials in applications.
- **Audit access:** Monitor permission changes and sensitive operations.
- **Test effective permissions:** Verify what an identity can actually do rather than relying only on configuration assumptions.

## Related Topics

- Authentication
- Role-Based Access Control (RBAC)
- Policy Management
- Identity and Access Management (IAM)
- Kubernetes and OpenShift
- SSH Keys
