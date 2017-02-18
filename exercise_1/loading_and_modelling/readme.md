Generate new file names and put data into HDFS:
```
$ ./load_data_lake.sh
```

Load raw data into Hive:
```
$ hive -f hive_base_ddl.sql
```