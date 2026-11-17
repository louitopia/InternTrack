## CS 26 Exam 2 - Technical Documentation

## 1. Program Title and Overview

**InternTrack** is a Python-based application developed using Visual Studio Code. It is designed to connect college students, particularly College of Computing Education students from the University of Mindanao, with companies offering internship or On-the-Job Training (OJT) opportunities. The system provides two account types: Student/User and Company/HR. Students can browse available internship opportunities, submit applications, manage required documents, and monitor their application progress. Meanwhile, companies can manage their profiles, publish internship opportunities, review student applications, verify submitted documents, and schedule interviews. Its main purpose is to provide an organized system for managing internship opportunities and applications in one program.

## 2. Problem Description

College of Computing Education students applying for internships need to find available opportunities, prepare required documents, submit applications, and monitor their application statuses and interview schedules. Managing multiple applications separately can make it difficult to organize records and remember important dates. Meanwhile, companies need an organized way to publish internship opportunities, review student applications, verify submitted documents, and manage interview schedules.

InternTrack addresses these concerns by providing a Python-based system with separate student and company accounts. It allows students to manage their internship applications while enabling companies to organize internship postings and applicant records.

**Input:** Student and company account details, company information, internship positions, application details, required documents, and interview schedules.
**Processing:** Register and authenticate accounts, manage profiles, create and update internship postings, submit and review applications, verify documents, schedule interviews, and update application statuses.
**Output:** Organized student profiles, company records, available internship opportunities, application lists, application statuses, interview schedules, and saved internship records.

## 3. Objectives

1. Provide separate registration and login options for students and companies.
2. Store and manage student accounts, company profiles, internship postings, and application records using an SQLite database.
3. Allow students to browse internship opportunities, submit applications, and monitor their application statuses.
4. Allow companies to create, view, update, and delete internship postings and manage student applicants.
5. Manage internship requirements, document verification, interview schedules, and application statuses.
6. Perform database operations such as inserting, retrieving, updating, and deleting records using SQL commands.
7. Apply input validation and error handling to maintain accurate and organized records.

## 4. Program Requirements and Functions

InternTrack uses Python functions, lists, dictionaries, and SQLite database handling to manage and store records. It supports application statuses such as Pending, Under Review, Interview Scheduled, Accepted, and Rejected. The system stores student accounts, company accounts, internship postings, and application records in a single SQLite database file named interntrack.db, allowing information to remain accessible even after the program is closed and reopened. InternTrack provides two main account types: Student/User and Company/HR. Each account type has access to different functions through its respective dashboard.

**Student/User Functions:** Register and log in, manage personal profiles, browse available internship opportunities, submit applications, monitor application statuses, manage required documents, and view interview schedules.

**Company/HR Functions:** Register and log in, manage company profiles, create and manage internship postings, view student applicants, review applications, verify submitted documents, schedule interviews, and update application statuses.

The system is organized into two major subsystems:

**User Management System:** Handles student registration, login, personal profile management, internship browsing, application submission, document management, and application monitoring.

**Company Management System:** Handles company registration, login, company profile management, internship posting management, applicant reviews, document verification, interview scheduling, and application status updates.

## 5. Program Structure

```text
InternTrack/
│
├── main.py
├── user.py
├── company.py
├── database.py
│
└── interntrack.db
```

- `main.py` – Contains the main menu, account selection, registration, login, and navigation to the appropriate student or company dashboard.
- `user.py` – Handles student registration, login, profile management, internship browsing, application submission, document management, and application tracking.
- `company.py` – Handles company registration, login, company profile management, internship posting management, applicant reviews, document verification, and interview scheduling.
- `database.py` – Establishes the SQLite database connection, creates database tables, and manages database operations.
- `interntrack.db` – The SQLite database file that stores student, company, internship, and application records.

**Example import:**

```python
from user import register_user, login_user
from company import register_company, login_company, add_internship
```

This separation keeps student-related and company-related operations organized in their respective modules. The `main.py` file handles user interaction and connects the functions from both modules, making the program easier to maintain, reuse, and test.

## 6. Data Structures Used

InternTrack uses Python data structures to organize and manage student accounts, company profiles, internship postings, and application records.

### 1. Lists

Lists store multiple records retrieved from the database. They can be used when displaying available internship opportunities or student applications.

Example:

```python
internships = [
    "Software Developer Intern",
    "Data Analyst Intern",
    "UI/UX Design Intern"
]
```

### 2. Dictionaries

