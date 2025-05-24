#Make a MongoDB Query Easier to write
def menu_db():
    print("1. Insert Data")
    print("2. Read Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Exit")
    selection = int(input("Select Option: "))
    return selection

def insert_data():
    print("Insert Data")
    print("1. Insert One")
    print("2. Insert Many")
    selection_in = int(input("Select Option: "))
    return selection_in

def read_data():
    print("Read Data")
    print("1. Read One")
    print("2. Read Many")
    selection_rd = int(input("Select Option: "))
    return selection_rd

def update_data():
    print("Update Data")
    print("1. Update One")
    print("2. Update Many")
    selection_up = int(input("Select Option: "))
    return selection_up

def delete_data():
    print("Delete Data")
    print("1. Delete One")
    print("2. Delete Many")
    selection_del = int(input("Select Option: "))
    return selection_del

def main_acv():
    while True:
        selection = menu_db()
        if selection == 1:
            selection_in = insert_data()
        elif selection == 2:
            selection_rd = read_data()
        elif selection == 3:
            selection_up = update_data()
        elif selection == 4:
            selection_del = delete_data()
        else:
            break

#The main function isn't active at the moment.
