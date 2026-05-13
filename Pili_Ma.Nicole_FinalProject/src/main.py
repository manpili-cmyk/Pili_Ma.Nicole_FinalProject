"""
main.py

Main entry point of the MindTrack CLI application.
"""
from wellness import (
    add_mood,
    write_journal,
    search_journal,
    view_analytics
)


def main():
    """
    Main application loop.
    """

    while True:

        print("\n================================")
        print("        MINDTRACK CLI")
        print(" Mental Wellness Tracker System")
        print("================================")

        print("1. Add Mood Entry")
        print("2. Write Journal Entry")
        print("3. Search Journal")
        print("4. View Mood Analytics")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_mood()

        elif choice == "2":
            write_journal()

        elif choice == "3":
            search_journal()

        elif choice == "4":
            view_analytics()

        elif choice == "5":
            print("\nThank you for using MindTrack CLI.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()