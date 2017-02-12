-- setup table for my_hospitals
DROP TABLE IF EXISTS my_hospitals;

CREATE TABLE my_hospitals AS
SELECT
provider_id, hospital_name name, city, state,
zip_code, hospital_type type, hospital_ownership ownership
FROM hospitals;


-- setup table for my_star_ratings
DROP TABLE IF EXISTS my_star_ratings;

CREATE TABLE my_star_ratings AS
SELECT
provider_id, hcahps_measure_id measure_id,
hcahps_question question, hcahps_answer_description answer,
cast(patient_survey_star_rating AS INT) star_rating,
cast(to_date(from_unixtime(unix_timestamp(measure_start_date, 'MM/dd/yy'))) as date) measure_start,
cast(to_date(from_unixtime(unix_timestamp(measure_end_date, 'MM/dd/yy'))) as date) measure_end
FROM hospital_survey;


-- setup table for my_survey_scores
DROP TABLE IF EXISTS my_survey_scores;

CREATE TABLE my_survey_scores AS
SELECT
provider_number provider_id,
cast(hcahps_base_score as INT) base_score,
cast(hcahps_consistency_score as INT) consistency_score,
cast(hcahps_base_score as INT) + cast(hcahps_consistency_score as INT) total_score
FROM surveys_responses;

-- setup table for my_care
DROP TABLE IF EXISTS my_care;

CREATE TABLE my_care AS
SELECT
provider_id, condition, measure_id,
measure_name,
cast(score as INT) score,
cast(to_date(from_unixtime(unix_timestamp(measure_start_date, 'MM/dd/yy'))) as date) measure_start,
cast(to_date(from_unixtime(unix_timestamp(measure_end_date, 'MM/dd/yy'))) as date) measure_end
FROM effective_care;

-- setup table for my_infections
DROP TABLE IF EXISTS my_infections;

CREATE TABLE my_infections AS
SELECT
provider_id, measure_id,
measure_name, compared_to_national,
cast(score as DECIMAL(16,4)) score,
cast(to_date(from_unixtime(unix_timestamp(measure_start_date, 'MM/dd/yy'))) as date) measure_start,
cast(to_date(from_unixtime(unix_timestamp(measure_end_date, 'MM/dd/yy'))) as date) measure_end
FROM infections;

-- setup table for my_readmissions
DROP TABLE IF EXISTS my_readmissions;

CREATE TABLE my_readmissions AS
SELECT
provider_id, measure_id,
measure_name, compared_to_national,
cast(score as DECIMAL(16,4)) score,
cast(to_date(from_unixtime(unix_timestamp(measure_start_date, 'MM/dd/yy'))) as date) measure_start,
cast(to_date(from_unixtime(unix_timestamp(measure_end_date, 'MM/dd/yy'))) as date) measure_end
FROM readmissions;

-- setup table for my_complications
DROP TABLE IF EXISTS my_complications;

CREATE TABLE my_complications AS
SELECT
provider_id, measure_id,
measure_name, compared_to_national,
cast(score as DECIMAL(16,4)) score,
cast(to_date(from_unixtime(unix_timestamp(measure_start_date, 'MM/dd/yy'))) as date) measure_start,
cast(to_date(from_unixtime(unix_timestamp(measure_end_date, 'MM/dd/yy'))) as date) measure_end
FROM complications;

SHOW TABLES LIKE 'my%';
