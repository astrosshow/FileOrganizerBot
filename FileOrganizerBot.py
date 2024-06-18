# imports the os and shutil modules 
# os module provides a way of using operating system dependent functionality
# shutil module provides a higher level interface that is easier to use
# os.path module provides functions for interacting with the file system
import os
import shutil

# Creates a variable called download_path and sets it to the path of the Downloads folder
# os.path. returns the path 
# expanduser() method returns the home directory of the user
download_path = os.path.expanduser('~/Downloads')

# Creates a variable called files and sets it to a list of all the files in the Downloads folder
# os.listdir() method returns a list of all the files in the specified directory
# os.path.isfile() method returns True if the specified path is an existing regular file
# os.path.join() method joins one or more path components intelligently
files = [f for f in os.listdir(download_path) if os.path.isfile(os.path.join(download_path, f))]

# Loops through each file in the files list
# os.path.splitext() method splits the path name into a pair root and extension
# os.path.join() method joins one or more path components intelligently
# os.path.exists() method returns True if the specified path exists
# os.makedirs() method creates a directory
# shutil.move() method moves a file to a new location
for file in files:

    file_extension = os.path.splitext(file)[1][1:]

    new_path = os.path.join(download_path, file_extension)

    if not os.path.exists(new_path):
        os.makedirs(new_path)

    current_file_path = os.path.join(download_path, file)
    new_file_path = os.path.join(new_path, file)

    shutil.move(current_file_path, new_file_path)