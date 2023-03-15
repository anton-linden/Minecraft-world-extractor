import os
import shutil
import zipfile
import datetime

# Get the current date and time
now = datetime.datetime.now()
date_time = now.strftime("%Y%m%d%H%M")

# Create a temporary folder for the saves
temp_folder = os.path.join(os.getcwd(), "temp")
os.makedirs(temp_folder, exist_ok=True)

# Copy the saves folders to the temp folder
saves_folder = os.path.join(os.getenv('APPDATA'), '.minecraft', 'saves')
shutil.copytree(saves_folder, os.path.join(temp_folder, 'saves'))

# Zip the temp folder
zip_name = "My minecraft worlds - " + date_time + ".zip"
with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zip_file:
    for foldername, subfolders, filenames in os.walk(temp_folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            zip_file.write(file_path, os.path.relpath(file_path, temp_folder))

# Delete the temp folder
shutil.rmtree(temp_folder)

print("Backup complete: " + zip_name)
