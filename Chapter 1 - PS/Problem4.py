import os

# Specify the directory path (for current directory use '.')
directory = '/Movies'

# Get the list of files and directories
contents = os.listdir(directory)

# Print the contents
print("Contents of the directory are:")
for item in contents:
    print(item)
