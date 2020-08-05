import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    load staging tables (staging_events, staging_songs) from the JSON data in S3 (log_data, songs_data)
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    insert Redshift tables songs_plat, users, songs, time, artists from staging tables (staging_events, staging_songs)
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    connect to Redshift database and call functions to load staging tables (staging_events, staging_songs) and insert data into Redshift tables songs_plat, users, songs, time and artists
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
