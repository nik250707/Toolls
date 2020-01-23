#info
version = "0.6 beta"
plan = "Fix all bugs and add functional to 1st option"

#What's new:
what_new = "\nAdded color and some fixes"

#import
import os
import sys
import time
import json
try:
    import colorama
    from termcolor import colored, cprint
    from colorama import Fore, Style
except ModuleNotFoundError:
    os.system("pip install colorama")
    os.system("pip install termcolor")
    import colorama
    from termcolor import colored, cprint
    from colorama import Fore, Style

#functions
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def load_data():
    global new_user
    f_name = "data.json"
    try:
        with open(f_name) as file:
            global data
            data = json.load(file)
            global easter
            global username
            easter = data["easter"]
            username = data["username"]
            new_user = False
    except FileNotFoundError:
        new_user = True

def save_data():
    global easter
    global username
    data = {"easter": easter, "username": username}
    f_name = "data.json"
    with open(f_name, "w") as file:
        json.dump(data, file)

def create_user():
    global username
    if lang == "en":
        username = input("What's your name? ")
    if lang == "ru":
        username = input("Как вас зовут? ")
    clear()

def greet_user():
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
    '''selecting language'''
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
    '''printing name'''
    print("         ╔╦╗┌─┐┌─┐┬  ┌─┐")
    print("          ║ │ ││ ││  └─┐")
    print("          ╩ └─┘└─┘┴─┘└─┘")
    print(colored("      made by: blnot and FYTUN", "green"))
    print("\n\n")

def print_options():
    '''printing available options'''
    global easter
    if lang == "en":
        print("\n1 - ROOT(need Root)")
        print("2 - Non Root")
        print("3 - Newbie Hacker :D")
        print("4 - Learn languages")
        print("5 - What's new")
        print("0 - Exit")
    if lang == "ru":
        print("\n1 - ROOT(нужны рут права)")
        print("2 - Без рут прав")
        print("3 - Новичок :D")
        print("4 - Изучение языков")
        print("5 - Что нового")
        print("0 - Выход")
    if easter >= 10:
        print(colored("\n10 - Secret panel\n", "green"))

def opt_1():
    '''using 1st option'''
    global easter
    easter += 1
    if lang == "en":
        print("\nNo data yet\n")
    if lang == "ru":
        print("\nПока ничего нет\n")

def opt_2():
    '''using 2nd option'''
    global easter
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install git -y")
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
    easter += 2

def opt_3():
    '''using 3rd option'''
    global easter
    easter += 3
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install git -y")
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
    while True:
        if lang == "en":
            print("Select language please \n 1 - Python\n 2 - JavaScript\n 0 - exit")
        if lang == "ru":
            print("Выберете язык \n 1 - Python\n 2 - JavaScript\n 0 - выход")
        language = input("#     ")
        if language == "1":
            print("\nhttps://drive.google.com/file/d/13ln9fLqFtDghHhdjEgGVyxblNusCdv6y/view\n")
        elif language == "2":
            print("\nhttps://learn.javascript.run\n")
        elif language == "0":
            clear()
            break
        else:
            incorrect()

def secret_opt():
    os.system("pkg install git -y")
    clear()
    if lang == "en":
        print("\nYou opened secret panel. Congratulations!\n")
        print("What do you want to do " + username.title() + "?\n")
    if lang == "ru":
        print("Ты открыл секретную панель. Поздравляю!")
        print("Ну так что ты хочешь сделать "  +username.title() + "?\n")
    time.sleep(2)
    while True:
        clear()
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
        else:
            incorrect()

def incorrect():
    '''printing icorrect message'''
    clear()
    if lang == "en":
        print(colored("\nIncorrect, try again\n", "red"))
    if lang == "ru":
        print(colored("\nНе корректно корректно, попробуйте ещё\n", "red"))

def check_status():
    '''checking status of work'''
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
            print(what_new)
            print_options()
        elif what_need == "0":
            clear()
            ending()
        elif what_need == "10":
            if easter >= 9:
                secret_opt()
                print_options()
            else:
                incorrect()
                print_options()
        else:
            incorrect()
            print_options()

def ending():
    '''printing final message'''
    save_data()
    clear()
    if lang == "en":
        print(Fore.GREEN + "\nGoodbye " + username.title() + "!")
    if lang == "ru":
        print(Fore.GREEN + "\nДо свидания " + username.title() + "!")
    time.sleep(1)
    print("\nMaked by blnot and FYTUN")
    if easter >= 10:
        print(colored("\nEaster is unlocked!", "red"))
    sys.exit()

def runing():
    global easter
    global new_user
    easter = 0
    colorama.init()
    clear()
    try:
        sel_lang()
        load_data()
        if new_user == False:
            greet_user()
        elif new_user == True:
            create_user()
        print_name()
        print_options()
        check_status()
        ending()
    except KeyboardInterrupt:
        if lang == "":
            clear()
            print(Fore.GREEN + "\nGoodbye!")
            time.sleep(1)
            print(Fore.GREEN + "\nMaked by blnot and FYTUN")
            sys.exit()
        else:
            ending()
    except Exception:
        print(colored("\nError\n", "red"))
        sys.exit()

#start
runing()