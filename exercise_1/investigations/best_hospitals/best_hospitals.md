What hospitals are models of high-quality care? That is, which hospitals have the most consistently high scores for a variety of procedures.

```
$ spark-submit best_hospitals.py

+-----------+-----------+---------+------------------+--------------------+------------------+-----+
|provider_id|  avg_score|sum_score|           std_dev|                name|              city|state|
+-----------+-----------+---------+------------------+--------------------+------------------+-----+
|     450388|91.52250000|6223.5300|20.674949430551997|  METHODIST HOSPITAL|       SAN ANTONIO|   TX|
|     030036|91.03030769|5916.9700| 20.81949413774214|CHANDLER REGIONAL...|          CHANDLER|   AZ|
|     450723|90.92936923|5910.4090|21.152496027706285|METHODIST CHARLTO...|            DALLAS|   TX|
|     050231|90.69501538|5895.1760|20.944048846311603|POMONA VALLEY HOS...|            POMONA|   CA|
|     050308|90.65812308|5892.7780|21.745274866761417|  EL CAMINO HOSPITAL|     MOUNTAIN VIEW|   CA|
|     260065|90.60870769|5889.5660| 20.79683189165938|MERCY HOSPITAL SP...|       SPRINGFIELD|   MO|
|     050570|90.52480000|5884.1120|20.972100787768206|FOUNTAIN VALLEY R...|   FOUNTAIN VALLEY|   CA|
|     050077|90.45890769|5879.8290| 20.85055615323418|SCRIPPS MERCY HOS...|         SAN DIEGO|   CA|
|     340091|90.37229231|5874.1990|21.383274657993137|MOSES H CONE MEMO...|        GREENSBORO|   NC|
|     360155|90.36926154|5874.0020|20.984063972656028|SOUTHWEST GENERAL...|MIDDLEBURG HEIGHTS|   OH|
+-----------+-----------+---------+------------------+--------------------+------------------+-----+
```

I looked at rates across a variety of procedures, infections, complications, and readmissions for all the hospitals. For most rates a higher score was better. There were some measures where lower was better so they were converted using 100 - rate = new_rate. Values that were not rates were excluded (such as times or counts) since they were not of the same type and had different ranges not comparable to the rates. I was than able to group by the provider and average the rates to get a final score. The hospitals with the highest average score are listed here. There were a large number of NA values which made comparisons difficult. These values were converted to zeros. Hospitals that were unable to provide a score for a measure for whatever reason would then get a zero for that particular measure.
