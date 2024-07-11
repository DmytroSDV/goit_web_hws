from CODE_CRAFTERS_CORE.AddressBook import *
from CODE_CRAFTERS_CORE.NoteFeature import *
from CODE_CRAFTERS_CORE.FileSorting import *
from abc import ABC, abstractmethod


class ListOfCommands():
    COMMAND_LIST_EN = [
            bcolors.ORANGE + "cli" + bcolors.RESET,
            bcolors.ORANGE + "change-language" + bcolors.RESET,
            bcolors.ORANGE + "contact-add" + bcolors.RESET,
            bcolors.ORANGE + "contact-find" + bcolors.RESET,
            bcolors.ORANGE + "contact-show-all" + bcolors.RESET,
            bcolors.ORANGE + "contact-phone-add" + bcolors.RESET,
            bcolors.ORANGE + "contact-phone-remove" + bcolors.RESET,
            bcolors.ORANGE + "contact-email-add" + bcolors.RESET,
            bcolors.ORANGE + "contact-email-remove" + bcolors.RESET,
            bcolors.ORANGE + "contact-phone-edit" + bcolors.RESET,
            bcolors.ORANGE + "contact-email-edit" + bcolors.RESET,
            bcolors.ORANGE + "contact-birthday-edit" + bcolors.RESET,
            bcolors.ORANGE + "contact-remove" + bcolors.RESET,
            bcolors.ORANGE + "display-birthdays" + bcolors.RESET,
            bcolors.ORANGE + "note-add" + bcolors.RESET,
            bcolors.ORANGE + "note-find" + bcolors.RESET,
            bcolors.ORANGE + "note-show-all" + bcolors.RESET,
            bcolors.ORANGE + "note-edit" + bcolors.RESET,
            bcolors.ORANGE + "note-remove" + bcolors.RESET,
            bcolors.ORANGE + "tag-add" + bcolors.RESET,
            bcolors.ORANGE + "tag-edit" + bcolors.RESET,
            bcolors.ORANGE + "tag-remove" + bcolors.RESET,
            bcolors.ORANGE + "tag-find-sort" + bcolors.RESET,
            bcolors.ORANGE + "file-sort" + bcolors.RESET,
            bcolors.ORANGE + "file-extension-show" + bcolors.RESET,
            bcolors.ORANGE + "file-extension-add" + bcolors.RESET,
            bcolors.ORANGE + "file-extension-remove" + bcolors.RESET,
            bcolors.ORANGE + "quit" + bcolors.RESET,
            bcolors.ORANGE + "exit" + bcolors.RESET,
            bcolors.ORANGE + "q" + bcolors.RESET,
        ]
    COMMANDS_EXPLAIN_EN = [
            bcolors.BLUE + "виводить список всіх доступних команд" + bcolors.RESET,
            bcolors.BLUE + "змінити мову додатка" + bcolors.RESET,
            bcolors.BLUE + "зберігає контакт з іменем, адресом, номером телефона, email та днем народження до книги контактів" + bcolors.RESET,
            bcolors.BLUE + "здійснює пошук контакту серед контактів книги" + bcolors.RESET,
            bcolors.BLUE + "показує всі існуючі контакти в книзі контактів" + bcolors.RESET,
            bcolors.BLUE + "додати іще 1-ин phone до існуючого контакту" + bcolors.RESET,
            bcolors.BLUE + "видалення існуючого phone" + bcolors.RESET,
            bcolors.BLUE + "додати іще 1-ин email до існуючого контакту" + bcolors.RESET,
            bcolors.BLUE + "видалення існуючого email" + bcolors.RESET,
            bcolors.BLUE + "редагування phone існуючого контакту" + bcolors.RESET,
            bcolors.BLUE + "редагування email існуючого контакту" + bcolors.RESET,
            bcolors.BLUE + "редагування birthday існуючого контакту" + bcolors.RESET,
            bcolors.BLUE + "видалення існуючого контакту" + bcolors.RESET,
            bcolors.BLUE + "виводить список контактів, у яких день народження через задану кількість днів від поточної дати" + bcolors.RESET,
            bcolors.BLUE + "зберігає нотатку за іменем автора" + bcolors.RESET,
            bcolors.BLUE + "здійснює пошук нотатки серед існуючих нотатків" + bcolors.RESET,
            bcolors.BLUE + "показує всі існуючі нотатки" + bcolors.RESET,
            bcolors.BLUE + "редагування існуючої нотатки" + bcolors.RESET,
            bcolors.BLUE + "видалення існуючої нотатки" + bcolors.RESET,
            bcolors.BLUE + "додавання тегів до існуючої нотатки" + bcolors.RESET,
            bcolors.BLUE + "редагування тегів існуючої нотатки" + bcolors.RESET,
            bcolors.BLUE + "видалення тегів з існуючої нотатки" + bcolors.RESET,
            bcolors.BLUE + "пошук та сортування нотаток за тегами" + bcolors.RESET,
            bcolors.BLUE + "сортування файлів у зазначеній папці за категоріями (зображення, документи, відео та ін.)." + bcolors.RESET,
            bcolors.BLUE + "показати всі розширення" + bcolors.RESET,
            bcolors.BLUE + "додавання додатково розширення для сортування" + bcolors.RESET,
            bcolors.BLUE + "видалення розширення із списку для сортування" + bcolors.RESET,
            bcolors.BLUE + "вихід з програми" + bcolors.RESET,
            bcolors.BLUE + "вихід з програми" + bcolors.RESET,
            bcolors.BLUE + "вихід з програми" + bcolors.RESET,
        ]
    COMMAND_LIST_RU = [
            bcolors.ORANGE + "команды" + bcolors.RESET,
            bcolors.ORANGE + "изменить язык" + bcolors.RESET,
            bcolors.ORANGE + "добавление контакта" + bcolors.RESET,
            bcolors.ORANGE + "поиск контакта" + bcolors.RESET,
            bcolors.ORANGE + "показать все контакты" + bcolors.RESET,
            bcolors.ORANGE + "добавить телефон" + bcolors.RESET,
            bcolors.ORANGE + "удалить телефон" + bcolors.RESET,
            bcolors.ORANGE + "добавить электронную почту" + bcolors.RESET,
            bcolors.ORANGE + "удалить электронную почту" + bcolors.RESET,
            bcolors.ORANGE + "редактировать телефон" + bcolors.RESET,
            bcolors.ORANGE + "редактировать электронную почту" + bcolors.RESET,
            bcolors.ORANGE + "редактировать день рождения" + bcolors.RESET,
            bcolors.ORANGE + "удалить контакт" + bcolors.RESET,
            bcolors.ORANGE + "показать дни рождения" + bcolors.RESET,
            bcolors.ORANGE + "добавить заметку" + bcolors.RESET,
            bcolors.ORANGE + "найти заметку" + bcolors.RESET,
            bcolors.ORANGE + "показать все заметки" + bcolors.RESET,
            bcolors.ORANGE + "редактировать заметку" + bcolors.RESET,
            bcolors.ORANGE + "удалить заметку" + bcolors.RESET,
            bcolors.ORANGE + "добавить тег" + bcolors.RESET,
            bcolors.ORANGE + "редактировать тег" + bcolors.RESET,
            bcolors.ORANGE + "удалить тег" + bcolors.RESET,
            bcolors.ORANGE + "найти и отсортировать по тегам" + bcolors.RESET,
            bcolors.ORANGE + "сортировать файлы" + bcolors.RESET,
            bcolors.ORANGE + "показать все разширения" + bcolors.RESET,
            bcolors.ORANGE + "добавить расширение" + bcolors.RESET,
            bcolors.ORANGE + "удалить расширение" + bcolors.RESET,
            bcolors.ORANGE + "выход" + bcolors.RESET,
        ]
    COMMANDS_EXPLAIN_RU = [
            bcolors.BLUE + "выводит все доступные команды" + bcolors.RESET,
            bcolors.BLUE + "изменение языка приложения" + bcolors.RESET,
            bcolors.BLUE + "сохраняет контакт с именем, адресом, номером телефона, электронной почтой и днем рождения в контактную книгу" + bcolors.RESET,
            bcolors.BLUE + "ищет контакт между контактами книги" + bcolors.RESET,
            bcolors.BLUE + "показывает все существующие контакты в контактной книге" + bcolors.RESET,
            bcolors.BLUE + "добавить еще 1-ин телефон к существующему контакту" + bcolors.RESET,
            bcolors.BLUE + "удаление существующего телефона" + bcolors.RESET,
            bcolors.BLUE + "добавить еще 1-ин email к существующему контакту" + bcolors.RESET,
            bcolors.BLUE + "удалять существующее письмо" + bcolors.RESET,
            bcolors.BLUE + "редактировать телефон действующего контактного лица" + bcolors.RESET,
            bcolors.BLUE + "редактирование электронной почты существующего контакта" + bcolors.RESET,
            bcolors.BLUE + "редактирование дня рождения существующего контакта" + bcolors.RESET,
            bcolors.BLUE + "удалять существующий контакт" + bcolors.RESET,
            bcolors.BLUE + "отображает список контактов, имеющих день рождения после указанного числа дней с текущей даты" + bcolors.RESET,
            bcolors.BLUE + "сохраняет примечание по имени автора" + bcolors.RESET,
            bcolors.BLUE + "поиск примечаний среди существующих примечаний" + bcolors.RESET,
            bcolors.BLUE + "показывает все существующие примечания" + bcolors.RESET,
            bcolors.BLUE + "редактирование существующей записки" + bcolors.RESET,
            bcolors.BLUE + "удаление существующего примечания" + bcolors.RESET,
            bcolors.BLUE + "добавление тегов в существующее примечание" + bcolors.RESET,
            bcolors.BLUE + "редактирование тегов для существующей заметки" + bcolors.RESET,
            bcolors.BLUE + "удаление тегов из существующей записи" + bcolors.RESET,
            bcolors.BLUE + "поиск и сортировка заметок по тегам" + bcolors.RESET,
            bcolors.BLUE + "Сортировать файлы в указанной папке по категориям (изображения, документы, видео и т.д.)." + bcolors.RESET,
            bcolors.BLUE + "показать все доступные расширения для сортировки." + bcolors.RESET,
            bcolors.BLUE + "добавление дополнительного расширения для сортировки" + bcolors.RESET,
            bcolors.BLUE + "удаление расширения из списка для сортировки" + bcolors.RESET,
            bcolors.BLUE + "виход" + bcolors.RESET,
        ]
    COMMAND_LIST_UA = [
            bcolors.ORANGE + "можливості" + bcolors.RESET,
            bcolors.ORANGE + "зміти мову" + bcolors.RESET,
            bcolors.ORANGE + "додати контакт" + bcolors.RESET,
            bcolors.ORANGE + "пошук контакта" + bcolors.RESET,
            bcolors.ORANGE + "показати всі контакти" + bcolors.RESET,
            bcolors.ORANGE + "додати телефон" + bcolors.RESET,
            bcolors.ORANGE + "видалити телефон" + bcolors.RESET,
            bcolors.ORANGE + "додати електронну пошту" + bcolors.RESET,
            bcolors.ORANGE + "видалити електронну пошту" + bcolors.RESET,
            bcolors.ORANGE + "редагувати телефон" + bcolors.RESET,
            bcolors.ORANGE + "редагувати електронну пошту" + bcolors.RESET,
            bcolors.ORANGE + "редагувати день народження" + bcolors.RESET,
            bcolors.ORANGE + "видалити контакт" + bcolors.RESET,
            bcolors.ORANGE + "показати дні народження" + bcolors.RESET,
            bcolors.ORANGE + "додати нотатку" + bcolors.RESET,
            bcolors.ORANGE + "знайти нотатку" + bcolors.RESET,
            bcolors.ORANGE + "показати всі нотатки" + bcolors.RESET,
            bcolors.ORANGE + "редагувати нотатку" + bcolors.RESET,
            bcolors.ORANGE + "видалити нотатку" + bcolors.RESET,
            bcolors.ORANGE + "додати тег" + bcolors.RESET,
            bcolors.ORANGE + "редагувати тег" + bcolors.RESET,
            bcolors.ORANGE + "видалити тег" + bcolors.RESET,
            bcolors.ORANGE + "знайти та сортувати по тегам" + bcolors.RESET,
            bcolors.ORANGE + "відсортувати файли" + bcolors.RESET,
            bcolors.ORANGE + "показати всі розширення" + bcolors.RESET,
            bcolors.ORANGE + "додати розширення файла" + bcolors.RESET,
            bcolors.ORANGE + "видалити розширення файла" + bcolors.RESET,
            bcolors.ORANGE + "до зустрічі" + bcolors.RESET,
        ]
    COMMANDS_EXPLAIN_UA = [
            bcolors.BLUE + "виводить список всіх доступних команд" + bcolors.RESET,
            bcolors.BLUE + "змінити мову додатка" + bcolors.RESET,
            bcolors.BLUE + "зберігає контакт з іменем, адресом, номером телефона, email та днем народження до книги контактів" + bcolors.RESET,
            bcolors.BLUE + "здійснює пошук контакту серед контактів книги" + bcolors.RESET,
            bcolors.BLUE + "показує всі існуючі контакти в книзі контактів" + bcolors.RESET,
            bcolors.BLUE + "додати іще 1-ин phone до існуючого контакту" + bcolors.RESET,
            bcolors.BLUE + "видалення існуючого phone" + bcolors.RESET,
            bcolors.BLUE + "додати іще 1-ин email до існуючого контакту" + bcolors.RESET,
            bcolors.BLUE + "видалення існуючого email" + bcolors.RESET,
            bcolors.BLUE + "редагування phone існуючого контакту" + bcolors.RESET,
            bcolors.BLUE + "редагування email існуючого контакту" + bcolors.RESET,
            bcolors.BLUE + "редагування birthday існуючого контакту" + bcolors.RESET,
            bcolors.BLUE + "видалення існуючого контакту" + bcolors.RESET,
            bcolors.BLUE + "виводить список контактів, у яких день народження через задану кількість днів від поточної дати" + bcolors.RESET,
            bcolors.BLUE + "зберігає нотатку за іменем автора" + bcolors.RESET,
            bcolors.BLUE + "здійснює пошук нотатки серед існуючих нотатків" + bcolors.RESET,
            bcolors.BLUE + "показує всі існуючі нотатки" + bcolors.RESET,
            bcolors.BLUE + "редагування існуючої нотатки" + bcolors.RESET,
            bcolors.BLUE + "видалення існуючої нотатки" + bcolors.RESET,
            bcolors.BLUE + "додавання тегів до існуючої нотатки" + bcolors.RESET,
            bcolors.BLUE + "редагування тегів існуючої нотатки" + bcolors.RESET,
            bcolors.BLUE + "видалення тегів з існуючої нотатки" + bcolors.RESET,
            bcolors.BLUE + "пошук та сортування нотаток за тегами" + bcolors.RESET,
            bcolors.BLUE + "сортування файлів у зазначеній папці за категоріями (зображення, документи, відео та ін.)." + bcolors.RESET,
            bcolors.BLUE + "показати всі наявні розширеннядля сортування" + bcolors.RESET,
            bcolors.BLUE + "додавання додатково розширення для сортування" + bcolors.RESET,
            bcolors.BLUE + "видалення розширення із списку для сортування" + bcolors.RESET,
            bcolors.BLUE + "бот іде відпочивати" + bcolors.RESET,
    ]

