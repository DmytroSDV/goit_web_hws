from AvadaKedavrassss import AvadaKedavra
# from AvadaKedavra import shutdown_with_countdown
from prompt_toolkit.application.current import get_app
from prompt_toolkit.completion import WordCompleter
from CODE_CRAFTERS_CORE.RecordData import bcolors
from CODE_CRAFTERS_CORE.AddressBook import *
from CODE_CRAFTERS_CORE.NoteFeature import *
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from pathlib import Path

from threading import Timer
import asyncio
import random
from CODE_CRAFTERS_CORE.CommandFactory import *

STYLE = Style.from_dict({"prompt": "bg:#ansigreen #ffffff"})

HI_COMMANDS_RU = [
    "🎩✨ Абракадабра! Введите волшебную команду:✍️  ",
    "👋 Скажите мне, что вы хотите сделать:✍️  ",
    "👋 Привет! Чем я могу помочь? Введите команду:✍️  "
    "💫 Жду вашу команду для начала работы:✍️  ",
    "👋 Добро пожаловать в удивительный мир возможностей! Ожидаю вашей команды для начала:✍️  ",
    "🌈 Добро пожаловать в мир возможностей! Ожидаю вашей волшебной команды:✍️  ",
    "🌈 Доброго времени суток! Ожидаю вашей команды:✍️ ",
    "🌈 Привет! Какие чудеса сегодня?:✍️  ",
]

HI_COMMANDS_EN = [
    "🎩✨ Abracadabra! Enter the magic command:✍️  ",
    "👋 Let me know what you want to do:✍️  ",
    "🎩✨ Tell me what you want to do: ",
    "💫 Waiting for your command to start work:✍️  ",
    "👋 Welcome to the amazing world of opportunities! Waiting for your command to start:✍️  ",
    "🌈 Welcome to the world of opportunities! Waiting for your magic command:✍️  ",
    "🎩✨ Welcome to the magical world of possibilities! Enter the magic command:✍️ ",
    "👋 Hello! How can I help? Enter a command:✍️  ",
    "🌈 Good day! Waiting for your command:✍️  ",
    "💫 Greetings! Enter a command:✍️  ",
    "👋 Hello! What wonders do you seek today?:✍️  ",
]

HI_COMMANDS_UA = [
    "🎩✨ Абракадабра! Введіть магічну команду:✍️  ",
    "👋 Будьте добрі скажіть, що я маю зробити:✍️  ",
    "💫 Чекаю на ваші накази:✍️  ",
    "👋 Вітаю Вас в чарівному світі можливостей! Чекаю на Вашу команду для початку:✍️  ",
    "🌈 Вітаю Вас в чарівному світі можливостей! Чекаю на Вашу чарівну команду:✍️  ",
    "🎩✨ Абракадабра! Введіть чарівну команду:✍️  ",
    "🎩✨ Скажіть мені, що ви хочете зробити:✍️  ",
    "👋 Привіт! Як я можу допомогти? Введіть команду:✍️  ",
    "🌈 Доброго дня! Очікую вашої команди:✍️  ",
    "💫 Вітаю вас! Введіть команду:✍️  ",
    "🕰 Привіт! Які чудеса сьогодні?:✍️  ",
]

COMMAND_EXPLAIN_RU = WordCompleter(
    [
        "команды",
        "изменить язык",
        "добавление контакта",  # добавление контакта
        "поиск контакта",  # поиск контакта
        "показать все контакты",  # показать все контакты
        "добавить телефон",  # добавить телефон к контакту
        "удалить телефон",  # удалить телефон у контакта
        "добавить электронную почту",  # добавить электронную почту к контакту
        "удалить электронную почту",  # удалить электронную почту у контакта
        "редактировать телефон",  # редактировать телефон контакта
        "редактировать электронную почту",  # редактировать электронную почту контакта
        "редактировать день рождения",  # редактировать день рождения контакта
        "удалить контакт",  # удалить контакт
        "показать дни рождения",  # показать дни рождения
        "добавить заметку",  # добавить заметку
        "найти заметку",  # найти заметку
        "показать все заметки",  # показать все заметки
        "редактировать заметку",  # редактировать заметку
        "удалить заметку",  # удалить заметку
        "добавить тег",  # добавить тег
        "редактировать тег",  # редактировать тег
        "удалить тег",  # удалить тег
        "найти и отсортировать по тегам",  # найти и отсортировать по тегам
        "сортировать файлы",  # сортировать файлы
        "показать все разширения",  # сортировать файлы
        "добавить расширение",  # добавить расширение для сортировки
        "удалить расширение",  # удалить расширение из списка сортировки
        "выход",  # выход
    ]
)

