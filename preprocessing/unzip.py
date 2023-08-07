import os
import zipfile

def unzip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

if __name__ == "__main__":
    data_dir = "data"
    image_zip_path = os.path.join(data_dir, "data_object_image_2.zip")
    label_zip_path = os.path.join(data_dir, "data_object_label_2.zip")
    
    # Check if input file names are as expected
    assert os.path.basename(image_zip_path) == "data_object_image_2.zip", "Incorrect image zip file name"
    assert os.path.basename(label_zip_path) == "data_object_label_2.zip", "Incorrect label zip file name"

    # Unzip image data
    unzip_file(image_zip_path, data_dir)
    
    # Unzip label data
    unzip_file(label_zip_path, data_dir)

    print("Image and label data extraction complete.")

    