class BotCommands(ABC):
    @abstractmethod
    def __init__(self, data: AddressBook = None):
        pass
    
    @abstractmethod
    def command_run(self):
        pass

class ShowAllContacts(BotCommands):
    def __init__(self, data: AddressBook = None):
        self.data = data
        self.command_run()
        
    def command_run(self):    
        if not self.data:
            print(f"{bcolors.WARNING}📋 Addressbook is empty😞 {bcolors.RESET}")
            print(f"{bcolors.GREEN}🤗 But, you can add a contact if you want ✏️ {bcolors.RESET}")
            return
        else:
            print(f"{bcolors.GREEN}📖 All contacts in book:🚀 {bcolors.RESET}")
            table = []
            for contact in self.data:
                phone_numbers = ", ".join(
                    str(phone) for phone in contact.get("phone", [])
                )
                emails = ", ".join(str(email) for email in contact.get("email", []))
                table.append(
                    [
                        str(contact["id"]),
                        str(contact["name"]),
                        phone_numbers,
                        str(contact.get("birthday", "")),
                        emails,
                    ]
                )
            headers = [
                emojize(f":id: {bcolors.BLUE}ID{bcolors.RESET}", language="alias"),
                emojize(f":bust_in_silhouette: {bcolors.BLUE}Name{bcolors.RESET}", language="alias"),
                emojize(f":telephone_receiver: {bcolors.BLUE}Phone{bcolors.RESET}", language="alias"),
                emojize(f":birthday_cake: {bcolors.BLUE}Birthday{bcolors.RESET}", language="alias"),
                emojize(f":e-mail: {bcolors.BLUE}Email{bcolors.RESET}", language="alias"),
            ]
            print(tabulate(table, headers=headers, tablefmt='pretty'))
 
