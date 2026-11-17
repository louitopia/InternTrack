def create_student_profile():
    print("\n===== CREATE STUDENT PROFILE =====")

    name = input("Full Name: ").strip()
    student_id = input("Student ID: ").strip()
    program = input("Program: ").strip()
    year_level = input("Year Level: ").strip()

    if not name or not student_id or not program or not year_level:
        print("\nAll fields are required.")
        return None

    student = {
        "name": name,
        "student_id": student_id,
        "program": program,
        "year_level": year_level
    }

    print("\nStudent profile created successfully!")

    return student


# VIEW STUDENT PROFILE
def view_profile(student):
    print("\n===== STUDENT PROFILE =====")
    print(f"Full Name: {student['name']}")
    print(f"Student ID: {student['student_id']}")
    print(f"Program: {student['program']}")
    print(f"Year Level: {student['year_level']}")
    print("===========================")


# BROWSE AVAILABLE INTERNSHIPS
def browse_internships(internships):
    print("\n===== AVAILABLE INTERNSHIPS =====")

    if not internships:
        print("No internship opportunities available.")
        return

    for internship in internships:
        print("\n------------------------------")
        print(f"ID: {internship['id']}")
        print(f"Company: {internship['company']}")
        print(f"Position: {internship['position']}")
        print(f"Description: {internship['description']}")

    print("------------------------------")


# APPLY FOR INTERNSHIP
def apply_internship(student, internships, applications):
    print("\n===== APPLY FOR INTERNSHIP =====")

    if not internships:
        print("No internships available to apply for.")
        return

    browse_internships(internships)

    internship_id = input(
        "\nEnter Internship ID to apply: "
    ).strip()

    selected_internship = None

    for internship in internships:
        if str(internship["id"]) == internship_id:
            selected_internship = internship
            break

    if selected_internship is None:
        print("\nInvalid Internship ID.")
        return

    print("\n===== SELECTED INTERNSHIP =====")
    print(f"Company: {selected_internship['company']}")
    print(f"Position: {selected_internship['position']}")

    # CHECK FOR DUPLICATE APPLICATION
    for application in applications:
        if (
            application["student_id"] == student["student_id"]
            and application["internship_id"] == selected_internship["id"]
        ):
            print("\nYou already applied for this internship.")
            return

    confirm = input(
        "\nSubmit application? (Y/N): "
    ).strip().lower()

    if confirm != "y":
        print("\nApplication cancelled.")
        return

    application = {
        "id": len(applications) + 1,
        "student_id": student["student_id"],
        "student_name": student["name"],
        "program": student["program"],
        "year_level": student["year_level"],
        "internship_id": selected_internship["id"],
        "company": selected_internship["company"],
        "position": selected_internship["position"],
        "status": "Pending"
    }

    applications.append(application)

    print("\n================================")
    print("    APPLICATION SUBMITTED!")
    print("================================")
    print(f"Application ID: {application['id']}")
    print(f"Student: {student['name']}")
    print(f"Company: {application['company']}")
    print(f"Position: {application['position']}")
    print(f"Status: {application['status']}")
    print("================================")


# VIEW STUDENT APPLICATIONS
def view_applications(student, applications):
    print("\n===== MY APPLICATIONS =====")

    found = False

    for application in applications:
        if application["student_id"] == student["student_id"]:
            found = True

            print("\n------------------------------")
            print(f"Application ID: {application['id']}")
            print(f"Company: {application['company']}")
            print(f"Position: {application['position']}")
            print(f"Status: {application['status']}")

    if not found:
        print("You have not submitted any applications.")

    print("------------------------------")


# STUDENT MAIN MENU
def student_menu(internships, applications):
    student = None

    while True:
        print("\n================================")
        print("         STUDENT/USER MENU")
        print("================================")
        print("1. Create Student Profile")
        print("2. View Student Profile")
        print("3. Browse Internships")
        print("4. Apply for Internship")
        print("5. My Applications")
        print("6. Back to Main Menu")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            new_profile = create_student_profile()

            if new_profile is not None:
                student = new_profile

        elif choice == "2":
            if student is not None:
                view_profile(student)
            else:
                print("\nPlease create your profile first.")

        elif choice == "3":
            browse_internships(internships)

        elif choice == "4":
            if student is not None:
                apply_internship(
                    student,
                    internships,
                    applications
                )
            else:
                print("\nPlease create your profile first.")

        elif choice == "5":
            if student is not None:
                view_applications(student, applications)
            else:
                print("\nPlease create your profile first.")

        elif choice == "6":
            print("\nReturning to Main Menu...")
            break

        else:
            print("\nInvalid choice. Please try again.")