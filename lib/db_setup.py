import sqlite3

def drop_tables():
    connection = sqlite3.connect('crew.db')
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS members")
    cursor.execute("DROP TABLE IF EXISTS albums")
    cursor.execute("DROP TABLE IF EXISTS crews")

    connection.commit()
    connection.close()

def create_tables():
    connection = sqlite3.connect('crew.db')
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS crews (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            crew_id INTEGER,
            FOREIGN KEY (crew_id) REFERENCES crews(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS albums (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            crew_id INTEGER,
            FOREIGN KEY (crew_id) REFERENCES crews(id)
        )
    """)

    connection.commit()
    connection.close()

def refresh_database():
    drop_tables()
    create_tables()

if __name__ == "__main__":
    refresh_database()
