import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()

seed_data = [
    (
        "Wildwood",
        132,
        "2026-10-23",
        "Fantasy",
        "playing",
        "PG-13",
        "Fathom Entertainment",
        "A girl ventures into an enchanted forest to rescue her baby brother "
        "and becomes caught up in a conflict threatening the hidden realm.",
        None,
        None,
    ),
    (
        "Dune: Part Three",
        140,
        "2026-12-18",
        "Sci-Fi",
        "coming_soon",
        "PG-13",
        "Warner Bros. Pictures",
        "Nearly two decades after taking control of the Imperium, Emperor Paul "
        "Atreides faces the consequences of his reign amid betrayal, new threats, "
        "and a conspiracy involving Chani.",
        None,
        None,
    ),
]

conn = psycopg2.connect(
    host=os.getenv("DB_HOST", "localhost"),
    dbname=os.getenv("DB_NAME", "movie_reservation"),
    user=os.getenv("DB_USER", "postgres"),
    password=os.getenv("DB_PASSWORD"),
    port=int(os.getenv("DB_PORT", "5432")),
)

try:
    with conn:
        with conn.cursor() as cur:
            cur.executemany(
                """
                INSERT INTO movies (
                    title, runtime, release_date, genre, status, rating,
                    distributor, synopsis, poster_url, trailer_url
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                seed_data,
            )
finally:
    conn.close()