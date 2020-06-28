import psycopg2 as pg

if __name__ == '__main__':
    conn = pg.connect(host="localhost",
                      port=5432,
                      user="app_user",
                      database="bmat",
                      password="123")

    cursor = conn.cursor()
    cursor.execute("""
    insert into works_metadata(title, contributors, iswc)
    values ('Shape of You', 'Edward Christopher Sheeran', 'T9204649558')
    """)
    conn.commit()
    cursor.execute("""
    select * from works_metadata
    """)
    print(cursor.fetchall())
