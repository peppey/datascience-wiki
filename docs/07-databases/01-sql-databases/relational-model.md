# Relational Model

## TL;DR

- The **relational model** represents data as relations, commonly implemented as tables in relational databases.
- Each table consists of rows (tuples) and columns (attributes).
- **Primary keys** uniquely identify rows; **foreign keys** establish relationships between tables.
- Constraints maintain data integrity, while normalization reduces redundancy and update anomalies.
- SQL is the most common language for querying and modifying relational databases.

## What Is the Relational Model?

The relational model, introduced by Edgar F. Codd in 1970, organizes data into relations. In practical database systems, these are typically represented as tables.

Consider a database for employees and departments:

**Employees**

| employee_id (PK) | name | department_id (FK) |
|---:|---|---:|
| 1 | Alice | 10 |
| 2 | Bob | 20 |
| 3 | Carol | 10 |

**Departments**

| department_id (PK) | department_name |
|---:|---|
| 10 | Data Science |
| 20 | Engineering |

Each row represents an entity or record, and each column represents an attribute. The `department_id` foreign key connects employees to their departments.

## Core Concepts

**Relation**

A set of tuples sharing the same attributes. In SQL databases, a relation is commonly represented as a table.

**Tuple**

A single row in a relation, representing one record.

**Attribute**

A named property of a relation, represented by a column.

**Domain**

The set of permitted values for an attribute, such as integers, dates, or a defined set of categories.

**Schema**

The structure of a relation, including its attributes and associated constraints.

## Keys

Keys identify records and establish relationships between tables.

- **Superkey:** Any set of attributes that uniquely identifies a row.
- **Candidate key:** A minimal superkey; removing any attribute would make it non-unique.
- **Primary key:** The candidate key selected as the main identifier.
- **Foreign key:** An attribute or set of attributes referencing a key in another table (or the same table).
- **Composite key:** A key consisting of multiple attributes.

Example:

```sql
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT REFERENCES departments(department_id)
);
```

The foreign key prevents an employee from referencing a department that does not exist, unless the reference is `NULL` and the column permits it.

## Relationships Between Tables

Relational databases commonly represent three types of relationships:

- **One-to-one (1:1):** Each record is associated with at most one record in the other table.
- **One-to-many (1:N):** One department can have many employees, but each employee references at most one department.
- **Many-to-many (M:N):** An employee can work on multiple projects, and each project can have multiple employees.

Many-to-many relationships are typically implemented using a junction table.

```sql
CREATE TABLE employee_projects (
    employee_id INT REFERENCES employees(employee_id),
    project_id INT REFERENCES projects(project_id),
    PRIMARY KEY (employee_id, project_id)
);
```

The composite primary key prevents the same employee-project assignment from being recorded twice.

## Integrity Constraints

Integrity constraints ensure that stored data remains valid.

- **Entity integrity:** A primary key must uniquely identify each row and cannot be `NULL`.
- **Referential integrity:** A foreign key must reference an existing key or be `NULL` if permitted.
- **Domain integrity:** Values must satisfy their data types and applicable constraints.
- **Uniqueness:** A `UNIQUE` constraint prevents duplicate values or combinations of values.
- **Business rules:** Additional constraints express application-specific requirements.

Example:

```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0)
);
```

This table prevents negative prices and missing price values.

## Normalization

Normalization structures relations to reduce unnecessary redundancy and prevent anomalies.

- **First Normal Form (1NF):** Attributes contain single values rather than repeating groups or nested lists of values.
- **Second Normal Form (2NF):** The relation is in 1NF, and every non-prime attribute depends on the whole of every candidate key, not just part of a composite candidate key.
- **Third Normal Form (3NF):** The relation is in 2NF, and non-key attributes do not have inappropriate transitive dependencies on candidate keys.

For example, storing a department name repeatedly in every employee record creates redundancy. Separating departments into their own table avoids inconsistent copies of the same department name.

Normalization improves consistency but can require additional joins. Some analytical systems deliberately use denormalized structures to improve query performance.

## Querying Relational Data

SQL retrieves and combines data from relations.

Example: list employees with their department names.

```sql
SELECT
    e.name,
    d.department_name
FROM employees AS e
JOIN departments AS d
    ON e.department_id = d.department_id;
```

The join combines rows based on the relationship between the foreign key and primary key.

Other fundamental SQL operations include:

- `SELECT`: Retrieve data.
- `WHERE`: Filter rows.
- `JOIN`: Combine relations.
- `GROUP BY`: Aggregate rows into groups.
- `INSERT`, `UPDATE`, and `DELETE`: Modify data.

## Relational Model vs. NoSQL

| Relational databases | NoSQL databases |
|---|---|
| Structured relations and schemas | Often flexible or specialized data models |
| Relationships represented using keys and joins | Relationships may use documents, references, or denormalized data |
| SQL is widely used | Query interfaces vary by database |
| Strong support for constraints and transactions in many systems | Capabilities vary significantly by database |
| Often well suited to structured, interconnected data | Often useful for specialized scalability or data-model requirements |

Neither approach is universally better. The appropriate choice depends on data structure, consistency requirements, access patterns, and operational constraints.

## Best Practices

- Define primary keys explicitly.
- Use foreign keys to enforce relationships where appropriate.
- Choose suitable data types and constraints.
- Normalize transactional data to reduce redundancy.
- Use junction tables for many-to-many relationships.
- Add indexes based on query patterns and measured performance.
- Avoid storing multiple independent values in a single column when they should be modeled as separate records.

## Related Topics

- SQL Joins
- Database Normalization
- Primary and Foreign Keys
- Database Indexes
- Transactions and ACID
- Data Modeling
- Entity-Relationship Diagrams (ERDs)