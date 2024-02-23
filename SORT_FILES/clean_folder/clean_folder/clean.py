import shutil
import zipfile
import tarfile
import sys
import os
import gzip
from pathlib import Path

def sort_dir(path):
    polish_to_english = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
        'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N',
        'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z'
    }
    for item in os.listdir(path):
        if item in ['archives', 'audio', 'documents', 'images', 'video']:
            continue
        else:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                folder_name = item
                new_name = folder_name.strip().replace(
                    " ", "").replace("-", "_").replace("!", "_")
                for polish, english in polish_to_english.items():
                    new_name = new_name.replace(polish, english)
                os.rename(path+'\\'+folder_name, path+'\\'+new_name)
            elif os.path.isfile(item_path):
                end = (item.split('.')[-1])
                start = (item.split('.')[0])
                file_name = start
                new_name = file_name.strip().replace(" ", "").replace("-", "_")
                for polish, english in polish_to_english.items():
                    new_name = new_name.replace(polish, english)
                os.rename(path+'\\'+file_name+"."+end,
                          path+'\\'+new_name+"."+end)
    list_music = []
    list_movie = []
    list_documents = []
    list_archives = []
    list_pictures = []
    list_others = []
    known = []
    unknown = []
    doc = path+r'\documents'
    music = path+r'\audio'
    movie = path+r'\video'
    picture = path+r'\images'
    archive = path+r'\archives'
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            end = (item.split('.')[-1])
            start = (item.split('.')[0])
            if end in ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx']:
                list_documents.append(item)
                known.append(end)
                # przenosi pliki dokumentowe do folderu documents
                shutil.move(item_path, doc)
            elif end in ['avi', 'mp4', 'mov', 'mkv']:
                list_movie.append(item)
                known.append(end)
                # przenosi pliki muzyczne do folderu video
                shutil.move(item_path, movie)
            elif end in ['jpeg', 'jpg', 'svg', 'png']:
                list_pictures.append(item)
                known.append(end)
                # przenosi pliki obrakowe do folderu images
                shutil.move(item_path, picture)
            elif end in ['mp3', 'ogg', 'wav', 'amr']:
                list_music.append(item)
                known.append(end)
                # przenosi pliki muzyczne do folderu audio
                shutil.move(item_path, music)
            elif end in ['zip', 'gz', 'tar']:
                list_archives.append(item)
                known.append(end)
                # przenosi pliki muzyczne do folderu archive
                shutil.move(item_path, archive)
            else:
                list_others.append(item)
                unknown.append(end)
        elif os.path.isdir(item_path):
            if item in ['archives', 'audio', 'documents', 'images', 'video']:
                continue
            else:
                dir_list_elements = os.listdir(item_path)
                if dir_list_elements != []:
                    for ele in os.listdir(item_path):
                        item_path_1 = os.path.join(item_path, ele)
                        if os.path.isfile(item_path_1):
                            end = (ele.split('.')[-1])
                            start = (ele.split('.')[0])
                            if end in ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx']:
                                list_documents.append(ele)
                                known.append(end)
                                # przenosi pliki dokumentowe do folderu documents
                                shutil.move(item_path_1, doc)
                            elif end in ['avi', 'mp4', 'mov', 'mkv']:
                                list_movie.append(ele)
                                known.append(end)
                                # przenosi pliki muzyczne do folderu video
                                shutil.move(item_path_1, movie)
                            elif end in ['jpeg', 'jpg', 'svg', 'png']:
                                list_pictures.append(ele)
                                known.append(end)
                                # przenosi pliki obrakowe do folderu images
                                shutil.move(item_path_1, picture)
                            elif end in ['mp3', 'ogg', 'wav', 'amr']:
                                list_music.append(ele)
                                known.append(end)
                                # przenosi pliki muzyczne do folderu audio
                                shutil.move(item_path_1, music)
                            elif end in ['zip', 'gz', 'tar']:
                                print(f'ele_plikuw folderze: {ele}')
                                list_archives.append(ele)
                                known.append(end)
                                # przenosi pliki muzyczne do folderu archives
                                shutil.move(item_path_1, archive)
                            else:
                                list_others.append(ele)
                                unknown.append(end)
                            os.rmdir(item_path)
                else:
                    os.rmdir(item_path)
    SETZ = set(known)
    SETNZ = set(unknown)
    archive = path+r'\archives'
    for item in os.listdir(archive):
        item_path = os.path.join(archive, item)
        name = (item.split('.')[0])
        end = (item.split('.')[-1])
        if end == 'zip':
            dest = archive+"//"+name
            shutil.unpack_archive(item_path, dest)
        elif end == 'tar':
            new = archive+"//"+name
            shutil.unpack_archive(item_path, new, filter='data')
        elif end == 'gz':
            gzfolder = archive+"\\"+name
            file = tarfile.open(str(item_path))
            file.extractall(gzfolder)
            file.close()
    print(f'SET Known: {SETZ}')
    print(f'SET unknown: {SETNZ}')
    print(f'Music files list:{list_music}')
    print(f'Movie files list: {list_movie}')
    print(f'Documents files list: {list_documents}')
    print(f'Archived files list: {list_archives}')
    print(f'Pictures fies list: {list_pictures}')
    print(f'Others files list: {list_others}')
    return SETZ, SETNZ, list_music, list_movie, list_documents, list_archives, list_pictures, list_others


 
def main():
    sort_dir(path) 
    
if __name__ == '__ main __':
    path = sys.argv[1]
    main()