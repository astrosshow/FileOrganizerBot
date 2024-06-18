import os
import shutil

download_path = os.path.expanduser('~/Downloads')

files = [f for f in os.listdir(download_path) if os.path.isfile(os.path.join(download_path, f))]

for file in files:

    file_extension = os.path.splitext(file)[1][1:]

    new_path = os.path.join(download_path, file_extension)

    if not os.path.exists(new_path):
        os.makedirs(new_path)

    current_file_path = os.path.join(download_path, file)
    new_file_path = os.path.join(new_path, file)

    shutil.move(current_file_path, new_file_path)