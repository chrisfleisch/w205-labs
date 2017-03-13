from __future__ import print_function

import psycopg2
import sys


if __name__ == '__main__':

    print('Testing SQL...')

    conn = psycopg2.connect(database="tcount", user="postgres", host="localhost", port="5432")

    cur = conn.cursor()
    
    word = sys.argv[1]  # get the word pass as argument

    cur.execute("SELECT word, count from tweetwordcount where word = %s", (word,))
    record = cur.fetchone()
    if record is None:
        cur.execute("INSERT INTO tweetwordcount (word, count) " \
                    "VALUES (%s, 1)", (word,));
        conn.commit()
    else:
         cur.execute("UPDATE tweetwordcount SET count = count + 1 WHERE word = %s",
                     (record[0],))
         conn.commit()

    cur.execute("SELECT word, count from Tweetwordcount")
    records = cur.fetchall()
    for rec in records:
       print("word = ", rec[0])
       print("count = ", rec[1], "\n")
    conn.commit()

    conn.close()
