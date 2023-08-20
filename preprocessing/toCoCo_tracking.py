import os
import json

def convert_kitti_to_coco(kitti_labels_dir, output_dir, image_dirs, data_type):
    coco_data = {
        "info": {},
        "licenses": [],
        "categories": [
            {"id": 1, "name": "Car"},
            {"id": 2, "name": "Van"},
            {"id": 3, "name": "Truck"},
            {"id": 4, "name": "Pedestrian"},
            {"id": 5, "name": "Person_sitting"},
            {"id": 6, "name": "Cyclist"},
            {"id": 7, "name": "Tram"},
            {"id": 8, "name": "Misc"}
        ],
        "images": [],
        "annotations": []
    }

    # Read and process each KITTI label file for the given image files
    for image_dir in image_dirs:

        if ( image_dir == ".DS_Store" ):continue

        with open(os.path.join(kitti_labels_dir, image_dir + ".txt"), "r") as file:
            lines = file.readlines()

            frame_annotation = {}  # Store the annotation info for each frame

            for line in lines:
                elements = line.strip().split()
                frame = int(elements[0])
                frame = "{:06d}".format(frame)  # Pad with leading zeros, e.g. "000001

                if frame not in frame_annotation:
                    image_id = image_dir + "_" + frame
                    file_name = image_id + ".png"
                    image_data = {
                        "id": image_id,  # Use the next available image ID
                        "width": 1280,  # 1382 / 1280
                        "height": 384,  # 512 / 384
                        "file_name": file_name, 
                    }

                    coco_data["images"].append(image_data)
                    frame_annotation[frame] = True  # Mark this frame as processed

                track_id = int(elements[1])
                class_name = elements[2]
                truncation = float(elements[3])
                occlusion = int(elements[4])
                alpha = float(elements[5])
                bbox = [float(coord) for coord in elements[6:10]]
                dimensions = [float(dim) for dim in elements[10:13]]
                location = [float(coord) for coord in elements[13:16]]
                rotation_y = float(elements[16])

                category_id = None
                for category in coco_data["categories"]:
                    if category["name"] == class_name:
                        category_id = category["id"]
                        break

                if category_id is not None:
                    annotation = {
                        "id": len(coco_data["annotations"]) + 1,
                        "image_id": image_id,
                        "category_id": category_id,
                        "bbox": [bbox[0], bbox[1], bbox[2] - bbox[0], bbox[3] - bbox[1]],
                        "area": (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]),
                        "iscrowd": 0,
                        "truncated": truncation,
                        "occluded": occlusion,
                        "alpha": alpha,
                        "dimensions": dimensions,
                        "location": location,
                        "rotation_y": rotation_y,
                    }

                    coco_data["annotations"].append(annotation)

    # Save the coco_data to a JSON file in the specified output directory
    file_name = f"kitti_coco_format_{data_type}.json"
    output_file = os.path.join(output_dir, file_name)
    with open(output_file, "w") as json_file:
        json.dump(coco_data, json_file)

if __name__ == "__main__":
    dir = "data/"
    test_image_path = dir + "test/image_02/"
    test_label_path = dir + "test/label_02/"
    test_coco_path = dir + "test/coco/"

    # Create directories for train and val if they don't exist
    os.makedirs(test_coco_path, exist_ok=True)

    # Get the list of image files for train and val sets
    test_image_files = os.listdir(test_image_path)

    # Convert test set to COCO format and save as JSON
    convert_kitti_to_coco(test_label_path, test_coco_path, test_image_files, "test")
