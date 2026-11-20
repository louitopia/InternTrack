# InternTrack

InternTrack is a Python-based internship management system designed to help college students organize internship opportunities and track their On-the-Job Training (OJT) applications.

The system also allows companies to post internship opportunities, view applicants, and manage application statuses.

This project is primarily intended for College of Computing Education students at the University of Mindanao.

**Development Status:** Work in Progress (Console-Based Prototype)

## 1. Features Implemented

### Student/User Management

- Create a student profile
- View student profile information
- Browse available internship opportunities
- Apply for an internship
- Prevent duplicate applications
- View submitted applications
- Track internship application statuses
- Search available internships by position using keywords

### Company/HR Management

- Create a company profile
- View company profile information
- Add internship postings
- View internship postings
- View student applicants
- Update application statuses

### Application Statuses

- Pending
- Under Review
- Interview Scheduled
- Accepted
- Rejected

## 2. Technologies Used

| Technology         | Purpose                   |
| ------------------ | ------------------------- |
| Python             | Main programming language |
| Visual Studio Code | Development environment   |
| Git                | Version control           |
| GitHub             | Source code hosting       |

### Planned Technologies

- SQLite - Permanent database storage
- SQL - Database operations
- Tkinter / CustomTkinter - Graphical User Interface (GUI)

## 3. Current Project Structure

```text
InternTrack/
│
├── main.py
├── user.py
├── company.py
├── README.md
└── .gitignore
```

### File Descriptions

- **main.py** - Handles the main menu and navigation between Student/User and Company/HR.
- **user.py** - Contains student profile management, internship browsing, application submission, and application tracking.
- **company.py** - Contains company profile management, internship postings, applicant viewing, and application status updates.
- **README.md** - Contains the project overview, features, and development progress.
- **.gitignore** - Specifies files excluded from Git version control.

## 4. How to Run the Program

### Requirements

- Python 3
- Visual Studio Code or another Python-compatible editor

### Instructions

1. Clone the repository:

```bash
git clone https://github.com/louitopia/InternTrack.git
```

2. Open the project directory:

```bash
cd InternTrack
```

3. Run the application:

```bash
python main.py
```

4. Select an option from the main menu:
   - Student/User
   - Company/HR
   - Exit

## 5. Current Limitations

InternTrack is currently a console-based prototype.

- Records are temporarily stored using Python lists and dictionaries.
- Data is lost when the program is closed.
- The current prototype supports one active student profile and one company profile.
- Registration and login features are not yet implemented.
- Permanent database storage has not yet been implemented.
- A graphical user interface (GUI) is not yet available.

These limitations will be addressed as development progresses.

## 6. Planned Features

### Student/User Management

- [x] Complete student profile persistence fix
- [x] Add internship search by position
- [ ] Student registration and login
- [ ] Manage student profile information
- [ ] Manage internship documents
- [ ] View interview schedules

### Company/HR Management

- [x] Create company profile
- [x] View company profile
- [x] Add internship postings
- [x] View internship postings
- [x] View applicants
- [x] Update application statuses
- [ ] Update internship postings
- [ ] Delete internship postings
- [ ] Company registration and login
- [ ] Verify applicant documents
- [ ] Schedule applicant interviews

### System Improvements

- [ ] Improve input validation and error handling
- [ ] Implement SQLite database integration
- [ ] Implement permanent data storage
- [ ] Develop Student/User GUI
- [ ] Develop Company/HR GUI
- [ ] Implement account-based access control
- [ ] Perform final system testing and debugging

## 7. Planned Database Structure

The final system will use SQLite to manage and store internship-related information.

### Proposed Tables

| Table        | Description                                              |
| ------------ | -------------------------------------------------------- |
| students     | Stores student profile information                       |
| companies    | Stores company profile information                       |
| internships  | Stores internship postings                               |
| applications | Stores student internship applications                   |
| documents    | Stores application requirements and verification records |
| interviews   | Stores interview schedules                               |

## 8. Project Objectives

InternTrack aims to:

1. Provide students with an organized internship application management system.
2. Allow students to browse available internship opportunities.
3. Enable students to submit and track their applications.
4. Allow companies to create and manage internship postings.
5. Provide companies with a way to review applicants and update application statuses.
6. Improve the organization of internship-related information.
7. Implement permanent data storage using SQLite.
8. Develop a graphical interface for students and companies.

## 9. Development Progress

InternTrack is being developed incrementally, with features implemented and tested before proceeding to the next stage.

Development progress is tracked through Git commits and GitHub.

### Recent Improvements (as of Nov 20, 2026, 7:25pm)

- Fixed student profile resetting when switching between menus.
- Student profiles now remain accessible throughout the program session.
- Fixed student profile persistence when switching between menus.
- Added internship search by position.
- Implemented case-insensitive keyword searching.
- Added handling for empty searches and no matching internships.

### Current Development Priorities

1. Improve input validation and error handling.
2. Implement Update Internship.
3. Implement Delete Internship.
4. Add interview scheduling and document management.
5. Integrate SQLite.
6. Develop the graphical user interface.
7. Conduct final testing and debugging.

## 10. Project Status

**InternTrack is currently under development.**

The existing version provides a functional console-based foundation for student internship applications and company internship management.
Future updates will focus on completing the remaining features, integrating SQLite, and developing a graphical desktop interface.
