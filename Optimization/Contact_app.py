phone_number_dict = {}

def menu():
    print("1-Add tel\n2-Delete tel\n3-Search by name\n4-Change phone number\n5-Change name phone number\n6-Display\n7-Exit\n")
    option = int(input("Please Enter your Options: "))
    return option

def add():
    name = input("Enter Name number: ")
    number = int(input("Enter Phone number: "))
    phone_number_dict[name]=number

def delete():
    number = int(input("Enter Phone number: "))
    for dixt in phone_number_dict:
        if phone_number_dict[dixt] == number:
            phone_number_dict.pop(dixt)
            return True
    return False

def search():
    name = input("Enter Name number: ")
    if phone_number_dict.get(name) != None:
        print("in dict exist")
        return name
    print("in dict doesn't exist")
    return ""

def changeName():
    res = search()
    if res !="":
        name = input("Enter New Name number: ")
        temp = phone_number_dict.get(res)
        phone_number_dict.pop(res)
        phone_number_dict[name]=temp
        return True  
    return False

def changePhone():
    res = search()
    if res !="":
        number = int(input("Enter Phone number: "))
        phone_number_dict[res] = number
        return True
    return False

def display():
    print(f"------- Phone number List -------")
    for dixt in phone_number_dict:
        print(f"{dixt} : {phone_number_dict[dixt]}\n")
    print(f"--------------")


while (True):
    print()
    opt = menu()

    if(opt == 1):
        add()
    elif (opt == 2):
        delete()
    elif (opt == 3):
        search()
    elif (opt == 4):
        changePhone()
    elif (opt == 5):
        changeName()
    elif (opt == 6):
        display()
    else:
        break
  



