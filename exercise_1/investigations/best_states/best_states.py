from pyspark import SparkContext
from pyspark.sql import HiveContext


sc = SparkContext()
sqlContext = HiveContext(sc)


# What states are models of high-quality care?
sql = """
SELECT state, avg(new_score) AS avg_score, 
sum(new_score) AS sum_score,
stddev(new_score) AS std_dev
FROM my_combined_procedures p INNER JOIN my_hospitals h 
ON p.provider_id = h.provider_id
GROUP BY state
ORDER BY avg_score DESC
LIMIT 10
"""
sqlContext.sql(sql).show()