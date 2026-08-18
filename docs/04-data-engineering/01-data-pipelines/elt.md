# ELT

## TL;DR

**ELT (Extract, Load, Transform)** is a data integration pattern where data is first loaded into a target system and transformed **afterwards**.

The basic workflow is:

$$
\boxed{
\text{Extract}
\rightarrow
\text{Load}
\rightarrow
\text{Transform}
}
$$

ELT is common with modern **data warehouses** and **data lakes**, where large amounts of raw data can be stored and transformed using the target system's computing power.

---

## Extract

Data is extracted from one or more sources, such as:

* databases
* APIs
* CSV files
* cloud storage
* applications

The extracted data is usually kept close to its original form.

---

## Load

The raw data is loaded directly into the target system.

For example:

$$
\text{Database}
\rightarrow
\text{Raw Data}
\rightarrow
\text{Data Warehouse}
$$

The raw data can be stored for later processing and auditing.

---

## Transform

Transformations are performed **inside the target system**.

Typical operations include:

* cleaning data
* filtering
* joining tables
* changing data types
* aggregating data
* removing duplicates

For example:

$$
\text{Raw Data}
\rightarrow
\text{Clean Data}
\rightarrow
\text{Analytics Tables}
$$

---

## ETL vs. ELT

The main difference is **when the transformation happens**.

**ETL:**

$$
\text{Extract}
\rightarrow
\text{Transform}
\rightarrow
\text{Load}
$$

**ELT:**

$$
\text{Extract}
\rightarrow
\text{Load}
\rightarrow
\text{Transform}
$$

ETL transforms data before it reaches the target system, while ELT keeps the raw data and transforms it afterwards.

---

## Advantages

ELT is useful when the target system provides significant computing power.

Advantages include:

* raw data is preserved
* transformations can be changed and rerun
* large datasets can be processed efficiently
* transformations can be performed directly in the data warehouse
* different downstream datasets can be created from the same raw data

---

## Example

A company collects sales data from many stores:

$$
\text{Store Databases}
\rightarrow
\text{Extract}
\rightarrow
\text{Raw Data Warehouse}
\rightarrow
\text{Transform}
\rightarrow
\text{Analytics}
$$

The raw data remains available, allowing transformations to be modified without extracting the source data again.

---

## Key Takeaway

ELT separates **data ingestion** from **data transformation**.

$$
\boxed{
\text{Extract}
\rightarrow
\text{Load Raw Data}
\rightarrow
\text{Transform}
}
$$

It is particularly suitable for modern data platforms that can store large amounts of raw data and perform transformations at scale.