class AddContact(BotCommands):
    def __init__(self, data: AddressBook = None):
        self.data = data
        self.command_run()

    def command_run(self):
        attempts = 0
        flag_name = False
        flag_phone = False
        flag_birthday = False
        flag_email = False

        while attempts < 3:
            try:
                while not flag_name:
                    print(f"{bcolors.ORANGE}📝 Please enter your name that contains more than two characters:✍️  {bcolors.RESET}")
                    name = input(f"{bcolors.BOLD}📝 Please enter your name:✍️  {bcolors.RESET}")

                    record = Record(name)
                    for contact in self.data:
                        if contact["name"].name == name:
                            print(f"{bcolors.WARNING}❌ Contact with this name already exists, try to enter another name!😞 {bcolors.RESET}")
                            print(f"{bcolors.WARNING}📝 Please enter the name again or command ['q', 'back', 'exit', 'quit'] for exit menu:✍️  {bcolors.RESET}")
                            if name in ['q', 'back', 'exit', 'quit']:
                                return 
                            break
                    else:
                        flag_name = True

                if not flag_phone:
                    while True:
                        print(f"{bcolors.ORANGE}📞 Exsamples of the input: (+380) or (380) or (10 digits)✅ {bcolors.RESET}")
                        phone = input(f"{bcolors.BOLD}📞 Please enter phone:✍️  {bcolors.RESET}")
                        if phone in ['q', 'back', 'exit', 'quit']:
                            return
                        try:
                            record.add_phone(phone)
                            flag_phone = True
                            break
                        except ValueError as error:
                            print(f"{bcolors.FAIL}❌ Error❗ - {error}{bcolors.RESET}")
                            print(f"{bcolors.WARNING}📞 Please enter the phone number again or command ['q', 'back', 'exit', 'quit'] for exit menu:✍️ {bcolors.RESET}")

                if not flag_birthday:
                    while True:
                        print(f"{bcolors.ORANGE}🎂 Please enter birthday in format (YYYY-MM-DD):✍️  {bcolors.RESET}")
                        birthday = input(f"{bcolors.BOLD}🎂 Please enter birthday:✍️  {bcolors.RESET}")
                        if birthday in ['q', 'back', 'exit', 'quit']:
                            return
                        if birthday:
                            try:
                                record.birthday = Birthday(birthday)
                                flag_birthday = True
                                break
                            except ValueError as error:
                                print(f"{bcolors.FAIL}❌ Error❗ - {bcolors.RESET}{error}")
                                print(f"{bcolors.WARNING}🎂 Please enter the birthday again or command ['q', 'back', 'exit', 'quit'] for exit menu:✍️  {bcolors.RESET}")

                if not flag_email:
                    while True:
                        print(f"{bcolors.ORANGE}📧 Please enter email in format (example@example.com):✍️  {bcolors.RESET}")
                        email = input(f"{bcolors.BOLD}📧 Please enter email:✍️  {bcolors.RESET}")
                        if email in ['q', 'back', 'exit', 'quit']:
                            return
                        try:
                            record.add_email(email)
                            flag_email = True
                            break
                        except ValueError as error:
                            print(f"{bcolors.FAIL}❌ Error❗ - {bcolors.RESET}{error}")
                            print(f"{bcolors.WARNING}📧 Please enter the email again or command ['q', 'back', 'exit', 'quit'] for exit menu:✍️ {bcolors.RESET}")

                contacts = {
                    "id": self.data.generate_id(),
                    "name": record.name,
                    "phone": record.phones,
                    "birthday": record.birthday,
                    "email": [str(email) for email in record.email],
                }
                self.data.append(contacts)
                print(f"{bcolors.GREEN}👤 Contact added successfully!✅{bcolors.RESET}")
                break
            except Exception as e:
                attempts += 1
                print(f"{bcolors.FAIL}Error❗ - {bcolors.RESET}{e}")
                print(f"{bcolors.WARNING}🔄 Please enter the information again!🔄 {bcolors.RESET}")


                flag_name = False
                flag_phone = False
                flag_birthday = False
                flag_email = False      

