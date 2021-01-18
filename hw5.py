
import sys
import pathlib

files = []
def recursive_func(path): 
    if path.is_dir():
        for file in path.iterdir():
            recursive_func(file)
    else:
        files.append(path.name)
    return files    
    

def sort_func(files):
    
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
    unknown = set()

    for file in files:
        for i, k in enumerate(file):
            if k == '.':
                if file[i:] in documents_files:
                    extension.add(file[i:])
                    documents.append(file)
                elif file[i:] in images_files:
                    extension.add(file[i:])
                    images.append(file)
                elif file[i:] in video_files:
                    extension.add(file[i:])
                    videos.append(file)
                elif file[i:] in music_files:
                    extension.add(file[i:])
                    music.append(file)
                else:
                    unknown.add(file[i:])
                    another.append(file)
            
    print(f"DOCUMENTS: {documents}")
    print(f"IMAGES: {images}")
    print(f"VIDEOS: {videos}")
    print(f"MUSIC: {music}")
    print(f"NOT DEFINED: {another}")

    print(f"List of extensions that are found in the target folder: {extension}, unknown extensions: {unknown}.")
    
def main():
    path = sys.argv[1]
    #path = '/Users/Me/Desktop' 
    path = pathlib.Path(path)
    recursive_func(path)
    sort_func(files)


if __name__ == '__main__':
    main()


