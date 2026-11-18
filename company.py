# CREATE COMPANY PROFILE
def create_company_profile(company_profile):
    print("\n===== CREATE COMPANY PROFILE =====")

    if company_profile:
        print("Company profile already exists.")
        return

    name = input("Company Name: ").strip()
    email = input("Company Email: ").strip()
    address = input("Company Address: ").strip()
    description = input("Company Description: ").strip()

    if not name or not email or not address or not description:
        print("\nAll fields are required.")
        return

    company_profile["name"] = name
    company_profile["email"] = email
    company_profile["address"] = address
    company_profile["description"] = description

    print("\nCompany profile created successfully!")

# VIEW COMPANY PROFILE
def view_company_profile(company_profile):
    print("\n===== COMPANY PROFILE =====")

    if not company_profile:
        print("Please create a company profile first.")
        return

    print(f"Company Name: {company_profile['name']}")
    print(f"Company Email: {company_profile['email']}")
    print(f"Company Address: {company_profile['address']}")
    print(f"Company Description: {company_profile['description']}")
    print("===========================")

# ADD INTERNSHIP
def add_internship(internships, company_profile):
    print("\n===== ADD INTERNSHIP =====")

    if not company_profile:
        print("Please create a company profile first.")
        return

    position = input("Internship Position: ").strip()
    description = input("Description: ").strip()

    if not position or not description:
        print("\nAll fields are required.")
        return

    internship = {
        "id": len(internships) + 1,
        "company": company_profile["name"],
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
def company_menu(internships, applications, company_profile):
    while True:
        print("\n================================")
        print("         COMPANY/HR MENU")
        print("================================")
        print("1. Create Company Profile")
        print("2. View Company Profile")
        print("3. Add Internship")
        print("4. View Internship Postings")
        print("5. View Applicants")
        print("6. Update Application Status")
        print("7. Back to Main Menu")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_company_profile(company_profile)
        
        elif choice == "2":
            view_company_profile(company_profile)
            
        elif choice == "3":
            add_internship(internships, company_profile)

        elif choice == "4":
            view_internships(internships)

        elif choice == "5":
            view_applicants(applications)

        elif choice == "6":
            update_application_status(applications)

        elif choice == "7":
            print("\nReturning to Main Menu...")
            break

        else:
            print("\nInvalid choice. Please try again.")