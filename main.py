from user import student_menu
from company import company_menu


def main():
    internships = []
    applications = []

    while True:
        print("\n================================")
        print("       WELCOME TO INTERNTRACK")
        print("================================")
        print("1. Student/User")
        print("2. Company/HR")
        print("3. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_menu(internships, applications)

        elif choice == "2":
            company_menu(internships, applications)

        elif choice == "3":
            print("\nThank you for using InternTrack!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()