# Lab 03
## Chris Fleisch

1) List the execution time of the weblog aggregation query for Hive,
SparkSQL, and SparkSQL on Parquet.

Hive: ```Time taken: 111.783 seconds, Fetched: 50 row(s)```

SparkSQL: ```Time taken: 27.922 seconds, Fetched 50 row(s)```

SparkSQL on Parquet: ```Time taken: 9.604 seconds, Fetched 50 row(s)```

2) How many jobs does Hive launch? Does SparkSQL launch jobs?

Hive: ```Total jobs = 2```

SparkSQL does not appear to launch jobs. It looks like SparkSQL collects all
the data into memory from HDFS. It then runs the query on the data in memory
resulting in much faster output.

3) Write a query which joins weblogs_parquet to user_info and counts the
top 5 locations. List the locations.

```
La Fayette    49
Leeds         47
Blountsville  46
Hayden        45
Hamilton      45
```

```
SELECT location, count(location) AS loc_count
FROM weblogs_parquet INNER JOIN user_info
ON weblogs_parquet.user_id = user_info.user_id
GROUP BY location
ORDER BY loc_count DESC
LIMIT 5;
```
