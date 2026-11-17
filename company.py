# ADD INTERNSHIP
def add_internship(internships):
    print("\n===== ADD INTERNSHIP =====")

    company = input("Company Name: ").strip()
    position = input("Internship Position: ").strip()
    description = input("Description: ").strip()

    if not company or not position or not description:
        print("\nAll fields are required.")
        return

    internship = {
        "id": len(internships) + 1,
        "company": company,
        "position": position,
        "description": description
    }

    internships.append(internship)

    print("\nInternship added successfully!")
    print(f"Internship ID: {internship['id']}")


# VIEW INTERNSHIP POSTINGS
def view_internships(internships):
    print("\n===== INTERNSHIP POSTINGS =====")

    if not internships:
        print("No internship postings available.")
        return

    for internship in internships:
        print("\n------------------------------")
        print(f"ID: {internship['id']}")
        print(f"Company: {internship['company']}")
        print(f"Position: {internship['position']}")
        print(f"Description: {internship['description']}")

    print("------------------------------")


# VIEW STUDENT APPLICANTS
def view_applicants(applications):
    print("\n===== STUDENT APPLICANTS =====")

    if not applications:
        print("No applications submitted yet.")
        return

    for application in applications:
        print("\n------------------------------")
        print(f"Application ID: {application['id']}")
        print(f"Student Name: {application['student_name']}")
        print(f"Student ID: {application['student_id']}")
        print(f"Program: {application['program']}")
        print(f"Year Level: {application['year_level']}")
        print(f"Company: {application['company']}")
        print(f"Position: {application['position']}")
        print(f"Status: {application['status']}")

    print("------------------------------")

# UPDATE APPLICATION STATUS
def update_application_status(applications):
    print("\n===== UPDATE APPLICATION STATUS =====")

    if not applications:
        print("No applications available.")
        return

    view_applicants(applications)

    application_id = input(
        "\nEnter Application ID: "
    ).strip()

    for application in applications:
        if str(application["id"]) == application_id:

            statuses = (
                "Pending",
                "Under Review",
                "Interview Scheduled",
                "Accepted",
                "Rejected"
            )

            print("\n===== SELECT NEW STATUS =====")

            for i, status in enumerate(statuses, 1):
                print(f"{i}. {status}")

            choice = input("Enter your choice: ")

            if choice in ("1", "2", "3", "4", "5"):
                application["status"] = statuses[int(choice) - 1]
                print("\nApplication status updated successfully!")
            else:
                print("\nInvalid status.")

            return

    print("\nApplication not found.")

# COMPANY/HR MENU
def company_menu(internships, applications):
    while True:
        print("\n================================")
        print("         COMPANY/HR MENU")
        print("================================")
        print("1. Add Internship")
        print("2. View Internship Postings")
        print("3. View Applicants")
        print("4. Update Application Status")
        print("5. Back to Main Menu")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_internship(internships)

        elif choice == "2":
            view_internships(internships)

        elif choice == "3":
            view_applicants(applications)
        elif choice == "4":
            update_application_status(applications)

        elif choice == "5":
            print("\nReturning to Main Menu...")
            break

        else:
            print("\nInvalid choice. Please try again.")