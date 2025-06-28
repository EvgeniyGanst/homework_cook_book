from pprint import pprint


def read_cook_book(file_patch):
    cook_book = {}
    with open(file_patch,'r', 1, "utf-8") as file:
        lines = file.read().split("\n\n")

    for block in lines:
        if not block.strip():
            continue
        block_lines = block.split("\n")
        dish_name = block_lines[0]
        ingredient_count = int(block_lines[1])

        ingredients = []
        for i in range(2, 2 + ingredient_count):
            ingredient_info = block_lines[i].split(" | ")
            ingredient_name = ingredient_info[0]
            quantity = int(ingredient_info[1])
            measure = ingredient_info[2]
            ingredients.append({
                "ingredient_name": ingredient_name,
                "quantity": quantity,
                "measure": measure
            })
        cook_book[dish_name] = ingredients

    return cook_book

file_path = r"D:\all_homework_project\homework_cook_book\cook_book.txt"
cook_book = read_cook_book(file_path)
pprint(cook_book)