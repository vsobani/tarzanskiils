import sys

sys.path.append(r'pa/home/vishalsobani/vishal/tarzanskiils')

from package import fibo
from package import filehandling

if __name__ == '__main__':
    result = fibo.fibo_1(10)
    filehandling.create_file(result)
    filehandling.read_file(result)

