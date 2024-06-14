# Music-manager

## Available globally

## Web Application for Managing Musical Crews, Members, and Albums

By [Daniel Kemboi]

## Description
The Music Manager application is a console-based platform designed for managing musical crews, their members, and their albums. Users can perform various operations, such as creating crews, adding members and albums, assigning albums to crews, and more. This application is ideal for those who need to organize and manage musical entities efficiently.

## How to Use

### Requirements
- Python 3.x
- SQLite3

### Installation Process

1. Clone this repository using
   ```bash
   git clone git@github.com:dannykhan02/Music-manager.git
or download the code as a ZIP file.

If downloaded as a ZIP file, extract it to your preferred location.

Navigate to the project folder.

Ensure you have SQLite3 installed. If not, you can download and install it from SQLite Downloads.

Running the Application
To start the application, run the following command:

bash
Copy code
python lib/app.py
Features
Add Crew: Create a new musical crew.
Add a Member to a Crew: Add a new member to an existing crew.
Add an Album: Create a new album.
Assign an Album to a Crew: Assign an existing album to a specific crew.
List Crews: List all crews along with their assigned albums.
List Members in a Crew: List all members in a specific crew and display the albums assigned to the crew.
List Albums: List all albums with their details.
Delete Crew: Delete a crew and all associated members and albums.
Exit: Exit the application.
Application Flow
Upon running the application, you will be presented with a menu of options:

markdown
Copy code
1. Add Crew
2. Add a member to a Crew
3. Add an Album
4. Assign an album to a Crew
5. List Crews
6. List members in a Crew
7. List Albums
8. Delete Crew
9. Exit
Adding a Crew
Select option 1.
Enter the name of the crew.
Adding a Member to a Crew
Select option 2.
Enter the first name and last name of the member.
Enter the ID of the crew to which the member will be added.
Adding an Album
Select option 3.
Enter the title of the album.
Assign an existing album to a specific crew.
List Crews
Select option 5.
The application will list all crews along with their assigned albums.
Listing Members in a Crew
Select option 6.
Enter the ID of the crew.
The application will list all members in the crew along with the crew name and assigned albums.
Listing Albums
Select option 7.
The application will list all albums along with their IDs, titles, and the crew they are assigned to (if any).
Deleting a Crew
Select option 8.
Enter the ID of the crew to delete.
The application will delete the crew and all associated members and albums.
Exiting the Application
Select option 9 to exit the application.
All database connections will be closed.
Database Schema
The application uses an SQLite database with the following schema:

crews: Stores information about musical crews.

id (INTEGER PRIMARY KEY)
name (TEXT NOT NULL)
members: Stores information about crew members.

id (INTEGER PRIMARY KEY)
first_name (TEXT NOT NULL)
last_name (TEXT NOT NULL)
crew_id (INTEGER, FOREIGN KEY references crews(id))
albums: Stores information about albums.

id (INTEGER PRIMARY KEY)
title (TEXT NOT NULL)
crew_id (INTEGER, FOREIGN KEY references crews(id))
Technologies Used
Python
SQLite3
Support and Contact Details
For inquiries, collaborations, or issues with the app, please contact daniel.kemboi@student.moringaschool.com

License
MIT License 

Copyright &copy; 2024 Daniel kemboi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.