#! /usr/bin/env python3

import argparse
import random
from pyperclip import copy
from leet import changer


def generate_strong_password(pass_length):
    print("\n[+] Generating Random Password...")

    lower_alphabets = "qwertyuiopasdfghjklmnbvcxz"
    upper_alphabets = lower_alphabets.upper()
    digits = '0123456789'
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    combination = list("{0}{1}{2}{3}".format(lower_alphabets, upper_alphabets, digits, punctuation))
    password = random.sample(combination, pass_length)
    password = "".join(password)

    return password


def generate_logical_password(ans_list):
    print("\n[+] Generating password with you answers...")

    password = ""
    words = ["And", "Or", "With", "Go", "Is", "For", "The", "As", "If", "Nor", "But", "Yet"]

    for _ in range(len(ans_list)):
        y = random.randrange(len(ans_list))
        x = random.randrange(len(words))
        password = "{0}{1}".format(password, str(words[x]))
        password = "{0}{1}".format(password, str(ans_list[y]))
        ans_list.pop(y)
        words.pop(x)

    leet_data = changer(password)

    print("[+] Password (without special characters) -> {0}.".format(password))

    if isinstance(leet_data[0], int):
        print("[*] {0} is changed to {1}.".format(password[leet_data[0]], leet_data[2]))
        return leet_data[1]
    else:
        print("[*] and is changed to @.")
        return leet_data


def selector(length):
    print("[*] Select security questions numbers...\n")

    ques_lib = ["What is your mother's maiden name?",
                "What is the name of your first car?",
                "What elementary school did you attend?",
                "Where was your best family vacation as a kid?",
                "In which city does your nearest sibling lives?",
                "What was your childhood name?",
                "In which city did you meet your spouse/significant others?",
                "In what city did your mother and father meet?",
                "Where were you when you had your first kiss?",
                "In which city or town was your first job?",
                "What was your first pet?",
                "What's your dream job?",
                "What is your favourite movie of all times?",
                "What is your favourite programming language?",
                "At what age you lost your virginity?"]

    for x in range(0, len(ques_lib)):
        print("{0}: {1}".format(x + 1, ques_lib[x]))

    ans_list = list()

    while length > 0:

        number = input("\n[>] Enter the question number: \n>>> ")

        if number.isdigit():
            number = int(number) - 1
            if not (0 <= number <= len(ques_lib) - 1):
                print("\n[-] Enter a valid question number.")
                continue
        else:
            print("\n[-] Enter a valid question number.")
            continue

        answer = input("\n[>] {0}\n>>> ".format(ques_lib[number]))

        if answer == "":
            print("\n[-] Enter a valid answer.")
            continue

        if answer.isalpha():
            answer = answer.capitalize()

        if " " in answer:
            answer = answer.replace(" ", "_")

        ans_list.append(answer)

        length = length - 1

    return ans_list


def get_arguments():
    parser = argparse.ArgumentParser(prog="Password Generator",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=""">>> | Password Generator v2.1 by Hack Hunt | <<<
    ----------------------------------------""")

    parser._optionals.title = "Optional Arguments"

    parent_parser = argparse.ArgumentParser(add_help=False)

    parent_parser.add_argument('-c', '--copy',
                               dest='copy',
                               action='store_true',
                               help='If specified, the password will be copied to clipboard.')

    subparsers = parser.add_subparsers(title="Two possible options to choose from",
                                       description="",
                                       help="Type option -h/--help to know more about that command.",
                                       metavar="strong/logical",
                                       dest="cmd",
                                       required=True)

    parser_strong = subparsers.add_parser('strong',
                                          description=">>> If specified, the program will generate strong password "
                                                      "using random characters.",
                                          parents=[parent_parser],
                                          help="strong -h/--help to know available options.")

    parser_strong._optionals.title = "Available Arguments"

    parser_logical = subparsers.add_parser('logical',
                                           description=">>> If specified, few questions will be asked and will generate"
                                                       "password accordingly.",
                                           parents=[parent_parser],
                                           help="logical -h/--help to know available options.")

    parser_logical._optionals.title = "Available Arguments"

    parser_strong.add_argument('-l', '--length',
                               dest='pass_length',
                               metavar="<value>",
                               type=int,
                               default=12,
                               help='Specify the password length. Default is 12')

    parser_logical.add_argument('-q', '--question-number',
                                dest="ques_number",
                                metavar='<value>',
                                type=int,
                                choices=range(1, 5),
                                default=random.randint(2, 3),
                                help="Specify number of questions you want to answer. Default is random.")

    args = parser.parse_args()
    return args


def main():
    args = get_arguments()

    print("[*] Initializing Password Generator v2.0 ...")

    if args.cmd == "logical":
        ans_list = selector(args.ques_number)

    try:
        while True:
            if args.cmd == "strong":
                password = generate_strong_password(args.pass_length)
            else:
                password = generate_logical_password(ans_list.copy())

            print("[+] Password generated successfully -> {0}".format(password))

            option = input("\n[>] Are you satisfied? [Y/N] (Default - Y)\n>>> ").lower()

            if option not in ['n', 'no']:
                break

        if args.copy:
            copy(password)
            print("\n[+] Generated Password has been copied to clipboard.")
        else:
            print("\n[!] Password is not copied to clipboard, make sure to copy it.")

    except KeyboardInterrupt:
        print("\n[+] User interrupted. Exiting...")

    except BaseException as e:
        print("\n[-] Error: {0}".format(e))


#####################################################
if __name__ == '__main__':
    main()
