import cv2
from pathlib import Path

def color_to_gray(path):
    image = cv2.imread(str(path))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    new_path = './data/gray/gray_'+str(path).split('/')[-1]
    print(f'New Path: {new_path}')
    cv2.imwrite(new_path, gray_image)

def convert_colored_dataset():
    directory = Path('./data/color')
    all_paths = [path for path in directory.rglob("*") if path.is_file()]  # Keep as Path objects
    print("Found paths:", all_paths)
    for path in all_paths:
        color_to_gray(path)

convert_colored_dataset()
