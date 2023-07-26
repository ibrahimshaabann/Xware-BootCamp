

## Page Unit in Database:
A page unit in a database refers to the smallest fixed-size block of data that can be read from or written to disk. It is used as a basic unit for data storage and retrieval. Databases store data on disk in pages to efficiently manage data storage and minimize disk I/O operations. Each page typically contains a specific number of data records or data blocks. When the database needs to read or write data, it operates on entire pages, reducing the overhead of reading or writing individual data items.

## Queries Execution with Execution Engine and Buffer Flow:
When a query is executed in a database, it goes through the following steps:

- Query Parsing: The database management system (DBMS) first parses the query to understand its syntax and semantics.

- Query Optimization: The DBMS then analyzes the query and generates an execution plan, which outlines the most efficient way to retrieve the requested data. The optimization phase aims to minimize the query's cost by selecting the best access methods, join algorithms, and indexes.

- Query Execution: The execution plan is executed by the query execution engine. The engine follows the steps specified in the plan to access the necessary data from disk or memory.

- Buffer Flow: When data is read from the disk, it is loaded into a buffer pool in memory. The buffer pool acts as a cache, holding frequently accessed data pages. When a query needs to read data, the engine first checks if the data is in the buffer pool. If it is, the engine retrieves it from memory, reducing the need for disk I/O, which is slower.

## Difference between SQL and NoSQL Databases:
SQL (Structured Query Language) and NoSQL (Not Only SQL) databases are two main categories of databases with different data models and characteristics:

- SQL Databases: SQL databases are relational databases that use SQL as the standard query language. They have a predefined schema that defines the structure of the data in tables with rows and columns. SQL databases are suitable for structured data and well-defined relationships between entities. They provide strong consistency, ACID properties (Atomicity, Consistency, Isolation, Durability), and are widely used for transactional applications.

- NoSQL Databases: NoSQL databases are non-relational databases that offer more flexibility in data modeling. They can handle unstructured or semi-structured data and are suitable for large-scale, distributed, and real-time applications. NoSQL databases relax consistency requirements in favor of high availability and scalability. They often use BASE properties (Basically Available, Soft state, Eventually consistent) instead of strict ACID properties.

## ACID and CRUD:

- ACID:
  - Atomicity: Ensures that a transaction is treated as a single unit of work, either all its operations are completed successfully or none at all.
  - Consistency: Guarantees that the database remains in a valid state before and after a transaction, and all data constraints are satisfied.
  - Isolation: Ensures that the operations of one transaction are isolated from the operations of other transactions until it is committed.
  - Durability: Ensures that the changes made by a committed transaction are permanent and survive system failures.

- CRUD:
  - Create: Inserting new records or objects into the database.
  - Read: Retrieving data or querying the database to read existing records.
  - Update: Modifying existing data in the database.
  - Delete: Removing records or objects from the database.

## Difference between CAD and BASE:

- CAD (Consistency, Availability, Durability):
  - Consistency: Similar to ACID, CAD ensures that the database remains in a valid state after a transaction.
  - Availability: Emphasizes that the database should always be accessible and responsive, even in the presence of failures or network partitions.
  - Durability: Similar to ACID, CAD ensures that committed transactions' changes are permanent and survive any failures.

- BASE (Basically Available, Soft state, Eventually consistent):
  - Basically Available: The system should be available to respond to read and write requests even if it is not fully consistent at all times.
  - Soft state: The system can be in an intermediate or partially inconsistent state during updates or replication.
  - Eventually consistent: Over time, the system converges to a consistent state as updates propagate through the system.

## Primary Key as Clustered Index:
In some SQL databases, the primary key is automatically implemented as a clustered index. A clustered index determines the physical order of data in a table based on the values of the indexed columns. When a table has a clustered index on the primary key, the rows of the table are physically stored on disk in the order of the primary key's values.

This arrangement has several benefits:
- Faster data retrieval: Since the rows are stored in the same order as the primary key, queries that use the primary key in their conditions can be executed more efficiently.
- Improved data locality: Related rows are stored together, which can lead to reduced disk I/O and better cache utilization.
- Efficient range queries: Range queries on the primary key or any column that follows the primary key's order can be performed more efficiently.

However, it's important to note that not all databases implement the primary key as a clustered index by default. Some databases offer separate options for specifying clustered and non-clustered indexes, allowing more flexibility in index design.
