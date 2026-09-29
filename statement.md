# Digital Contact Book -- Project Statement

## 1. Project Title

**Digital Contact Book**

## 2. Problem Statement

Managing a collection of personal contacts manually can make it
difficult to add new contact information, find a particular contact,
modify outdated details, or remove an unwanted contact.

The **Digital Contact Book** is developed as a simple Python-based
solution to this problem. It provides a menu-driven system through which
a user can add, view, search, update, and delete contact information.

Each contact contains three main details:

-   Name
-   Phone number
-   Email address

The project applies basic problem-solving and programming concepts from
**CSE1021 -- Introduction to Problem Solving and Programming**,
including Python lists, dictionaries, functions, conditional statements,
loops, input/output, and basic validation.

## 3. Scope of the Project

The scope of the Digital Contact Book is limited to basic contact
management through a command-line interface.

The system allows the user to:

-   Add a new contact.
-   View all stored contacts.
-   Search for contacts by name.
-   Update an existing contact using its phone number.
-   Delete an existing contact using its phone number.
-   Exit the application through the main menu.

Contacts are stored in memory using a Python list containing
dictionaries. The current version does not use a database or permanent
file storage, so the contact data is available only while the program is
running.

The project focuses on demonstrating fundamental programming and
problem-solving concepts rather than advanced frameworks, databases, or
graphical interfaces.

## 4. Target Users

The primary target users are:

-   Students learning basic Python programming.
-   Individuals who need a simple command-line contact management
    application.
-   Beginners who want to understand how CRUD-style operations can be
    implemented using Python lists and dictionaries.

The project is primarily intended as an educational application for
demonstrating the concepts covered in the CSE1021 course.

## 5. High-Level Features

### 5.1 Add Contact

Allows the user to enter a contact's name, phone number, and email
address.

The system checks that the name and phone number are provided and
prevents the same phone number from being added more than once.

### 5.2 View All Contacts

Displays all contacts currently stored in the contact book, including
their name, phone number, and email address.

### 5.3 Search Contact

Allows the user to search for a contact using a name.

The search supports partial matching and is case-insensitive.

### 5.4 Update Contact

Allows the user to find a contact using its phone number and update the
name, phone number, or email address.

A blank field can be used to keep the existing value.

### 5.5 Delete Contact

Allows the user to find a contact using its phone number and remove it
from the contact book.

### 5.6 Menu-Driven Interface

The application provides a simple numbered menu that allows the user to
select an operation and return to the main menu after completing it.

## 6. Project Objective

The main objective of the project is to apply basic programming and
problem-solving techniques to create a practical contact-management
application.

The project specifically aims to demonstrate:

-   Problem decomposition.
-   Algorithmic thinking.
-   Python lists and dictionaries.
-   Functions and modular programming.
-   Conditional statements.
-   Loops and iteration.
-   User input and output.
-   Basic input validation.
-   Searching and updating data.

## 7. Project Limitations

The current version has the following limitations:

-   Contact data is stored only in memory.
-   Contacts are not permanently saved after the program exits.
-   The application uses a command-line interface.
-   There is no database integration.
-   Phone and email values have basic input handling but are not
    validated against detailed formatting rules.

## 8. Future Scope

The project can be extended in the future by adding:

-   Permanent file or database storage.
-   More detailed phone and email validation.
-   Contact sorting.
-   Search by phone number or email.
-   Contact categories or groups.
-   Import and export functionality.
-   A graphical user interface.

## 9. Course Relevance

The Digital Contact Book is relevant to **CSE1021 -- Introduction to
Problem Solving and Programming** because it applies the course concepts
of problem solving, algorithms, Python data structures, functions,
conditional statements, iteration, lists, and dictionaries.

The project converts a real-world contact-management problem into a set
of smaller programming operations and implements them using basic Python
techniques.
