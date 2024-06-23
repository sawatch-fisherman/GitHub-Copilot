# ToDoリストアプリのコード例です。このコードはコマンドラインから操作できます。

# ToDoリストを管理するためのリスト
todo_list = []

def display_todos():
    """ToDoリストの内容を表示する"""
    if not todo_list:
        print("ToDoリストは空です。")
    else:
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")

def add_todo(item):
    """ToDoリストに項目を追加する"""
    todo_list.append(item)
    print(f"'{item}'をToDoリストに追加しました。")

def remove_todo(index):
    """指定されたインデックスのToDoをリストから削除する"""
    try:
        removed_item = todo_list.pop(index - 1)
        print(f"'{removed_item}'をToDoリストから削除しました。")
    except IndexError:
        print("指定されたインデックスはリストの範囲外です。")

def main():
    """アプリケーションのメインループ"""
    while True:
        print("\nToDoリスト管理アプリ")
        print("1. ToDoを表示")
        print("2. ToDoを追加")
        print("3. ToDoを削除")
        print("4. アプリを終了")
        choice = input("選択してください(1-4): ")

        if choice == "1":
            display_todos()
        elif choice == "2":
            item = input("追加するToDo: ")
            add_todo(item)
        elif choice == "3":
            index = int(input("削除するToDoの番号: "))
            remove_todo(index)
        elif choice == "4":
            print("アプリを終了します。")
            break
        else:
            print("無効な入力です。1から4の数字を入力してください。")

if __name__ == "__main__":
    main()