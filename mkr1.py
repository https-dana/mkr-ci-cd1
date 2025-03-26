def read_file(file_path):
    """Зчитує текстовий файл і повертає його вміст."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
