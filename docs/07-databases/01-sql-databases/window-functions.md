# SQL Window Functions

## TL;DR

- **Window functions** perform calculations across related rows without collapsing them into a single row.
- `OVER()` defines the window over which a function operates.
- `PARTITION BY` divides rows into groups; `ORDER BY` defines their order within each group.
- Common use cases include ranking, running totals, moving averages, and comparing values across rows.
- Unlike `WHERE`, window functions are evaluated after filtering and grouping, so filtering their results usually requires a subquery or CTE.

## What Are Window Functions?

Window functions calculate a value using the current row and potentially other rows in the query result. Unlike aggregate functions used with `GROUP BY`, they preserve the individual rows.

Consider a table called `sales`:

| employee | department | amount |
|---|---|---:|
| Alice | Sales | 100 |
| Bob | Sales | 200 |
| Carol | IT | 150 |
| Dave | IT | 300 |

Using `GROUP BY` aggregates rows into groups:

```sql
SELECT department, SUM(amount) AS total
FROM sales
GROUP BY department;
```

Result:

| department | total |
|---|---:|
| Sales | 300 |
| IT | 450 |

A window function keeps every row while adding the department total:

```sql
SELECT
    employee,
    department,
    amount,
    SUM(amount) OVER (
        PARTITION BY department
    ) AS department_total
FROM sales;
```

Each employee remains in the result, with the corresponding department total added as a column.

## The OVER Clause

The `OVER` clause defines the window used by a window function.

```sql
function_name() OVER (
    PARTITION BY column
    ORDER BY column
)
```

Its components are:

- **`OVER()`** defines the window.
- **`PARTITION BY`** divides rows into independent groups. It is optional.
- **`ORDER BY`** defines the order in which rows are processed. It is optional, depending on the calculation.
- **Window frame** optionally specifies which rows within a partition participate in a calculation.

Without `PARTITION BY`, all rows belong to one partition.

## Ranking Functions

Ranking functions assign positions to rows, for example when identifying the highest sales per department.

```sql
SELECT
    employee,
    department,
    amount,
    ROW_NUMBER() OVER (
        PARTITION BY department
        ORDER BY amount DESC
    ) AS row_num,
    RANK() OVER (
        PARTITION BY department
        ORDER BY amount DESC
    ) AS sales_rank,
    DENSE_RANK() OVER (
        PARTITION BY department
        ORDER BY amount DESC
    ) AS dense_rank
FROM sales;
```

The ranking functions behave differently when values are tied:

| Amounts (descending) | `ROW_NUMBER()` | `RANK()` | `DENSE_RANK()` |
|---|---|---|---|
| 300 | 1 | 1 | 1 |
| 200 | 2 | 2 | 2 |
| 200 | 3 | 2 | 2 |
| 100 | 4 | 4 | 3 |

- `ROW_NUMBER()` assigns a unique sequential number to each row.
- `RANK()` assigns equal ranks to ties and leaves gaps afterward.
- `DENSE_RANK()` assigns equal ranks to ties without leaving gaps.

If deterministic row numbering is required, add a unique tie-breaker to the `ORDER BY` clause.

## Aggregate Window Functions

Aggregate functions such as `SUM()`, `AVG()`, `MIN()`, and `MAX()` can also be used as window functions.

### Running totals

A running total accumulates values in a specified order.

```sql
SELECT
    employee,
    amount,
    SUM(amount) OVER (
        ORDER BY employee
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM sales;
```

The total increases with each row according to the ordering by employee.

### Moving averages

Moving averages smooth fluctuations in time-series data.

```sql
SELECT
    date,
    daily_sales,
    AVG(daily_sales) OVER (
        ORDER BY date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS moving_avg_7_rows
FROM daily_sales;
```

This calculates an average over the current row and the six preceding rows. It represents a seven-day moving average only if the data contains exactly one row per day without gaps.

### Comparing values with group averages

```sql
SELECT
    employee,
    department,
    amount,
    AVG(amount) OVER (
        PARTITION BY department
    ) AS department_avg
FROM sales;
```

This is useful for comparing individual observations against group-level statistics without losing row-level detail.

## LAG and LEAD

`LAG()` and `LEAD()` access values from preceding or subsequent rows in a defined ordering.

- `LAG()` accesses a preceding row.
- `LEAD()` accesses a subsequent row.

Example: compare daily sales with the previous day.

```sql
SELECT
    date,
    daily_sales,
    LAG(daily_sales) OVER (
        ORDER BY date
    ) AS previous_day_sales
FROM daily_sales;
```

Calculate the change from the previous observation:

```sql
SELECT
    date,
    daily_sales,
    daily_sales - LAG(daily_sales) OVER (
        ORDER BY date
    ) AS sales_change
FROM daily_sales;
```

The first row has no preceding observation, so `LAG()` returns `NULL` by default.

## Window Frames

A window frame specifies which rows within a partition are considered for a calculation.

For example:

```sql
ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
```

includes the current row and the two preceding rows.

Common frame boundaries include:

- `UNBOUNDED PRECEDING`: Start of the partition.
- `n PRECEDING`: A specified number of preceding rows.
- `CURRENT ROW`: The current row.
- `n FOLLOWING`: A specified number of following rows.
- `UNBOUNDED FOLLOWING`: End of the partition.

**Important:** When an aggregate window function uses `ORDER BY` without an explicit frame, the default frame in PostgreSQL includes rows from the start of the partition through the current row and its peers. Tied ordering values can therefore affect running totals. Specify the frame explicitly when the intended behavior matters.

`ROWS` counts physical rows, whereas `RANGE` uses ordering values and peer groups. These are not interchangeable in every query.

## Filtering Window Function Results

Window functions cannot generally be used directly in a `WHERE` clause because they are evaluated later in the query's logical processing order.

For example, to select the highest-paid employee in each department, calculate the rank in a CTE and filter afterward:

```sql
WITH ranked_sales AS (
    SELECT
        employee,
        department,
        amount,
        ROW_NUMBER() OVER (
            PARTITION BY department
            ORDER BY amount DESC, employee
        ) AS rn
    FROM sales
)
SELECT employee, department, amount
FROM ranked_sales
WHERE rn = 1;
```

The CTE calculates the row numbers first. The outer query then filters the result to one employee per department. Here, ties are resolved alphabetically by employee name.

## Common Use Cases

| Use case | Typical functions |
|---|---|
| Top-N records per group | `ROW_NUMBER()`, `RANK()` |
| Running totals | `SUM() OVER()` |
| Moving averages | `AVG() OVER()` |
| Previous or next observation | `LAG()`, `LEAD()` |
| Group-level comparisons | `AVG() OVER(PARTITION BY ...)` |
| Cumulative distributions and relative rankings | `CUME_DIST()`, `PERCENT_RANK()` |
| First or last value in a frame | `FIRST_VALUE()`, `LAST_VALUE()` |

## Best Practices

- Use `PARTITION BY` to define the correct comparison groups.
- Specify `ORDER BY` whenever the result depends on row order.
- Add a unique tie-breaker when deterministic ordering is important.
- Define window frames explicitly for running totals and moving calculations when necessary.
- Use a CTE or subquery to filter window function results.
- Consider the cost of sorting and partitioning on large datasets; appropriate indexes and query plans may improve performance.

## Related Topics

- SQL Aggregations and `GROUP BY`
- Common Table Expressions (CTEs)
- SQL Joins
- Time-Series Analysis
- Data Modeling and Query Optimization
