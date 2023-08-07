import os
import zipfile
import shutil
import random
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract and split data for training and validation.")
    parser.add_argument("--split", type=float, default=0.8, help="Fraction of data to allocate for training (default: 0.8)")
    args = parser.parse_args()

    data_dir = "data"
    
    output_train_image_path = os.path.join(data_dir, "train/image")
    output_train_label_path = os.path.join(data_dir, "train/label")
    output_val_image_path = os.path.join(data_dir, "val/image")
    output_val_label_path = os.path.join(data_dir, "val/label")

    # Create directories for train and val if they don't exist
    os.makedirs(output_train_image_path, exist_ok=True)
    os.makedirs(output_train_label_path, exist_ok=True)
    os.makedirs(output_val_image_path, exist_ok=True)
    os.makedirs(output_val_label_path, exist_ok=True)

    train_image_path = os.path.join(data_dir, "training/image_2")
    train_label_path = os.path.join(data_dir, "training/label_2")

    # Read and shuffle image files
    training_image_files = os.listdir(train_image_path)
    num_images = len(training_image_files)
    shuffled_indices = list(range(num_images))

    # You can use any randomization method you prefer here
    # For simplicity, let's assume the list is randomly shuffled
    random.shuffle(shuffled_indices)

    # Calculate the index to split the data
    split_idx = int(num_images * args.split)

    for i, idx in enumerate(shuffled_indices):
        image_file = training_image_files[idx]
        image_path = os.path.join(train_image_path, image_file)

        # 레이블 정보 불러오기
        label_file = os.path.join(train_label_path, image_file.replace(".png", ".txt"))

        if i < split_idx:
            # Save to training directories
            shutil.copy(image_path, os.path.join(output_train_image_path, image_file))
            shutil.copy(label_file, os.path.join(output_train_label_path, image_file.replace(".png", ".txt")))
        else:
            # Save to validation directories
            shutil.copy(image_path, os.path.join(output_val_image_path, image_file))
            shutil.copy(label_file, os.path.join(output_val_label_path, image_file.replace(".png", ".txt")))

    print(f"Data split into training ({args.split:.2f}) and validation ({1 - args.split:.2f}).")