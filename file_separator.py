import os, shutil

audio = ('.mp3','.m4a','.wav','.flac')
video = ('.mp4','.mkv','.MKV','.flv','.mpeg')
document = ('.docx','.pdf','.txt')
image = ('.png','.jpeg')
executable = ('.exe','.com')

path = input('enter directory path : ')

os.chdir(path)

data = os.walk(path)

def copy_file(folder_name,file_path,file):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    shutil.copy(os.path.join(file_path,file),folder_name + '/' + file)

for file_path, _, files in data:
    if files:
        for file in files:
            _, extension = os.path.splitext(file)
            if extension in audio:
                copy_file('audio',file_path,file)
            if extension in video:
                copy_file('video',file_path,file)
            if extension in document:
                copy_file('document',file_path,file)
            if extension in image:
                copy_file('image',file_path,file)
            if extension in executable:
                copy_file('executable',file_path,file)