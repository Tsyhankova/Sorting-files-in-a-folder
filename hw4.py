import os
import sys

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
path = '/Users/Me/Desktop'
print(f"Start in {path}")

# files - это список имен файлов и папок в path.
files = os.listdir(path)
#print(files)

music = []
music_files = ['.mp3', '.ogg',  '.wav', '.amr']
images = []
images_files = ['.png', '.jpeg', '.jpg']
documents = []
documents_files = ['.txt', '.doc', '.docx', '.ppt', '.pdf']
videos = []
video_files = ['.avi', '.mp4', '.mov']
another = []
extension = set()

for file in files:
    for i, k in enumerate(file):
        if k == '.':
            extension.add(file[i:])
            if file[i:] in documents_files:
                documents.append(file)
            elif file[i:] in images_files:
                images.append(file)
            elif file[i:] in video_files:
                videos.append(file)
            elif file[i:] in music_files:
                music.append(file)
            else:
                another.append(file)
        
print(f"DOCUMENTS: {documents}")
print(f"IMAGES: {images}")
print(f"VIDEOS: {videos}")
print(f"MUSIC: {music}")
print(f"NOT DEFINED: {another}")

print(f"List of all extensions that are found in the target folder: {extension}")

