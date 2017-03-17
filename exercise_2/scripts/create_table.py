from __future__ import print_function

import psycopg2

if __name__ == '__main__':
    print('Creating table in database...')

    conn = psycopg2.connect(database="tcount", user="postgres", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute('''
       CREATE TABLE tweetwordcount
           (word TEXT PRIMARY KEY NOT NULL,
            count INT NOT NULL);''')
    conn.commit()
    conn.close()
    print('Done.')