class ShowContactInfo(BotCommands):
    def __init__(self, data: AddressBook = None):
        self.data = data
        self.command_run()
    
    def command_run(self):
        name = input(f"{bcolors.BOLD}🔍 Please enter the name of the contact you want to find:✍️  {bcolors.RESET}")
        matching_contacts = [contact for contact in self.data if contact["name"].name.lower() == name.lower()]

        if not matching_contacts:
            print(f"{bcolors.WARNING}😞 No contacts found with the name 👤 '{name}'{bcolors.RESET}")
            print(emojize(f"{bcolors.WARNING}😞 Contact with name '{name}' does not found❌ {bcolors.RESET}"))
            print(f"{bcolors.GREEN}🤗 But, you can add a contact if you want ✏️ {bcolors.RESET}")
            return

        print(f"{bcolors.GREEN}🔍 Search results for '{name}':🚀  {bcolors.RESET}")
        print(f"{bcolors.GREEN}🎉 Find contact with name🤗  {name}{bcolors.RESET}")
        table = []
        for contact in matching_contacts:
            phone_numbers = ", ".join(str(phone) for phone in contact.get("phone", []))
            emails = ", ".join(str(email) for email in contact.get("email", []))
            table.append([
                str(contact["id"]),
                str(contact["name"]),
                phone_numbers,
                str(contact.get("birthday", "")),
                emails,
            ])

        headers = [
            emojize(f":id: {bcolors.BLUE}ID{bcolors.RESET}", language="alias"),
            emojize(f":bust_in_silhouette: {bcolors.BLUE}Name{bcolors.RESET}", language="alias"),
            emojize(f":telephone_receiver: {bcolors.BLUE}Phone{bcolors.RESET}", language="alias"),
            emojize(f":birthday_cake: {bcolors.BLUE}Birthday{bcolors.RESET}", language="alias"),
            emojize(f":e-mail: {bcolors.BLUE}Email{bcolors.RESET}", language="alias"),
        ]

        print(tabulate(table, headers=headers, tablefmt='pretty'))

class RemovePhone(BotCommands):
    def __init__(self, data: AddressBook = None):
        self.data = data
        self.command_run()
        
    def command_run(self):
        name = input(f"{bcolors.BOLD}🔍 Please enter name:✍️  {bcolors.RESET}")
        error_flag = False
        for contacts in self.data:
            if str(contacts["name"]) == name:
                error_flag = True
                phone_numbers = ", ".join(
                    str(phone) for phone in contacts.get("phone", [])
                )
                print(f"{bcolors.WARNING}Select the phone you want to delete{bcolors.RESET}")
                print(f"{bcolors.BLUE}{phone_numbers}{bcolors.WARNING}")
                phone_to_remove = input(f"{bcolors.BOLD}🔍 Please enter the phone number to remove:✍️  {bcolors.RESET}")
                phone_object_to_remove = None

                for phone_object in contacts["phone"]:
                    if str(phone_object) == phone_to_remove:
                        phone_object_to_remove = phone_object
                        break

                if phone_object_to_remove is not None:
                    contacts["phone"].remove(phone_object_to_remove)
                    print(f"{bcolors.GREEN}📞 The phone number '{name}' was successfully deleted!✅{bcolors.RESET}")
                else:
                    print(f"{bcolors.FAIL}📞 Phone number '{phone_to_remove}' not found❌ {bcolors.RESET}")
        if not error_flag:
            print(f"{bcolors.FAIL}👤 Contact '{name}' isn't here!❌ {bcolors.RESET}")

class RemoveContact(BotCommands):
    def __init__(self, data: AddressBook = None):
        self.data = data
        self.command_run()
    
    def command_run(self):
        name = input(f"{bcolors.BOLD }📝 Please enter name:✍️  {bcolors.RESET}")
        contacts=[]
        for contact in self.data:
            if str(contact["name"]) == name:
                contacts.append(contact)
                self.data.remove(contact)
        if contacts:
            for i in contacts:
                print(f"{bcolors.GREEN}👤 Contact '{i['name'].name}' was deleted!✅{bcolors.RESET}")
        else:
            print(f"{bcolors.FAIL}🔍 Contact '{name}' is not found! 😞{bcolors.RESET}")
            
class AddEmail(BotCommands):
    def __init__(self, data: AddressBook = None):
        self.data = data
        self.command_run()
    
    def command_run(self):
        user_input = input(f"{bcolors.BOLD}🔍 Please enter name:✍️  {bcolors.RESET}")
        error_flag = False
        for contact in self.data:
            if str(contact["name"]) == user_input:
                error_flag = True
                email = input(f"{bcolors.BOLD}📧 Please enter email:✍️  {bcolors.RESET}")
                contact["email"].append(email)
                print(f"{bcolors.GREEN}📧 Email '{email}' Successfully added!✅{bcolors.RESET}")
                
        if not error_flag:
            print(f"{bcolors.FAIL}👤 Contact isn't here!😞{bcolors.RESET}")

class EditEmail(BotCommands):
    def __init__(self, data: AddressBook = None):
        self.data = data
        self.command_run()
        
    def command_run(self):
        user_input = input(f"{bcolors.BOLD}🔍 Please enter name:✍️  {bcolors.RESET}")
        error_flag = False
        for contact in self.data:
            if str(contact["name"]) == user_input:
                error_flag = True
                email_list = ", ".join(
                    str(email) for email in contact.get("email", [])
                )
                print(f"{bcolors.WARNING}Select the emails you want to edit{bcolors.RESET}")
                print(f"{bcolors.BLUE}{email_list}{bcolors.WARNING}")
                edit_to_email = input(f"{bcolors.BOLD}🔍 Enter the email to edit: {bcolors.RESET}")
                new_email = input(f"{bcolors.BOLD}📧 Enter new email:✍️  {bcolors.RESET}")
                email_object_to_edit = None
                
                for i, email_object in enumerate(contact["email"]):
                    if str(email_object) == edit_to_email:
                        email_object_to_edit = email_object
                        break
                
                if email_object_to_edit is not None:
                    print(f"{bcolors.BOLD}📧 Old email: '{email_object_to_edit}{bcolors.RESET}'")
                    print(f"{bcolors.GREEN}📧 Email successfully changed to '{new_email}'✅{bcolors.RESET}")
                                 
                    contact["email"].remove(email_object_to_edit)            
                    contact["email"].append(new_email)
                    
                    print(f"{bcolors.GREEN}📧 Email edited '{edit_to_email}' successfully!✅{bcolors.RESET}")
                else:
                    print(f"{bcolors.FAIL}❌ Error editing email '{edit_to_email}': email not found!❌{bcolors.RESET}")
        if not error_flag:
            print(f"{bcolors.FAIL}❌ Contact '{user_input}' isn't here!😞{bcolors.RESET}")

