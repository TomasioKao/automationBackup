
import os
import sys


SRC_PATH = "D:\\FJU Course Material\\JAVA"
DEST_PATH = "C:\\Users\\tomas"


def checkSrc():
    if not os.path.exists(SRC_PATH):
        print(SRC_PATH)
        print("Source path does not exist")
        sys.exit(1)
    else:
        pass


def checkDest():
    if not os.path.exists(DEST_PATH):
        print("This destination path does not exist so system is creatng directory...")
        os.mkdir(DEST_PATH)
    elif not os.path.isdir(DEST_PATH):
        print("The destination is not a directory")
        sys.exit(1)
    else:
        pass


def main():
    checkSrc()
    checkDest()


if __name__ == '__main__':
    main()
