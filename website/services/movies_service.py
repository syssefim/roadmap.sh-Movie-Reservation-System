from .. import database



def list_movies():
    conn = database.connect()
    cur = conn.cursor()

    cur.execute("""SELECT title FROM movies;""")
    movie_titles = cur.fetchall()

    cur.close()

    result = " ".join(str(item) for item in movie_titles)

    return result


#genre
def list_movies_by_genre(genre):
    conn = database.connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT title FROM movies WHERE genre = %s",
        (genre,)
    )
    movie_titles = cur.fetchall()

    cur.close()

    result = " ".join(str(item) for item in movie_titles)

    return result


#by id
def list_movies_by_id(id):
    conn = database.connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT title FROM movies WHERE id = %s",
        (id,)
    )
    movie_titles = cur.fetchall()

    cur.close()

    result = " ".join(str(item) for item in movie_titles)

    return result


