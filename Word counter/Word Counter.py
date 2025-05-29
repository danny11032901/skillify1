#  Word Counter

from collections import Counter
import re
import os
import time

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    print("Installing colorama...")
    os.system('pip install colorama')
    from colorama import Fore, Style, init
    init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    print(Fore.CYAN + """
  ╔════════════════════════════════════╗
         Welcome to Word Counter 
  ╚════════════════════════════════════╝
    """)
    print(Fore.MAGENTA + "Let's get started!\n")

def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

def display_counts(word_counts):
    print(Fore.YELLOW + "\n Word Frequency")
    print("=" * 35)
    for word, count in word_counts.most_common():
        print(Fore.CYAN + f"{word:<15}" + Fore.LIGHTWHITE_EX + f"{count}")
    print("=" * 35)
    print(Fore.LIGHTMAGENTA_EX + f"Total Unique Words: {len(word_counts)}")
    print(Fore.LIGHTGREEN_EX + "Thank you for using Word Counter! \n")

def main():
    clear_screen()
    show_banner()
    text = input(Fore.LIGHTRED_EX + "Please enter your text below:\n\n")
    
    print(Fore.LIGHTBLUE_EX + "\nAnalyzing your text...")
    time.sleep(1)
    
    word_counts = count_words(text)
    display_counts(word_counts)

    choice = input(Fore.LIGHTCYAN_EX + "\nWant to analyze another text? (y/n): ")
    if choice.lower() == 'y':
        main()
    else:
        print(Fore.LIGHTGREEN_EX + "\nHave a wonderful day!\n")
        exit()

if __name__ == "__main__":
    main()
