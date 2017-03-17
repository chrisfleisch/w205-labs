from __future__ import print_function

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

if __name__ == '__main__':
    print('Creating database...')
    
    conn = psycopg2.connect(database="postgres", user="postgres", host="localhost", port="5432")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    try:
        cur = conn.cursor()
        cur.execute("CREATE DATABASE tcount")
        cur.close()
        conn.close()
    except:
        raise
        print("Could not create tcount")

