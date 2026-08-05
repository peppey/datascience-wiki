# APIs 

## API Definition

An **API definition** describes the contract between two software components: what requests can be sent, what responses are returned, and how communication works.

An API definition specifies:

- available endpoints
- input and output formats
- authentication
- error handling
- expected behavior

## API Contract

An API acts as an agreement between a **client** and a **server**.

```text
Client  ───── Request ─────>  API  ─────>  Server

Client  <──── Response ─────  API  <───── Server
```

The contract defines:
Endpoint: where to send requests
HTTP method: what operation to perform
Parameters: required inputs
Request schema: input structure
Response schema: output structure
Status codes: success/error states

## Endpoints

An endpoint consists of:
HTTP Method + Path + Parameters + Response


## API Schemas

Common schema technologies:
- JSON Schema
- OpenAPI
- Pydantic models

## API versioning

APIs evolve over time. Versioning prevents breaking existing clients.

Example:

```text
/api/v1/predict
/api/v2/predict
```

Common strategies:
URL versioning
Header versioning
Query parameter versioning


## Authentication and Authorization
APIs often require authentication.

Common methods:
- API keys
- OAuth2
- JWT tokens
- session-based authentication

Authentication answers: Who are you?

Authorization answers: What are you allowed to do?

## Error Handling

Good APIs provide structured errors.

Example:
```text
{
  "error": "Invalid input",
  "message": "Feature vector has wrong dimension",
  "code": "INVALID_FEATURES"
}
```



