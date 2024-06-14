import sqlite3

class AlbumDB:
    def __init__(self):
        self.connection = sqlite3.connect('crew.db')
        self.cursor = self.connection.cursor()

    def add_album(self, title):
        self.cursor.execute('INSERT INTO albums (title) VALUES (?)', (title,))
        self.connection.commit()

    def assign_album_to_crew(self, album_id, crew_id):
        self.cursor.execute('UPDATE albums SET crew_id = ? WHERE id = ?', (crew_id, album_id))
        self.connection.commit()

    def list_albums(self):
        self.cursor.execute("""
            SELECT albums.id, albums.title, albums.crew_id, crews.name
            FROM albums
            LEFT JOIN crews ON albums.crew_id = crews.id
        """)
        rows = self.cursor.fetchall()
        albums = []
        for row in rows:
            albums.append({
                'id': row[0],
                'title': row[1],
                'crew_id': row[2],
                'crew_name': row[3] if row[3] else 'Unassigned'
            })
        return albums

    def close(self):
        self.connection.close()
