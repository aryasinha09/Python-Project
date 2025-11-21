import json

NOTES_FILE = "notes.json"

def search_notes(keyword):
    try:
        with open(NOTES_FILE, "r") as f:
            notes = json.load(f)
    except:
        return "No notes found!"

    results = {title: text for title, text in notes.items() if keyword.lower() in text.lower()}

    return results if results else "No matching notes."
