from pyspark.sql import HiveContext
sqlContext = HiveContext(sc)


# Setup table for my hospitals
sqlContext.sql("DROP TABLE my_hospitals")

sql = """
CREATE TABLE my_hospitals AS
SELECT
provider_id, hospital_name name, city, state,
zip_code, hospital_type type, hospital_ownership ownership
FROM hospitals
"""
sqlContext.sql(sql)


# Setup table for my_star_ratings
sql = """DROP TABLE my_star_ratings"""
sqlContext.sql(sql)

sql = """
CREATE TABLE my_star_ratings AS
SELECT
provider_id, hcahps_measure_id measure_id,
hcahps_question question, hcahps_answer_description answer,
cast(patient_survey_star_rating AS INT) star_rating,
cast(to_date(from_unixtime(unix_timestamp(measure_start_date, 'MM/dd/yy'))) as date) measure_start,
cast(to_date(from_unixtime(unix_timestamp(measure_end_date, 'MM/dd/yy'))) as date) measure_end
FROM hospital_survey
"""
sqlContext.sql(sql)

# create a table for survey scores
sql = """DROP TABLE my_survey_scores"""
sqlContext.sql(sql)

sql = """
CREATE TABLE my_survey_scores AS
SELECT
provider_number provider_id,
cast(hcahps_base_score as INT) base_score,
cast(hcahps_consistency_score as INT) consistency_score,
cast(hcahps_base_score as INT) + cast(hcahps_consistency_score as INT) total_score
FROM surveys_responses
"""
sqlContext.sql(sql)


# setup table for my_care
sql = """
DROP TABLE my_care
"""
sqlContext.sql(sql)


sql = """
CREATE TABLE my_care AS
SELECT
provider_id, condition, measure_id,
measure_name,
cast(score as INT) score,
cast(to_date(from_unixtime(unix_timestamp(measure_start_date, 'MM/dd/yy'))) as date) measure_start,
cast(to_date(from_unixtime(unix_timestamp(measure_end_date, 'MM/dd/yy'))) as date) measure_end
FROM effective_care
"""
sqlContext.sql(sql)


# setup table for my_infections
sql = """
DROP TABLE my_infections
"""
sqlContext.sql(sql)

sql = """
CREATE TABLE my_infections AS
SELECT
provider_id, measure_id,
measure_name, compared_to_national,
cast(score as DECIMAL(16,4)) score,
cast(to_date(from_unixtime(unix_timestamp(measure_start_date, 'MM/dd/yy'))) as date) measure_start,
cast(to_date(from_unixtime(unix_timestamp(measure_end_date, 'MM/dd/yy'))) as date) measure_end
FROM infections
"""
sqlContext.sql(sql)


# setup table for my_readmissions
sql = """DROP TABLE my_readmissions"""
sqlContext.sql(sql)

sql = """
CREATE TABLE my_readmissions AS
SELECT
provider_id, measure_id,
measure_name, compared_to_national,
cast(score as DECIMAL(16,4)) score,
cast(to_date(from_unixtime(unix_timestamp(measure_start_date, 'MM/dd/yy'))) as date) measure_start,
cast(to_date(from_unixtime(unix_timestamp(measure_end_date, 'MM/dd/yy'))) as date) measure_end
FROM readmissions
"""
sqlContext.sql(sql)


# setup table for my_complications
sql = """DROP TABLE my_complications"""
sqlContext.sql(sql)

sql = """
CREATE TABLE my_complications AS
SELECT
provider_id, measure_id,
measure_name, compared_to_national,
cast(score as DECIMAL(16,4)) score,
cast(to_date(from_unixtime(unix_timestamp(measure_start_date, 'MM/dd/yy'))) as date) measure_start,
cast(to_date(from_unixtime(unix_timestamp(measure_end_date, 'MM/dd/yy'))) as date) measure_end
FROM complications
"""
sqlContext.sql(sql)
