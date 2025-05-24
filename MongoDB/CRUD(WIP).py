# Make a MongoDB Query Easier to be written and copy pasted
# By @weiss-gcm and @shn-enaa
def menu_db():
    print("\nMongoDB Query Generator")
    print("1. Insert Query")
    print("2. Find Query")
    print("3. Update Query")
    print("4. Delete Query")
    print("5. Exit")
    selection = input("Select Option (1-5): ")
    return selection

def insert_data():
    print("\nGenerate Insert Query")
    print("1. Insert One")
    print("2. Insert Many")
    print("3. Back to Main Menu")
    choice = input("Select Option (1-3): ")
    
    if choice == "1":
        print("\nInsert One Document")
        print("Enter field names and values (type 'done' when finished)")
        document = {}
        while True:
            key = input("Field name: ")
            if key.lower() == 'done':
                break
            value = input(f"Value for {key}: ")
            try:
                value = int(value) if value.isdigit() else float(value) if value.replace('.', '', 1).isdigit() else value
            except ValueError:
                pass
            document[key] = value
        
        if document:
            query = f"db.collection.insertOne({document})"
            print("\nYour MongoDB query:")
            print(query)
        else:
            print("No fields provided, query not generated.")
    
    elif choice == "2":
        print("\nInsert Many Documents")
        print("Enter documents one by one (type 'done' when finished)")
        documents = []
        while True:
            print(f"\nDocument #{len(documents) + 1}")
            doc = {}
            while True:
                key = input("Field name (or 'done' for this document): ")
                if key.lower() == 'done':
                    break
                value = input(f"Value for {key}: ")
                try:
                    value = int(value) if value.isdigit() else float(value) if value.replace('.', '', 1).isdigit() else value
                except ValueError:
                    pass
                doc[key] = value
            
            if doc:
                documents.append(doc)
            else:
                print("Empty document skipped.")
            
            more = input("Add another document? (y/n): ").lower()
            if more != 'y':
                break
        
        if documents:
            query = f"db.collection.insertMany({documents})"
            print("\nYour MongoDB query:")
            print(query)
        else:
            print("No documents provided, query not generated.")

def find_data():
    print("\nGenerate Find Query")
    print("1. Find One")
    print("2. Find Many")
    print("3. Find All")
    print("4. Back to Main Menu")
    choice = input("Select Option (1-4): ")
    
    query = {}
    print("\nBuild your query (leave empty to match all documents)")
    while True:
        key = input("Field to filter by (or 'done' to finish): ")
        if key.lower() == 'done':
            break
        value = input(f"Value for {key}: ")
        try:
            value = int(value) if value.isdigit() else float(value) if value.replace('.', '', 1).isdigit() else value
        except ValueError:
            pass
        query[key] = value
    
    if choice == "1":
        mongo_query = f"db.collection.findOne({query})"
    elif choice == "2":
        try:
            limit = int(input("Maximum documents to return: "))
            mongo_query = f"db.collection.find({query}).limit({limit})"
        except ValueError:
            mongo_query = f"db.collection.find({query})"
            print("Invalid number, using no limit")
    elif choice == "3":
        mongo_query = f"db.collection.find({query})"
    
    print("\nYour MongoDB query:")
    print(mongo_query)

def update_data():
    print("\nGenerate Update Query")
    print("1. Update One")
    print("2. Update Many")
    print("3. Back to Main Menu")
    choice = input("Select Option (1-3): ")
    
    print("\nBuild your filter (which documents to update)")
    filter_query = {}
    while True:
        key = input("Field to filter by (or 'done' to finish): ")
        if key.lower() == 'done':
            break
        value = input(f"Value for {key}: ")
        try:
            value = int(value) if value.isdigit() else float(value) if value.replace('.', '', 1).isdigit() else value
        except ValueError:
            pass
        filter_query[key] = value

    print("\nBuild your update operation")
    print("Format examples:")
    print(" - Set field: field=new_value")
    print(" - Increment: field+=number")
    update = {}
    while True:
        op = input("Operation (or 'done' to finish): ")
        if op.lower() == 'done':
            break
        
        if "+=" in op:
            field, value = op.split("+=")
            field = field.strip()
            try:
                value = int(value.strip()) if value.strip().isdigit() else float(value.strip())
            except ValueError:
                print(f"Invalid number: {value}")
                continue
            if "$inc" not in update:
                update["$inc"] = {}
            update["$inc"][field] = value
        elif "=" in op:
            field, value = op.split("=", 1)
            field = field.strip()
            value = value.strip()
            try:
                value = int(value) if value.isdigit() else float(value) if value.replace('.', '', 1).isdigit() else value
            except ValueError:
                pass
            if "$set" not in update:
                update["$set"] = {}
            update["$set"][field] = value
        else:
            print("Invalid format. Use field=value or field+=number")
    
    if choice == "1":
        mongo_query = f"db.collection.updateOne({filter_query}, {update})"
    else:
        mongo_query = f"db.collection.updateMany({filter_query}, {update})"
    
    print("\nYour MongoDB query:")
    print(mongo_query)

def delete_data():
    print("\nGenerate Delete Query")
    print("1. Delete One")
    print("2. Delete Many")
    print("3. Back to Main Menu")
    choice = input("Select Option (1-3): ")
    
    print("\nBuild your filter (which documents to delete)")
    filter_query = {}
    while True:
        key = input("Field to filter by (or 'done' to finish): ")
        if key.lower() == 'done':
            break
        value = input(f"Value for {key}: ")
        try:
            value = int(value) if value.isdigit() else float(value) if value.replace('.', '', 1).isdigit() else value
        except ValueError:
            pass
        filter_query[key] = value
    
    if choice == "1":
        mongo_query = f"db.collection.deleteOne({filter_query})"
    else:
        mongo_query = f"db.collection.deleteMany({filter_query})"
    
    print("\nYour MongoDB query:")
    print(mongo_query)

def main():
    print("Simple MongoDB Query Generator")
    print("This tool helps you build MongoDB queries to copy-paste")
    
    while True:
        selection = menu_db()
        if selection == "1":
            insert_data()
        elif selection == "2":
            find_data()
        elif selection == "3":
            update_data()
        elif selection == "4":
            delete_data()
        elif selection == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid selection, please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
