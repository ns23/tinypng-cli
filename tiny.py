'''
A tiny utility to compress all the images in the folder and copy it to folder name output
@author Nitesh Sawant
'''

import tinify
import os

tinify.key = "nwrfQRfgzwj3hfSbKpCghwfXswR1GXbx"


def output_dir_path():
    return os.path.join(os.getcwd(), 'output')


def create_output_folder(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


def get_png_files():
    filelist = os.listdir(os.getcwd())
    for file in filelist[:]:  # filelist[:] makes a copy of filelist.
        if not(file.endswith(".png")):
            filelist.remove(file)
    return filelist


def compress_image(img, out):
    try:
        source = tinify.tinify.from_file(path=img)
        source.to_file(out)
        pass
    except:
        print('cannot compress ' + img)
        pass


if __name__ == "__main__":
    output_dir = output_dir_path()
    create_output_folder(output_dir)
    png_files = get_png_files()

    for img in png_files:
        out_path = os.path.join(output_dir, img)
        img_path = os.path.join(os.getcwd(), img)
        compress_image(img, out_path)
