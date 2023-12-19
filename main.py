import shutil
import zipfile
import tarfile
import sys
import os
import gzip
from pathlib import Path


from funkcje import normalize,sortowanie_Balaganu,unpack_archive_files

path = sys.argv[1]
print(path)

if __name__ == "__main__":
    normalize(path)
    sortowanie_Balaganu(path)
    unpack_archive_files(path)
    


    




    