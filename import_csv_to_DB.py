import pandas as pd
import psycopg2
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

    t_df.rename(columns = {'id':'person_id'})
    droped = t_df.drop(columns=['age_certification','seasons','genres','production_countries','imdb_id', 'imdb_score', 'imdb_votes', 'tmdb_popularity', 'tmdb_score'])
    res = droped.to_csv( "main_coma.csv", index=False, index_label='id', sep=',')

    sql = '''CREATE TABLE titles(
        id SERIAL PRIMARY KEY,
        title_id VARCHAR(10),
        title varchar(200),
        type varchar(10),
        description text,
        release_year smallint,
        runtime smallint
    )'''
    cur.execute(sql) 
    conn.commit()

    with open('main_coma.csv', newline='',encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            cur.execute(
                "INSERT INTO titles VALUES (DEFAULT, %s, %s, %s, %s, %s, %s)", row
            )
    conn.commit()

    sql = '''CREATE TABLE credits(
        id int,
        title_id VARCHAR(10),
        name varchar(200),
        character varchar(1000),
        role varchar(30)
    )'''
    cur.execute(sql) 
    conn.commit()

    with open('credits.csv', newline='',encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            cur.execute(
                "INSERT INTO credits VALUES (%s, %s, %s, %s, %s)", row
            )
    conn.commit()
    conn.close()