import os.path
import json



def load_json_from_file(path1, file_name):
    """
    Функция возвращает объект по строкам из json файла
    """
    file_ID = os.path.join(path1, file_name)  # Считываем файл с диска
    with open(file_ID, 'r', encoding='utf-8') as file_JS:  # Читаем файл построчно
        return json.load(file_JS)
