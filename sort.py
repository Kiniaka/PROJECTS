import main as main_program
import sys
from funkcje import normalize,sortowanie_Balaganu,unpack_archive_files

path = sys.argv[1]
# aby wystartować plik uruchom przkłąd jako  python sort.py 'C:\Users\User\Desktop\TEST\06_Homework\Bałagan'

main_program.normalize(path)
main_program.sortowanie_Balaganu(path)
main_program.unpack_archive_files(path)
