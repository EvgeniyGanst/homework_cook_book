from pprint import pprint

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    text_list = text.split("\n")
        # origin_text = file.read()
    len_line = str(len(text_list))
    return [len_line, text]
file_path = r"D:\all_homework_project\homework_cook_book\task_3.txt"
text1 = read_file(r"D:\all_homework_project\homework_cook_book\1.txt")
text2 = read_file(r"D:\all_homework_project\homework_cook_book\2.txt")
text3 = read_file(r"D:\all_homework_project\homework_cook_book\3.txt")

with open(file_path, "w", encoding="utf-8") as file_up:
    file_up.write(f'2.txt\n{text2[0]}\n')
    file_up.write(text2[1])
    file_up.write(f'\n1.txt\n{text1[0]}\n')
    file_up.write(text1[1])
    file_up.write(f'\n3.txt\n{text3[0]}\n')
    file_up.write(text3[1])







print(text1)
print(text2)
print(text3)
