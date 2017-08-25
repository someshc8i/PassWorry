from getpass import getpass
import pickle
from Crypto.Cipher import AES


def generateAESobj(key):
    obj = AES.new(key, AES.MODE_CFB, 'This is an IV456')
    return obj


def generate_key(key):
    new_key = key
    while(len(new_key) < 16):
        new_key = new_key + 'a'
    return new_key


class Key:
    key = None
    description = None
    password = None

    def __init__(self, key, password, description=None):
        self.key = key
        self.password = password
        self.description = description

    def __str__(self):
        return self.key


def add(arguments):
    try:
        KEYS = pickle.load(open("keys.p", "rb"))
    except:
        KEYS = []
        print("You need to enter security every time you add a new password.\
        Keeping the key same for all passwords is recommended.")
    while(True):
        key1 = getpass(
            "Enter securty key (Remember this key to access passwords):")
        key2 = getpass("Enter securty key (again):")
        if (key1 != key2):
            print("Passwords didnt match. Try again.")
        else:
            break
    password = generateAESobj(generate_key(key1)).encrypt(arguments.password)
    k = Key(arguments.key, password, arguments.description)
    KEYS.append(k)
    pickle.dump(KEYS, open("keys.p", "wb"))
    return


def show(arguments):
    try:
        KEYS = pickle.load(open("keys.p", "rb"))
    except:
        print("You have no passwords saved. Use add command to save passwords")
    for key in KEYS:
        if str(key) == arguments.key:
            security_key = getpass("Enter security key:")
            password = generateAESobj(
                generate_key(security_key)).decrypt(key.password)
            print("Password: " + password.decode("utf-8"))
            print("Description: " + key.description)
            return
    print("No such key-password is saved.")


def showall(arguments):
    try:
        KEYS = pickle.load(open("keys.p", "rb"))
    except:
        print("You have no passwords saved. Use add command to save passwords")
    if len(KEYS) == 0:
        print("You have no passwords saved. Use add command to save passwords")
        return
    i = 1
    for key in KEYS:
        print(str(i) + ": " + str(key))
        i = i+1


def delete(arguments):
    try:
        KEYS = pickle.load(open("keys.p", "rb"))
    except:
        print("You have no passwords saved. Use add command to save passwords")
    for i in range(len(KEYS)):
        if str(KEYS[i]) == arguments.key:
            confirmation = getpass("Are you sure you want to delete password \
            associated with key " + str(KEYS[i]) + "? (y/n):")
            if confirmation == 'y':
                print(confirmation)
                KEYS.pop(i)
                pickle.dump(KEYS, open("keys.p", "wb"))
                return
            return
    print("No such key-password is saved.")
