from remainder.alarm import set_alarm
from remainder.timer import set_timer
from remainder.remainder import add_reminder, check_reminders

from notes_manager.create import create_note
from notes_manager.delete import delete_note
from notes_manager.search import search_notes

from automation.open_apps import open_app
from automation.open_sites import open_website
from automation.auto_folder import create_folder

while True:
    print("\n=== PERSONAL ASSISTANT TOOLKIT ===")
    print("1. Reminder & Alarm")
    print("2. Notes Manager")
    print("3. Automation")
    print("4. Exit")

    choice = input("Choose option: ")

    # ------ REMINDER ------
    if choice == "1":
        print("a. Set Alarm")
        print("b. Set Timer")
        print("c. Add Reminder")
        print("d. Check Reminders")
        sub = input("Choose sub-option: ")

        if sub == "a":
            t = input("Enter time (HH:MM): ")
            set_alarm(t)

        elif sub == "b":
            sec = int(input("Enter seconds: "))
            print(set_timer(sec))

        elif sub == "c":
            text = input("Reminder text: ")
            time_ = input("Time (HH:MM): ")
            print(add_reminder(text, time_))

        elif sub == "d":
            print(check_reminders())

    # ------ NOTES ------
    elif choice == "2":
        print("a. Create Note")
        print("b. Delete Note")
        print("c. Search Notes")
        sub = input("Choose sub-option: ")

        if sub == "a":
            t = input("Title: ")
            c = input("Content: ")
            print(create_note(t, c))

        elif sub == "b":
            t = input("Title to delete: ")
            print(delete_note(t))

        elif sub == "c":
            k = input("Keyword: ")
            print(search_notes(k))

    # ------ AUTOMATION ------
    elif choice == "3":
        print("a. Open Application")
        print("b. Open Website")
        print("c. Create Folder")
        sub = input("Choose sub-option: ")

        if sub == "a":
            p = input("App path: ")
            print(open_app(p))

        elif sub == "b":
            url = input("Enter URL: ")
            print(open_website(url))

        elif sub == "c":
            name = input("Folder name: ")
            print(create_folder(name))

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option!")
