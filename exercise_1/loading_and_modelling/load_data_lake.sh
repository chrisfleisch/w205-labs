#!/bin/bash
DATA_FILE_PATH="../data/Hospital_Revised_Flatfiles/"
DATA_FILE_RENAMED_PATH="../data/hospital_renamed_files/"
HDFS_BASE_PATH="/user/w205/hospital_compare"

# make a dir to hold renamed files
mkdir -p $DATA_FILE_RENAMED_PATH


# rename and remove headers of data files
echo "Renaming files..."
tail -n +2 ${DATA_FILE_PATH}Complications\ -\ Hospital.csv > ${DATA_FILE_RENAMED_PATH}complications.csv
tail -n +2 ${DATA_FILE_PATH}Healthcare\ Associated\ Infections\ -\ Hospital.csv > ${DATA_FILE_RENAMED_PATH}infections.csv
tail -n +2 ${DATA_FILE_PATH}Hospital\ General\ Information.csv > ${DATA_FILE_RENAMED_PATH}hospitals.csv
tail -n +2 ${DATA_FILE_PATH}hvbp_hcahps_05_28_2015.csv > ${DATA_FILE_RENAMED_PATH}surveys_responses.csv
tail -n +2 ${DATA_FILE_PATH}Measure\ Dates.csv > ${DATA_FILE_RENAMED_PATH}measures.csv
tail -n +2 ${DATA_FILE_PATH}Readmissions\ and\ Deaths\ -\ Hospital.csv > ${DATA_FILE_RENAMED_PATH}readmissions.csv
tail -n +2 ${DATA_FILE_PATH}Timely\ and\ Effective\ Care\ -\ Hospital.csv > ${DATA_FILE_RENAMED_PATH}effective_care.csv

# make directories for files hdfs
echo "Making directories in HDFS..."
hdfs dfs -mkdir -p ${HDFS_BASE_PATH}
hdfs dfs -mkdir -p ${HDFS_BASE_PATH}/complications
hdfs dfs -mkdir -p ${HDFS_BASE_PATH}/infections
hdfs dfs -mkdir -p ${HDFS_BASE_PATH}/hospitals
hdfs dfs -mkdir -p ${HDFS_BASE_PATH}/surveys_responses
hdfs dfs -mkdir -p ${HDFS_BASE_PATH}/measures
hdfs dfs -mkdir -p ${HDFS_BASE_PATH}/readmissions
hdfs dfs -mkdir -p ${HDFS_BASE_PATH}/effective_care

# put the files hdfs
echo "Moving files into HDFS..."
hdfs dfs -put -f ${DATA_FILE_RENAMED_PATH}complications.csv ${HDFS_BASE_PATH}/complications
hdfs dfs -put -f ${DATA_FILE_RENAMED_PATH}infections.csv ${HDFS_BASE_PATH}/infections
hdfs dfs -put -f ${DATA_FILE_RENAMED_PATH}hospitals.csv ${HDFS_BASE_PATH}/hospitals
hdfs dfs -put -f ${DATA_FILE_RENAMED_PATH}surveys_responses.csv ${HDFS_BASE_PATH}/surveys_responses
hdfs dfs -put -f ${DATA_FILE_RENAMED_PATH}measures.csv ${HDFS_BASE_PATH}/measures
hdfs dfs -put -f ${DATA_FILE_RENAMED_PATH}readmissions.csv ${HDFS_BASE_PATH}/readmissions
hdfs dfs -put -f ${DATA_FILE_RENAMED_PATH}effective_care.csv ${HDFS_BASE_PATH}/effective_care
