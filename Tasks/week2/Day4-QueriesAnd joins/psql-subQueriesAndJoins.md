# Queries and Joins exercises from psql

### 1. <a href = "https://pgexercises.com/questions/joins/simplejoin.html"> Retrieve the start times of members' bookings</a>

> Answer
```sql
SELECT starttime from cd.bookings 
	WHERE memid = 
		(
  			SELECT memid FROM cd.members 
  			WHERE firstname = 'David' 
  			AND surname = 'Farrell'
		);
```

### 2. [Work out the start times of bookings for tennis courts - LIKE operator] (https://pgexercises.com/questions/joins/simplejoin2.html)
> Answer
```sql
SSELECT cd.bookings.starttime, cd.facilities.name 
	FROM 
		cd.bookings INNER JOIN cd.facilities 
		ON cd.bookings.facid =  cd.facilities.facid
	WHERE 
		cd.bookings.starttime >= '2012-09-21' AND
		cd.bookings.starttime < '2012-09-22'AND
		cd.facilities.name IN ('Tennis Court 1','Tennis Court 2')
ORDER BY cd.bookings.starttime;
```

### 3. [Produce a list of all members who have recommended another member- SELF RELATIONSHIP] (https://pgexercises.com/questions/joins/self.html)
> Answer
```sql
SELECT DISTINCT recs.firstname as firstname, recs.surname surname
	FROM 
		cd.members mems
		INNER JOIN cd.members recs
				ON recs.memid = mems.recommendedby
ORDER BY surname, firstname;
```

### 4. [Produce a list of all members, along with their recommender] (https://pgexercises.com/questions/joins/self2.html)
> Answer
```sql
SELECT mems.firstname as memfname, mems.surname as memsname,
       recs.firstname as recfname, recs.surname as recsname
	   		FROM cd.members mems 
				LEFT OUTER JOIN cd.members recs 
					ON recs.memid = mems.recommendedby
						ORDER BY mems.surname, mems.firstname;
```

### 5. [Produce a list of all members who have used a tennis court] (https://pgexercises.com/questions/basic/unique.html) 
* <span style = "color: Red;">That's a good question! </span> :+1:
> Answer
```sql
SELECT DISTINCT (cd.members.firstname || ' ' || cd.members.surname) AS member ,
       cd.facilities.name AS facility FROM cd.members 
	   		INNER JOIN cd.bookings
				ON cd.bookings.memid = cd.members.memid
					INNER JOIN cd.facilities
						ON cd.bookings.facid = cd.facilities.facid 
							 WHERE cd.facilities.name LIKE ('%Tennis Court%')
								ORDER BY member, facility;
				
```


