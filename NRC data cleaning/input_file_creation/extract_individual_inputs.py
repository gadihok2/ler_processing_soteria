import os
import sys
import shutil
from shutil import copyfile

def path_maker(path,file):
    new = path + '/' + file
    return new

def main(master_folder):
    path_output_folder = path_maker(master_folder,'individual inputs')
    if os.path.isdir(path_output_folder) == False:
        os.mkdir(path_output_folder)
    i = 0
    for folder in os.listdir(master_folder):
        if path_maker(master_folder,folder) == path_output_folder:
            continue
        elif os.path.isdir(path_maker(master_folder,folder)) == False:
            continue
        else:
            for filename in os.listdir(path_maker(master_folder,folder)):
                json = 'json'
                if json in filename:
                    path_0 = path_maker(master_folder,folder)
                    path_1 = path_maker(path_0,filename)
                    path_2 = path_maker(path_output_folder,filename)
                    copyfile(path_1, path_2)
                    i += 1
                    print i
                else:
                    continue


if __name__ == '__main__':
	main(sys.argv[1])
