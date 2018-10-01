import sys
from titlecase import titlecase

def convert(str):
    return titlecase(str)

def main(str):    
    print(convert(str))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
