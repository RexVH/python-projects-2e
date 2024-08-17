import os

full_path = 'c:/Users/rexyo/OneDrive/Documents/GitHub/python-projects-2e/ascii/data/input/the_file_name.jpg'
file_name = os.path.basename(full_path)
print("The file name: ", file_name)

# Get the file extension
_, file_extension = os.path.splitext(full_path)
print("File extension:", file_extension)

# Get the file name without the extension
file_name_without_extension = os.path.splitext(os.path.basename(full_path))[0]
print("File name without extension:", file_name_without_extension)

# Get the file name and extension in one:
file_name_without_extension = os.path.splitext(os.path.basename(full_path))
print("Both - File name without extension:", file_name_without_extension[0])
print("Both - File extension only:", file_name_without_extension[1])