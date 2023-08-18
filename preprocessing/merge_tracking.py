import os
import shutil

# Set the source and target directory paths
source_directory = "data/data_tracking_image_2/training/image_02"
target_directory = "data/data_tracking_image_2/training/images"

# Create the target directory if it doesn't exist
os.makedirs(target_directory, exist_ok=True)

# Traverse through all subdirectories
for folder_name in os.listdir(source_directory):
    folder_path = os.path.join(source_directory, folder_name)
    
    if os.path.isdir(folder_path):
        # Process all PNG files within the folder
        for file_name in os.listdir(folder_path):
            if file_name.lower().endswith(".png"):
                source_file_path = os.path.join(folder_path, file_name)
                target_file_name = f"{folder_name}_{file_name}"
                target_file_path = os.path.join(target_directory, target_file_name)
                
                # Avoid duplicates by appending a number if the file already exists
                count = 1
                while os.path.exists(target_file_path):
                    target_file_name = f"{folder_name}_{count:06d}.png"
                    target_file_path = os.path.join(target_directory, target_file_name)
                    count += 1
                
                # Copy the file
                shutil.copy(source_file_path, target_file_path)

print("Merging image files complete")
