-- Creates the movies table and defines its columns and constraints.
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title TEXT NOT NULL,
    runtime INTEGER CHECK (runtime > 0),
    release_date DATE,
    genre TEXT CHECK (genre IN (
        'Action', 'Adventure', 'Animation', 'Comedy', 'Crime',
        'Documentary', 'Drama', 'Family', 'Fantasy', 'Horror',
        'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western'
    )),
    status TEXT NOT NULL DEFAULT 'coming_soon'
        CHECK (status IN ('coming_soon', 'playing', 'archived')),
    rating TEXT CHECK (rating IN ('G', 'PG', 'PG-13', 'R', 'NC-17')),
    distributor TEXT,
    synopsis TEXT,
    poster_url TEXT,
    trailer_url TEXT
);