COMMAND_EXPLAIN_EN = WordCompleter(
    [
        "cli",
        "change-language",
        "contact-add",
        "contact-find",
        "contact-show-all",
        "contact-phone-add",
        "contact-phone-remove",
        "contact-email-add",
        "contact-email-remove",
        "contact-phone-edit",
        "contact-email-edit",
        "contact-birthday-edit",
        "contact-remove",
        "display-birthdays",
        "note-add",
        "note-find",
        "note-show-all",
        "note-edit",
        "note-remove",
        "tag-add",
        "tag-edit",
        "tag-remove",
        "tag-find-sort",
        "file-sort",
        "file-extension-show",
        "file-extension-add",
        "file-extension-remove",
        "quit",
        "exit",
        "q",
    ]
)

COMMAND_EXPLAIN_UA = WordCompleter(
    [
        "можливості",
        "зміти мову",
        "додати контакт",
        "пошук контакта",
        "показати всі контакти",
        "додати телефон",
        "видалити телефон",
        "додати електронну пошту",
        "видалити електронну пошту",
        "редагувати телефон",
        "редагувати електронну пошту",
        "редагувати день народження",
        "видалити контакт",
        "показати дні народження",
        "додати нотатку",
        "знайти нотатку",
        "показати всі нотатки",
        "редагувати нотатку",
        "видалити нотатку",
        "додати тег",
        "редагувати тег",
        "видалити тег",
        "знайти та сортувати по тегам",
        "відсортувати файли",
        "показати всі розширення",
        "додати розширення файла",
        "видалити розширення файла", 
        "до зустрічі",  
    ]
)

def pre_run():
    app = get_app()
    b = app.current_buffer
    if b.complete_state:
        b.complete_next()
    else:
        b.start_completion(select_first=False)

async def get_input():
    global exit_flag
    if language == "ru":
        HI_COMMANDS = HI_COMMANDS_RU
        COMMAND_EXPLAIN = COMMAND_EXPLAIN_RU
        print(f"{bcolors.PINK}🤖 Я здесь, чтобы сделать твой день немного ярче!\n🌞 Не стесняйтесь задавать вопросы или просто общаться. Вместе мы можем сделать этот день незабываемым! 🎉🎈{bcolors.RESET}")
    elif language == "en":
        HI_COMMANDS = HI_COMMANDS_EN
        COMMAND_EXPLAIN = COMMAND_EXPLAIN_EN
        print(f"{bcolors.PINK}🤖 I'm here to make your day a little brighter!\n🌞 Feel free to ask questions or just communicate. Together we can make this day unforgettable!{bcolors.RESET}")
    elif language == "ua" :
        HI_COMMANDS = HI_COMMANDS_UA
        COMMAND_EXPLAIN = COMMAND_EXPLAIN_UA
        print(f"{bcolors.PINK}🤖 Я тут, щоб зробити ваш день трохи яскравішим!\n🌞 Не соромтеся задавати питання або просто спілкуватися. Разом ми можемо зробити цей день незабутнім!{bcolors.RESET}")   
    try:
        session = PromptSession()
        
        timer = Timer(103, timer_function)
        timer.start()
        
        while True:
            try:
                result = await asyncio.wait_for(session.prompt_async(
                    random.choice(HI_COMMANDS),
                    completer=COMMAND_EXPLAIN,
                    pre_run=pre_run,
                    style=STYLE,
                ), timeout=30)
                timer.cancel()
                return result
        
            except asyncio.TimeoutError:
                ...
           
    except KeyboardInterrupt:
        print(f"\n{bcolors.FAIL}❌ KeyBoard interrupt error, EXITING❗{bcolors.RESET}\n")
        serialization = AddressBook()
        serialization.save_to_file(file_name, book)
        note_serialization = NoteBook()
        note_serialization.note_save_to_file(note_name, note)
        exit_flag = True
        
    except RuntimeError:
        pass

def timer_function():
    print(f"\n{bcolors.WARNING}⏰ Time's up! You didn't enter any command💀 {bcolors.RESET}")
    print(f"{bcolors.WARNING}😄 I'm offended, you're not using me, so I run the Awadakedabra command and I shut down you forever!💀 {bcolors.RESET}")
    shutdown_with_countdown()
    AvadaKedavra()()
    
# def wait_for_input(timeout=4, timeout2=500):
#     global loop
#     global timer_thread
#     global exit_flag
#     loop = asyncio.new_event_loop()
#     result = None
    
#     async def wait_input():
#         nonlocal result
#         result = await get_input()
        

#     timer_thread = threading.Timer(timeout2, timer_function)
#     timer_thread.start()

#     try:
#         loop.run_until_complete(wait_input())
#     except asyncio.TimeoutError:
#         print(f"{bcolors.ORANGE}\n⏰: You are here, I'm waiting for your command{bcolors.RESET}")
#         loop.close()
        
#     except KeyboardInterrupt as ex:
#         loop.close()
#         timer_thread.cancel()
#         exit_flag = True
#         print(ex)
#     finally:    
#         return result

