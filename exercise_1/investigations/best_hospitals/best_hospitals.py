from pyspark import SparkContext
from pyspark.sql import HiveContext


sc = SparkContext()
sqlContext = HiveContext(sc)


# What hospitals are models of high-quality care? 
# That is, which hospitals have the most consistently 
# high scores for a variety of procedures.
sql = """
SELECT p.provider_id, avg(new_score) AS avg_score, 
sum(new_score) AS sum_score,
stddev(new_score) AS std_dev,
name, city, state
FROM my_combined_procedures p INNER JOIN my_hospitals h 
ON p.provider_id = h.provider_id
GROUP BY p.provider_id, name, city, state
ORDER BY avg_score DESC 
LIMIT 10
"""
combined_scores_df = sqlContext.sql(sql)
combined_scores_df.show()