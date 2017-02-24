from pyspark import SparkContext
from pyspark.sql import HiveContext
from pyspark.sql import functions as func
from pyspark.sql import DataFrameWriter

sc = SparkContext("local")
sqlContext = HiveContext(sc)


# Setup table for my hospitals
sqlContext.sql("DROP TABLE IF EXISTS my_hospitals")

sql = """
CREATE TABLE my_hospitals AS
SELECT
provider_id, hospital_name name, city, state,
zip_code, hospital_type type, hospital_ownership ownership
FROM hospitals
"""
sqlContext.sql(sql)


# create a table for survey scores
sql = """DROP TABLE IF EXISTS my_survey_scores"""
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
sql = """DROP TABLE IF EXISTS my_care"""
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
sql = """DROP TABLE IF EXISTS my_infections"""
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
sql = """DROP TABLE IF EXISTS my_readmissions"""
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
sql = """DROP TABLE IF EXISTS my_complications"""
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

#####################################################################
# combine some of the procedures into one table and transform scores
#####################################################################

# get data from my_care, ignore the values with times
sql = """
SELECT provider_id, measure_name,
measure_id, score
FROM my_care
WHERE measure_id != 'ED_1b' AND measure_id != 'ED_2b'
AND measure_id != 'EDV' AND measure_id != 'OP_1'
AND measure_id != 'OP_18b' AND measure_id != 'OP_20' AND measure_id != 'OP_21'
AND measure_id != 'OP_3b' AND measure_id != 'OP_5'
"""
care_df = sqlContext.sql(sql)

# add new column for transformed score
care_df = care_df.withColumn('new_score', care_df.score)

# convert measure_id = 'OP_22' OR measure_id = 'PC_01' OR measure_id = 'VTE_6' to 100 - new_score
care_df = care_df.withColumn('new_score',
                         func.when(care_df.measure_id == 'OP_22', 100 - care_df.new_score). \
                         otherwise(care_df.new_score))
care_df = care_df.withColumn('new_score',
                             func.when(care_df.measure_id == 'PC_01', 100 - care_df.new_score). \
                             otherwise(care_df.new_score))
care_df = care_df.withColumn('new_score',
                             func.when(care_df.measure_id == 'VTE_6', 100 - care_df.new_score).
                             otherwise(care_df.new_score))


# select data from readmissions and deaths
sql = """
SELECT provider_id, measure_name,
measure_id, score
FROM my_readmissions
"""
read_df = sqlContext.sql(sql)

# convert scores to new_score so that higher is better
read_df = read_df.withColumn('new_score', read_df.score)
read_df = read_df.withColumn('new_score', 100 - read_df.new_score)


# select data from complications (exclude death counts in PSI_4_SURG_COMP)
sql = """
SELECT provider_id, measure_name,
measure_id, score
FROM my_complications
WHERE measure_id != 'PSI_4_SURG_COMP'
"""
comp_df = sqlContext.sql(sql)

# convert scores to new_score so that higher is better
comp_df = comp_df.withColumn('new_score', comp_df.score)
comp_df = comp_df.withColumn('new_score', 100 - comp_df.new_score)


# select data from infections, use Standardized Infections Ratios (SIR) for calculations
sql = """
SELECT provider_id, measure_name,
measure_id, score
FROM my_infections
WHERE measure_id LIKE '%SIR%'
"""
infect_df = sqlContext.sql(sql)

# convert scores to new_score so that higher is better
infect_df = infect_df.withColumn('new_score', infect_df.score)
infect_df = infect_df.withColumn('new_score', 100 - infect_df.new_score)


# combine the all the tables
combined_df = care_df.unionAll(read_df).unionAll(comp_df).unionAll(infect_df)

# convert null values to 0s
combined_df = combined_df.fillna({'new_score': 0})


# save new combined table
sqlContext.sql('DROP TABLE IF EXISTS my_combined_procedures')
df_writer = DataFrameWriter(combined_df)
df_writer.saveAsTable('my_combined_procedures')


# display new tables
df = sqlContext.sql("SHOW TABLES")
df.registerTempTable('temp_tables')
query = """SELECT * FROM temp_tables WHERE tableName LIKE '%my%'"""
sqlContext.sql(query).show()
