from __future__ import print_function

import psycopg2
import sys


if __name__ == '__main__':

    conn = psycopg2.connect(database="tcount", user="postgres", host="localhost", port="5432")
    cur = conn.cursor()
    
    try: 
        word = sys.argv[1]  # get the word passed as argument
    except IndexError:
        cur.execute("SELECT word, count from tweetwordcount order by word")
        records = cur.fetchall()
        for record in records:
            print(record[0], record[1])
        conn.close()
    else:
        cur.execute("SELECT word, count from tweetwordcount where word = %s", (word,))
        record = cur.fetchone()
        if record is None:
            print("No results found.")
        else:
            print("Total number of occurrences of \"%s\": %s" % (record[0], record[1]))
        conn.close()