Dictionaries store information using key-value pairs. They can represent individual student profiles, company details, internship postings, and application records.

Example:

```python
student = {
    "student_id": 562819,
    "full_name": "John Louie T. Bingil",
    "email": "j.bingil.562819@umindanao.edu.ph"
}
```

### 3. Tuples

Tuples store fixed information that should not be modified during program execution. InternTrack can use tuples to define the available application statuses.

Example:

```python
application_statuses = (
    "Pending",
    "Under Review",
    "Interview Scheduled",
    "Accepted",
    "Rejected"
)
```

These data structures help the program organize records, retrieve information, and manage internship applications efficiently.

## 7. Functions and Responsibilities

InternTrack uses reusable Python functions to organize the operations of its two major subsystems. Each function performs a specific task, making the program easier to maintain and understand.

| Function                      | Subsystem          | Responsibility                                              |
| ----------------------------- | ------------------ | ----------------------------------------------------------- |
| `register_user()`             | User Management    | Creates a new student account.                              |
| `login_user()`                | User Management    | Checks student login credentials.                           |
| `view_profile()`              | User Management    | Displays student profile information.                       |
| `browse_internships()`        | User Management    | Displays available internship opportunities.                |
| `apply_internship()`          | User Management    | Submits an application to an internship posting.            |
| `view_applications()`         | User Management    | Displays the student's submitted applications and statuses. |
| `register_company()`          | Company Management | Creates a new company account.                              |
| `login_company()`             | Company Management | Checks company login credentials.                           |
| `manage_company_profile()`    | Company Management | Displays or updates company information.                    |
| `add_internship()`            | Company Management | Creates a new internship posting.                           |
| `update_internship()`         | Company Management | Updates an existing internship posting.                     |
| `delete_internship()`         | Company Management | Removes an internship posting.                              |
| `view_applicants()`           | Company Management | Displays applicants for the company's internship postings.  |
| `update_application_status()` | Company Management | Updates the status of a student application.                |
| `schedule_interview()`        | Company Management | Adds an interview schedule to an application.               |

**Example Function 1: Registering a Student**

```python
def register_user(name, email):
    student = {
        "name": name,
        "email": email
    }

    print("Student registered successfully!")
```

This function collects student information and creates a student record

**Example Function 2: Adding an Internship**

```python
def add_internship(position, description):
    internship = {
        "position": position,
        "description": description
    }

    print("Internship added successfully!")
```

This function creates an internship record containing the position and description.

**Example Function 3: Updating Application Status**

```python
def update_application_status(application, status):
    application["status"] = status
    print("Application status updated successfully!")
```

This function changes the status of a student's internship application.

These examples demonstrate how functions help divide the program into smaller operations. The actual implementation includes additional input validation and database operations to save, retrieve, and update records in the SQLite database.

## 8. File Handling and Data Storage

InternTrack uses an SQLite database file to save and retrieve records. This allows student accounts, company profiles, internship postings, and application information to remain available even after the program is closed.

The system uses one database file:

| File             | Stored Information                                                                                                                                   |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `interntrack.db` | Student accounts, company profiles, internship postings, applications, submitted document information, interview schedules, and application statuses |

**Database Connection**

The `sqlite3` module is used to connect the Python program to the `interntrack.db` file. If the database file does not exist, SQLite automatically creates it.

Example:

```python
import sqlite3

connection = sqlite3.connect("interntrack.db")
cursor = connection.cursor()
```

**Saving Records**

The `commit()` function saves changes made to the database, such as adding or updating student accounts, company profiles, and internship applications.

Example:

```python
connection.commit()
```

**Closing the Database**

The `close()` function ends the database connection after the required operations are completed.

Example:

```python
connection.close()
```

These operations allow InternTrack to store and retrieve organized records whenever the program is executed. Since the project uses a local SQLite database, the records are stored on the computer where the program runs.

## 9. Error Handling and Input Validation

InternTrack uses error handling and input validation to prevent invalid information from affecting the program. These techniques help ensure that users provide the required information when registering, submitting applications, and managing records.

The following situations are considered:

| Possible Error                           | Handling Method                                                          |
| ---------------------------------------- | ------------------------------------------------------------------------ |
| Empty required fields                    | Display a message asking the user to complete the required information.  |
| Invalid login credentials                | Display an error message and allow the user to try again.                |
| Duplicate email address                  | Prevent registration using an existing email address.                    |
| Invalid application status               | Accept only the predefined application statuses.                         |
| Database connection error                | Catch the database error and display an appropriate message.             |
| Duplicate or invalid record              | Prevent the insertion of records that do not meet database requirements. |
| Nonexistent internship or application ID | Display a message indicating that the requested record cannot be found.  |

