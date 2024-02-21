import os
import sys

def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

if __name__ == "__main__":
    if len(sys.argv) !=  2:
        print("Введите название файла")
        sys.exit(1)

    filename = sys.argv[1]
    search_path = os.path.dirname(os.path.abspath(__file__))
    file_path = find_file(filename, search_path)

    if file_path:
        with open(file_path, 'r') as file:
            for i, line in enumerate(file):
                if i ==  5:
                    break
                print(line, end='')
    else:
        print(f"Файл \"{filename}\" не найден")