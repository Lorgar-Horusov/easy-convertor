from PIL import Image
from pathlib import Path
from alive_progress import alive_bar
import os


def clear():
    if os.name == "nt":
        os.system('cls')
    elif os.name == "posix":
        os.system('clear')


def pause():
    if os.name == "nt":
        os.system('pause')
    elif os.name == "posix":
        os.system('read -n 1 -s -r -p "Press any key to continue..."')


def convertor(new_suffix='.jpg'):
    input_path = Path(__file__).parent / 'input_img'
    output_path = Path(__file__).parent / 'output_img'
    folder_path = Path('input_img')
    files = folder_path.glob('*')
    total_files = sum(1 for _ in files)
    files = folder_path.glob('*')
    with alive_bar(total_files, bar='circles', spinner='classic') as bar:
        for file in files:
            if file.is_file():
                file_name = input_path / file.name
                new_name = 'converted_' + file.stem + new_suffix
                convert_file = Image.open(file_name)
                convert_file.save(output_path / new_name)
                print(f'{new_name} Done!')
                bar()


def main():
    while True:
        suffixes = {1: '.png', 2: '.gif', 3: '.bmp', 4: '.tif', 5: '.webp', 6: '.ico', 0: 'exit'}
        for k, v in suffixes.items():
            print(f'{k}:{v}')
        suffix = int(input(f'[=>] please select new suffix: '))
        if suffix not in suffixes.keys():
            print(f'[!] suffix {suffix} not a found')
        if suffix == 0:
            exit()

        clear()
        convertor(new_suffix=suffixes[suffix])
        print(f'[>>] Job finish!')
        pause()
        clear()


if __name__ == "__main__":
    main()
