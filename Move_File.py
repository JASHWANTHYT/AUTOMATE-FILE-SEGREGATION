import os
import shutil

from_dir = "Downloads"
to_dir = "Document_Files"

# Get the list of files in the source path
list_of_files = os.listdir(from_dir)
print("Files in the source path:")
print(list_of_files)

# Traverse through the list of files and move them
for file_name in list_of_files:
    # Capture the name and extension of each file
    name, extension = os.path.splitext(file_name)
    
    # Check if the extension is blank or not in the allowed extensions list
    if extension == '' or extension not in ['.txt', '.doc', '.docx', '.pdf']:
        continue

    # Create directory paths
    path1 = os.path.join(from_dir, file_name)
    path2 = os.path.join(to_dir, extension[1:].upper())  # Remove the leading dot and convert to uppercase
    path3 = os.path.join(to_dir, extension[1:].upper(), file_name)

    # Check if the destination path exists
    if os.path.exists(path2):
        print(f"Moving {file_name} to {path2}")
        shutil.move(path1, path3)
    else:
        # If the destination path doesn't exist, create it and then move the file
        os.makedirs(path2)
        print(f"Moving + file_name + path2")
        shutil.move(path1, path3)

print("Files moved successfully.")
