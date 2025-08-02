file_note = 'notes.txt'

#display menu

def menu():
    print("\n~~NOTES MENU~~\n" \
    "1. Add new note\n" \
    "2. View all notes\n" \
    "3. Delete all notes\n" \
    "4. Exit")

#add new notes

def new_note():
    note = input('Add the new note: \n')
    with open(file_note, 'a') as file:
        file.write(note + '\n')
    print('Note added.')

#view note
def view_notes():
    try:
        with open(file_note, 'r') as file:
            content = file.read()
            if content:
                print('~~Your notes~~\n', content)
            else: print('Notes not found.')
    except FileNotFoundError:
        print('Notes not found')

#delete note

def delete_notes():
    confirm = int(input('Are you sure to delete all notes?\n1. Yes\n2. No.\n'))
    if confirm == 1:
            with open(file_note, 'w') as file: 
                pass
            print('All notes deleted')

    else: print('Deletion cancelled')

#main menu


while True:
        menu()
        choice = int(input('Enter the option: '))
        if choice == 1: new_note()
        elif choice == 2: view_notes()
        elif choice == 3: delete_notes()
        elif choice == 4:
            print('exiting')
            break
        else: print('Invalid choice')

