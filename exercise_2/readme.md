## Setup
1. Change to w205 user:
```su w205```

1. Clone code repo:
```git clone https://github.com/chrisfleisch/w205-labs.git```

1. Move to exercise 2 dir:
```cd w205-labs/exercise_2```

1. Switch back to root, using python 2.7.3 install requirements, then switch back to w205:
 ```exit```
 ```cd w205-labs/exercise_2```
 ```pip install -r requirements.txt```
 ```su w205```

1. Create database:

 ```cd scripts```

 ```python create_db.py```

1. Create table:

 ```python create_table.py```

## Run stream

```cd ../extweetwordcount```

```sparse run```
 When you have enough data, hit Contol-C to stop the stream

### Results:
```cd ../scripts```

1. Final results:

 ```python finalresults.py```

 ```python finalresults.py hello```

1. Histogram:

 ```python histogram.py 10,12```
