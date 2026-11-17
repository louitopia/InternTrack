
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


def company_menu(internships):
    while True:
        print("\n================================")
        print("         COMPANY/HR MENU")
        print("================================")
        print("1. Add Internship")
        print("2. View Internship Postings")
        print("3. Back to Main Menu")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_internship(internships)

        elif choice == "2":
            view_internships(internships)

        elif choice == "3":
            print("\nReturning to Main Menu...")
            break

        else:
            print("\nInvalid choice. Please try again.")
