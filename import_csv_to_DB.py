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
    # t_df.to_sql('titles', engine, if_exists="replace", index=False)
    # movies_clean = t_df.dropna(
    #     subset=['imdb_id', 'imdb_score', 'imdb_votes', 'tmdb_popularity', 'tmdb_score'])
    # mv_genres = movies_clean.genres

    # for row in movies_clean.itertuples():
    #     print(row.genres)
    # print(df.duplicated().sum())
    # print(df.isnull().sum())
    # print(df.head())
    # print(movies_clean.genres.value_counts())
    # res = t_df.to_sql(name="titles", con=con, if_exists="replace", index=True)
    droped = t_df.drop(columns=["id",'age_certification','seasons','genres','production_countries','imdb_id', 'imdb_score', 'imdb_votes', 'tmdb_popularity', 'tmdb_score'])
    res = droped.to_csv( "main_coma.csv", index=False, index_label='id', sep=',')

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

    with open('main_coma.csv', newline='',encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            cur.execute(
                "INSERT INTO titles VALUES (DEFAULT, %s, %s, %s, %s, %s)", row
            )
    conn.commit()
    conn.close()

    # titles_count = cur.execute("SELECT genres, count(genres) FROM titles group by genres ").fetchall()
    # print(titles_count)
    # cur.execute("SELECT COUNT(*) as credits_count FROM credits")
    # print(cur.fetchall())
