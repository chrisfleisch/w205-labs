from pyspark import SparkContext
from pyspark.sql import HiveContext


sc = SparkContext()
sqlContext = HiveContext(sc)


# Are average scores for hospital quality correlated with patient survey scores?
sql = """
SELECT p.provider_id, avg(new_score) AS avg_score, 
sum(new_score) AS sum_score,
stddev(new_score) AS std_dev,
name, city, state,
total_score AS survey_score
FROM my_combined_procedures p INNER JOIN my_survey_scores s 
ON p.provider_id = s.provider_id INNER JOIN my_hospitals h 
ON p.provider_id = h.provider_id
GROUP BY p.provider_id, name, city, state, total_score
"""
df = sqlContext.sql(sql)
quality_corr = df.stat.corr('avg_score', 'survey_score')


# Are scores for hospital procedural variability correlated with patient survey responses?
sql = """
SELECT p.provider_id, avg(new_score) AS avg_score, 
sum(new_score) AS sum_score,
stddev(new_score) AS std_dev,
name, city, state,
total_score AS survey_score
FROM my_combined_procedures p INNER JOIN my_survey_scores s 
ON p.provider_id = s.provider_id INNER JOIN my_hospitals h 
ON p.provider_id = h.provider_id
WHERE score IS NOT NULL
GROUP BY p.provider_id, name, city, state, total_score
"""
df = sqlContext.sql(sql)
var_corr = df.stat.corr('std_dev', 'survey_score')


print 'Correlation between average hospital quality rates and survey scores: ', quality_corr
print 'Correlation between standard deviations of hospital procedure rates and survey scores: ', var_corr