from shopping_list import ShoppingList


def main():
    shopping_list = ShoppingList()

    while True:
        print("\n1. アイテムを追加")
        print("2. アイテムを削除")
        print("3. アイテムを表示")
        print("4. アイテム数を表示")
        print("5. 終了")

        choice = input("選択してください（1-5）: ")

        if choice == "1":
            item = input("追加するアイテムを入力してください: ")
            shopping_list.add_item(item)
        elif choice == "2":
            item = input("削除するアイテムを入力してください: ")
            shopping_list.remove_item(item)
        elif choice == "3":
            items = shopping_list.get_items()
            print("買い物リスト:", items)
        elif choice == "4":
            count = shopping_list.get_item_count()
            print("アイテム数:", count)
        elif choice == "5":
            print("プログラムを終了します。")
            break
        else:
            print("無効な選択です。もう一度お試しください。")


if __name__ == "__main__":
    main()
