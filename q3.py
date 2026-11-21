# Q3: Append rice, insert sugar at index 1, remove milk, then pop and print the last item.

shopping_list = ["bread", "milk", "eggs"]

shopping_list.append("rice")
shopping_list.insert(1, "sugar")
shopping_list.remove("milk")

popped_item = shopping_list.pop()
print("popped", popped_item)
print("final list", shopping_list)
