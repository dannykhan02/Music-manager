import sqlite3

class CrewDB:
    def __init__(self):
        self.connection = sqlite3.connect('crew.db')
        self.cursor = self.connection.cursor()

    def add_crew(self, name):
        self.cursor.execute('INSERT INTO crews (name) VALUES (?)', (name,))
        self.connection.commit()

    def list_crews_with_albums(self):
        self.cursor.execute("SELECT id, name FROM crews")
        crews = self.cursor.fetchall()
        crew_list = []
        for crew in crews:
            crew_id = crew[0]
            self.cursor.execute("SELECT id, title FROM albums WHERE crew_id = ?", (crew_id,))
            albums = self.cursor.fetchall()
            crew_list.append({
                'id': crew_id,
                'name': crew[1],
                'albums': [{'id': album[0], 'title': album[1]} for album in albums]
            })
        return crew_list

    def delete_crew(self, crew_id):
        self.cursor.execute('DELETE FROM albums WHERE crew_id = ?', (crew_id,))
        self.cursor.execute('DELETE FROM members WHERE crew_id = ?', (crew_id,))
        self.cursor.execute('DELETE FROM crews WHERE id = ?', (crew_id,))
        self.connection.commit()

    def close(self):
        self.connection.close()
