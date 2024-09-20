
"""
start_name = input("Enter your name:")

print(f"Welcome sir/madam {start_name}")



def add():
    name = input("Enter your username:\n ")
    pwd = input("Enter your password: \n")
    file = open("password.txt" ,"a") 
    file.write(f"{name}    {pwd} \n")
    file.close()
    print("sucessfully created password file:" + file.name)



def view():
    file = open("password.txt","a")
    file.read()
    file.close()
    print(file.read())
    
    
    



while True:
    user_chioce = input("Enter any of the mode of your password choosen (view/add)")
    if user_chioce == "add":
        add()
    elif user_chioce == "view":
        view()
    else: 
     if user_chioce not in ["view", "add"]:
        print("Invalid choice!")
    
    continue
"""
"""""
start_name = input("Enter your name: ")
print(f"Welcome sir/madam {start_name}")

def add():
    name = input("Enter your username:\n ")
    pwd = input("Enter your password:\n ")
    file = open("password.txt", "a") 
    file.write(name + " " + pwd + "\n")  # Added space and newline for readability
    file.close()
    print("Successfully created password file.")

def view():
    file = open("password.txt", "r")  # Changed mode to 'r' for reading
    data = file.read()  # Storing the file content
    file.close()
    print(data)  # Printing the content

while True:
    user_choice = input("Enter any mode (view/add): ")
    if user_choice == "add":
        add()
    elif user_choice == "view":
        view()
    else:
        print("Invalid choice!")
    
    continue
"""


from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
