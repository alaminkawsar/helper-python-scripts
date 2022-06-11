import os
import zipfile
import random
import shutil


def extract_folder(dataset_path, source_dir, num_directories=4):
    if not os.path.exists("ZIP_FOLDER_NAME"):
        print("Extracting files")
        zip_ref = zipfile.ZipFile(dataset_path, 'r')
        print("> Extracting Dataset files")
        zip_ref.extractall("egohands")
        print("> Extraction complete")
        zip_ref.close()
        '''append all of file or folder into 'dirs' list'''
        dirs = [os.path.join(source_dir, dir) for dir in os.listdir(source_dir)]
        random.shuffle(dirs)
        
    else:
        print("Files already extracted.")
        return False

if __name__ == '__main__':
    FOLDER_NAME = 'FOLDER_NAME'
    SOURCE_DIR = 'SOURCE_DIR'
    extract_folder(FOLDER_NAME,SOURCE_DIR)