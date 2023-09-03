from colorama import *

x = f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET}"
y = f"{Fore.LIGHTRED_EX}[~]{Fore.RESET}"

def logger(msg, level="0"):

    if level == "0":
        print(f"{x}{Fore.LIGHTCYAN_EX}:: DEBUG :: --=>: {msg}")

    elif level == "1":
        print(f"{y}{Fore.LIGHTRED_EX}:: ERROR :: --=>: {msg}")

