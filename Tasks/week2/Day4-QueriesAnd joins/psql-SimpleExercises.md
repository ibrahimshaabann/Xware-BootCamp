# Simple exercises from psql

### <a href = "https://pgexercises.com/questions/basic/where2.html"> 1. Control which rows are retrieved - part 2</a>
> Answer
```sql
SELECT facid, name, membercost, monthlymaintenance 
	FROM cd.facilities 
		WHERE membercost < monthlymaintenance/50.0
			AND membercost > 0;
```

### <a href = "https://pgexercises.com/questions/basic/where3.html">2. Basic string searches - LIKE operator</a>
> Answer
```sql
SSELECT * FROM cd.facilities
	WHERE name 
		like '%Tennis%';
```
### <a href = "https://pgexercises.com/questions/basic/where4.html">3. Matching against multiple possible values - IN Operator</a>
> Answer
```sql
SELECT * FROM cd.facilities 
	WHERE facid IN (1, 5);
```

### <a href = "https://pgexercises.com/questions/basic/date.html">4. Working with dates</a>
> Answer
```sql
SELECT memid, surname, firstname, joindate
	FROM cd.members
		WHERE joindate >= '2012-09-01 00:00:00'; 
```

### <a href = "https://pgexercises.com/questions/basic/unique.html">5. Removing duplicates, and ordering results- LIMIT OPERATOR</a>
> Answer
```sql
SELECT DISTINCT surname from cd.members 
	ORDER BY surname ASC 
		LIMIT 10;
```

### <a href = "https://pgexercises.com/questions/basic/union.html">6. [Combining results from multiple queries - UNION]/a>
> Answer
```sql
SELECT name as surname from cd.facilities 
	UNION 
		SELECT surname from cd.members;
```

### <a href = "https://pgexercises.com/questions/basic/agg2.html">7. More aggregation </a>
> Answer
```sql
SELECT firstname, surname , joindate FROM cd.members 
	WHERE joindate = (
		SELECT MAX(joindate) 
	  		FROM cd.members);
```
