import pandas as pd
import psycopg2
import time
import csv

if __name__ == "__main__":
    conn = psycopg2.connect(
        user='postgres',
        password='1234',
        port=5432,
        host='localhost',
        database='postgres')
    cur = conn.cursor()

    title_data = pd.read_csv('titles.csv')
    t_df = pd.DataFrame(title_data)

    t_df.rename(columns={'id': 'title_id'}, inplace=True)
    t_df['id'] = range(1, len(t_df)+1)
    t_df.insert(0, 'id', t_df.pop('id'))
    t_df = t_df.drop(columns=['age_certification', 'seasons', 'genres', 'production_countries',
                       'imdb_id', 'imdb_score', 'imdb_votes', 'tmdb_popularity', 'tmdb_score'])

    credits_data = pd.read_csv('credits.csv')
    c_df = pd.DataFrame(credits_data)

    c_df['title_id'] = 0
    c_df.insert(1, 'title_id', c_df.pop('title_id'))
    start_time=time.time_ns()
    for index, row in t_df.iterrows():
        c_df.loc[c_df['id'] == row['title_id'], 'title_id'] = row['id']
    print("parsing time: ", (time.time_ns()-start_time)// (10 ** 9))
    t_df = t_df.drop(columns=['title_id'])
    res = t_df.to_csv("titles_parsed.csv", index=False,
                        index_label='id', sep=',')
    c_df = c_df.drop(columns=['id'])
    res = c_df.to_csv("credits_paresd.csv", index=False, sep=',')

    sql = '''CREATE TABLE titles(
        id SERIAL PRIMARY KEY,
        title varchar(200),
        type varchar(10),
        description text,
        release_year smallint,
        runtime smallint
    )'''
    cur.execute(sql)
    conn.commit()

    with open('titles_parsed.csv', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            cur.execute(
                "INSERT INTO titles VALUES (DEFAULT, %s, %s, %s, %s, %s)", row[1:]
            )
    conn.commit()

    sql = '''CREATE TABLE credits(
        id SERIAL PRIMARY KEY,
        person_id int,
        title_id int,
        name varchar(200),
        character varchar(1000),
        role varchar(30)
    )'''
    cur.execute(sql)
    conn.commit()

    with open('credits_parsed.csv', newline='',encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            cur.execute(
                "INSERT INTO credits VALUES (DEFAULT, %s, %s, %s, %s, %s)", row
            )
    conn.commit()
    conn.close()
