# Simple exercises from psql

### 2. [Control which rows are retrieved - part 2] (https://pgexercises.com/questions/basic/where2.html)
> Answer
```sql
SELECT facid, name, membercost, monthlymaintenance 
	FROM cd.facilities 
		WHERE membercost < monthlymaintenance/50.0
			AND membercost > 0;
```

### 2. [Basic string searches - LIKE operator] (https://pgexercises.com/questions/basic/where3.html)
> Answer
```sql
SSELECT * FROM cd.facilities
	WHERE name 
		like '%Tennis%';
```

### 3. [Matching against multiple possible values - IN Operator] (https://pgexercises.com/questions/basic/where4.html)
> Answer
```sql
SELECT * FROM cd.facilities 
	WHERE facid IN (1, 5);
```

### 4. [Working with dates] (https://pgexercises.com/questions/basic/date.html)
> Answer
```sql
SELECT memid, surname, firstname, joindate
	FROM cd.members
		WHERE joindate >= '2012-09-01 00:00:00'; 
```

### 5. [Removing duplicates, and ordering results- LIMIT OPERATOR] (https://pgexercises.com/questions/basic/unique.html)
> Answer
```sql
SELECT DISTINCT surname from cd.members 
	ORDER BY surname ASC 
		LIMIT 10;
```

### 6. [Combining results from multiple queries - UNION] (https://pgexercises.com/questions/basic/union.html)
> Answer
```sql
SELECT name as surname from cd.facilities 
	UNION 
		SELECT surname from cd.members;
```

### 7. [More aggregation ] (https://pgexercises.com/questions/basic/agg2.html)
> Answer
```sql
SELECT firstname, surname , joindate FROM cd.members 
	WHERE joindate = (
		SELECT MAX(joindate) 
	  		FROM cd.members);
```
