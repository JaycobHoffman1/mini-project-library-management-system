# Mini-Project: Library Management System

- Author: Jaycob Hoffman

- Date: 27 July 2024

## Documentation

The Library Management System is a CLI application that allows the user to create and manage data on books, authors, genres, and library ID holders within a library.

### Main Features

- **Book Operations**: With the ```Book operations``` feature, the user can add books, borrow books, return books, search for a specific book, and display all books.
- **User Operations**: With the ```User operations``` feature, the user can add users under unique library IDs, search for a specific library user, and display all users.
- **Author Operations**: With the ```Author operations``` feature, the user can add authors, search for a specific author, and display all authors.
- **Genre Operations**: With the ```Genre operations``` feature, the user can add genres, search for a specific genre, and display all genres.

### Bonus Features

- **Duplicate Detection**: When adding an instance of any entity (book, library user, author, or genre), the program will detect and notify the user when a duplicate identifier (e.g., book title or user library ID) is added (case-insensitive).

### UI

When the user first runs the Library Management System, the following UI will display:

```
Welcome to the Library Management System!

Main Menu:
1. Book operations
2. User operations
3. Author operations
4. Genre operations
5. Quit

Please select an option from the menu above: 
```

The user can select an option from the menu by entering the number that precedes it. Each selection (except for "Quit") will take the user to a separate menu, where they can then select a task. This cycle will continue indefinitely until the user selects option #5 and quits the program. Then, the following message will display:

```
Quitting program. Thank you for using the Library Management System!
```

The menus are as follows:

Book operations:
```
Book operations:
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books
6. Main menu

Please select an option from the menu above: 
```

User operations:
```
User operations:
1. Add a new user
2. View user details
3. Display all users
4. Main menu

Please select an option from the menu above:
```

Author operations:
```
Author operations:
1. Add a new author
2. View author details
3. Display all authors
4. Main menu

Please select an option from the menu above:
```

Genre operations:
```
Genre operations:
1. Add a new genre
2. View genre details
3. Display all genres
4. Main menu
```

When the task has finished, the menu will display again and prompt the user to select another option. This cycle will continue indefinitely until the user selects the "Main menu" option, in which they will be returned to the main menu.

### Errors

The Library Management System will raise ```ValueError```s with accompanying messages under the following circumstances:

- If any input is blank or consists entirely of spaces.
- If a regex pattern does not match an indicated input, where applicable.
- If the user tries to add an entity with a unique identifier that already exists in the system.
- If the user tries to search for an entity by a unique identifier that doesn't exist in the system.
- If the user tries to perform an operation on a specific entity when no entities of that class have been added yet.
- If the user tries to borrow a book that has already been borrowed.
- If the user tries to return a book they have not borrowed.
- If the user enters a non-numeric value when making a menu selection.
- If the user enters a numeric value that does not appear on the menu when making a menu selection.

#

View the Library Management System [GitHub Repository](https://github.com/JaycobHoffman1/mini-project-library-management-system)
