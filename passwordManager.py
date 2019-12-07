import pyperclip, time, sys, json
from pathlib import Path
import random

file = "passwords.txt"
filePath = Path("passwords.txt")
if filePath.is_file():
    open(file, "r+")
    passwords = json.load(open(file))
else:
    open(file, "w")
    passwords = {}

def printMenu():
    print("Password Manager")
    print()
    print("F - Find Password")
    print("A - Add Password")
    print("G - Generate Password")
    print("E - Exit")
    print()

    menuSelection = input("Enter Your Selection: ")

    while menuSelection:
        if menuSelection == 'F':
            findPassword()
        elif menuSelection == 'A':
            addPassword()
        elif menuSelection == 'G':
            generatePassword()
        elif menuSelection == 'E':
            break
        else:
            print("Invalid Selection - Selections are case sensitive.")
        print()
        print("F - Find Password")
        print("A - Add Password")
        print("G - Generate Password")
        print("E - Exit")
        menuSelection = input("Enter Your Selection: ")
        print()

    print("Finishing")
    print()

def generatePassword():
    password = ''
    print("Generating new password.\n")
    length = int(input("Enter Desired Length of New Password: "))
    print()
    alphabet = chooseAlphabet()
    while(length > 0):
        length = length - 1
        password += random.choice(alphabet)
    print("Password = ", password)
    pyperclip.copy(password)
    print("Password copied for 10 seconds...")
    time.sleep(10)
    pyperclip.copy("")
    print("Password removed from clipboard")

def chooseAlphabet():
    alphabet = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print("Do you want your password to include: (y/n)")
    numbers = input("Numbers? ")
    specialCharacters = input("Special characters? ")

    if(numbers == 'y'):
        alphabet += '0123456789'
    if(specialCharacters == 'y'):
        alphabet += '!@#$%^&*()_-'
    return alphabet

def addPassword():
    account = input("Enter Account - Website/App: ")
    #userName = input("Enter Username: ")
    password = input("Enter Password: ")
    passwords[account] = encode(password)
    json.dump(passwords, open(file, "w"))
    print("Saved Password")

def findPassword():
    account = input("Enter Account - Website/App: ")
    if account in passwords.keys():
        encryptedPassword = passwords[account]
        pyperclip.copy(decode(encryptedPassword))
        print("Password = ", decode(encryptedPassword))
        print("Password copied for 10 seconds...")
        time.sleep(10)
        pyperclip.copy("")
        print("Password removed from clipboard")
    else:
        print("Account: ", account, " not found.")

def encode(password):
    encodedChars = []
    for i in range(len(password)):
        encodedChar = chr(ord(password[i]) - len(password))
        encodedChars.append(encodedChar)
    encodedPassword = "".join(encodedChars)
    return encodedPassword

def decode(encodedPassword):
    decodedChars = []
    for i in range(len(encodedPassword)):
        decodedChar = chr(ord(encodedPassword[i]) + len(encodedPassword))
        decodedChars.append(decodedChar)
    decodedPassword = "".join(decodedChars)
    return decodedPassword

printMenu()