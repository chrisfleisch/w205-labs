What states are models of high-quality care?

```
$ spark-submit best_states.py

+-----+-----------+-----------+------------------+                              
|state|  avg_score|  sum_score|           std_dev|
+-----+-----------+-----------+------------------+
|   NJ|80.15610979|335854.1000|34.342725071482654|
|   DE|80.06332134| 33386.4050| 34.50229093623751|
|   CT|73.83223116|145966.3210| 39.39658237877559|
|   FL|73.29968334|868747.8470| 39.96398023239047|
|   RI|73.28125202| 54374.6890| 39.28783979441245|
|   MA|69.39629851|283622.6720| 42.01992836228156|
|   DC|68.26902377| 37343.1560| 41.56831749952921|
|   VA|67.73025287|366420.6680|43.053910645623695|
|   NY|66.36262537|747707.7000| 42.96222685958356|
|   PA|66.20132765|722124.0820| 43.49033522646685|
+-----+-----------+-----------+------------------+
```

The same hospital measures where used to find the states with the highest quality of care. This time I grouped the rates together by state and took the average. The states with the highest scores on average are listed here.
