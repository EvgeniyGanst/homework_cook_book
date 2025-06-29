from pprint import pprint


def read_in_save_dict(file_dict, file_name):
    """
    Reads the file, calculates the number of lines, and saves everything to the dictionary
    """
    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()
        line_count = text.count("\n") + 1
    file_dict[file_name] = line_count


def sorted_and_write_file (file_dict, new_file):
    """
    Sorts the dictionary by key.
    Opens a file or creates it.
    Reads a file and writes to a new file
    """
    sorted_file_dict = dict(sorted(file_dict.items(), key=lambda item: item[1]))
    with open(str(new_file), "w", encoding="utf-8") as file_write:
        for key, values in sorted_file_dict.items():
            with open(key, "r", encoding="utf-8") as file:
                text = file.read()
            file_write.write(f'Имя файла: {key}\n')
            file_write.write(f'Количество строк: {values}\n')
            file_write.write(f'Текст файла: \n{text}\n')
    print(f'Файл успешно сохранен')
#Проверка работоспособности
file_dict = {}
read_in_save_dict(file_dict, "1.txt")
read_in_save_dict(file_dict, "2.txt")
read_in_save_dict(file_dict, "3.txt")

sorted_and_write_file(file_dict, "task_3.txt")
