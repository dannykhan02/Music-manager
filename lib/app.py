import sqlite3
from crews import CrewDB
from members import MemberDB
from album import AlbumDB
import db_setup

db_setup.create_tables()

def get_valid_string(prompt):
    while True:
        value = input(prompt)
        if value.replace(" ", "").isalpha():
            return value
        else:
            print("Invalid input. Please enter a string containing only letters and spaces.")

def main():
    crew_db = CrewDB()
    member_db = MemberDB()
    album_db = AlbumDB()

    while True:
        print("\n1. Add Crew")
        print("2. Add a member to a Crew")
        print("3. Add an Album")
        print("4. Assign an album to a Crew")
        print("5. List Crews")
        print("6. List members in a Crew")
        print("7. List Albums")
        print("8. Delete Crew")
        print("9. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = get_valid_string("Enter Crew name: ")
            crew_db.add_crew(name)
        elif choice == '2':
            first_name = get_valid_string("Enter Member's first name: ")
            last_name = get_valid_string("Enter Member's last name: ")
            crew_id = int(input("Enter Crew ID: "))
            member_db.add_member(first_name, last_name, crew_id)
        elif choice == '3':
            title = get_valid_string("Enter Album title: ")
            album_db.add_album(title)
        elif choice == '4':
            album_id = int(input("Enter Album ID: "))
            crew_id = int(input("Enter Crew ID: "))
            album_db.assign_album_to_crew(album_id, crew_id)
        elif choice == '5':
            crews = crew_db.list_crews_with_albums()
            for crew in crews:
                print(f"Crew ID: {crew['id']}, Name: {crew['name']}")
                for album in crew['albums']:
                    print(f"  Album ID: {album['id']}, Title: {album['title']}")
        elif choice == '6':
            crew_id = int(input("Enter Crew ID to list members: "))
            crew_name, members, albums = member_db.list_members_in_crew(crew_id)
            print(f"Crew Name: {crew_name}")
            print("Members:")
            for member in members:
                print(f"Member ID: {member[0]}, First Name: {member[1]}, Last Name: {member[2]}")
            print("Albums:")
            for album in albums:
                print(f"Album ID: {album[0]}, Title: {album[1]}")
        elif choice == '7':
            albums = album_db.list_albums()
            for album in albums:
                print(f"Album ID: {album['id']}, Title: {album['title']}, Crew ID: {album['crew_id']}, Crew Name: {album['crew_name']}")
        elif choice == '8':
            crew_id = int(input("Enter Crew ID to delete: "))
            crew_db.delete_crew(crew_id)
        elif choice == '9':
            crew_db.close()
            member_db.close()
            album_db.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
