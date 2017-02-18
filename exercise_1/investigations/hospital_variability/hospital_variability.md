Which procedures have the greatest variability between hospitals?

```
$ spark-submit hospital_variability.py

+-------------------+--------------------+-----------+-----------+------------------+
|         measure_id|        measure_name|  avg_score|  sum_score|           std_dev|
+-------------------+--------------------+-----------+-----------+------------------+
|          HAI_2_SIR|Catheter-Associat...|48.30051912|224887.2170| 49.45932191841454|
|              AMI_2|Aspirin prescribe...|46.76739691|217749.0000|49.334403774660466|
|          HAI_1_SIR|Central line-asso...|42.76890163|199132.0060| 49.26597269849545|
|              VTE_4|Unfractionated he...|43.39819588|202062.0000| 49.17729021645856|
|          HAI_3_SIR|Surgical Site Inf...|43.31772380|201687.3220| 49.14184522159113|
|             AMI_10| Statin at Discharge|45.86168385|213532.0000| 48.86002194975948|
|              STK_2|Discharged on Ant...|56.60674399|263561.0000| 48.84487628252045|
|PSI_14_POSTOP_DEHIS|A wound that spli...|54.71919029|254772.5500|48.829550373292854|
|          HAI_5_SIR|Methicillin-resis...|40.52777857|188697.3370|48.726715857075924|
|              STK_5|Antithrombotic Th...|56.16967354|261526.0000| 48.50840425178849|
+-------------------+--------------------+-----------+-----------+------------------+
```

Using the same table of measures as before, I grouped the data by measure_id and found the standard deviation for each measure rate. This shows use the variabliity of each procedure.