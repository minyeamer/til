# Merge
  1. [INNER JOIN](#1-inner-join)
  2. [LEFT JOIN](#2-left-join)
     + [SELF JOIN](#self-join)
  3. [Grouping Data](#3-grouping-data)
  4. [Subquery](#4-subquery)

---

## 1. INNER JOIN

```sql
SELECT 
    l.Title,
    r.Name
FROM 
    albums AS l
INNER JOIN
    artists AS r
ON 
    r.ArtistId = l.ArtistId;
```

```sql
SELECT
   Title, 
   Name
FROM
   albums
INNER JOIN artists USING(ArtistId);
```

---

## 2. LEFT JOIN

```sql
SELECT
    Name, 
    Title
FROM
    artists
LEFT JOIN albums ON artists.ArtistId = albums.ArtistId
ORDER BY 
    Name;
```

### SELF JOIN

```sql
SELECT m.firstname || ' ' || m.lastname AS 'Manager',
       e.firstname || ' ' || e.lastname AS 'Receives reports from'
FROM
    employees e
INNER JOIN 
    employees m 
ON 
    m.employeeid = e.reportsto
ORDER BY 
    manager;
```

- 'A 테이블'과 A 테이블의 복사본인 'B 테이블'을 합치기

---

## 3. Grouping Data

![agg_func](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fcd1Qdy%2Fbtry2mpwTaX%2FLmDbCSlFsyDXGTPz1Ajrik%2Fimg.png)

```sql
SELECT
    albumid,
    COUNT(trackid)
FROM
    tracks
GROUP BY
    albumid
ORDER BY 
    COUNT(trackid) DESC;
```

```sql
SELECT
    albumid,
    COUNT(trackid)
FROM
    tracks
GROUP BY
    albumid
HAVING
    albumid = 1;
```

```sql
SELECT
    albumid,
    COUNT(trackid)
FROM
    tracks
WHERE
    COUNT(trackid) BETWEEN 18 AND 20
GROUP BY
    albumid;
```

- **에러발생**: `WHERE`문에는 집계함수 사용 불가   
- `WHERE`가 집계함수보다 우선적으로 실행되기 때문

```sql
SELECT
    tracks.albumid,
    title,
    MIN(tracks.milliseconds),
    MAX(tracks.milliseconds),
    ROUND(AVG(tracks.milliseconds), 2)
FROM
    tracks
INNER JOIN albums ON albums.albumid = tracks.albumid
GROUP BY
    tracks.albumid;
```

- `ROUND`는 n번째 자리까지 나타나도록 반올림

---

## 4. Subquery

```sql
SELECT AVG(SUM(bytes))
FROM tracks
GROUP BY albumid;
```

- SELECT 문에서 집계함수의 결과 값에 바로 중첩하여 집계함수 적용 불가

```sql
SELECT
    AVG(SIZE)
FROM
    (SELECT
         SUM(bytes) AS SIZE
     FROM
         tracks
     GROUP BY
         albumid);
```
