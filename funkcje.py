from pathlib import Path
import os
import shutil
from zipfile import ZipFile 
import tarfile
import gzip


def sortowanie_Balaganu(path):
    list_music=[]
    list_film=[]
    list_documents=[]
    list_archiwa=[]
    list_pictures=[]
    list_others=[]
    Znane=[]
    Nieznane=[]
    doc=path+r'\documents'
    music=path+r'\audio'
    film=path+r'\video'
    picture=path+r'\images'
    archive=path+r'\archives'
    for item in os.listdir(path):
        item_path = os.path.join(path,item)
        if os.path.isfile(item_path):
            end=(item.split('.')[-1])
            start=(item.split('.')[0])
            if end=='doc' or end=='docx' or end=='txt' or end=='pdf'or end=='xlsx' or end=='pptx':
                list_documents.append(item)
                Znane.append(end)
                shutil.move(item_path,doc) # przenosi pliki dokumentowe do folderu documents
            elif end=='avi'or end=='mp4'or end=='mov' or end=='mkv':
                list_film.append(item)
                Znane.append(end)
                shutil.move(item_path,film) # przenosi pliki muzyczne do folderu video
            elif end=='jpeg' or end=='jpg' or end=='svg' or end=='png':  
                list_pictures.append(item)
                Znane.append(end)
                shutil.move(item_path,picture) # przenosi pliki obrakowe do folderu images
            elif end=='mp3' or end=='ogg' or end=='wav' or end=='amr':
                list_music.append(item)
                Znane.append(end)
                shutil.move(item_path,music) # przenosi pliki muzyczne do folderu audio
            elif end=='zip' or end=='gz'or end=='tar':
                list_archiwa.append(item)
                Znane.append(end)
                shutil.move(item_path,archive) # przenosi pliki muzyczne do folderu archive
            else:
                list_others.append(item)
                Nieznane.append(end)
        elif os.path.isdir(item_path):
            if item=="archives" or item=="audio" or item=="documents" or item=="images" or item=="video":
                continue
            else:
                lista_elementów_folderu=os.listdir(item_path)
                if lista_elementów_folderu!=[]:
                   for ele in os.listdir(item_path):
                        item_path_1=os.path.join(item_path,ele)
                        if os.path.isfile(item_path_1):
                            end=(ele.split('.')[-1])
                            start=(ele.split('.')[0])
                            if end=='doc' or end=='docx' or end=='txt' or end=='pdf'or end=='xlsx' or end=='pptx':
                                list_documents.append(ele)
                                Znane.append(end)
                                shutil.move(item_path_1,doc) # przenosi pliki dokumentowe do folderu documents
                            elif end=='avi'or end=='mp4'or end=='mov' or end=='mkv':
                                list_film.append(ele)
                                Znane.append(end)
                                shutil.move(item_path_1,film) # przenosi pliki muzyczne do folderu video
                            elif end=='jpeg' or end=='jpg' or end=='svg' or end=='png':
                                list_pictures.append(ele)
                                Znane.append(end)  
                                shutil.move(item_path_1,picture) # przenosi pliki obrakowe do folderu images
                            elif end=='mp3' or end=='ogg' or end=='wav' or end=='amr':
                                list_music.append(ele)
                                Znane.append(end)
                                shutil.move(item_path_1,music) # przenosi pliki muzyczne do folderu audio
                            elif end=='zip' or end=='gz'or end=='tar':
                                print(f'ele_plikuw folderze: {ele}')
                                list_archiwa.append(ele)
                                Znane.append(end)
                                shutil.move(item_path_1,archive) # przenosi pliki muzyczne do folderu archives
                            else:
                                list_others.append(ele)
                                Nieznane.append(end)
                            os.rmdir(item_path)
                else:
                    os.rmdir(item_path)
    SETZ=set(Znane)
    SETNZ=set(Nieznane)
    print(f'SET Znane: {SETZ}')
    print(f'SET Nieznane: {SETNZ}')
    print(f'Lista plikó muzycznych:{list_music}')
    print(f'Lista plików filmowych: {list_film}')
    print(f'Lista plików tekstowych: {list_documents}')
    print(f' Lista plików archiwalnych: {list_archiwa}')
    print(f'Lista plików obrazkowych: {list_pictures}')
    print(f' Lista plików pozostałych: {list_others}')
    return SETZ,SETNZ,list_music,list_film,list_documents,list_archiwa,list_pictures,list_others

def unpack_archive_files(path):
    archive=path+r'\archives'
    for item in os.listdir(archive):
        item_path=os.path.join(archive,item)
        name=(item.split('.')[0])
        end=(item.split('.')[-1])
        if end=='zip':
            dest=archive+"//"+name
            shutil.unpack_archive(item_path,dest)
        elif end=='tar':
            new=archive+"//"+name
            shutil.unpack_archive(item_path,new,filter='data')
        elif end=='gz':
            gzfolder=archive+"\\"+name
            file=tarfile.open(str(item_path))
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
        if item=="archives" or item=="audio" or item=="documents" or item=="images" or item=="video":
                continue
        else:
            item_path = os.path.join(path,item)
            if os.path.isdir(item_path):
                nazwa_folderu=item
                nowa_nazwa=nazwa_folderu.strip().replace(" ","").replace("-","_").replace("!","_")
                for polish, english in polish_to_english.items():
                    nowa_nazwa = nowa_nazwa.replace(polish, english)
                os.rename(path+'\\'+nazwa_folderu,path+'\\'+nowa_nazwa)
            elif os.path.isfile(item_path):
                end=(item.split('.')[-1])
                start=(item.split('.')[0])
                nazwa_pliku=start
                nowa_nazwa=nazwa_pliku.strip().replace(" ","").replace("-","_")
                for polish, english in polish_to_english.items():
                    nowa_nazwa = nowa_nazwa.replace(polish, english)
                os.rename(path+'\\'+nazwa_pliku+"."+end,path+'\\'+nowa_nazwa+"."+end)
    return