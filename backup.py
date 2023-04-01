
import os
import sys
import time
import shutil

SRC_PATH = "D:\\FJU Course Material\\JAVA"
DEST_PATH = "D:\\tomasioDir\\"
CURRENT_TIME = time.strftime("%m-%d-%Y", time.localtime())
FILE_NAME = DEST_PATH + CURRENT_TIME + "_backup"


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
        print(DEST_PATH + " : this directory is now available")
    elif not os.path.isdir(DEST_PATH):
        print("The destination is not a directory")
        sys.exit(1)
    else:
        pass


def copyDir():
    shutil.make_archive(FILE_NAME, 'zip', SRC_PATH)


def checkResult():
    if os.path.exists(FILE_NAME+'.zip'):
        print("Backup succeeded")
    else:
        print("Backup failed")


def checkResult():
    if os.path.exists(FILE_NAME+'.zip'):
        print("Backup succeeded")
    else:
        print("Backup failed")


def main():
    print("start working")
    checkSrc()
    checkDest()
    copyDir()
    checkResult()
    sys.exit(0)


if __name__ == '__main__':
    main()
