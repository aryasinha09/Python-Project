import json

NOTES_FILE = "notes.json"

def delete_note(title):
    try:
        with open(NOTES_FILE, "r") as f:
            notes = json.load(f)
    except:
        return "No notes found!"

    if title in notes:
        del notes[title]
        with open(NOTES_FILE, "w") as f:
            json.dump(notes, f, indent=4)
        return "Note deleted!"
    else:
        return "Note not found."
