#file exists to ensure dota and yolo combatability

import os
import cv2
import numpy as np

# map class to numbers 
CLASS_NAMES = [
    'plane', 'ship', 'storage-tank', 'baseball-diamond', 'tennis-court',
    'basketball-court', 'ground-track-field', 'harbor', 'bridge',
    'large-vehicle', 'small-vehicle', 'helicopter', 'roundabout',
    'soccer-ball-field', 'swimming-pool', 'container-crane'
]

#take one label file, its image and where to save new label 
def convert_dota_to_yolo_obb(dota_label_path, image_path, output_path):
    img = cv2.imread(image_path) #open image to get w and h
                                 #dota coordinates in pixels, YOLO need fractions
                                 #hence need img size to div by 
    if img is None:
        print(f"Could not read image: {image_path}")#error handling
        return
    h, w = img.shape[:2]

    with open(dota_label_path, 'r') as f:
        lines = f.readlines()

    yolo_lines = []
    for line in lines:
        line = line.strip()#first 2 lines are metadata, strip them jarvis 
        if not line or line.startswith('imagesource') or line.startswith('gsd'):
            continue 
        parts = line.split()
        if len(parts) < 9:
            continue

        coords = list(map(float, parts[:8]))#split 4 corner points & class name
        class_name = parts[8].lower()

        if class_name not in CLASS_NAMES:
            continue
        class_id = CLASS_NAMES.index(class_name)

        # normalise 4 corner points
        points = np.array(coords, dtype=np.float32).reshape(4, 2)#conv to yolo format
        points[:, 0] /= w #ref to div in line 17
        points[:, 1] /= h

        # Write as: class_id x1 y1 x2 y2 x3 y3 x4 y4
        pts_str = ' '.join([f'{p:.6f}' for p in points.flatten()])
        yolo_lines.append(f'{class_id} {pts_str}')#what yolov8 obb expects

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write('\n'.join(yolo_lines))


def convert_split(images_dir, labels_dir, output_labels_dir):#loop thru all in folder
                                                             #find matching label file
                                                             #call convert function on each pair
    image_files = [f for f in os.listdir(images_dir) if f.endswith('.png')]
    print(f"Converting {len(image_files)} images...")

    for img_file in image_files:
        name = os.path.splitext(img_file)[0]
        image_path = os.path.join(images_dir, img_file)
        label_path = os.path.join(labels_dir, name + '.txt')
        output_path = os.path.join(output_labels_dir, name + '.txt')

        if not os.path.exists(label_path):
            print(f"No label found for {img_file}, skipping")
            continue

        convert_dota_to_yolo_obb(label_path, image_path, output_path)

    print("Done.")


if __name__ == '__main__':
    BASE = r'C:\Users\natha\OneDrive\Desktop\GITHUB\satDetection\data'
#call for train and val
#pointning at right folders

    convert_split(
        images_dir=os.path.join(BASE, 'train', 'trainImages'),
        labels_dir=os.path.join(BASE, 'train', 'trainLabels'),
        output_labels_dir=os.path.join(BASE, 'train', 'trainLabels_yolo')
    )

    convert_split(
        images_dir=os.path.join(BASE, 'val', 'valImages'),
        labels_dir=os.path.join(BASE, 'val', 'valLabels'),
        output_labels_dir=os.path.join(BASE, 'val', 'valLabels_yolo')
    )