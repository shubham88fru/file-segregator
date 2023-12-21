'''
import os
import shutil

def organize_files(src_dir, dest_base_dir):
    # Create destination directories if not exists
    for file_type in set(file.split('.')[-1] for file in os.listdir(src_dir)):
        dest_dir = os.path.join(dest_base_dir, file_type.upper())
        os.makedirs(dest_dir, exist_ok=True)

    # Move files to their respective directories
    for file in os.listdir(src_dir):
        if os.path.isfile(os.path.join(src_dir, file)):
            file_type = file.split('.')[-1].upper()
            dest_dir = os.path.join(dest_base_dir, file_type)
            shutil.move(os.path.join(src_dir, file), os.path.join(dest_dir, file))

if __name__ == "__main__":
    source_directory = "."  # Change this to the path of your source directory
    destination_base_directory = "./dest"  # Change this to the path of your destination directory

    organize_files(source_directory, destination_base_directory)
    print("Files organized successfully.")
'''

'''
import os
import shutil

def organize_files(src_dir, dest_base_dir, script_file):
    # Create destination directories if not exists
    for file_type in set(file.split('.')[-1] for file in os.listdir(src_dir)):
        dest_dir = os.path.join(dest_base_dir, file_type.upper())
        os.makedirs(dest_dir, exist_ok=True)

    # Move files to their respective directories
    for file in os.listdir(src_dir):
        file_path = os.path.join(src_dir, file)
        if os.path.isfile(file_path) and file != script_file:
            file_type = file.split('.')[-1].upper()
            dest_dir = os.path.join(dest_base_dir, file_type)
            shutil.move(file_path, os.path.join(dest_dir, file))

if __name__ == "__main__":
    source_directory = "."  # Change this to the path of your source directory
    destination_base_directory = "./dest"  # Change this to the path of your destination directory
    script_file_name = "file_segregator.py"  # Change this to the actual name of your script file

    organize_files(source_directory, destination_base_directory, script_file_name)
    print("Files organized successfully.")
'''

import os
import shutil
import csv

def organize_files(src_dir, dest_base_dir, script_file):
    # Create destination directories if not exists
    for file_type in set(file.split('.')[-1] for file in os.listdir(src_dir)):
        dest_dir = os.path.join(dest_base_dir, file_type.upper())
        os.makedirs(dest_dir, exist_ok=True)

    # Move files to their respective directories and count file types
    file_counts = {}
    for file in os.listdir(src_dir):
        file_path = os.path.join(src_dir, file)
        if os.path.isfile(file_path) and file != script_file:
            file_type = file.split('.')[-1].upper()
            dest_dir = os.path.join(dest_base_dir, file_type)
            shutil.move(file_path, os.path.join(dest_dir, file))

            # Count the file type
            file_counts[file_type] = file_counts.get(file_type, 0) + 1

    # Write file counts to a CSV file
    csv_file_path = os.path.join(dest_base_dir, "file_counts.csv")
    with open(csv_file_path, mode='w', newline='') as csv_file:
        fieldnames = ['File Type', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for file_type, count in file_counts.items():
            writer.writerow({'File Type': file_type, 'Count': count})

    print(f"Files organized successfully. File counts written to {csv_file_path}.")

if __name__ == "__main__":
    source_directory = "."  # Change this to the path of your source directory
    destination_base_directory = "./dest"  # Change this to the path of your destination directory
    script_file_name = "file_segregator.py"  # Change this to the actual name of your script file

    organize_files(source_directory, destination_base_directory, script_file_name)
