Are average scores for hospital quality or procedural variability correlated with patient survey responses?

```
$ spark-submit hospitals_and_patients.py

Correlation between average hospital quality rates and survey scores:  -0.370482414859
Correlation between standard deviations of hospital procedure rates and survey scores:  -0.0790966602295
```

I combined the base score and the consistency score from the survey scores to get one total survey score as described in the HCAHPS Fact Sheet May 2012.pdf file in the data directory. This is the Patient Experience of Care Domain score that the HCAHPS survey uses. The total survey score was then combined with the same hospital procedure data as before.

The correlation between the average hospital quality and the total survey scores was calculated. I used the same average score to rate hospitals as before. I found that they are negatively correlated at -.370. 

The correlation between the standard deviation of procedure rate for hospitals and the total survey scores was calculated. I used the transformed scores so that they were all in the same format and excluded NA values so my transformed 0 scores for NA would not affect the variance. I found that they are slightly negatively correlated at -0.079.