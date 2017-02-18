Are average scores for hospital quality or procedural variability correlated with patient survey responses?

```
$ spark-submit hospitals_and_patients.py

Correlation between average hostpital quality rates and survey scores: -0.370482414859

Correlation between standard deviations of hosptial procedure rates and survey scores: 0.304098432054
```

I combined the base score and the consistency score from the survey scores to get one total survey score. The total survey score was then combined with the hospital procedure data.

The correlation between the average hospital quality and the total survey scores was calculated. I found that they are negativately correlated at -.370. 

The correlation between the standard deviation of procedure rate and the total survey scores was calculated. I found that they are positively correlated at 0.304.