import subprocess
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("directory", help='the location of the folder of images')
parser.add_argument("save", help='directory to save images')
parser.add_argument("height", help='height of cropped image')
parser.add_argument("width",help='width of cropped image')
args = parser.parse_args()

directory = args.directory
save = args.save
height, width = args.height, args.width

image_types = ('.jpg', '.png')
image_files = []
log = []

for file in os.listdir(directory):
    if file.endswith(image_types):
        image_files.append(file)

print(image_files)

try:
    # attempt to create directory to save output
    os.mkdir(directory+'/'+save)
    print('Directory ', directory+'/'+save, ' created')
except FileExistsError:
    print(directory+'/'+save, ' already exists')


for file_name in image_files:
    sp = directory +'/' + file_name + ' ' + directory+'/'+save + ' ' + height + ' ' + width    
    subprocess.Popen("python crop.py " + sp) 
    log.append(file_name)

log_txt = open("log.txt","w") 
log_txt.write(str(log)) 
log_txt.close() 