# SQL CRUD
  1. [SELECT](#1-select)
  2. [INSERT](#2-insert)
  3. [UPDATE](#3-update)
  4. [Sorting](#4-sorting)
  5. [Filtering](#5-filtering)
     + [DISTINCT](#distinct)
     + [WHERE](#where)
     + [WHERE & LIKE](#where--like)
     + [WHERE & IN](#where--in)
     + [WHERE & LIMIT/OFFSET](#where--limitoffset)
     + [WHERE & BETWEEN](#where--between)
     + [WHERE & IS NULL](#where--is-null)

---

## 1. SELECT

```sql
SELECT 10 / 5, 2 * 4;
```

```sql
SELECT trackid, name FROM tracks;
```

```sql
SELECT * FROM tracks;
```

---

## 2. INSERT

```sql
INSERT INTO artists (name) VALUES('Bud Powell');
```

```python
script = """
INSERT INTO artists (name) VALUES ("?");
"""

data = [
    ("Buddy Rich"),
    ("Candido"),
    ("Charlie Byrd")
]

cur.executemany(script, data)
```

```sql
SELECT
    ArtistId,
    Name
FROM
    Artists
ORDER BY
    ArtistId DESC;
```

---

## 3. UPDATE

```sql
UPDATE employees SET lastname = 'Smith' WHERE employeeid = 3;
```

```sql
UPDATE employees
SET city = 'Toronto', 
    state = 'ON',
    postalcode = 'M5P 2N7'
WHERE
    employeeid = 4;
```

```sql
UPDATE employees
SET email = UPPER(firstname || "." || lastname || "@corp.co.kr");
```

---

## 4. Sorting

```sql
SELECT 
    TrackId, 
    Name, 
    Composer 
FROM 
   tracks
ORDER BY 
   Composer;
```

- NULL Data인 `None`은 SQLite3에서 가장 작은 값으로 인식

---

## 5. Filtering

![filter](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fcd8FQA%2Fbtry8PcADOq%2FzrkmkbE8MVVc1SWXLWz4b1%2Fimg.png)

### DISTINCT

```sql
SELECT DISTINCT city FROM customers;
```

- NULL을 포함한 중복값을 하나만 남기고 제외

```sql
SELECT DISTINCT city, country FROM customers;
```

- 2개 열의 값이 모두 동일한 행들을 제외

### WHERE

![where](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FqByrF%2Fbtry317a3uz%2Fa60xzAT4A92AkXLff1wXq1%2Fimg.png)

```sql
SELECT
   name,
   milliseconds,
   bytes,
   albumid
FROM
   tracks
WHERE
   (albumid = 10) AND (milliseconds > 250000);
```

### WHERE & LIKE

![wildcard](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdCL8hC%2Fbtry5DdLCRW%2FdCVmZCCpFPN2i5m3JSTqK0%2Fimg.png)

```sql
SELECT
    trackid,
    name
FROM
    tracks
WHERE
    name LIKE 'Wild%';
```

### WHERE & IN

```sql
SELECT
    TrackId,
    Name,
    MediaTypeId
FROM
    Tracks
WHERE
    MediaTypeId IN (1, 2)
```

### WHERE & LIMIT/OFFSET

```sql
SELECT
    trackId,
    name
FROM
    tracks
LIMIT 10 OFFSET 7;
```
- `LIMIT`: 불러오는 값의 수
- `OFFSET`: OFFSET에 해당하는 수만큼 떼어내 그 이후의 데이터 불러옴

### WHERE & BETWEEN

```sql
SELECT
    InvoiceId,
    BillingAddress,
    Total
FROM
    invoices
WHERE
    Total BETWEEN 14.91 AND 18.86
ORDER BY
    Total; 
```

### WHERE & IS NULL

```sql
SELECT
    Name, 
    Composer
FROM
    tracks
WHERE
    Composer IS NULL
ORDER BY 
    Name; 
```
