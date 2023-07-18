import pickle

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NotesManager:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def delete_note(self, note):
        self.notes.remove(note)

    def display_notes(self):
        if not self.notes:
            print("Нет заметок.")
        else:
            for i, note in enumerate(self.notes):
                print(f"Заметка {i+1}:")
                print(f"Заголовок: {note.title}")
                print(f"Содержание: {note.content}")
                print()

    def save_notes(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.notes, file)

    def load_notes(self, filename):
        with open(filename, "rb") as file:
            self.notes = pickle.load(file)

def main():
    notes_manager = NotesManager()

    while True:
        print("1. Создать заметку")
        print("2. Удалить заметку")
        print("3. Показать заметки")
        print("4. Сохранить заметки")
        print("5. Загрузить заметки")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            content = input("Введите содержание заметки: ")
            note = Note(title, content)
            notes_manager.add_note(note)
            print("Заметка создана.")
        elif choice == "2":
            notes_manager.display_notes()
            index = int(input("Введите номер заметки, которую хотите удалить: ")) - 1
            if 0 <= index < len(notes_manager.notes):
                note = notes_manager.notes[index]
                notes_manager.delete_note(note)
                print("Заметка удалена.")
            else:
                print("Недопустимый номер заметки.")
        elif choice == "3":
            notes_manager.display_notes()
        elif choice == "4":
            filename = input("Введите имя файла для сохранения заметок: ")
            notes_manager.save_notes(filename)
            print("Заметки сохранены.")
        elif choice == "5":
            filename = input("Введите имя файла для загрузки заметок: ")
            notes_manager.load_notes(filename)
            print("Заметки загружены.")
        elif choice == "0":
            break
        else:
            print("Недопустимый выбор.")

if __name__ == "__main__":
    main()