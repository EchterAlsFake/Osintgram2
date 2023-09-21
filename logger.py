from colorama import *
import random

colours = [Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTMAGENTA_EX,
           Fore.LIGHTBLUE_EX]


def logger(msg, level=0):

    if level == 0:
        print(f"{Fore.LIGHTGREEN_EX}[+]{random.choice(colours)}{msg}")

    elif level == 1:
        print(f"{Fore.LIGHTRED_EX}[~]{Fore.LIGHTWHITE_EX}{msg}")