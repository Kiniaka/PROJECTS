from pathlib import Path
import os
import shutil
from zipfile import ZipFile
import tarfile
import gzip


def sort_Balagan_dir(path):
    list_music = []
    list_film = []
    list_documents = []
    list_archives = []
    list_pictures = []
    list_others = []
    Known = []
    Unknown = []
    doc = path+r'\documents'
    music = path+r'\audio'
    film = path+r'\video'
    picture = path+r'\images'
    archive = path+r'\archives'
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            end = (item.split('.')[-1])
            start = (item.split('.')[0])
            if end in ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx']:
                list_documents.append(item)
                Known.append(end)
                # przenosi pliki dokumentowe do folderu documents
                shutil.move(item_path, doc)
            elif end in ['avi', 'mp4', 'mov', 'mkv']:
                list_film.append(item)
                Known.append(end)
                # przenosi pliki muzyczne do folderu video
                shutil.move(item_path, film)
            elif end in ['jpeg', 'jpg', 'svg', 'png']:
                list_pictures.append(item)
                Known.append(end)
                # przenosi pliki obrakowe do folderu images
                shutil.move(item_path, picture)
            elif end in ['mp3', 'ogg', 'wav', 'amr']:
                list_music.append(item)
                Known.append(end)
                # przenosi pliki muzyczne do folderu audio
                shutil.move(item_path, music)
            elif end in ['zip', 'gz', 'tar']:
                list_archives.append(item)
                Known.append(end)
                # przenosi pliki muzyczne do folderu archive
                shutil.move(item_path, archive)
            else:
                list_others.append(item)
                Unknown.append(end)
        elif os.path.isdir(item_path):
            if item in ['archives', 'audio', 'documents', 'images', 'video']:
                continue
            else:
                lista_elementów_folderu = os.listdir(item_path)
                if lista_elementów_folderu != []:
                    for ele in os.listdir(item_path):
                        item_path_1 = os.path.join(item_path, ele)
                        if os.path.isfile(item_path_1):
                            end = (ele.split('.')[-1])
                            start = (ele.split('.')[0])
                            if end in ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx']:
                                list_documents.append(ele)
                                Known.append(end)
                                # przenosi pliki dokumentowe do folderu documents
                                shutil.move(item_path_1, doc)
                            elif end in ['avi', 'mp4', 'mov', 'mkv']:
                                list_film.append(ele)
                                Known.append(end)
                                # przenosi pliki muzyczne do folderu video
                                shutil.move(item_path_1, film)
                            elif end in ['jpeg', 'jpg', 'svg', 'png']:
                                list_pictures.append(ele)
                                Known.append(end)
                                # przenosi pliki obrakowe do folderu images
                                shutil.move(item_path_1, picture)
                            elif end in ['mp3', 'ogg', 'wav', 'amr']:
                                list_music.append(ele)
                                Known.append(end)
                                # przenosi pliki muzyczne do folderu audio
                                shutil.move(item_path_1, music)
                            elif end in ['zip', 'gz', 'tar']:
                                print(f'ele_plikuw folderze: {ele}')
                                list_archives.append(ele)
                                Known.append(end)
                                # przenosi pliki muzyczne do folderu archives
                                shutil.move(item_path_1, archive)
                            else:
                                list_others.append(ele)
                                Unknown.append(end)
                            os.rmdir(item_path)
                else:
                    os.rmdir(item_path)
    SETZ = set(Known)
    SETNZ = set(Unknown)
    print(f'SET Known: {SETZ}')
    print(f'SET Unknown: {SETNZ}')
    print(f'Lista plikó muzycznych:{list_music}')
    print(f'Lista plików filmowych: {list_film}')
    print(f'Lista plików tekstowych: {list_documents}')
    print(f' Lista plików archiwalnych: {list_archives}')
    print(f'Lista plików obrazkowych: {list_pictures}')
    print(f' Lista plików pozostałych: {list_others}')
    return SETZ, SETNZ, list_music, list_film, list_documents, list_archives, list_pictures, list_others


def unpack_archive_files(path):
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
    return


def normalize(path):
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
    return
