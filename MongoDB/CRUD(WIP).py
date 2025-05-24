# Make a MongoDB Query Easier to be written and copy pasted
# By @weiss-gcm and @shn-enaa
# このコードは、GitHubリポジトリにアップロードされる前に何度も修正されています。
# https://www.mongodb.com/ja-jp/docs/manual/crud/
# Work In Progress - Code isn't entirely stable.
# 開発中 - コードは完全に安定していません。
# Yg request bahasa indonesia, tunggu yak... lagi malas 

collection_name = "collection"

def menu_db():
    print("\nMongoDB Query Generator | MongoDBクエリ生成ツール")
    print("1. Insert Query | 挿入クエリ")
    print("2. Find Query | 検索クエリ")
    print("3. Update Query | 更新クエリ")
    print("4. Delete Query | 削除クエリ")
    print("5. Exit | 終了")
    selection = input("Select Option (1-5) | 選択 (1～5): ")
    return selection

def insert_data():
    print("\nGenerate Insert Query | 挿入クエリ生成")
    print("1. Insert One | 1件挿入")
    print("2. Insert Many | 複数挿入")
    print("3. Back to Main Menu | メインメニューに戻る")
    choice = input("Select Option (1-3) | 選択 (1～3): ")

    if choice == "1":
        print("\nInsert One | 1件挿入")
        print("Enter field names and values (type 'done' when finished) | フィールド名と値を入力 ('done'で終了):")
        document = {}
        while True:
            key = input("Field name | フィールド名: ")
            if key.lower() == 'done':
                break
            value = input(f"Value for {key} | {key}の値: ")
            try:
                value = int(value) if value.isdigit() else float(value) if value.replace('.', '', 1).isdigit() else value
            except ValueError:
                pass
            document[key] = value

        if document:
            query = f"db.{collection_name}.insertOne({document})"
            print("\nYour MongoDB query | 生成されたクエリ:")
            print(query)
        else:
            print("No fields provided, query not generated. | フィールドが未入力のためクエリを生成できません。")

    elif choice == "2":
        print("\nInsert Many Documents | 複数ドキュメント挿入")
        print("Enter documents one by one (type 'done' when finished) | ドキュメントを入力 ('done'で終了):")
        documents = []
        while True:
            print(f"\nDocument #{len(documents) + 1} | ドキュメント #{len(documents) + 1}")
            doc = {}
            while True:
                key = input("Field name (or 'done' for this document) | フィールド名 ('done'でこのドキュメントを終了): ")
                if key.lower() == 'done':
                    break
                value = input(f"Value for {key} | {key}の値: ")
                try:
                    value = int(value) if value.isdigit() else float(value) if value.replace('.', '', 1).isdigit() else value
                except ValueError:
                    pass
                doc[key] = value

            if doc:
                documents.append(doc)
            else:
                print("Empty document skipped. | 空のドキュメントはスキップされます。")

            more = input("Add another document? (y/n) | 別のドキュメントを追加しますか？ (y/n): ").lower()
            if more != 'y':
                break

        if documents:
            query = f"db.{collection_name}.insertMany({documents})"
            print("\nYour MongoDB query | 生成されたクエリ:")
            print(query)
        else:
            print("No documents provided, query not generated. | ドキュメントが未入力のためクエリを生成できません。")

def find_data():
    print("\nGenerate Find Query | 検索クエリ生成")
    print("1. Find One | 1件検索")
    print("2. Find Many | 複数検索 (件数指定)")
    print("3. Find All | 全件検索")
    print("4. Back to Main Menu | メインメニューに戻る")
    choice = input("Select Option (1-4) | 選択 (1～4): ")

    query = {}
    print("\nBuild your query (leave empty to match all documents) | 検索条件を入力 (空欄で全件一致):")
    while True:
        key = input("Field to filter by (or 'done' to finish) | フィルタ対象フィールド ('done'で終了): ")
        if key.lower() == 'done':
            break
        value = input(f"Value for {key} | {key}の値: ")
        try:
            value = int(value) if value.isdigit() else float(value) if value.replace('.', '', 1).isdigit() else value
        except ValueError:
            pass
        query[key] = value

    if choice == "1":
        mongo_query = f"db.{collection_name}.findOne({query})"
    elif choice == "2":
        try:
            limit = int(input("Maximum documents to return | 取得する最大件数: "))
            mongo_query = f"db.{collection_name}.find({query}).limit({limit})"
        except ValueError:
            mongo_query = f"db.{collection_name}.find({query})"
            print("Invalid number, using no limit. | 無効な数値のため制限なしで検索します。")
    elif choice == "3":
        mongo_query = f"db.{collection_name}.find({query})"
    else:
        return

    print("\nYour MongoDB query | 生成されたクエリ:")
    print(mongo_query)

