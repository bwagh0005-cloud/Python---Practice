# program with commemt



import os
# specific the directory path
directory_path = '.'
# list all files and directories
try:
    contents = os.listdir(directory_path) 
    print("Contents of the directory:") #current directory
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("Permission denied to access the directory.")