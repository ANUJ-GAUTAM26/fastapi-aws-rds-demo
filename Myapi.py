from fastapi import FastAPI, HTTPException
import psycopg2
import configparser
import logging
from pydantic import BaseModel

# ---------------- Logging ----------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ---------------- App ----------------
app = FastAPI()

# ---------------- Database Config ----------------
def get_db_connection_params():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return {
        "host": config.get('database', 'host'),
        "database": config.get('database', 'db_name'),
        "user": config.get('database', 'user'),
        "password": config.get('database', 'password')
    }

def get_db_connection():
    params = get_db_connection_params()
    try:
        conn = psycopg2.connect(**params)
        logging.info("✅ Database connection successful!")
        return conn
    except Exception as e:
        logging.error(f"❌ Database connection failed: {e}")
        return None

# ---------------- Test Endpoint ----------------
@app.get("/test-db-connection")
async def test_db_connection():
    conn = None
    try:
        conn = get_db_connection()
        if conn:
            return {"status": "success", "message": "Successfully connected to the database."}
        else:
            raise HTTPException(status_code=500, detail="Could not establish database connection.")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    finally:
        if conn:
            conn.close()

# ---------------- Models ----------------
class Source(BaseModel):
    source_id: int
    source_name: str

class Author(BaseModel):
    author_id: int
    author_name: str

# ---------------- Routes ----------------
@app.get("/sources", response_model=list[Source])
async def get_sources():
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            raise HTTPException(status_code=500, detail="Database connection failed.")

        cursor = conn.cursor()
        cursor.execute("SELECT source_id, source_name FROM dim_sources ORDER BY source_name;")
        data = cursor.fetchall()
        cursor.close()

        if not data:
            raise HTTPException(status_code=404, detail="No sources found.")

        return [{"source_id": row[0], "source_name": row[1]} for row in data]

    except HTTPException as e:
        raise e
    except Exception as e:
        logging.error(f"❌ Error fetching sources: {e}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    finally:
        if conn:
            conn.close()

@app.get("/authors", response_model=list[Author])
async def get_authors():
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            raise HTTPException(status_code=500, detail="Database connection failed.")

        cursor = conn.cursor()
        cursor.execute("SELECT author_id, author_name FROM dim_authors ORDER BY author_name;")
        data = cursor.fetchall()
        cursor.close()

        if not data:
            raise HTTPException(status_code=404, detail="No authors found.")

        return [{"author_id": row[0], "author_name": row[1]} for row in data]

    except HTTPException as e:
        raise e
    except Exception as e:
        logging.error(f"❌ Error fetching authors: {e}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    finally:
        if conn:
            conn.close()