def update_data():
    print("\nGenerate Update Query | 更新クエリ生成")
    print("1. Update One | 1件更新")
    print("2. Update Many | 複数更新")
    print("3. Back to Main Menu | メインメニューに戻る")
    choice = input("Select Option (1-3) | 選択 (1～3): ")

    print("\nBuild your filter (which documents to update) | 更新対象のフィルタ条件:")
    filter_query = {}
    while True:
        key = input("Field to filter by (or 'done' to finish) | フィルタ対象フィールド ('done'で終了): ")
        if key.lower() == 'done':
            break
        value = input(f"Value for {key} | {key}の値: ")
        try:
            value = int(value) if value.isdigit() else float(value) if value.replace('.', '', 1).isdigit() else value
        except ValueError:
            pass
        filter_query[key] = value

    print("\nBuild your update operation | 更新内容を入力:")
    print("Format examples | 入力例:")
    print(" - Set field: field=new_value | フィールド設定: フィールド名=新しい値")
    print(" - Increment: field+=number | 数値増加: フィールド名+=数値")
    update = {}
    while True:
        op = input("Operation (or 'done' to finish) | 操作 ('done'で終了): ")
        if op.lower() == 'done':
            break

        if "+=" in op:
            field, value = op.split("+=")
            field = field.strip()
            try:
                value = int(value.strip()) if value.strip().isdigit() else float(value.strip())
            except ValueError:
                print(f"Invalid number: {value} | 無効な数値: {value}")
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
            print("Invalid format. Use field=value or field+=number | 無効な形式。field=値 または field+=数値 で入力してください。")

    if choice == "1":
        mongo_query = f"db.{collection_name}.updateOne({filter_query}, {update})"
    elif choice == "2":
        mongo_query = f"db.{collection_name}.updateMany({filter_query}, {update})"
    else:
        return

    print("\nYour MongoDB query | 生成されたクエリ:")
    print(mongo_query)

def delete_data():
    print("\nGenerate Delete Query | 削除クエリ生成")
    print("1. Delete One | 1件削除")
    print("2. Delete Many | 複数削除")
    print("3. Back to Main Menu | メインメニューに戻る")
    choice = input("Select Option (1-3) | 選択 (1～3): ")

    print("\nBuild your filter (which documents to delete) | 削除対象のフィルタ条件:")
    filter_query = {}
    while True:
        key = input("Field to filter by (or 'done' to finish) | フィルタ対象フィールド ('done'で終了): ")
        if key.lower() == 'done':
            break
        value = input(f"Value for {key} | {key}の値: ")
        try:
            value = int(value) if value.isdigit() else float(value) if value.replace('.', '', 1).isdigit() else value
        except ValueError:
            pass
        filter_query[key] = value

    if choice == "1":
        mongo_query = f"db.{collection_name}.deleteOne({filter_query})"
    elif choice == "2":
        mongo_query = f"db.{collection_name}.deleteMany({filter_query})"
    else:
        return

    print("\nYour MongoDB query | 生成されたクエリ:")
    print(mongo_query)

def main():
    global collection_name
    print("Simple MongoDB Query Generator | MongoDBクエリ簡易生成ツール")
    print("This tool helps you build MongoDB queries to copy-paste | コピペ用のMongoDBクエリを生成します")

    collection_name = input("Enter your MongoDB collection name | MongoDBコレクション名を入力: ").strip()
    if not collection_name:
        collection_name = "collection"

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
            print("Goodbye! | 終了します。")
            break
        else:
            print("Invalid selection, please try again. | 無効な選択です。再試行してください。")

        input("\nPress Enter to continue... | Enterキーを押して続行...")

if __name__ == "__main__":
    main()
