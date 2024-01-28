"""This module provides access to some variables used or maintained 
by the interpreter and to functions that interact strongly with the interpreter. 
"""
import sys
from pathlib import Path
from colorama import Fore, Back, Style


def main():
    """main Function uses takes path in command line argument and iterates through
    each item in the directory recursively, printing them.
    """
    user_input = "" if len(sys.argv) < 2 else sys.argv[1]
    path = Path(user_input)
    if path.exists():
        if path.is_dir():
            items = path.glob("**/*")
            for item in items:
                if item.is_dir():
                    print(f"{Fore.BLUE} {Back.GREEN} {item} {Style.RESET_ALL}")
                else:
                    print(f"{Fore.BLUE} {item} {Style.RESET_ALL}")
        else:
            print(f"{path} is a file")
    else:
        print(f"{path.absolute()} does not exist")


if __name__ == "__main__":
    main()
