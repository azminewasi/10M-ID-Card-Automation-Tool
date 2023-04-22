import os

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f'Folder {folder_name} created successfully!')
    else:
        print(f'Folder {folder_name} already exists.')