Example:

```
import sqlite3

def register_user(name, email, password_hash):
    try:
        if not name or not email or not password_hash:
            raise ValueError("All required fields must be completed.")

        connection = sqlite3.connect("interntrack.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO users (name, email, password_hash)
            VALUES (?, ?, ?)
        """, (name, email, password_hash))

        connection.commit()
        print("Student registered successfully!")

    except ValueError as error:
        print("Invalid entry:", error)

    except sqlite3.IntegrityError:
        print("This email address is already registered.")

    except sqlite3.Error as error:
        print("Database error:", error)

    finally:
        if "connection" in locals():
            connection.close()
```

A ValueError occurs when required fields are empty. A sqlite3.IntegrityError handles duplicate email addresses, while sqlite3.Error catches other database-related problems. These techniques help prevent unexpected errors from immediately stopping the program.

## 10. Testing and Debugging

Testing and debugging are important to ensure that InternTrack performs its intended functions. Each major feature should be tested to identify errors and verify that the program produces the expected results.

The following test cases can be used to evaluate the system:

| Test Case                                   | Expected Result                                                      |
| ------------------------------------------- | -------------------------------------------------------------------- |
| Register a student using valid information. | Student account is created and saved in the SQLite database.         |
| Register a company using valid information. | Company account is created and saved in the SQLite database.         |
| Log in using correct credentials.           | User is directed to the appropriate dashboard.                       |
| Log in using incorrect credentials.         | An error message is displayed.                                       |
| Create an internship posting.               | Internship opportunity is saved and displayed.                       |
| Browse available internships.               | Available internship postings are displayed.                         |
| Submit an internship application.           | Application record is created and saved in the database.             |
| Review student applications as a company.   | Only applicants for the company's internship postings are displayed. |
| Update an application status.               | The selected application status is updated in the database.          |
| Schedule an interview.                      | Interview details are saved in the application record.               |
| Restart the program.                        | Previously saved records are retrieved from the SQLite database.     |
| Enter incomplete or invalid information.    | The program displays an appropriate error message.                   |

**Debugging Considerations**

During development, possible errors may involve incorrect database connections, missing records, invalid inputs, duplicate accounts, and incorrect application references. These issues can be addressed through input validation, exception handling, and checking the program's functions individually.

The actual results should be recorded after each test case is performed during program testing.

## 11. Conclusion

InternTrack provides an organized way for college students and companies to manage internship opportunities and applications through one Python-based program. With its two major subsystems, User Management System and Company Management System, students can browse internship opportunities, submit applications, manage required documents, and monitor their application progress. Companies can manage their profiles, publish internship opportunities, review applicants, verify documents, and schedule interviews.

Through the use of Python functions, lists, dictionaries, tuples, and SQLite database handling, the program demonstrates how fundamental programming concepts can be applied to develop a practical information management system. Overall, InternTrack aims to simplify internship application management and provide a more organized process for both students and companies.

## 12. References

- Amazon Web Services. (n.d.). What is Python? - Cloud beginner’s guide to python - AWS. Amazon Web Services, Inc. Retrieved November 13, 2026, from https://aws.amazon.com/what-is/python/
- Amazon Web Services. (n.d.). What is SQL (Structured Query Language)? Amazon Web Services, Inc. https://aws.amazon.com/what-is/sql/
- Bouchrika, I. (2022). On the job training: OJT meaning, advantages & types « guide 2 research. Research.Com. https://research.com/careers/on-the-job-training
- Heller, M. (2022). What is visual studio code? Microsoft’s extensible code editor. InfoWorld. https://www.infoworld.com/article/2335960/what-is-visual-studio-code-microsofts-extensible-code-editor.html
- Power, G. (2024). What is SQLite3? A comprehensive overview. Medium. https://global-power.medium.com/what-is-sqlite3-a-comprehensive-overview-fde294e72298
- Python Software Foundation. (n.d.). Built-in types. Python documentation. https://docs.python.org/3/builtins/stdtypes.html
- Python Software Foundation. (n.d.). Errors and exceptions\*. Python documentation. https://docs.python.org/3/tutorial/errors.html
- Python Software Foundation. (n.d.). Functions. Python documentation. https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- SQLite. (n.d.). About SQLite. https://www.sqlite.org/about.html
