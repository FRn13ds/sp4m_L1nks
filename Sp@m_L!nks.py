import time
import requests
from colorama import *
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