import shutil
import zipfile
import tarfile
import sys
import os
import gzip
from pathlib import Path


from functions import normalize, sort_Balagan_dir, unpack_archive_files


path = sys.argv[1]

if __name__ == "__main__":

    normalize(path)
    sort_Balagan_dir(path)
    unpack_archive_files(path)

    


    




    