from __future__ import print_function

import psycopg2
import sys


if __name__ == '__main__':

    conn = psycopg2.connect(database="tcount", user="postgres", host="localhost", port="5432")
    cur = conn.cursor()
    
    try: 
         k1, k2 = sys.argv[1].split(',')  # get k1, k2 passed as argument
    except IndexError:
        print('Please provide k1,k2')
    else:
        cur.execute("SELECT word, count FROM tweetwordcount " \
                    "WHERE count >= %s AND count <= %s ORDER BY count", 
                    (k1, k2))
        records = cur.fetchall()
        for record in records:
           print("%s:" % record[0], record[1])

        conn.close()
