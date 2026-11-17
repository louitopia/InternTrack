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


def apply_internship(internships, applications):
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

    name = input("\nEnter Full Name: ").strip()
    email = input("Enter Email: ").strip()

    if not name or not email:
        print("\nAll fields are required.")
        return

    if "@" not in email:
        print("\nInvalid email address.")
        return

    for application in applications:
        if (
            application["internship_id"]
            == selected_internship["id"]
            and application["email"].lower() == email.lower()
        ):
            print("\nYou already applied for this internship.")
            return

    application = {
        "id": len(applications) + 1,
        "internship_id": selected_internship["id"],
        "company": selected_internship["company"],
        "position": selected_internship["position"],
        "student_name": name,
        "email": email,
        "status": "Pending"
    }

    applications.append(application)

    print("\n================================")
    print(" APPLICATION SUBMITTED!")
    print("================================")
    print(f"Application ID: {application['id']}")
    print(f"Company: {application['company']}")
    print(f"Position: {application['position']}")
    print(f"Status: {application['status']}")
    print("================================")


def student_menu(internships, applications):
    while True:
        print("\n================================")
        print("        STUDENT/USER MENU")
        print("================================")
        print("1. Browse Internships")
        print("2. Apply for Internship")
        print("3. Back to Main Menu")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            browse_internships(internships)

        elif choice == "2":
            apply_internship(internships, applications)

        elif choice == "3":
            print("\nReturning to Main Menu...")
            break

        else:
            print("\nInvalid choice. Please try again.")
