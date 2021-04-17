#! /usr/bin/env python3

import argparse
from random import sample as select_random
from pyperclip import copy
from termcolor import colored


def generate_password(pass_length):

    print(colored("\n[+] Generating Random Password...", 'blue'))

    lower_alphabets = "qwertyuiopasdfghjklmnbvcxz"
    upper_alphabets = lower_alphabets.upper()
    digits = '0123456789'
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    combination = list("{0}{1}{2}{3}".format(lower_alphabets, upper_alphabets, digits, punctuation))
    password = select_random(combination, pass_length)
    password = "".join(password)

    return password


def get_arguments():
    parser = argparse.ArgumentParser(prog="Password Generator",
                                     usage="%(prog)s [options]\n\t[-l | --length] [number]",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=""">>> | Password Generator v1.0 by Hack Hunt | <<<
    ----------------------------------------""")

    parser._optionals.title = "Optional Argument"

    parser.add_argument('-l', '--length',
                        dest='pass_length',
                        metavar='',
                        type=int,
                        default=12,
                        help='Specify the password length. Default is 12.')

    parser.add_argument('-c', '--copy',
                        dest='copy',
                        action='store_true',
                        help='If specified, the password will be copied to clipboard.')

    args = parser.parse_args()
    return args


def main():
    args = get_arguments()
    pass_length = args.pass_length
    copy_clipboard = args.copy

    try:
        while True:
            password = generate_password(pass_length)
            print(colored("[+] Password generated successfully -> {0}".format(password), 'green'))

            option = input(colored("\nAre you satisfied? [Y/N] (Default - Y)", 'yellow') + "\n>>> ").lower()

            if option not in ['n', 'no']:
                break

        if copy_clipboard:
            copy(password)
            print(colored("\n[+] Generated Password has been copied to clipboard", 'green'))
        else:
            print(colored("\n[!] Password is not copied to clipboard, make sure to copy it.", 'red'))

    except KeyboardInterrupt:
        print(colored("\n[+] User interrupted. Exiting...", 'red'))

    except BaseException as e:
        print(colored("\n[-] Error: {0}".format(e), 'red'))


#####################################################
if __name__ == '__main__':
    main()