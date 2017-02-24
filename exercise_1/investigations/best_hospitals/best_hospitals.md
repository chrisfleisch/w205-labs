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

In order to calculate scores for the best hospitals I looked at a variety of procedures or measures. The data from effective care, readmissions and deaths, complications, and infections was combined into one table to make calculations easier and allows transformations to be performed.

The data from effective care was filtered so that only measures with rates were used. Measures with times or other types of scores was removed. It was not clear from the data dictionary what a good time would be for those measures or how they should be evaluated. For most measures higher rates are better. For some of the measures lower was better -- in these cases the scores where converted so that higher was better. I used the data dictionary and exploration of the data to determine how each score should be treated.

All the measures from readmissions and deaths was used and converted to rates so that higher was better.

For complications, the death counts were filtered out, because the data dictionary did not provide enough information about this measure or how it should be evaluated. The rest of the scores were converted so that higher rates are better.

The infection data was filtered to only use the Standardized Infections Ratios (SIR) scores. The SIR was used, because it provided an overall rate for infections for a particular measure. All the rates were converted so that higher is better.

Once all the scores were in the same format (higher is better) they could be summed or averaged over much easier giving us a more uniform score for each measure. NA values for scores were converted to zeros so that hospitals that provided less data would see a negative impact on their overall quality score.

I was than able to group by the provider and average the rates to get a final score. The hospitals with the highest average score are listed here.
