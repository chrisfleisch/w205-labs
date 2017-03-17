## Setup
1. Using python 2.7.3 install requirements:

 ```pip install -r requirements.txt```

1. Create database:

 ```cd scripts```

 ```python create_db.py```

1. Create table:

 ```python create_table.py```

## Run stream

```cd extweetwordcount```

```sparse run```

### Results:
```cd scripts```

1. Final results:

 ```python finalresults.py```

 ```python finalresults.py hello```

1. Histogram:

 ```python histogram.py 10,12```
