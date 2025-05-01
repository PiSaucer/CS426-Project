#!/usr/bin/env python3

import os
import zipfile

def zip_files():
    # Output zip filename
    zip_filename = "project.zip"
    
    # Files and directories to include
    items_to_zip = [
        "diabetes.ipynb",
        "README.md",
        "requirements.txt",
        # "Abstract.pdf",
        "img/",
        "all_data/"
        "diabetes_data/"
    ]
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for item in items_to_zip:
            if item.endswith('/'):  # It's a directory
                for root, dirs, files in os.walk(item.rstrip('/')):
                    for file in files:
                        if file.lower() == ".ds_store":  # Ignore .DS_Store files
                            continue
                        file_path = os.path.join(root, file)
                        # Add file with path relative to current directory
                        zipf.write(file_path, file_path)
                    print(f"Added directory: {root}")
            else:  # It's a file
                if os.path.exists(item):
                    if os.path.basename(item).lower() == ".ds_store":  # Ignore .DS_Store files
                        continue
                    zipf.write(item)
                    print(f"Added file: {item}")
                else:
                    print(f"Warning: {item} not found!")
    
    print(f"Successfully created {zip_filename}")

if __name__ == "__main__":
    zip_files()
    