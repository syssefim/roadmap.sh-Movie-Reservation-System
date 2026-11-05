from website import database


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
        (
        "Spider-Man: Brand New Day",
        145,
        "2026-07-31",
        "Action",
        "archived",
        "PG-13",
        "Sony Pictures",
        "Peter Parker fights crime full-time in a world that no longer remembers him. "
        "As he feels his old friends moving on, a change begins that may help him stop "
        "a new threat to the city.",
        None,
        None,
    ),
    (
        "The Odyssey",
        172,
        "2026-07-17",
        "Adventure",
        "playing",
        "R",
        "Universal Pictures",
        "After the Trojan War, Odysseus faces a perilous journey home to Ithaca, "
        "where he encounters gods, monsters, and other dangers.",
        None,
        None,
    ),
    (
        "Avengers: Doomsday",
        None,
        "2026-12-18",
        "Sci-Fi",
        "coming_soon",
        None,
        "Walt Disney Studios Motion Pictures",
        "Heroes from three distinct universes are set on a collision course as they "
        "face an existential threat.",
        None,
        None,
    ),
]


# Initialize the database
database.init_db()


# Clear table and insert seed_data
conn = database.connect()
try:
    with conn:
        with conn.cursor() as cur:
            # Clear database before seeding to prevent duplication
            cur.execute("TRUNCATE movies RESTART IDENTITY CASCADE;")

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
        print("🌱 Seeded db successfully...")
finally:
    conn.close()