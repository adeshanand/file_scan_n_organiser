import os, shutil


file_extensions = {
    'audio' : ('.mp3','.m4a','.wav','.flac'),
    'video' : ('.mp4','.mkv','.MKV','.flv','.mpeg'),
    'document' : ('.docx','.pdf','.txt'),
    'image' : ('.png','.jpeg'),
    'executable' : ('.exe','.com')
}

def copy_file(folder_name,file_path,file):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    if not os.path.exists(folder_name + '/' + file):
        shutil.copy(os.path.join(file_path,file),folder_name + '/' + file)

scan_folder_path = input('enter directory path : ')
os.chdir(scan_folder_path)
data = os.walk(scan_folder_path)

for file_path, _, files in data:
    if files:
        for file in files:
            _, extension = os.path.splitext(file)
            for file_extension_format, file_extension_values in file_extensions.items():
                if extension in file_extension_values:
                    copy_file(file_extension_format,file_path,file)
