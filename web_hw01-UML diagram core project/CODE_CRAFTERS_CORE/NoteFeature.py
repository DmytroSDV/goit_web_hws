from CODE_CRAFTERS_CORE.RecordData import bcolors
from collections import UserDict
from tabulate import tabulate
from emoji import emojize
import pickle


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class AuthorName(Field):
    def __init__(self, value):
        super().__init__(value)
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val: str):
        if val and val[0].isalpha:
            self._value = val
        else:
            raise ValueError(
               bcolors.FAIL + "❌ Invalid note format❗ Must be not empty and started with the letter❗ 😞" + bcolors.RESET
            )

class Note(Field):
    def __init__(self, value):
        super().__init__(value)
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val: str):
        if val:
            self._value = val
        else:
            raise ValueError(bcolors.FAIL + "❌ Invalid note format! Must be not empty❗ 😞" + bcolors.RESET)

class Tag(Field):
    def __init__(self, value):
        super().__init__(value)
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val: str):
        if val:
            self._value = val
        else:
            raise ValueError(bcolors.FAIL + "❌ Invalid note format! Must be not empty❗ 😞" + bcolors.RESET)

class NoteRec:
    def __init__(self, name):
        self.name = AuthorName(name)
        self.tags = []
        self.note = ""

    def add_tag(self, tag):
        if str(Tag(tag)):
            self.tags.append(Tag(tag))

    def remove_tag(self, del_tag):
        for tag in self.tags:
            if tag.value == del_tag:
                self.tags.remove(tag)

    def edit_tag(self, exist_tag, new_tag):
        check_flag = False
        for ind, tag in enumerate(self.tags):
            if tag.value == exist_tag:
                self.tags[ind] = Tag(new_tag)
                check_flag = True
        if not check_flag:
            raise ValueError(bcolors.FAIL + "❌ Such tag is missed in the list❗ 😞" + bcolors.RESET)

    def add_note(self, note):
        if Note(note):
            self.note = Note(note)

    def edit_note(self, new_note):
        self.note = Note(new_note)

def responce_visualization(func):
    def inner(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        if isinstance(result, dict):
            print(f" {bcolors.BOLD}😊 All notes in the notebook!📝 {bcolors.RESET}")
            table = []
            headers = [
                emojize(":id: Author", language="alias"),
                emojize(":bust_in_silhouette: Tags", language="alias"),
                emojize(":notebook: Note", language="alias"),
            ]
            for note_name in result.values():

                table.append([
                    emojize(f"🎅 '{note_name.name.value}'"
                            , language="alias"),
                    emojize(
                        f"🔥 [{' | '.join(tag.value for tag in note_name.tags)}]", language="alias"),
                    emojize(f"💼 '{note_name.note}'", language="alias"),
                ])
            print(bcolors.B + tabulate(table, headers=headers,
                                        tablefmt='pretty') + bcolors.RESET)
    return inner
    
class NoteBook(UserDict):
        
    def note_save_to_file(self, file_path: str, data):
        with open(file_path, "wb") as file:
            pickle.dump(data, file)
            print(f"{bcolors.GREEN}💾 Notes added to:{bcolors.RESET} 📂 {bcolors.UNDERLINE}{file_path}{bcolors.RESET}✅")
            
    def note_read_from_file(self, file_path: str):
        with open(file_path, "rb") as file:
            print(f"{bcolors.GREEN}📖 Reading notes from:{bcolors.RESET} 📂 {bcolors.UNDERLINE}{file_path}{bcolors.RESET}✅")
            return pickle.load(file)
