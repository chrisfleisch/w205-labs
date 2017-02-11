DROP TABLE measures;
CREATE EXTERNAL TABLE measures (
  measure_name STRING,
  measure_id STRING,
  measure_start_quarter STRING,
  measure_start_date TIMESTAMP,
  measure_end_quarter STRING,
  measure_end_date TIMESTAMP
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  "separatorChar" = ",", "quoteChar" = '"', "escapeChar" = '\\'
)
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare/measures';

DROP TABLE complications;
CREATE EXTERNAL TABLE complications (
  provider_id STRING,
  hospital_name STRING,
  address STRING,
  city STRING,
  state STRING,
  zip_code STRING,
  county_name STRING,
  phone_number STRING,
  measure_name STRING,
  measure_id STRING,
  compared_to_national STRING,
  denominator STRING,
  score STRING,
  lower_estimate STRING,
  higher_estimate STRING,
  footnote STRING,
  measure_start_date STRING,
  measure_end_date STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  "separatorChar" = ",", "quoteChar" = '"', "escapeChar" = '\\'
)
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare/complications';

DROP TABLE hospital_survey;
CREATE EXTERNAL TABLE hospital_survey (
provider_id STRING,
hospital_name STRING,
address STRING,
city STRING,
state STRING,
zip_code STRING,
county_name STRING,
phone_number STRING,
hcahps_measure_id STRING,
hcahps_question STRING,
hcahps_answer_description STRING,
patient_survey_star_rating STRING,
patient_survey_star_rating_footnote STRING,
hcahps_answer_percent STRING,
hcahps_answer_percent_footnote STRING,
number_of_completed_surveys STRING,
number_of_completed_surveys_footnote STRING,
survey_response_rate_percent STRING,
survey_response_rate_percent_footnote STRING,
measure_start_date STRING,
measure_end_date STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  "separatorChar" = ",", "quoteChar" = '"', "escapeChar" = '\\'
)
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare/hospital_survey';

DROP TABLE infections;
CREATE EXTERNAL TABLE infections (
provider_id STRING,
hospital_name STRING,
address STRING,
city STRING,
state STRING,
zip_code STRING,
county_name STRING,
phone_number STRING,
measure_name STRING,
measure_id STRING,
compared_to_national STRING,
score STRING,
footnote STRING,
measure_start_date STRING,
measure_end_date STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  "separatorChar" = ",", "quoteChar" = '"', "escapeChar" = '\\'
)
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare/infections';

DROP TABLE hospitals;
CREATE EXTERNAL TABLE hospitals (
provider_id STRING,
hospital_name STRING,
address STRING,
city STRING,
state STRING,
zip_code STRING,
county_name STRING,
phone_number STRING,
hospital_type STRING,
hospital_ownership STRING,
emergency_services STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  "separatorChar" = ",", "quoteChar" = '"', "escapeChar" = '\\'
)
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare/hospitals';

DROP TABLE surveys_responses;
CREATE EXTERNAL TABLE surveys_responses (
provider_number STRING,
hospital_name STRING,
address STRING,
city STRING,
state STRING,
zip_code STRING,
county_name STRING,
communication_with_nurses_achievement_points STRING,
communication_with_nurses_improvement_points STRING,
communication_with_nurses_dimension_score STRING,
communication_with_doctors_achievement_points STRING,
communication_with_doctors_improvement_points STRING,
communication_with_doctors_dimension_score STRING,
responsiveness_of_hospital_staff_achievement_points STRING,
responsiveness_of_hospital_staff_improvement_points STRING,
responsiveness_of_hospital_staff_dimension_score STRING,
pain_management_achievement_points STRING,
pain_management_improvement_points STRING,
pain_management_dimension_score STRING,
communication_about_medicines_achievement_points STRING,
communication_about_medicines_improvement_points STRING,
communication_about_medicines_dimension_score STRING,
cleanliness_and_quietness_of_hospital_environment_achievement_points STRING,
cleanliness_and_quietness_of_hospital_environment_improvement_points STRING,
cleanliness_and_quietness_of_hospital_environment_dimension_score STRING,
discharge_information_achievement_points STRING,
discharge_information_improvement_points STRING,
discharge_information_dimension_score STRING,
overall_rating_of_hospital_achievement_points STRING,
overall_rating_of_hospital_improvement_points STRING,
overall_rating_of_hospital_dimension_score STRING,
hcahps_base_score STRING,
hcahps_consistency_score STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  "separatorChar" = ",", "quoteChar" = '"', "escapeChar" = '\\'
)
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare/surveys_responses';

DROP TABLE readmissions;
CREATE EXTERNAL TABLE readmissions (
provider_id STRING,
hospital_name STRING,
address STRING,
city STRING,
state STRING,
zip_code STRING,
county_name STRING,
phone_number STRING,
measure_name STRING,
measure_id STRING,
compared_to_national STRING,
denominator STRING,
score STRING,
lower_estimate STRING,
higher_estimate STRING,
footnote STRING,
measure_start_date STRING,
measure_end_date STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  "separatorChar" = ",", "quoteChar" = '"', "escapeChar" = '\\'
)
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare/readmissions';

DROP TABLE effective_care;
CREATE EXTERNAL TABLE effective_care (
provider_id STRING,
hospital_name STRING,
address STRING,
city STRING,
state STRING,
zip_code STRING,
county_name STRING,
phone_number STRING,
condition STRING,
measure_id STRING,
measure_name STRING,
score STRING,
sample STRING,
footnote STRING,
measure_start_date STRING,
measure_end_date STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  "separatorChar" = ",", "quoteChar" = '"', "escapeChar" = '\\'
)
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare/effective_care';

