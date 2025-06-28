from pprint import pprint

def read_file(file_path):
    """
    Reads the file and returns a list of blocks.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().strip()
    blocks = text.split("\n\n")
    return blocks


def parse_block(block):
    """
    Parses one block of text and returns the name of the dish and the list of ingredients.
    """
    lines = block.split('\n')
    dish_name = lines[0]
    ingredient_count = int(lines[1])

    ingredients = []
    for i in range(2, 2 + ingredient_count):
        ingredients_info = lines[i].split(" | ")
        ingredients.append({
            "ingredient_name": ingredients_info[0],
            "quantity": ingredients_info[1],
            "measure": ingredients_info[2]
        })
    return dish_name, ingredients


def cook_book_build(blocks):
    """
    Creates a cook_book dictionary from a list of blocks.
    """
    cook_book = {}
    for block in blocks:
        dish_name, ingredients = parse_block(block)
        cook_book[dish_name] = ingredients
    return cook_book


def get_cook_book(file_path):
    """
    The main function is to read a file and create a dictionary.
    :param file_path: file directory
    :return: returns the dictionary
    """
    blocks = read_file(file_path)
    cook_book = cook_book_build(blocks)
    return(cook_book)


def get_shop_list_by_dishes(dishes, person_count, file_path=r"D:\all_homework_project\homework_cook_book\cook_book.txt"):
    cook_books = get_cook_book(file_path)

    shop_list = {}
    for dish in dishes:
        if dish not in cook_books:
            print(f'Блюдо {dish} отсутствует в книге рецептов!')
            continue
        for ingredient in cook_books[dish]:
            ingredient_name = ingredient["ingredient_name"]
            measure = ingredient["measure"]
            quantity = int(ingredient["quantity"]) * person_count

            if ingredient_name in shop_list:
                shop_list[ingredient_name][quantity] += quantity
            else:
                shop_list[ingredient_name] = {"quantity": quantity,"measure":measure}
    return shop_list

file_path = r"D:\all_homework_project\homework_cook_book\cook_book.txt"
cook_book = get_cook_book(file_path)
# pprint(cook_book)

cokie = get_shop_list_by_dishes(["Омлет", "Запеченный картофель"], 3)
pprint(cokie)