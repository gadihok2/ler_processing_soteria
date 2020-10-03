import os
import sys
import shutil
from shutil import copyfile

#Inefficient program that does the job. Needs more functions. Also, too many 'continue' keywords. Understand their meaning and delete the ones not needed

def main(folder):
	for filename in os.listdir(folder):
		if filename.startswith('ML', 0, 2):
			html = 'html'
			txt = 'txt'
			if html in filename:
				old = folder + "/" + filename
				new = folder + "/" + filename.replace(".html",".txt")
				os.rename(old,new)
				filename = filename.replace(".html",".txt")
			elif txt not in filename:
				path_1 = folder + "/" + filename + "/" + filename + ".txt"
				path_dir = folder + "/" + 'LER_text_files'
				if os.path.isdir(path_dir):
					path_new_1 = path_dir + '/' + filename + ".txt"
					if os.path.isfile(path_new_1):
						continue
					else:
						copyfile(path_1, path_new_1)
						continue
				else:
					os.mkdir(path_dir)

					path_new_1 = path_dir + '/' + filename + ".txt"
					if os.path.isfile(path_new_1):
						continue
					else:
						copyfile(path_1, path_new_1)
						continue

			filename_strip = filename.replace(".txt","")
			path = folder + "/" + filename_strip
			name = filename_strip[-4:]
			if os.path.isdir(path):
				path_old_1 = folder + "/" + filename
				os.remove(path_old_1)
				continue
			else:
				os.mkdir(path)
				path_old = folder + "/" + filename
				path_new = folder + "/" + filename_strip + '/' + filename
				shutil.move(path_old,path_new)
				open(path+'/out_'+name+'.txt','w+')
				open(path+'/anchor_'+name+'.json','w+')
				#open(path+'/notes_'+name+'.txt','w+')


				path_dir = folder + "/" + 'LER_text_files'
				if os.path.isdir(path_dir):
					path_new_2 = path_dir + '/' + filename
					if os.path.isfile(path_new_2):
						continue
					else:
						copyfile(path_new, path_new_2)
						continue
				else:
					os.mkdir(path_dir)

					path_new_2 = path_dir + '/' + filename
					if os.path.isfile(path_new_2):
						continue
					else:
						copyfile(path_new, path_new_2)
						continue
		else:
			continue
if __name__ == '__main__':
	main(sys.argv[1])
