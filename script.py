import time
import requests
from colorama import *
header = "Tool Created By : 4nnonymous "
row1 = "Contact  : alexandre.privatechat@gmail.com "
row2 = "About Tool  : Save All of Your Accounts "

print(Fore.RED +"|"," "*45,"|")
print("|",header," "*15,"|")
print(" ","-"*45)
print("|"," "*45,"|")
print("|",row1," "*1,"|")
print(" ","-"*45)
print("|"," "*45,"|")
print("|",row2," "*4,"|")
print(" ","-"*45)

def spam_telegram_link(link, count):
    for i in range(count):
        response = requests.get(link)
        print(f"Visited {link} - Attempt {i + 1}")
        time.sleep(1)

if __name__ == "__main__":
    link_to_spam = input(Fore.RED+"Link To Spam :")
    number_of_visits = int(input(Fore.GREEN+"Number Of Visits :")) 
    spam_telegram_link(link_to_spam, number_of_visits)
print(Fore.BLUE+"Your Order Placed Succsesfuly !")
print(Fore.CYAN+Back.RED+"The Admin Says ",Fore.GREEN+"Thanks"," For Using His TOOL !",Style.RESET_ALL)
print(Fore.BLUE +"  _    _                 _                 _            ")
print(Fore.YELLOW +" | |  | |               | |               | |           ")
print(Fore.RED +" | |__| | ___  _ __ ___ | |__   __ _ _ __ | |_ ___ _ __ ")
print(Fore.BLUE +" |  __  |/ _ \| '_ ` _ \| '_ \ / _` | '_ \| __/ _ \ '__|")
print(Fore.YELLOW +" | |  | | (_) | | | | | | | | | (_| | | | | ||  __/ |   ")
print(Fore.RED +" |_|  |_|\___/|_| |_| |_|_| |_|\__,_|_| |_|\__\___|_|   ")	