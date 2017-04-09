## Setup

1. Change to w205 user:

  ```
  su w205
  ```

2. Clone code repo:

  ```
  git clone https://github.com/chrisfleisch/w205-labs.git
  ```

3. Move to exercise 2 dir:

 ```
 cd w205-labs/exercise_2
 ```

4. Switch back to root, using python 2.7.3 install requirements, then switch back to w205:

 ```
 exit
 cd w205-labs/exercise_2
 pip install -r requirements.txt
 su w205
 ```

5. Create database (may take a little while to complete):

 ```
 cd scripts
 python create_db.py
 ```

6. Create table:

 ```
 python create_table.py
 ```

## Get streaming

1. Input your twitter credentials at the top of tweets.py:

 ```
 cd ../
 vim extweetwordcount/src/spouts/tweets.py
 ```

2. Run the stream

 ```
 cd extweetwordcount
 sparse run
 ```

 When you have enough data, hit Contol-C to stop the stream

### Results:

1. Move to scripts directory:

 ```
 cd ../scripts
 ```

2. Final results:

 ```
 python finalresults.py
 python finalresults.py hello
 ```

3. Histogram:

 ```
 python histogram.py 10,12
 ```
