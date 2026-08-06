# SQL Joins

## TL;DR

**SQL Joins** combine rows from multiple tables based on a related column.

They are used to retrieve connected information stored in different tables.

---

## Example Tables

### Customers

| id | name |
|---|---|
| 1 | Alice |
| 2 | Bob |

### Orders

| id | customer_id | product |
|---|---|---|
| 1 | 1 | Laptop |
| 2 | 2 | Phone |

---

## INNER JOIN

Returns only rows where a match exists in both tables.

```sql
SELECT *
FROM customers
INNER JOIN orders
ON customers.id = orders.customer_id;
```

Result:

| name  | product |
| ----- | ------- |
| Alice | Laptop  |
| Bob   | Phone   |


## LEFT JOIN

Returns all rows from the left table and matching rows from the right table.

```sql
SELECT *
FROM customers
LEFT JOIN orders
ON customers.id = orders.customer_id;
Useful when all entries from the main table should be kept.
```

## RIGHT JOIN

Returns all rows from the right table and matching rows from the left table.

```sql
SELECT *
FROM customers
RIGHT JOIN orders
ON customers.id = orders.customer_id;
```

## FULL OUTER JOIN

Returns all rows from both tables. Missing matches are filled with NULL.

```sql
SELECT *
FROM customers
FULL OUTER JOIN orders
ON customers.id = orders.customer_id;
```

## Summary

| Join            | Returns                             |
| --------------- | ----------------------------------- |
| INNER JOIN      | Only matching rows                  |
| LEFT JOIN       | All rows from left table + matches  |
| RIGHT JOIN      | All rows from right table + matches |
| FULL OUTER JOIN | All rows from both tables           |







