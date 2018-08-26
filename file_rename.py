import os, glob, shutil
from os import path
import sys


folder_name = sys.argv[1]
all_files = glob.glob( folder_name + '/*.jpg')
print(all_files)



for index, filename in enumerate(all_files):

    # file rename
    current_filename = path.realpath(filename)
    print(current_filename)
    new_filename = folder_name + '/' + str(index + 1) + '.jpg'
    os.rename(current_filename, new_filename)

    print('renamed {0} files'.format(index+1))
