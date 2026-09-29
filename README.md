# Digital Contact Book

A simple command-line **Digital Contact Book** built in Python using
basic programming concepts from the CSE1021 -- Introduction to Problem
Solving and Programming course.

## Project Overview

The Digital Contact Book allows users to store and manage contact
information through a simple menu-driven interface.

Each contact contains:

-   Name
-   Phone number
-   Email address

The project is designed using basic Python concepts such as lists,
dictionaries, functions, conditional statements, loops, input/output
operations, and simple problem-solving techniques.

## Features

### 1. Add Contact

-   Add a new contact with name, phone number, and email.
-   Name and phone number are required.
-   Prevents duplicate phone numbers.

### 2. View All Contacts

-   Displays all contacts currently stored in the contact book.
-   Shows the contact number, name, phone number, and email.

### 3. Search Contact

-   Search for a contact by name.
-   Supports partial name matching.
-   Displays all matching contacts.

### 4. Update Contact

-   Find a contact using its phone number.
-   Update the name, phone number, or email.
-   Leave a field blank to keep its existing value.

### 5. Delete Contact

-   Find a contact using its phone number.
-   Remove the contact from the contact book.

### 6. Exit

-   Safely exits the program.

## Technologies Used

-   **Programming Language:** Python
-   **Interface:** Command-line / Terminal
-   **Data Storage:** Python list containing dictionaries
-   **External Libraries:** None

## Python Concepts Used

This project demonstrates the following basic programming concepts:

-   Variables
-   Strings
-   Lists
-   Dictionaries
-   Functions
-   `if`, `elif`, and `else` statements
-   `for` loops
-   `while` loops
-   `return`
-   User input and output
-   String methods such as `strip()` and `lower()`
-   List operations such as `append()` and `remove()`
-   Basic validation
-   Searching through a list

## How the Data Is Stored

Contacts are stored in a Python list:

``` python
contacts = []
```

Each contact is represented using a dictionary:

``` python
contact = {
    "name": "Example Name",
    "phone": "9876543210",
    "email": "example@email.com"
}
```

Multiple contact dictionaries are stored inside the `contacts` list.

## How to Run the Project

### Prerequisites

Install **Python 3** on your computer.

You can check whether Python is installed by running:

``` bash
python --version
```

or:

``` bash
python3 --version
```

### Running the Program

1.  Save the Python program as:

``` text
digital_contact_book.py
```

2.  Open a terminal in the project folder.

3.  Run:

``` bash
python digital_contact_book.py
```

If your system uses `python3`, run:

``` bash
python3 digital_contact_book.py
```

## Program Menu

When the program starts, it displays:

``` text
===== DIGITAL CONTACT BOOK =====
1. Add Contact
2. View All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
```

Enter a number from **1 to 6** to select an operation.

## Example

### Adding a Contact

``` text
--- Add Contact ---
Enter name: Rahul
Enter phone number: 9876543210
Enter email: rahul@example.com
Contact added successfully!
```

### Viewing Contacts

``` text
--- All Contacts ---

Contact 1
Name: Rahul
Phone: 9876543210
Email: rahul@example.com
```

### Searching for a Contact

``` text
--- Search Contact ---
Enter name to search: rah

Contact Found
Name: Rahul
Phone: 9876543210
Email: rahul@example.com
```

## Project Structure

``` text
Digital-Contact-Book/
│
├── digital_contact_book.py
└── README.md
```

## Limitations

-   Contacts are stored only while the program is running.
-   The program does not use a database or external file for permanent
    storage.
-   The interface is command-line based.
-   Phone numbers are treated as text input rather than being validated
    for a particular format.

## Learning Objectives

This project provides practical experience with:

-   Breaking a problem into smaller functions
-   Designing a menu-driven program
-   Working with lists and dictionaries
-   Using loops to search and process data
-   Using conditional statements for decision making
-   Performing basic input validation
-   Creating reusable functions
-   Applying basic Python problem-solving techniques

## Course Relevance

The project is aligned with topics in **CSE1021 -- Introduction to
Problem Solving and Programming**, particularly Python data, expressions
and statements, functions, control flow, lists, dictionaries, and basic
problem-solving techniques.

## Future Improvements

Possible future improvements include:

-   Saving contacts permanently in a file
-   Adding sorting functionality
-   Searching by phone number or email
-   Validating phone numbers and email addresses
-   Adding a graphical user interface
-   Adding contact groups or categories

## Author

**Digital Contact Book -- CSE1021 Project**

------------------------------------------------------------------------

*This project is created for educational purposes using basic Python
programming concepts.*

