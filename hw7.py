import os
import pathlib
import re
import shutil
import sys
from os import makedirs, getcwd
from pathlib import Path
from shutil import move, unpack_archive


new_dir = os.chdir('C:/')
path = os.getcwd()
#print(path)

files = []
def recursive_func(path): 
    if path.is_dir():
        for file in path.iterdir():  
            recursive_func(file)
    else:
        files.append(path.name)
    return files

def without_extension(file, ext_list):
    for i in ext_list:
      if i in file:
        name_ = file.split(i)
        new_name = normalize(name_[0])
    return new_name

def new_with_ext(file, ext_list):
    for i in ext_list:
      if i in file:
        name_ = file.split(i)
        new_name = normalize(name_[0])
        new_name = new_name + str(i)
    return new_name
    
def normalize(text):
  alphabet = {ord('а'): 'a', ord('A'): 'A',
            ord('б'): 'b', ord('Б'): 'B',
            ord('в'): 'v', ord('В'): 'V',
            ord('г'): 'g', ord('Г'): 'G',
            ord('д'): 'd', ord('Д'): 'D',
            ord('е'): 'e', ord('Е'): 'E',
            ord('ё'): 'yo', ord('Ё'): 'Yo',
            ord('ж'): 'zh', ord('Ж'): 'Zh',
            ord('з'): 'z', ord('З'): 'Z',
            ord('и'): 'i', ord('И'): 'I',
            ord('й'): 'j', ord('Й'): 'J',
            ord('к'): 'k', ord('К'): 'K',
            ord('л'): 'l', ord('Л'): 'L',
            ord('м'): 'm', ord('М'): 'M',
            ord('н'): 'n', ord('Н'): 'N',
            ord('о'): 'o', ord('О'): 'O',
            ord('п'): 'p', ord('П'): 'P',
            ord('р'): 'r', ord('Р'): 'R',
            ord('с'): 's', ord('С'): 'S',
            ord('т'): 't', ord('Т'): 'T',
            ord('у'): 'u', ord('У'): 'U',
            ord('ф'): 'f', ord('Ф'): 'F',
            ord('х'): 'h', ord('Х'): 'H',
            ord('ц'): 'c', ord('Ц'): 'C',
            ord('ч'): 'ch', ord('Ч'): 'Ch',
            ord('ш'): 'sh',  ord('Ш'): 'Sh',
            ord('щ'): 'shch', ord('Щ'): 'Shch',
            ord('ъ'): "'", ord('ь'): '`',
            ord('ы'): 'y', ord('Ы'): 'Y',
            ord('э'): 'e', ord('Э'): 'E',
            ord('ю'): 'ju', ord('Ю'): 'Ju',
            ord('я'): 'ja', ord('Я'): 'Ja'}
  new_text = ''
  for letter in text:
    letter = letter.translate(alphabet)
    new_text += letter
  return re.sub(r"(\W)", '_', new_text)

def current_full_path(path, file):
    for dirs, folder, files in os.walk(path):
        for el in files:
            if el == file:
                current_dir = os.path.join(dirs, file)
                return current_dir
                
def archive_folder(files):
    archives = os.path.join(path, '/archives')
    makedirs(archives, exist_ok = True)
    for file in files:
        archive_files = ['.zip', '.tar', '.gztar', '.bztar', '.xztar']
        if os.path.splitext(file)[1] in archive_files:
            new_name = without_extension(file, archive_files)
            folder_with_unpack_archive ='/' + new_name
            
            makedirs(folder_with_unpack_archive, exist_ok = False)        
            unpack_archive(os.path.join(path,file),os.path.join(path, archives, folder_with_unpack_archive))
            new_name = new_with_ext(file, archive_files)
            move(os.path.join(path, folder_with_unpack_archive),os.path.join(path, archives, new_name))
            print(os.path.join(path,file))

def docs_folder(files):
    documents = os.path.join(path, '/documents')
    makedirs(documents, exist_ok = True)
    for file in files:
        documents_files = ['.txt', '.doc', '.docx', '.ppt', '.pdf', '.pptx', '.ods']
        if os.path.splitext(file)[1] in documents_files:
            current_dir = current_full_path(path, file)
            new_name = new_with_ext(file, documents_files)
            move(current_dir, os.path.join(path, documents, new_name))

def audio_folder(files):
    audio = os.path.join(path, '/audio')
    makedirs(audio, exist_ok = True)
    for file in files:
        music_files = ['.mp3', '.ogg',  '.wav', '.amr']
        if os.path.splitext(file)[1] in music_files:
            current_dir = current_full_path(path, file)
            new_name = new_with_ext(file, music_files)
            move(current_dir, os.path.join(path, audio, new_name))

def video_folder(files):
    video = os.path.join(path, '/video')
    makedirs(video, exist_ok = True)
    for file in files:
        video_files = ['.avi', '.mp4', '.mov']
        if os.path.splitext(file)[1] in video_files:
            current_dir = current_full_path(path, file)
            new_name = new_with_ext(file, video_files)
            move(current_dir, os.path.join(path, video, new_name))

def images_folder(files):
    images= os.path.join(path, '/images')
    makedirs(images, exist_ok = True)
    for file in files:
        images_files = ['.png', '.jpeg', '.jpg']
        if os.path.splitext(file)[1] in images_files:
            current_dir = current_full_path(path, file)
            new_name = new_with_ext(file, images_files)
            move(current_dir, os.path.join(path, images, new_name))

def programs_folder(files):
    programs = os.path.join(path, '/programs')
    makedirs(programs, exist_ok = True)
    for file in files:
        programs_files = ['.exe', '.sql', '.msi', '.ova', '.vdi', '.vbox']
        if os.path.splitext(file)[1] in programs_files:
            current_dir = current_full_path(path, file)
            move(current_dir, os.path.join(path, programs, file))
       
def delete_empty_folders(path):
    for i in os.listdir(path):
        normalize(i)
        d = os.path.join(path, i)
        if os.path.isdir(d):
            delete_empty_folders(d)
            if not os.listdir(d):
                os.rmdir(d)               


def main():
    path = sys.argv[0]
    #path = 'C:/' 
    path = pathlib.Path(path)   
    recursive_func(path)
    docs_folder(files)
    audio_folder(files)
    video_folder(files)
    images_folder(files)
    archive_folder(files)
    programs_folder(files)
    delete_empty_folders(path)
    


if __name__ == '__main__':
    main()


