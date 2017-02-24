Which procedures have the greatest variability between hospitals?

```
$ spark-submit hospital_variability.py

+----------------+--------------------+-----------+-----------+------------------+
|      measure_id|        measure_name|  avg_score|  sum_score|           std_dev|
+----------------+--------------------+-----------+-----------+------------------+
|           STK_4|Thrombolytic Therapy|15.56164089| 72455.0000|21.954194561164023|
|           OP_23|     Head CT results|15.56263683| 63978.0000|21.844653491103774|
|          AMI_7a|Fibrinolytic Ther...| 0.03134796|   150.0000|  18.7794213613377|
|            OP_2|Fibrinolytic Ther...| 1.16200438|  4777.0000|18.048443797995763|
|IMM_3_FAC_ADHPCT|Healthcare worker...|80.68061252|295049.0000|16.348047889323595|
|           VTE_5|Warfarin therapy ...|47.11361684|219361.0000| 16.30300466996529|
|           VTE_1|Venous thromboemb...|67.63960481|314930.0000|15.257401142298388|
|           STK_8|    Stroke Education|46.12542955|214760.0000|14.013262732452308|
|           CAC_3|Home Management P...|84.11764706|  8580.0000| 12.71912110433212|
|           IMM_2|Immunization for ...|71.79573043|343040.0000|11.944885922069522|
+----------------+--------------------+-----------+-----------+------------------+
```

Using the same table of combined measures as before, I grouped the data by measure\_id and found the standard deviation for each measure rate using the original scores. The original scores where used so that my transformed scores that converted NA values to zero do not affect the variability. This shows us the variability of each procedure. The procedures with the highest variability are listed here.
