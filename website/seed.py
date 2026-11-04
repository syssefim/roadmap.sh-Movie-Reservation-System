
# seed data
cur.executemany(
    """
    INSERT INTO movies (
        title, runtime, release_date, genre, status, rating,
        distributor, synopsis, poster_url, trailer_url
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """,
    [
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
    ],
)