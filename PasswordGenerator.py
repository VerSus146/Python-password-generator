import random

letters = ["a", "b", "c", "d", "e", "f", "g",
           "h", "i", "j", "k", "l", "m", "n",
           "o", "p", "q", "r", "s", "t", "u",
           "v", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

signs = [",", ".", "<", ">", "/", "?", ";", ":",
         "'", "[", "{", "]", "}", "|", "`", "~",
         "!", "@", "#", "$", "%", "^", "&", "*",
         "(", ")", "_", "-", "=", "+"]


def glob():
    # make lists global
    global letters
    global numbers
    global signs


def end():
    # Would you like to restart?
    if input("Would you like to generate new password? (y/N)") == "y":
        start()


def makepassword(diff):
    glob()

    if diff == "weak":
        password = []
        # Higher randint \/ = more letters in password
        for x in range(random.randint(4, 8)):
            # y = odds for letter/number/sign
            y = random.randint(0, 6)
            # 1/6 for number
            if y == 5:
                # password.append adds a letter/number/sign to your list
                password.append(random.choice(numbers))
            # 1/6 for uppercase letter
            elif y == 1:
                password.append(random.choice(letters).upper())
            # 4/6 for normal letter
            else:
                password.append(random.choice(letters))
    elif diff == "normal":
        password = []
        for x in range(random.randint(6, 12)):
            y = random.randint(0, 6)
            if y == 5 or y == 4 or y == 3:
                password.append(random.choice(numbers))
            elif y == 1 or y == 2:
                password.append(random.choice(letters).upper())
            else:
                password.append(random.choice(letters))
    elif diff == "hard":
        password = []
        for x in range(random.randint(8, 14)):
            y = random.randint(0, 7)
            if y == 5 or y == 4 or y == 3:
                password.append(random.choice(numbers))
            elif y == 1 or y == 2:
                password.append(random.choice(letters).upper())
            elif y == 6:
                password.append(random.choice(signs))
            else:
                password.append(random.choice(letters))
    elif diff == "impossible":
        password = []
        for x in range(random.randint(12, 21)):
            y = random.randint(0, 10)
            if y == 5 or y == 4 or y == 3:
                password.append(random.choice(numbers))
            elif y == 1 or y == 2 or y == 9:
                password.append(random.choice(letters).upper())
            elif y == 6 or y == 7 or y == 8:
                password.append(random.choice(signs))
            else:
                password.append(random.choice(letters))
    else:
        print("ERROR 01 - wrong str")

    # random.shuffle() shuffles your password once more
    random.shuffle(password)
    # join changes your list to string
    password = "".join(password)
    # print password for user
    print("Your generated password is: " + password)

    end()


def start():
    diff = input("How strong your password should be? (WEAK/normal/hard/impossible)")
    if diff == "weak" or diff == "normal" or diff == "hard" or diff == "impossible":
        print("")
    else:
        diff = "weak"

    makepassword(diff)


start()

#################################################################
# ver 1.0 by Krystian Dąbrowki Github: https://github.com/VerSus146
# ERROR 01 - difficulty problem. Probably wrong string got sent from start() to makepassword().
