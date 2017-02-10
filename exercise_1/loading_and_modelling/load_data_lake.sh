#!/bin/bash
DATA_FILE_PATH="../data/Hospital_Revised_Flatfiles/"
DATA_FILE_RENAMED_PATH="../data/hospital_renamed_files/"

# make a dir to hold renamed files
mkdir -p $DATA_FILE_RENAMED_PATH

# rename and remove headers of data files
tail -n +2 ${DATA_FILE_PATH}Complications\ -\ Hospital.csv > ${DATA_FILE_RENAMED_PATH}complications.csv
tail -n +2 ${DATA_FILE_PATH}Healthcare\ Associated\ Infections\ -\ Hospital.csv > ${DATA_FILE_RENAMED_PATH}infections.csv
tail -n +2 ${DATA_FILE_PATH}Hospital\ General\ Information.csv > ${DATA_FILE_RENAMED_PATH}hospitals.csv
tail -n +2 ${DATA_FILE_PATH}hvbp_hcahps_05_28_2015.csv > ${DATA_FILE_RENAMED_PATH}surveys_responses.csv
tail -n +2 ${DATA_FILE_PATH}Measure\ Dates.csv > ${DATA_FILE_RENAMED_PATH}measures.csv
tail -n +2 ${DATA_FILE_PATH}Readmissions\ and\ Deaths\ -\ Hospital.csv > ${DATA_FILE_RENAMED_PATH}readmissions.csv
tail -n +2 ${DATA_FILE_PATH}Timely\ and\ Effective\ Care\ -\ Hospital.csv > ${DATA_FILE_RENAMED_PATH}effective_care.csv
