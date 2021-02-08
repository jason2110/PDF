import pikepdf
from termcolor import colored

file = open("wordlist.txt")

for password in file:
    try:
        with pikepdf.open("remote.pdf",password.strip()) as pdf:
            print(colored("Password Found: {}".format(passsword),'green'))
            break
        except:
            print(colored("Trying Password: {}".format(password), 'red'))
            continue