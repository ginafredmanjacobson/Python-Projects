from cmath import e
from genericpath import isfile
import os
from re import I
import shutil

def sort_docs():
    target_folder = ('/Users/ginafredman-jacobson/Documents')
    extensions = {item.split('.')[-1]for item in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, item))}

    #Creates a folder for each extension type
    for extension in extensions:
        if not os.path.exists(os.path.join(target_folder, extension)):
            os.mkdir(os.path.join(target_folder, extension))

    #Moving files
    for item in os.listdir(target_folder):
        if os.path.isfile(os.path.join(target_folder, item)):
            file_extension = item.split('.')[-1]
            shutil.move(os.path.join(target_folder, item), os.path.join(target_folder, file_extension, item))
sort_docs()


def sort_docs_photos():
    target_folder = ('/Users/ginafredman-jacobson/Documents/Photographs')
    extentions = {item.split('.')[-1]for item in os.listdir(target_folder)if os.path.isfile(os.path.join(target_folder, item))}

    for extention in extentions:
        if not os.path.exists(os.path.join(target_folder, extention)):
            os.mkdir(os.path.join(target_folder, extention))

    for item in os.listdir(target_folder):
        if os.path.isfile(os.path.join(target_folder, item)):
            file_extension = item.split('.')[-1]
            shutil.move(os.path.join(target_folder, item), os.path.join(target_folder, file_extension, item))
sort_docs_photos()
