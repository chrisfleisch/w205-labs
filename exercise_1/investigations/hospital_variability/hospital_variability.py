from pyspark import SparkContext
from pyspark.sql import HiveContext


sc = SparkContext()
sqlContext = HiveContext(sc)


# Which procedures have the greatest variability between hospitals?
sql = """
SELECT measure_id, measure_name, avg(new_score) AS avg_score, 
sum(score) AS sum_score,
stddev(score) AS std_dev
FROM my_combined_procedures
GROUP BY measure_id, measure_name
ORDER BY std_dev DESC
LIMIT 10
"""
sqlContext.sql(sql).show()