async def main():
    global exit_flag
    global file_name
    global note_name
    global book
    global note
    global language
    exit_flag = False
    language_flag = False
    file_name = "database.bin"
    note_name = "notebase.bin"
    file_database = Path(file_name)
    note_database = Path(note_name)
    
    
    # Deserialization adddressbook
    if file_database.exists() and file_database.is_file():
        with open(file_database, "rb") as fh:
            check_content = fh.read()

        if not check_content:
            book = AddressBook()
        else:
            deserialization = AddressBook()
            book = deserialization.read_from_file(file_name)
    else:
        with open(file_database, "wb") as fh:
            pass
        book = AddressBook()


    # Deserialization notebook
    if note_database.exists() and note_database.is_file():
        with open(note_database, "rb") as fh:
            check_content = fh.read()
        if not check_content:
            note = NoteBook()
        else:
            deserialization = NoteBook()
            note = deserialization.note_read_from_file(note_name)
    else:
        with open(note_database, "wb") as fh:
            pass
        note = NoteBook()
    
        
    execute_command = CommandFactory(book, note)
    print(f"{bcolors.PINK}👋 Hello! My name is Bot Jul. Please choose the language and we will begin 🤖 {bcolors.RESET}")

    try:
        while 1:
            if not language_flag:
                language = input(f"{bcolors.BOLD}🏳️  Please choose a language (en/:ru:/ua): {bcolors.RESET}")
                language_flag = True
                if not language in ("en", "ru", 'ua'):
                    while 1:
                        print(f"{bcolors.BOLD}🙃  Wrong language format entered!\nPlease enter en | ru or ua to choose language:{bcolors.RESET}")
                        language = input(f"{bcolors.BOLD}🫠  Please choose a language (en/ru/ua): {bcolors.RESET}")
                        if language in ("en", "ru", 'ua'):
                            language_flag = True
                            break
                        
            user_input = await get_input()            
            execute_command.command_execute('one-command-info', language=language, c_user=user_input)
            
            if user_input in execute_command._full_list_command:
                execute_command.command_execute(user_input, language=language)
            elif user_input == "change-language":
                language_flag = False
            elif  user_input in ("quit", "exit", "q", "выход", "в", "до зустрічі", "д"):
                print("Good bye!\n")
                serialization = AddressBook()
                serialization.save_to_file(file_name, book)
                note_serialization = NoteBook()
                note_serialization.note_save_to_file(note_name, note)
                break
            else:
                if language == "en":
                    error_messages = [
                        f"{bcolors.WARNING}😔 Oh! You seem to have introduced the wrong command. Please try again!😔{bcolors.RESET}",
                        f"{bcolors.WARNING}😔 Oops! This is not like the right command. Let's try again😔{bcolors.RESET}",
                        f"{bcolors.WARNING}😟 Error: The command is not recognized. Try again.😔{bcolors.RESET}",
                        f"{bcolors.WARNING}😮 Hmm, I don't understand this command. Let's try something else.😔{bcolors.RESET}"
                    ]
                elif language == "ru":
                    error_messages = [
                        f"{bcolors.WARNING}🙃 Ой! Похоже, вы ввели неправильную команду. Пожалуйста, попробуйте снова!😔{bcolors.RESET}",
                        f"{bcolors.WARNING}😟 Упс! Это не похоже на правильную команду. Давайте попробуем еще раз😔{bcolors.RESET}",
                        f"{bcolors.WARNING}😯 Ошибка: Команда не распознана. Попробуйте еще раз.{bcolors.RESET}",
                        f"{bcolors.WARNING}😮 Хмм, я не понимаю эту команду. Давайте попробуем что-то еще.😔{bcolors.RESET}"
                    ]
                elif language == "ua":
                    error_messages = [
                        f"{bcolors.WARNING}😔 Ой! Начебто Ви ввели хибну команду. Будь ласка спробуйте ыще раз!😔{bcolors.RESET}",
                        f"{bcolors.WARNING}😯 Упс! Це не схоже правельну команду. Давайте спробуэмо ыще раз!😔{bcolors.RESET}",
                        f"{bcolors.WARNING}😔 Помилка: Незрозумыла команда. Спробуйте іще раз.😔{bcolors.RESET}",
                        f"{bcolors.WARNING}😔😮 Хмм, я не розумію цю команду. давайте спробуємо щось інше!😔{bcolors.RESET}"
                    ]
                       
                print(random.choice(error_messages))
                print(exit_flag, "*****************")
                if exit_flag:
                    break
                            
    except Exception as ex:
        print(f"{bcolors.FAIL}\n❌ Unnexpected error!{bcolors.RESET}")
        print(ex)
        serialization = AddressBook()
        serialization.save_to_file(file_name, book)
        note_serialization = NoteBook()
        note_serialization.note_save_to_file(note_name, note)

    except KeyboardInterrupt as ex:
        print(f"{bcolors.FAIL}\n❌ KeyBoard interrupt error, EXITING!\n{bcolors.RESET}")
        print(ex)
        serialization = AddressBook()
        serialization.save_to_file(file_name, book)
        note_serialization = NoteBook()
        note_serialization.note_save_to_file(note_name, note)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"{bcolors.BLUE}The script is interrupted by the user!{bcolors.RESET}")


