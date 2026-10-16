# MongoDB

## TL;DR

- **MongoDB** is a document-oriented NoSQL database that stores data in flexible, JSON-like documents.
- Documents are stored in **BSON**, a binary representation of JSON with additional data types.
- Collections group documents, roughly corresponding to tables in relational databases.
- MongoDB supports filtering, aggregation pipelines, indexes, and transactions.
- Its flexible schema is useful for evolving data structures, but data validation and thoughtful modeling are still important.

## What Is MongoDB?

MongoDB is a document database designed to store and query data as documents rather than rows in relational tables.

A document can contain nested objects, arrays, and fields of different supported data types.

Example document:

```json
{
  "_id": "user_001",
  "name": "Alice",
  "role": "Data Scientist",
  "skills": ["Python", "SQL", "Machine Learning"],
  "location": {
    "city": "Munich",
    "country": "Germany"
  }
}
```

MongoDB stores documents in BSON (Binary JSON). BSON supports additional types, such as dates and binary data, that are not part of standard JSON.

## Core Concepts

| Concept | Description | Relational equivalent |
|---|---|---|
| Database | Container for collections | Database |
| Collection | Group of documents | Table |
| Document | Individual record | Row |
| Field | Named value in a document | Column |
| `_id` | Unique document identifier within a collection | Primary key |
| Index | Data structure that speeds up queries | Database index |

Unlike a traditional relational schema, documents in the same collection can have different fields. MongoDB also supports schema validation when consistent structures are required.

## Basic CRUD Operations

CRUD stands for Create, Read, Update, and Delete.

### Create

Insert a document into a collection:

```javascript
db.users.insertOne({
  name: "Alice",
  role: "Data Scientist",
  active: true
});
```

### Read

Find documents matching a filter:

```javascript
db.users.find({
  role: "Data Scientist",
  active: true
});
```

Find one document:

```javascript
db.users.findOne({
  name: "Alice"
});
```

### Update

Update a field in a matching document:

```javascript
db.users.updateOne(
  { name: "Alice" },
  { $set: { active: false } }
);
```

### Delete

Delete matching documents:

```javascript
db.users.deleteOne({
  name: "Alice"
});
```

Always check the filter before running update or delete operations to avoid modifying unintended documents.

## Query Operators

MongoDB provides operators for filtering documents.

```javascript
db.products.find({
  price: { $gt: 100 },
  category: { $in: ["laptop", "tablet"] }
});
```

Common operators include:

- `$eq`: Equal to.
- `$gt` / `$gte`: Greater than / greater than or equal to.
- `$lt` / `$lte`: Less than / less than or equal to.
- `$in`: Matches any value in a specified list.
- `$and` / `$or`: Combine conditions.
- `$exists`: Checks whether a field exists.

MongoDB also supports projections to select which fields are returned.

```javascript
db.users.find(
  { active: true },
  { name: 1, role: 1, _id: 0 }
);
```

## Aggregation Pipeline

The aggregation framework processes documents through a sequence of stages. It is useful for grouping, transforming, and summarizing data.

Example: calculate average product prices by category.

```javascript
db.products.aggregate([
  {
    $group: {
      _id: "$category",
      averagePrice: { $avg: "$price" },
      productCount: { $sum: 1 }
    }
  },
  {
    $sort: { averagePrice: -1 }
  }
]);
```

Common aggregation stages include:

- `$match`: Filter documents.
- `$group`: Group documents and calculate aggregates.
- `$project`: Select or transform fields.
- `$unwind`: Expand an array into individual documents.
- `$sort`: Sort documents.
- `$limit`: Limit the number of results.
- `$lookup`: Join data from another collection.

The order of stages matters because each stage processes the output of the preceding stage.

## Data Modeling: Embedding vs. Referencing

MongoDB supports two common approaches to representing related data.

**Embedding:** Store related data inside the same document.

```json
{
  "name": "Alice",
  "address": {
    "city": "Munich",
    "country": "Germany"
  }
}
```

Embedding can simplify reads when related data is usually accessed together.

**Referencing:** Store an identifier that points to a document in another collection.

```json
{
  "name": "Alice",
  "department_id": "dept_10"
}
```

Referencing is useful when related data is shared, changes independently, or would otherwise create excessively large documents.

The choice depends on access patterns, data duplication, update requirements, and document size.

## Indexes

Indexes improve query performance by allowing MongoDB to find matching documents without scanning an entire collection in many cases.

Create an index on a frequently queried field:

```javascript
db.users.createIndex({ email: 1 }, { unique: true });
```

The unique constraint prevents duplicate indexed email values, subject to MongoDB's handling of missing and `null` fields.

Common index types include:

- Single-field indexes.
- Compound indexes.
- Multikey indexes for array fields.
- Text indexes.
- Geospatial indexes.
- Specialized indexes, depending on the deployment and use case.

Indexes consume storage and increase the cost of writes. Use `explain()` to inspect query plans and evaluate whether an index improves performance.

## MongoDB vs. Relational Databases

| MongoDB | Relational databases |
|---|---|
| Stores documents in collections | Stores data in tables |
| Flexible document structures | Typically uses predefined schemas |
| Supports embedding and references | Commonly models relationships using foreign keys and joins |
| Uses aggregation pipelines | Uses SQL for querying and aggregation |
| Supports multi-document transactions | Transaction support is common, with behavior depending on the database |
| Useful for nested or evolving data structures | Useful for highly structured data and relational constraints |

MongoDB is not automatically faster or more scalable than a relational database. The best choice depends on the data model, consistency requirements, query patterns, and operational constraints.

## Best Practices

- Design document structures around actual query and update patterns.
- Use schema validation when data consistency matters.
- Create indexes based on measured query performance.
- Avoid unbounded arrays and excessively large documents.
- Use projections to return only the fields needed.
- Apply appropriate authentication and access controls.
- Use backups and test restoration procedures.
- Inspect expensive queries with `explain()`.
- Use transactions when operations across multiple documents must be atomic.

## Related Topics

- NoSQL Databases
- Relational Model
- Database Indexes
- Data Modeling
- Aggregation
- Database Transactions
- ETL and Data Pipelines