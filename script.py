import time
import requests
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

def print_centered(text, width, color=Fore.WHITE):
    padding = (width - len(text)) // 2
    print(color + "|" + " " * padding + text + " " * (width - len(text) - padding) + "|")

def print_divider(width, color=Fore.WHITE):
    print(color + "+" + "-" * width + "+")

# Header and Logo
logo = [
    "   _____ _             _         _            ",
    "  / ____| |           | |       | |           ",
    " | (___ | |_ _   _  __| |_   _  | |_ ___ _ __ ",
    "  \\___ \\| __| | | |/ _` | | | | | __/ _ \\ '__|",
    "  ____) | |_| |_| | (_| | |_| | | ||  __/ |   ",
    " |_____/ \\__|\\__,_|\\__,_|\\__,_|  \\__\\___|_|   "
]
header = "Tool Created By : FRn13ds"

# Menu Options
menu_options = {
    "1": "Start",
    "2": "About",
    "3": "How to Use",
    "4": "Creator",
    "0": "Exit"
}

def display_logo_and_header():
    width = max(len(line) for line in logo) + 10
    print_divider(width, Fore.BLUE)
    for line in logo:
        print_centered(line, width, Fore.YELLOW)
    print_divider(width, Fore.BLUE)
    print_centered(header, width, Fore.GREEN)
    print_divider(width, Fore.BLUE)

def display_menu():
    print(Fore.CYAN + "\nMain Menu:")
    for key, value in menu_options.items():
        print(Fore.YELLOW + f" [{key}] {value}")

def about_tool():
    print(Fore.GREEN + "\nThis tool allows you to send requests to any URL repeatedly.")
    print("It is designed for educational purposes only. Use responsibly!")

def how_to_use():
    print(Fore.CYAN + "\nHow to Use:")
    print(" 1. Choose 'Start' from the menu.")
    print(" 2. Enter the link you want to send requests to.")
    print(" 3. Specify the number of requests you want to send.")
    print(" 4. Watch the tool execute your request.")

def creator_info():
    print(Fore.MAGENTA + "\nCreator Info:")
    print(" Name: FRn13ds")
    print(" Contact: med.yassine.salmi110@gmail.com")

def spam_link(link, count):
    for i in range(count):
        try:
            response = requests.get(link)
            status_code = response.status_code
            print(Fore.CYAN + f"Request to {link} - Attempt {i + 1} - Status Code: {status_code}")
            time.sleep(1)
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Error during request: {e}")
            break

if __name__ == "__main__":
    display_logo_and_header()
    while True:
        display_menu()
        choice = input(Fore.YELLOW + "\nChoose an option: ").strip()
        if choice == "1":
            print(Fore.GREEN + "\nStarting...")
            try:
                link_to_spam = input(Fore.RED + "Link to Spam: ").strip()
                number_of_requests = int(input(Fore.GREEN + "Number of Requests: ").strip())
                spam_link(link_to_spam, number_of_requests)
                print(Fore.BLUE + "\nTask completed successfully!")
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a valid number for requests.")
        elif choice == "2":
            about_tool()
        elif choice == "3":
            how_to_use()
        elif choice == "4":
            creator_info()
        elif choice == "0":
            print(Fore.RED + "\nExiting the tool. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")
