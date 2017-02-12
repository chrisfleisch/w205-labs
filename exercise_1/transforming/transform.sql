-- transform tables
CREATE TABLE my_hospitals AS 
SELECT
provider_id, hospital_name name, city, state,
zip_code, hospital_type type, hospital_ownership ownership
FROM hospitals;
