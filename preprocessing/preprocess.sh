# Step 1: Unzip files
python preprocessing/unzip.py

# Step 2: Split to train/val sets
python preprocessing/split.py --split 0.9

# Step 3: Transfer KITTI annotation to COCO format
python preprocessing/toCOCO.py