class RemoveEmail(BotCommands):
    def __init__(self, data: AddressBook = None):
        self.data = data
        self.command_run()
        
    def command_run(self):
        user_input = input(f"{bcolors.BOLD}🔍 Please enter name:✍️  {bcolors.RESET}")
        error_flag = False
        for contact in self.data:
            if str(contact["name"]) == user_input:
                error_flag = True
                email_list = ", ".join(
                    str(email) for email in contact.get("email", [])
                )
                print(f"{bcolors.WARNING}Select the emails you want to delete{bcolors.RESET}")
                print(f"{bcolors.BLUE}{email_list}{bcolors.WARNING}")
                email_to_remove = input(f"{bcolors.BOLD}🔍 Please enter the email to remove:✍️  {bcolors.RESET}")
                email_object_to_remove = None
                
                for email_object in contact["email"]:
                    if str(email_object) == email_to_remove:
                        email_object_to_remove = email_object
                        break

                if email_object_to_remove is not None:
                    contact["email"].remove(email_object_to_remove)
                    print(f"{bcolors.GREEN}📧 Email '{email_to_remove}' successfully delete!✅{bcolors.RESET}")
                else:
                    print(f"{bcolors.FAIL}❌ Email '{email_to_remove}' not found.😞{bcolors.RESET}")
        if not error_flag:
            print(f"{bcolors.FAIL}❌ Contact '{user_input}' isn't here!😞{bcolors.RESET}")
            
class AddPhone(BotCommands):
    def __init__(self, data: AddressBook = None):
        self.data = data
        self.command_run()
        
    def command_run(self):
        user_input = input(f"{bcolors.BOLD}🔍 Please enter name:✍️  {bcolors.RESET}")
        error_flag = False
        for contact in self.data:
            if str(contact["name"]) == user_input:
                error_flag = True
                phone = input(f"{bcolors.BOLD}🔍 Please enter phone📞: {bcolors.RESET}")
                contact["phone"].append(phone)
                print(f"{bcolors.GREEN}📞 Phone number '{phone}' successfully added!✅{bcolors.RESET}")
        if not error_flag:
            print(f"{bcolors.FAIL}❌ Contact '{user_input}' isn't here!😞{bcolors.RESET}")

class EditPhone(BotCommands):
    def __init__(self, data: AddressBook = None):
        self.data = data
        self.command_run()
        
    def command_run(self):
        user_input = input(f"{bcolors.BOLD}🔍 Please enter name:✍️  {bcolors.RESET}")
        error_flag = False 
        for contact in self.data:
            if str(contact["name"]) == user_input:
                error_flag = True
                phone_numbers = ", ".join(
                    str(phone) for phone in contact.get("phone", [])
                )
                print(f"{bcolors.WARNING}Select the phone you want to edit{bcolors.RESET}")
                print(f"{bcolors.BLUE}{phone_numbers}{bcolors.WARNING}")
                edit_to_phone_number = input(f"{bcolors.BOLD}📞 Enter the phone number to edit:✍️  {bcolors.RESET}")
                new_phone_number = input(f"{bcolors.BOLD}📞 Enter the new phone number:✍️  {bcolors.RESET}")
                phone_number_object_to_edit = None
                
                for i, phone_number_object in enumerate(contact["phone"]):
                    if str(phone_number_object) == edit_to_phone_number:
                        phone_number_object_to_edit = phone_number_object
                        break
                
                if phone_number_object_to_edit is not None:
                    print(f"{bcolors.WARNING}📞 Old phone number: '{phone_number_object_to_edit}'{bcolors.RESET}")
                    print(f"{bcolors.GREEN}📞 Successfully changed to '{new_phone_number}'✅{bcolors.RESET}")                                 
                    contact["phone"].remove(phone_number_object_to_edit)            
                    contact["phone"].append(new_phone_number)
                    print(f"{bcolors.GREEN}📞 Phone number '{new_phone_number}' edited successfully!✅{bcolors.RESET}")
                else:
                    print(f"{bcolors.FAIL}📞 Error editing phone number '{new_phone_number}': Phone Number not found❌{bcolors.RESET}")
                    
        if not error_flag:
            print(f"{bcolors.FAIL}❌ There are no contacts with such name '{user_input}'!{bcolors.RESET}")

class EditBirthday(BotCommands):
    def __init__(self, data: AddressBook = None):
        self.data = data
        self.command_run()
        
    def command_run(self):  # редагування birthday існуючого контакту
        name = input(f'{bcolors.BOLD}🔍 Enter name of contact:✍️  {bcolors.RESET}')
        error_flag = False
        for contact in self.data:
            if contact['name'].name == name and contact['birthday']:
                new_birthday = input('Enter new birthday: ')
                try:
                    contact['birthday'] = Birthday(new_birthday)
                    print(f'{bcolors.GREEN}🎂 Birthday "{new_birthday}" was changed!✅{bcolors.RESET}')
                except ValueError as ex:
                    print(ex)
                error_flag = True
                
        if not error_flag:
            print(f"{bcolors.FAIL}❌ There are no contacts with such name '{name}'!{bcolors.RESET}")
                              
class ShowContactsBirthdays(BotCommands):
    def __init__(self, data: AddressBook = None):
        self.data = data
        self.command_run()
        
    def command_run(self):
        while 1:
            try:
                days = int(input(f"{bcolors.BOLD}🤗 Enter days:✍️  {bcolors.RESET}"))
                break
            except Exception as e:
                print(f"{bcolors.WARNING}Enter the number of days by number and not string!{bcolors.RESET}")
                continue
            
        contacts = []

        for contact in self.data:
            if 'birthday' in contact and contact['birthday']:
                birthday_date = contact['birthday'].value
                record = Record(contact['name'].name, birthday=birthday_date)
                if record.days_to_date(days, birthday_date):
                    contacts.append(contact)

        if contacts:
            for uzer in contacts:
                print(f'{bcolors.GREEN}Name: {uzer["name"].name}, Birthday:🎂  {uzer["birthday"].value}{bcolors.RESET}')
        else:
            print(f'{bcolors.WARNING}🎂 There are no birthdays in this number of day!{bcolors.RESET}')

