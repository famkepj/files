__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
from zipfile import ZipFile

def clean_cache ():
    if not os.path.exists('files/cache'):
        os.makedirs('files/cache')
    else: 
        shutil.rmtree('files/cache')
        os.makedirs('files/cache')
    return dir

def cache_zip(zip_file_path, cache_dir_path):
    with ZipFile(zip_file_path, 'r') as zipObj:
        zipObj.extractall(cache_dir_path)
    return zipObj

def cached_files():
    path= os.path.abspath('files\cache')
    list_cached_files = [os.path.join(path, file) for file in os.listdir(path)]
    return list_cached_files

def find_password(list_cached_files):
    for file in list_cached_files:
        open_file = open(file,'r')
        text = open_file.readlines()
        if 'password' in str(text):
            for string in text:
                if 'password' in string:
                    password = (string[string.find(' ')+1:-1])
    return password

if __name__ == '__main__':
    clean_cache() 
    cache_zip('files/data.zip', 'files/cache' )
    print(cached_files()) 
    print(find_password(cached_files()))
