import os
import glob

folder_path = os.getcwd()

# Use glob to get a list of file names matching the pattern
files = glob.glob(folder_path + "\*.xml")
print(files)

# Iterate through each file and rename it
for old_file_path in files:
    # Extract the file name and extension
    old_filename, old_extension = os.path.splitext(os.path.basename(old_file_path))

    # Create the new file name by adding the suffix
    new_filename = old_filename

    # Create the new file path
    new_file_path = os.path.join(folder_path, new_filename)

    # Rename the file
    os.rename(old_file_path, new_file_path)

print("Files renamed successfully.")