class AddNote(BotCommands):
    def __init__(self, data: NoteBook = None):
        self.data = data
        self.command_run()
    
    def command_run(self):
        tries = 2
        one_flag=False
        two_flag=False
        three_flag=False
        while True:
            try:
                if not one_flag:
                    while True:
                        note_name = input(f"{bcolors.BOLD}📝 Please enter Author name:✍️  {bcolors.RESET}")
                        if note_name in ['q', 'back', 'exit', 'quit']:
                            return
                        try:
                            note_rec = NoteRec(note_name)
                            one_flag=True
                            break
                        except ValueError as error:
                            print(f"{bcolors.FAIL}❌ Error❗ - {bcolors.RESET}{error}")
                            print(f"{bcolors.WARNING}📝 Please enter Author name again or command ['q', 'back', 'exit', quit] for exit menu:✍️  {bcolors.RESET}")
                    if not two_flag:
                        while True:
                            note_data = input(f"{bcolors.BOLD}📝 Please type your note:✍️  {bcolors.RESET}")
                            if note_data in ['q', 'back', 'exit', 'quit']:
                                return
                            try:
                                note_rec.add_note(note_data)
                                two_flag=True
                                break
                            except ValueError as error:
                                print(f"{bcolors.FAIL}❌ Error❗ - {bcolors.RESET}{error}")
                                print(f"{bcolors.WARNING}📝 Please type your note again or command ['q', 'back', 'exit', quit] for exit menu:✍️  {bcolors.RESET}")
                    if not three_flag:
                        while True:
                            tag_data = input(f"{bcolors.BOLD}📝 Please enter applicable tag:✍️  {bcolors.RESET}")
                            if tag_data in ['q', 'back', 'exit', 'quit']:
                                return
                            try:
                                note_rec.add_tag(tag_data)

                                three_flag=True
                                break
                            except ValueError as error:
                                print(f"{bcolors.FAIL}❌ Error❗ - {bcolors.RESET}{error}")
                                print(f"{bcolors.WARNING}📝 Please enter applicable tag again or command ['q', 'back', 'exit', quit] for exit menu:✍️  {bcolors.RESET}")

                self.data[note_rec.name.value] = note_rec
                print(f"{bcolors.GREEN}📋 New note successfully added!✅{bcolors.RESET}")
                break
            except Exception as ex:
                message = (
                    f"\n{bcolors.FAIL}❌ Exeption❗ - {bcolors.RESET}{ex}\n{bcolors.WARNING}🔄 You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}❌ Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue

class ShowNoteInfo(BotCommands):
    def __init__(self, data: NoteBook = None):
        self.data = data
        self.command_run()
        
    @responce_visualization
    def command_run(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input(f"{bcolors.BOLD}🔍 Please enter note name:✍️  {bcolors.RESET}")
                for key in self.data:
                    if key == note_name:
                        return {self.data[note_name].name: self.data[note_name]}
                if not note_name in self.data:
                    raise ValueError(
                        bcolors.FAIL + "❌ Such note does not exist❗ 😞" + bcolors.RESET)
                break

            except Exception as ex:
                tries -= 1
                message = (
                    f"\n{bcolors.FAIL}❌ Exeption❗ - {bcolors.RESET}{ex}\n{bcolors.WARNING}🔄 You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}❌ Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue

class ShowAllNotes(BotCommands):
    def __init__(self, data: NoteBook = None):
        self.data = data
        self.command_run()
        
    @responce_visualization
    def command_run(self):
        if self.data:
            return self.data

        if not self.data:
            print(f"{bcolors.WARNING}❌ Note list is empty❗ 😞{bcolors.RESET}")
            print(f"{bcolors.GREEN}🏷️  But, you can add a note if you want ✏️ {bcolors.RESET}")
            
class EditNote(BotCommands):
    def __init__(self, data: NoteBook = None):
        self.data = data
        self.command_run()
        
    def command_run(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input(f"{bcolors.BOLD}🔍 Please enter note name:✍️  {bcolors.RESET}")
                if not note_name in self.data:
                    raise ValueError(bcolors.FAIL + "❌ Such note does not exist❗ 😞" + bcolors.RESET)

                new_note = input(f"{bcolors.BOLD}📝 Please type new note:✍️  {bcolors.RESET}")
                for key in self.data:
                    if key == note_name:
                        self.data[note_name].edit_note(new_note)
                        print(f"{bcolors.GREEN}📋 Note successfully updated!✅{bcolors.RESET}")
                break

            except Exception as ex:
                tries -= 1
                message = (
                    f"\n{bcolors.FAIL}❌ Exeption❗ - {bcolors.RESET}{ex}\n{bcolors.WARNING}🔄 You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}❌ Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue  

class RemoveMote(BotCommands):
    def __init__(self, data: NoteBook = None):
        self.data = data
        self.command_run()
                      
    def command_run(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input(f"{bcolors.BOLD}🔍 Please enter note name:✍️  {bcolors.RESET}")
                if not note_name in self.data:
                    raise ValueError(bcolors.FAIL + "❌ Such note does not exist❗ 😞" + bcolors.RESET)

                temp_dict = self.data.copy()
                for key in temp_dict:
                    if key == note_name:
                        self.data.pop(note_name)
                        print(f"{bcolors.GREEN}📋 Note successfully deleted✅!{bcolors.RESET}")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\n{bcolors.FAIL}❌ Exeption❗ - {bcolors.RESET}{ex}\n{bcolors.WARNING}🔄 You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}❌ Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue
  
class AddTag(BotCommands):
    def __init__(self, data: NoteBook = None):
        self.data = data
        self.command_run()
        
    def command_run(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input(f"{bcolors.BOLD}🔍 Please enter note name:✍️  {bcolors.RESET}")
                if not note_name in self.data:
                    raise ValueError(bcolors.FAIL + "❌ Such note does not exist❗ 😞" + bcolors.RESET)

                additional_tag = input(f"{bcolors.BOLD}📝 Please type additional tag:✍️ {bcolors.RESET}")
                for key in self.data:
                    if key == note_name:
                        self.data[note_name].add_tag(additional_tag)
                        print(f"{bcolors.GREEN}📋 Tag successfully added✅!{bcolors.RESET}")
                break

            except Exception as ex:
                tries -= 1
                message = (
                    f"\n{bcolors.FAIL}❌ Exeption❗ - {bcolors.RED}{ex}\n{bcolors.WARNING}🔄 You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}❌ Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue  

class EditTag(BotCommands):
    def __init__(self, data: NoteBook = None):
        self.data = data
        self.command_run()
        
    def command_run(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input(f"{bcolors.BOLD}🔍 Please enter note name:✍️  {bcolors.RESET}")
                if not note_name in self.data:
                    raise ValueError(bcolors.FAIL + "❌ Such note does not exist❗ 😞" + bcolors.RESET)

                print(
                    f"{bcolors.BOLD}📝 Available tags in the note 📝 {bcolors.RESET}{note_name} - ",
                    " | ".join(tag.value for tag in self.data[note_name].tags),
                )
                old_tag = input(f"{bcolors.BOLD}📝 Please choose the tag that must be replaced:✍️  {bcolors.RESET}")

                check_tag = any(
                    tag.value == old_tag for tag in self.data[note_name].tags
                )
                if not check_tag:
                    raise ValueError(bcolors.FAIL + "❌ Such tag does not exist❗ 😞" + bcolors.RESET)

                additional_tag = input(f"{bcolors.BOLD}📝 Please type new tag:✍️  {bcolors.RESET}")
                for key in self.data:
                    if key == note_name:
                        self.data[note_name].edit_tag(old_tag, additional_tag)
                        print(f"{bcolors.GREEN}📋 Tag successfully added!✅{bcolors.RESET}")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\n{bcolors.FAIL}❌ Exeption❗ - {bcolors.RESET}{ex}\n{bcolors.WARNING}🔄 You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}❌ Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue

class RemoveTag(BotCommands):
    def __init__(self, data: NoteBook = None):
        self.data = data
        self.command_run()
        
    def command_run(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input(f"{bcolors.BOLD}🔍 Please enter note name:✍️  {bcolors.RESET}")
                if not note_name in self.data:
                    raise ValueError(bcolors.FAIL + "❌ Such note does not exist❗ 😞" + bcolors.RESET)

                print(
                    f"{bcolors.BOLD}🏷️  Available tags in the note 📝{bcolors.RESET} {note_name} - ",
                    " | ".join(tag.value for tag in self.data[note_name].tags),
                )
                old_tag = input(f"{bcolors.BOLD}📝 Please choose the tag that must be replaced:✍️  {bcolors.RESET}")

                check_tag = any(
                    tag.value == old_tag for tag in self.data[note_name].tags
                )
                if not check_tag:
                    raise ValueError(bcolors.FAIL + "❌ Such tag does not exist❗ 😞" + bcolors.RESET)

                for key in self.data:
                    if key == note_name:
                        self.data[note_name].remove_tag(old_tag)
                        print(f"{bcolors.GREEN}📋 Tag successfully removed!✅{bcolors.RESET}")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\n{bcolors.FAIL}❌ Exeption❗ - {bcolors.RESET}{ex}\n{bcolors.WARNING}🔄 You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}❌ Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue

class FindSortTag(BotCommands):
    def __init__(self, data: NoteBook = None):
        self.data = data
        self.command_run()
    
    @responce_visualization
    def command_run(self):
        tag_name = input(f"{bcolors.BOLD}🔍 Please enter tag name:✍️  {bcolors.RESET}")
        match_dict = {}
        similar_dict = {}
        for key in self.data:
            for tag in self.data[key].tags:
                if tag.value == tag_name:
                    match_dict[self.data[key].name] = self.data[key]
                if tag_name in tag.value:
                    similar_dict[self.data[key].name] = self.data[key]
        if match_dict:
            print(f"{bcolors.GREEN}📋 We have a 100% match!✅{bcolors.RESET}")
            return match_dict
        elif not match_dict and similar_dict:
            print(f"{bcolors.WARNING}❌ There are no notes with exact tag 📋 {bcolors.RESET}{bcolors.UNDERLINE}'{tag_name}'{bcolors.RESET}{bcolors.WARNING} in the notebook, but I found some similarity❗ 🔄{bcolors.RESET}")
            return similar_dict
        elif not match_dict and not similar_dict:
            suggested_dict = {}
            for key in self.data:
                if self.data[key].note.value.__contains__(tag_name):   
                    suggested_dict[self.data[key].name] = self.data[key]
            if suggested_dict:
                print(f"{bcolors.WARNING}❌ There are no notes with exact tag 📋 {bcolors.RESET}{bcolors.UNDERLINE}'{tag_name}'{bcolors.RESET}{bcolors.WARNING} in the notebook, but I found some similarity in note body❗ 🔄{bcolors.RESET}")
                return suggested_dict
            else:
                return print(f"{bcolors.WARNING}❌ There are no notes with exact tag 📋 {bcolors.RESET}{bcolors.UNDERLINE}'{tag_name}'{bcolors.RESET}{bcolors.WARNING} in the notebook, as well as any similarity..😞{bcolors.RESET}")

class FileSort(BotCommands):
    def __init__(self):
        self.command_run()
        
    def command_run(self):
        tries = 2
        while tries > 0:
            try:
                sorter = FileSorter(input(f"{bcolors.BOLD}📂 Please etter folder path:✍️  {bcolors.RESET}"))
                sorter.trash_sorting()
                print(f"{bcolors.GREEN}📂 Files are successfully sorted!✅{bcolors.RESET}")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\n❌ {bcolors.FAIL}Exeption❗ - {bcolors.RESET}{ex}\n{bcolors.WARNING}🔄 You have one more last try to enter folder path!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}❌ Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue

class FileExtensionAdd(BotCommands):
    def __init__(self):
        self.command_run()
        
    def command_run(self):
        tries = 2
        while tries > 0:
            try:
                adding_extension(
                    input(
                        f"{bcolors.BOLD}📝 Please enter file type Image / Audio / Video / Document or Archive:✍️  {bcolors.RESET}"
                    ),
                    input(f"{bcolors.BOLD}📝 Please enter any extension in the format '.***':✍️  {bcolors.RESET}"),
                )
                print(f"{bcolors.GREEN}📂 New extension successfully added!✅{bcolors.RESET}")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\n❌ {bcolors.FAIL}Exeption❗ - {bcolors.RESET}{ex}\n{bcolors.WARNING}🔄 You have one more last try to enter file type!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n❌ {bcolors.RED}Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue
            
class FileExtensionRemove(BotCommands):
    def __init__(self):
        self.command_run()
        
    def command_run(self):
        tries = 2
        while tries > 0:
            try:
                removing_extension(
                    input(
                        f"{bcolors.BOLD}📝 Please enter file type Image / Audio / Video / Document or Archive:✍️  {bcolors.RESET}"
                    ),
                    input(f"{bcolors.BOLD}📝 Please enter any extension in the format '.***':✍️  {bcolors.RESET}"),
                )
                print(f"{bcolors.GREEN}📝 Extension successfully removed!✅{bcolors.RESET}")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\n❌ {bcolors.FAIL}Exeption❗ - {bcolors.RESET}{ex}.\n{bcolors.WARNING}You have one more last try to enter file type!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n❌ {bcolors.RED}Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue   

class FileExtensionShow(BotCommands):
    def __init__(self):
        self.command_run()
        
    def command_run(self):
        img = FileSorter.extensions_dict["Image"]
        vid = FileSorter.extensions_dict["Video"]
        doc = FileSorter.extensions_dict["Document"]
        aud = FileSorter.extensions_dict["Audio"]
        arch = FileSorter.extensions_dict["Audio"]
        print(f"{bcolors.BLUE}Image: {bcolors.RESET}", f"{bcolors.WARNING} {img} {bcolors.RESET}")
        print(f"{bcolors.BLUE}Video: {bcolors.RESET}", f"{bcolors.WARNING} {vid} {bcolors.RESET}")
        print(f"{bcolors.BLUE}Document: {bcolors.RESET}", f"{bcolors.WARNING} {doc} {bcolors.RESET}")
        print(f"{bcolors.BLUE}Audio: {bcolors.RESET}", f"{bcolors.WARNING} {aud} {bcolors.RESET}")
        print(f"{bcolors.BLUE}Archive: {bcolors.RESET}", f"{bcolors.WARNING} {arch} {bcolors.RESET}\n")      

class ShowAllCommands(BotCommands):
    def __init__(self, language:str = None, c_user: str = None):
        self.language = language
        self.command_run()
        
    def command_run(self):
        if self.language == 'en':
            command_list = ListOfCommands.COMMAND_LIST_EN
            command_explain = ListOfCommands.COMMANDS_EXPLAIN_EN
        elif self.language == 'ru':
            command_list = ListOfCommands.COMMAND_LIST_RU
            command_explain = ListOfCommands.COMMANDS_EXPLAIN_RU
        
        elif self.language == 'ua':
            command_list = ListOfCommands.COMMAND_LIST_UA
            command_explain = ListOfCommands.COMMANDS_EXPLAIN_UA

        print("".join(
            "|{:<10} - {:<20}|\n".format(command_list[item], command_explain[item])
            for item in range(len(command_list))
        ))
               
class ShowOneCommands(BotCommands):
    def __init__(self, language: str = None, c_user: str = None):
        self.language = language
        self.c_user = c_user
        self.command_run()
        
    def command_run(self):
        if self.language == 'en':
            command_list = ListOfCommands.COMMAND_LIST_EN
            command_explain = ListOfCommands.COMMANDS_EXPLAIN_EN
        elif self.language == 'ru':
            command_list = ListOfCommands.COMMAND_LIST_RU
            command_explain = ListOfCommands.COMMANDS_EXPLAIN_RU
        
        elif self.language == 'ua':
            command_list = ListOfCommands.COMMAND_LIST_UA
            command_explain = ListOfCommands.COMMANDS_EXPLAIN_UA

        if self.c_user:
            for com_list, ex_com in zip(command_list, command_explain):  
                if com_list.__contains__(self.c_user):
                    print(f"{com_list} {ex_com}\n")
        
class CommandFactory:
    def __init__(self, data: AddressBook, note: NoteBook):
        self.data = data
        self.note = note
        self._full_list_command = {}
        self._general_commands = {}
        self._contact_commands = {}
        self._note_commands = {}
        self._file_commands = {}
        self.command_list_en()
        self.command_list_ru()
        self.command_list_ua()
        self._full_list_command.update(self._general_commands)
        self._full_list_command.update(self._contact_commands)
        self._full_list_command.update(self._note_commands)
        self._full_list_command.update(self._file_commands)
        
    def command_registration(self, section_type: str, command: str, command_type: BotCommands):
        if section_type == 'contact':
            self._contact_commands[command] = command_type
            
        elif section_type == 'note':
            self._note_commands[command] = command_type
            
        elif section_type == 'file':
            self._file_commands[command] = command_type
            
        elif section_type == 'general':
            self._general_commands[command] = command_type
            
    def command_execute(self, command: str, language: str = None, c_user: str = None):
        if command in self._contact_commands:
            return self._contact_commands[command](self.data)
        
        elif command in self._note_commands:
            return self._note_commands[command](self.note)
        
        elif command in self._file_commands:
            return self._file_commands[command]()
        
        elif command in self._general_commands:
            return self._general_commands[command](language, c_user)
        
        raise ValueError(f"Unkown command please add this command '{command}' to my commnad list!")
    
    def command_list_en(self):
        self.command_registration("contact", "contact-show-all", ShowAllContacts)
        self.command_registration("contact", "contact-add", AddContact)
        self.command_registration("contact", "contact-find", ShowContactInfo)
        self.command_registration("contact", "contact-phone-remove", RemovePhone)
        self.command_registration("contact", "contact-remove", RemoveContact)
        self.command_registration("contact", "contact-email-add", AddEmail)
        self.command_registration("contact", "contact-email-edit", EditEmail)
        self.command_registration("contact", "contact-email-remove", RemoveEmail)
        self.command_registration("contact", "contact-phone-add", AddPhone)
        self.command_registration("contact", "contact-phone-edit", EditPhone)
        self.command_registration("contact", "contact-birthday-edit", EditBirthday)
        self.command_registration("contact", "display-birthdays", ShowContactsBirthdays)
        self.command_registration("note", "note-add", AddNote)
        self.command_registration("note", "note-find", ShowNoteInfo)
        self.command_registration("note", "note-show-all", ShowAllNotes)
        self.command_registration("note", "note-edit", EditNote)
        self.command_registration("note", "note-remove", RemoveMote)
        self.command_registration("note", "tag-add", AddTag)
        self.command_registration("note", "tag-edit", EditTag)
        self.command_registration("note", "tag-remove", RemoveTag)
        self.command_registration("note", "tag-find-sort", FindSortTag)
        self.command_registration("file", "file-sort", FileSort)
        self.command_registration("file", "file-extension-add", FileExtensionAdd)
        self.command_registration("file", "file-extension-remove", FileExtensionRemove)
        self.command_registration("file", "file-extension-show", FileExtensionShow)
        self.command_registration("general", "cli", ShowAllCommands)
        self.command_registration("general", "one-command-info", ShowOneCommands)
           
    def command_list_ru(self):
        self.command_registration("contact", "показать все контакты", ShowAllContacts)
        self.command_registration("contact", "добавление контакта", AddContact)
        self.command_registration("contact", "поиск контакта", ShowContactInfo)
        self.command_registration("contact", "удалить телефон", RemovePhone)
        self.command_registration("contact", "удалить контакт", RemoveContact)
        self.command_registration("contact", "добавить электронную почту", AddEmail)
        self.command_registration("contact", "редактировать электронную почту", EditEmail)
        self.command_registration("contact", "удалить электронную почту", RemoveEmail)
        self.command_registration("contact", "добавить телефон", AddPhone)
        self.command_registration("contact", "редактировать телефон", EditPhone)
        self.command_registration("contact", "редактировать день рождения", EditBirthday)
        self.command_registration("contact", "показать дни рождения", ShowContactsBirthdays)
        self.command_registration("note", "добавить заметку", AddNote)
        self.command_registration("note", "найти заметку", ShowNoteInfo)
        self.command_registration("note", "показать все заметки", ShowAllNotes)
        self.command_registration("note", "редактировать заметку", EditNote)
        self.command_registration("note", "удалить заметку", RemoveMote)
        self.command_registration("note", "добавить тег", AddTag)
        self.command_registration("note", "редактировать тег", EditTag)
        self.command_registration("note", "удалить тег", RemoveTag)
        self.command_registration("note", "найти и отсортировать по тегам", FindSortTag)
        self.command_registration("file", "сортировать файлы", FileSort)
        self.command_registration("file", "добавить расширение", FileExtensionAdd)
        self.command_registration("file", "удалить расширение", FileExtensionRemove)
        self.command_registration("file", "показать все разширения", FileExtensionShow)
        self.command_registration("general", "команды", ShowAllCommands)
    
    def command_list_ua(self):
        self.command_registration("contact", "показати всі контакти", ShowAllContacts)
        self.command_registration("contact", "додати контакт", AddContact)
        self.command_registration("contact", "пошук контакта", ShowContactInfo)
        self.command_registration("contact", "видалити телефон", RemovePhone)
        self.command_registration("contact", "видалити контакт", RemoveContact)
        self.command_registration("contact", "додати електронну пошту", AddEmail)
        self.command_registration("contact", "редагувати електронну пошту", EditEmail)
        self.command_registration("contact", "видалити електронну пошту", RemoveEmail)
        self.command_registration("contact", "додати телефон", AddPhone)
        self.command_registration("contact", "редагувати телефон", EditPhone)
        self.command_registration("contact", "редагувати день народження", EditBirthday)
        self.command_registration("contact", "показати дні народження", ShowContactsBirthdays)
        self.command_registration("note", "додати нотатку", AddNote)
        self.command_registration("note", "знайти нотатку", ShowNoteInfo)
        self.command_registration("note", "показати всі нотатк", ShowAllNotes)
        self.command_registration("note", "редагувати нотатку", EditNote)
        self.command_registration("note", "видалити нотатку", RemoveMote)
        self.command_registration("note", "додати тег", AddTag)
        self.command_registration("note", "редагувати тег", EditTag)
        self.command_registration("note", "видалити тег", RemoveTag)
        self.command_registration("note", "знайти та сортувати по тегам", FindSortTag)
        self.command_registration("file", "відсортувати файли", FileSort)
        self.command_registration("file", "додати розширення файла", FileExtensionAdd)
        self.command_registration("file", "видалити розширення файла", FileExtensionRemove)
        self.command_registration("file", "показати всі розширення", FileExtensionShow)
        self.command_registration("general", "можливості", ShowAllCommands)
