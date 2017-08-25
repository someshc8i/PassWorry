from getpass import getpass
import pickle
from Crypto.Cipher import AES


def save_file(obj):
    pickle.dump(obj, open("/usr/local/etc/keys.p", "wb"))


def load_file():
    return pickle.load(open("/usr/local/etc/keys.p", "rb"))


def generateAESobj(key):
    obj = AES.new(key, AES.MODE_CFB, 'SomeshChaturvedi')
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
        KEYS = load_file()
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
    save_file(KEYS)
    return


def show(arguments):
    try:
        KEYS = load_file()
    except:
        print("You have no passwords saved. Use add command to save passwords")
        return
    for key in KEYS:
        if str(key) == arguments.key:
            security_key = getpass("Enter security key:")
            password = generateAESobj(
                generate_key(security_key)).decrypt(key.password)
            print("Password: " + password.decode("utf-8"))
            if key.description:
                print("Description: " + key.description)
            return
    print("No such key-password is saved.")


def showall(arguments):
    try:
        KEYS = load_file()
    except:
        print("You have no passwords saved. Use add command to save passwords")
        return
    if len(KEYS) == 0:
        print("You have no passwords saved. Use add command to save passwords")
        return
    i = 1
    for key in KEYS:
        print(str(i) + ": " + str(key))
        i = i+1


def delete(arguments):
    try:
        KEYS = load_file()
    except:
        print("You have no passwords saved. Use add command to save passwords")
        return
    for i in range(len(KEYS)):
        if str(KEYS[i]) == arguments.key:
            confirmation = getpass("Are you sure you want to delete password \
            associated with key " + str(KEYS[i]) + "? (y/n):")
            if confirmation == 'y':
                print(confirmation)
                KEYS.pop(i)
                save_file(KEYS)
                return
            return
    print("No such key-password is saved.")
