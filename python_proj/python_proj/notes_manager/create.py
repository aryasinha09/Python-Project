import json

NOTES_FILE = "notes.json"

def create_note(title, content):
    try:
        with open(NOTES_FILE, "r") as f:
            notes = json.load(f)
    except:
        notes = {}

    notes[title] = content

    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)

    return "Note saved!"
