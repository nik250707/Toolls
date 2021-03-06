#info
version = "0.8"
plan = "Get release"
whats_new = "\nSome fixes"

#import
import os
import sys
import time
import json
while True:
    try:
        import colorama
        from termcolor import colored, cprint
        from colorama import Fore, Style
        break
    except ModuleNotFoundError:
        os.system("pip3 install colorama")
        os.system("pip3 install termcolor")
        import colorama
        from termcolor import colored, cprint
        from colorama import Fore, Style
        break

#functions
def clear():
    '''clear screen'''
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def load_data():
    '''load data from file'''
    global new_user
    f_name = "data.json"
    try:
        with open(f_name) as file:
            global data
            data = json.load(file)
            global easter
            global username
            global debug
            easter = data["easter"]
            username = data["username"]
            debug = data['debug']
            new_user = False
    except FileNotFoundError:
        new_user = True

def save_data():
    '''save data to file'''
    global easter
    global username
    global debug
    try:
        data = {"easter": easter, "username": username, "debug": debug}
    except Exception:
        data = {"easter": easter, "username": username, "debug": "False"}
    f_name = "data.json"
    with open(f_name, "w") as file:
        json.dump(data, file)

def create_user():
    '''create new user'''
    global username
    if lang == "en":
        username = input("What's your name? ")
    if lang == "ru":
        username = input("Как вас зовут? ")
    clear()

def greet_user():
    '''greet user'''
    while True:
        if lang == "en":
            print(colored("Welcome back ", "green") + colored(username.title(), "green") + colored("!", "green"))
            print("Right?")
            print("1 - Yes\n2 - No\n")
        if lang == "ru":
            print(colored("Добро пожаловать ", "green") + colored(username.title(), "green") + colored("!", "green"))
            print("Верно?")
            print("1 - Да\n2 - Нет\n")
        answer = input()
        if answer == "1":
            clear()
            break
        elif answer == "2":
            clear()
            create_user()
            del answer
            break
        else:
            incorrect()

def sel_lang():
    '''select language'''
    while True:
        global lang
        print("select language/выберете язык")
        lang = ""
        lang = input(" 1 - EN\n 2 - RU\n")
        if lang == "1":
            lang = "en"
        elif lang == "2":
            lang = "ru"
        else:
            print(colored("try again/попробуйте ещё", "green"))
            time.sleep(0.5)
            clear()
            continue
        clear()
        break

def print_name():
    '''print name'''
    print("         ╔╦╗┌─┐┌─┐┬  ┌─┐")
    print("          ║ │ ││ ││  └─┐")
    print("          ╩ └─┘└─┘┴─┘└─┘")
    print(colored("      made by: blnot and FYTUN", "green"))
    print(colored("\nhttps://discord.gg/HASHUKW", "green"))
    print("\n\n")

def print_options():
    '''print available options'''
    global easter
    if lang == "en":
        print("\n1 - ROOT(need Root)")
        print("2 - Non Root")
        print("3 - Newbie Hacker :D")
        print("4 - Learn languages")
        print("5 - What's new")
        print("6 - Contact us")
        print("0 - Exit")
    if lang == "ru":
        print("\n1 - ROOT(нужны рут права)")
        print("2 - Без рут прав")
        print("3 - Новичок :D")
        print("4 - Изучение языков")
        print("5 - Что нового")
        print("6 - Связь с нами")
        print("0 - Выход")
    if easter >= 10:
        print(colored("\n10 - Secret panel\n", "green"))

def opt_1():
    '''using 1st option'''
    global easter
    easter += 1
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install tsu -y")
    clear()
    if lang == "en":
        print("\nTsu was installed. Usage: tsu")
    if lang == "ru":
        print("\nTsu был установлен. Использование: tsu")

def opt_2():
    '''using 2nd option'''
    global easter
    easter += 2
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install python -y")
    os.system("pkg install ruby -y")
    os.system("pkg install python2 -y && pkg install python3 -y")
    os.system("pkg install nodejs-lts -y")
    os.system("pkg install wget -y")
    os.system("pkg install hydra -y")
    clear()
    if lang == "en":
        print("\nAll installed, now you can install many patch for hacking\n")
    if lang == "ru":
        print("\nВсё установленно, теперь можете установить что-нибудь ещё\n")

def opt_3():
    '''using 3rd option'''
    global easter
    easter += 3
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install python -y")
    os.system("pkg install ruby -y")
    os.system("pkg install python2 -y && pkg install python3 -y")
    os.system("pkg install nodejs-lts -y")
    os.system("git clone https://github.com/Rajkumrdusad/Tool-X")
    os.system("pkg install ruby -y")
    os.system("pkg install wget -y")
    os.system("pkg install hydra -y")
    clear()
    if lang == "en":
        print("\nAll installed, now you can install many patch for hacking\n")
    if lang == "ru":
        print("\nВсё установленно, теперь можете установить что-нибудь ещё\n")

def opt_4():
    '''using 4th option'''
    global easter
    easter += 15
    while True:
        if lang == "en":
            print("Select language please \n 1 - Python\n 2 - JavaScript\n 0 - exit")
        if lang == "ru":
            print("Выберете язык \n 1 - Python\n 2 - JavaScript\n 0 - выход")
        selected_lang = input("#     ")
        if selected_lang == "1":
            clear()
            print("\nhttps://drive.google.com/file/d/13ln9fLqFtDghHhdjEgGVyxblNusCdv6y/view\n")
        elif selected_lang == "2":
            clear()
            print("\nhttps://learn.javascript.run\n")
        elif selected_lang == "0":
            clear()
            break
        else:
            incorrect()

