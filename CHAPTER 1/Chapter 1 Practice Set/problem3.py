''' write a progam to print the content of 
the directory an directory using the direct module
 .Search online for the function which does that.'''

import os

# Specify the directory path
directory_path = '/new folder'  # Current directory

# List all files and directories
try:
    contents = os.listdir(directory_path)
    print("Contents of the directory:")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("Permission denied to access the directory.")
