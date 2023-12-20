import main as main_program
import sys
from functions import normalize, sort_Balagan_dir, unpack_archive_files

path = sys.argv[1]
# aby wystartować plik uruchom przkład jako  python sort.py 'C:\Users\User\Desktop\TEST\06_Homework\Bałagan'

main_program.normalize(path)
main_program.sort_Balagan_dir(path)
main_program.unpack_archive_files(path)
