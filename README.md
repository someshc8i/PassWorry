# PassWorry
Passwords saving cli tool 

## Motivation
No need to remember a lot many passwords or save them somewhere in system without any security.
Just remember one security key and you are good to go :)

## Installation
```bash
sudo pip install git+https://github.com/someshchaturvedi/PassWorry.git
```

## Description
Stores passwords associated with a particular ```key```. Uses 2-way hashing algorithm AES.
Security key and key are different. Key is used to map password while security key serves as a password.

## commands

### add
You'll be prompted for a security key. Keeping the security key same for all passwords is recommended.
```bash
passworry add -k <key> -p <password> -d <description>
```

### show
You'll be prompted for the scurity key you entered during addition of this password.
```bash
passworry show -k <key>
```

### delete
```bash
passworry delete -k <key>
```

### showall
```bash
passworry showall 
```
