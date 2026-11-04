import os
import psycopg2
from dotenv import load_dotenv
from pathlib import Path

SCHEMA_PATH = Path(__file__).parent / "schema.sql"

load_dotenv()

if not load_dotenv():
    raise FileNotFoundError("Failed to load the .env file. Does it exist?")



def connect():
    return psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            dbname=os.getenv("DB_NAME", "movie_reservation"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD"),
            port=int(os.getenv("DB_PORT", 5432)),
        )




def init_db():
    conn = connect()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(SCHEMA_PATH.read_text())
    finally:
        conn.close()



def close_connection():
    conn.commit()
    cur.close()
    conn.close()





if __name__ == "__main__":
    connect()