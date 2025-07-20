from mcp import tool, serve
import sqlite3

DB_PATH = "example.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS data (key TEXT, value TEXT)")
    conn.commit()
    conn.close()

@tool(name="add_data", description="Add key-value pair to SQLite DB")
def add_data(key: str, value: str) -> str:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO data (key, value) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()
    return f"Added {key}: {value}"

@tool(name="fetch_data", description="Fetch value for a given key from SQLite DB")
def fetch_data(key: str) -> str:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT value FROM data WHERE key=?", (key,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else "Key not found"

if __name__ == "__main__":
    init_db()
    serve()
