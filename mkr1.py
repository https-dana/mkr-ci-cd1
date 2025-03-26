import re



def read_file(file_path):
    """Зчитує текстовий файл і повертає його вміст."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def count_sentences(text):
    """Рахує кількість речень у тексті."""
    sentence_endings = re.compile(r'[.!?]+')
    sentences = sentence_endings.split(text)
    return sum(1 for s in sentences if s.strip())
