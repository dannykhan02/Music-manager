import sqlite3

class MemberDB:
    def __init__(self):
        self.connection = sqlite3.connect('crew.db')
        self.cursor = self.connection.cursor()

    def is_valid_name(self, first_name, last_name):
        combined_name = f"{first_name} {last_name}"
        return combined_name.replace(" ", "").isalpha()

    def add_member(self, first_name, last_name, crew_id):
        if self.is_valid_name(first_name, last_name):
            self.cursor.execute('INSERT INTO members (first_name, last_name, crew_id) VALUES (?, ?, ?)', (first_name, last_name, crew_id))
            self.connection.commit()
        else:
            print("Invalid member name. Please enter valid first and last names.")

    def list_members_in_crew(self, crew_id):
        self.cursor.execute("SELECT id, first_name, last_name FROM members WHERE crew_id = ?", (crew_id,))
        members = self.cursor.fetchall()

        self.cursor.execute("SELECT name FROM crews WHERE id = ?", (crew_id,))
        crew_name = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT id, title FROM albums WHERE crew_id = ?", (crew_id,))
        albums = self.cursor.fetchall()

        return crew_name, members, albums

    def delete_member(self, first_name, last_name):
        self.cursor.execute('DELETE FROM members WHERE first_name = ? AND last_name = ?', (first_name, last_name))
        self.connection.commit()

    def close(self):
        self.connection.close()
