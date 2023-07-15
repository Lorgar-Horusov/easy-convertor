import os
import sys
from pathlib import Path

from PIL import Image
from alive_progress import alive_bar


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
        print('1 png\n'
              '2 gif\n'
              '3 bmp\n'
              '4 tif\n'
              '5 webp (not support linux)\n'
              '6 ico\n'
              '0 exit\n')
        suffix = input('please select suffix or number').lower().strip()
        clear()
        match suffix:
            case '1', 'png', 'p':
                convertor(new_suffix='.png')
                break
            case '2', 'gif', 'g':
                convertor(new_suffix='.gif')
                break
            case '3', 'bmp', 'b':
                convertor(new_suffix='.bmp')
                break
            case '4', 'tif', 't':
                convertor(new_suffix='.tif')
                break
            case '5', 'webp', 'w':
                if os.name == "nt":
                    convertor(new_suffix='.webp')
                    break
                elif os.name == "posix":
                    print('[!] "webp" not support linux')
                    break
            case '6', 'ico', 'i':
                convertor(new_suffix='.ico')
                break
            case '0', 'exit', 'e':
                sys.exit()
            case _:
                print('suffix not a found')


if __name__ == "__main__":
    main()
