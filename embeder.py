from re import sub
from subprocess import run
from sys import argv, exit
from os import listdir
from os.path import isfile, join, isdir


allowed_file_types = ['.png']


def append_to_file(file_path: str, content: str) -> None:
    with open(file_path, 'a') as file:
        file.write(content)



def normalize_xxd_output(input_str: str) -> str:
    return sub(r'\{([^}]*)}', lambda m: '{' + m.group(1).replace('\n', '') + '}', input_str) + '\n'


def embed_file(file_path: str) -> str:
    result = run(['xxd', '-i', file_path], capture_output=True, text=True)
    return normalize_xxd_output(result.stdout)


def explore(folder_path: str, output_file: str) -> None:
    entries = listdir(folder_path)
    files, folders = [f for f in entries if isfile(join(folder_path, f))], [d for d in entries if isdir(join(folder_path, d))]

    for file in files:
        if not any(file.endswith(ext) for ext in allowed_file_type):
            continue
        append_to_file(output_file, embed_file(join(folder_path, file)))
        #result = embed_file(join(folder_path, file))
        #print(result)


    for folder in folders:
        explore(join(folder_path, folder), output_file)


def logger(message: str) -> None:
    print(message)
    exit(1)


def main() -> None:
    if len(argv) != 3:
        logger("Usage: python3 embeder.py <input_folder> <output_file>")

    if not isdir(argv[1]):
        logger("The input folder does not exist")

    if not argv[2].endswith(".hpp") and not argv[2].endswith(".h"):
        logger("The output file must be a .hpp or a .h file")

    try:
        with open(argv[2], 'x') as file:
            file.write("#pragma once\n\n")
    except FileExistsError:
        logger("The output file already exists")

    explore(argv[1], argv[2])


if __name__ == "__main__":
    main()
