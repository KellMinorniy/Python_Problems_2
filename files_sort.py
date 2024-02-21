import os
import sys
from collections import defaultdict

def list_files_by_extension(directory):
    files_by_extension = defaultdict(list)
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            name, ext = os.path.splitext(filename)
            files_by_extension[ext].append(filename)
    return files_by_extension

def main(directory):
    files_by_extension = list_files_by_extension(directory)
    for ext in sorted(files_by_extension.keys()):
        for filename in sorted(files_by_extension[ext]):
            print(filename)

if __name__ == "__main__":
    if len(sys.argv) !=  2:
        print("Введите путь к директории")
        sys.exit(1)

    directory = sys.argv[1]
    main(directory)