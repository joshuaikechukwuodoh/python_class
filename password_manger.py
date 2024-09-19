password = input("Enter you password: ")
view = ""
def view(password):
    
    if password == view:
        view.append(password)
        print(view)
    

def add():
    
    pass

while True:
    user_input = input("would you like to add or view your new password click(view or add) ").lower()
    
    if user_input == "q":
        
        print("Quitting...")
        break
    elif user_input == "add":
        
        print("You selected 'add'.")
        view()
        
    elif user_input == "view":
        
        print("You selected 'view'.")
        
        add()
    
    else:
        print("Invalid input. Please enter 'add', 'view', or 'Q' to quit.")
        
user = view(password)    
print(user)    