def opt_contact():
    '''print contact data'''
    if lang == "en":
        print("Contact us")
    if lang == "ru":
        print("Связь с нами")
    print(colored("Discord \nhttps://discord.gg/HASHUKW", "green"))

def secret_opt():
    '''using secret panel'''
    global debug
    while True:
        clear()
        if lang == "en":
            print("\nYou opened secret panel. Congratulations!\n")
            print("What do you want to do " + username.title() + "?\n")
        if lang == "ru":
            print("Ты открыл секретную панель. Поздравляю!")
            print("Ну так что ты хочешь сделать "  +username.title() + "?\n")
        print("1 - SellPhish\n2 - InstagramBrute\n3 - Xerxes\n4 - IPGeoLocation\n5 - Toolss")
        if lang == "en":
            print("0 - Exit\n")
        if lang == "ru":
            print("0 - Выход\n")
        what_need = input()
        if what_need == "1":
            os.system("git clone https://github.com/thelinuxchoice/shellphish")
        elif what_need == "2":
            os.system("pkg install python3 -y")
            os.system("git clone https://github.com/Pure-L0G1C/Instagram")
        elif what_need == "3":
            os.system("git clone https://github.com/XCHADXFAQ77X/XERXES")
        elif what_need == "4":
            os.system("git clone https://github.com/maldevel/IPGeoLocation")
        elif what_need == "5":
            os.system("pkg install python -y")
            os.system("git clone https://github.com/AnonHackerr/toolss")
        elif what_need == "0":
            clear()
            break
        elif what_need == "debug_on":
            debug = "True"
        elif what_need == "debug_off":
            debug = "False"
        elif what_need == "999":
            if easter >= 15:
                clear()
                if lang == "en":
                    print(colored("Wow! You unlocked super secret panel!\nAnd it's nothing here.\n", "green"))
                if lang == "ru":
                    print(colored("Вау! Ты открыл супер секретную панель!\nИ здесь ничего нет.\n", "green"))
                time.sleep(3)
            else:
                incorrect()
                time.sleep(3)
        else:
            incorrect()
            time.sleep(3)

def incorrect():
    '''print icorrect message'''
    clear()
    if lang == "en":
        print(colored("\nIncorrect, try again\n", "red"))
    if lang == "ru":
        print(colored("\nНе корректно, попробуйте ещё\n", "red"))

def check_status():
    '''check status of work'''
    global easter
    while True:
        if lang == "en":
            what_need = input("\nSelect option  :")
        if lang == "ru":
            what_need = input("\nВыберете опцию  :")
        if what_need == "1":
            clear()
            opt_1()
            print_options()
        elif what_need == "2":
            clear()
            opt_2()
            print_options()
        elif what_need == "3":
            clear()
            opt_3()
            print_options()
        elif what_need == "4":
            clear()
            opt_4()
            print_options()
        elif what_need == "5":
            clear()
            print(whats_new)
            print_options()
        elif what_need == "6":
            clear()
            opt_contact()
            print_options()
        elif what_need == "0":
            clear()
            ending()
        elif what_need == "10":
            if easter >= 10:
                secret_opt()
                print_options()
            else:
                incorrect()
                print_options()
        else:
            incorrect()
            print_options()

def ending():
    '''print final message'''
    save_data()
    clear()
    if lang == "en":
        print(Fore.GREEN + "\nGoodbye " + username.title() + "!")
    if lang == "ru":
        print(Fore.GREEN + "\nДо свидания " + username.title() + "!")
    time.sleep(1)
    print("\nMaked by blnot and FYTUN")
    print(colored("\nhttps://discord.gg/HASHUKW", "green"))
    sys.exit()

def simple_run():
    '''simple execute programm'''
    try:
        sel_lang()
        if new_user == False:
            greet_user()
        elif new_user == True:
            create_user()
        print_name()
        print_options()
        check_status()
        ending()
    except KeyboardInterrupt:
        try:
            save_data()
        except Exception:
            pass
        if lang == "":
            clear()
            print(Fore.GREEN + "\nGoodbye!")
            time.sleep(1)
            print(Fore.GREEN + "\nMaked by blnot and FYTUN")
            print(colored("\nhttps://discord.gg/HASHUKW", "green"))
            sys.exit()
        elif lang == "en":
            clear()
            print(Fore.GREEN + "\nGoodbye!")
            time.sleep(1)
            print(Fore.GREEN + "\nMaked by blnot and FYTUN")
            print(colored("\nhttps://discord.gg/HASHUKW", "green"))
            sys.exit()
        else:
            clear()
            print(Fore.GREEN + "\nДо свидания!")
            time.sleep(1)
            print(Fore.GREEN + "\nMaked by blnot and FYTUN")
            print(colored("\nhttps://discord.gg/HASHUKW", "green"))
            sys.exit()
    except Exception:
        print(colored("\nError\n", "red"))
        sys.exit()

def debug_run():
    '''debug execute programm'''
    sel_lang()
    if new_user == False:
        greet_user()
    elif new_user == True:
        create_user()
    print_name()
    print_options()
    check_status()
    ending()

def run():
    '''run programm'''
    global easter
    global new_user
    global debug
    easter = 0
    colorama.init()
    os.system("pkg install git -y")
    clear()
    load_data()
    try:
        if debug == "True":
            debug_run()
        else:
            simple_run()
    except Exception:
        simple_run()

#run
run()
