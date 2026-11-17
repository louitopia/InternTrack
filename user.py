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


def student_menu(internships):
    while True:
        print("\n================================")
        print("        STUDENT/USER MENU")
        print("================================")
        print("1. Browse Internships")
        print("2. Back to Main Menu")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            browse_internships(internships)

        elif choice == "2":
            print("\nReturning to Main Menu...")
            break

        else:
            print("\nInvalid choice. Please try again.")
