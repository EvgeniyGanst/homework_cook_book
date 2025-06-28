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

file_path = r"D:\all_homework_project\homework_cook_book\cook_book.txt"
cook_book = get_cook_book(file_path)
pprint(cook_book)