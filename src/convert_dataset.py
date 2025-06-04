import os
import shutil
from tqdm import tqdm
from pycocotools.coco import COCO

def convert_coco_to_yolo(coco_json_path, image_dir, output_dir):
    coco = COCO(coco_json_path)
    img_ids = coco.getImgIds()

    categories = coco.loadCats(coco.getCatIds())
    cat2id = {cat['id']: i for i, cat in enumerate(categories)}

    os.makedirs(f"{output_dir}/images", exist_ok=True)
    os.makedirs(f"{output_dir}/labels", exist_ok=True)

    for img_id in tqdm(img_ids, desc=f"Converting {os.path.basename(coco_json_path)}"):
        img_info = coco.loadImgs(img_id)[0]
        img_filename = img_info['file_name']
        h, w = img_info['height'], img_info['width']

        src_img_path = os.path.join(image_dir, img_filename)
        dst_img_path = os.path.join(output_dir, "images", img_filename)
        if not os.path.exists(src_img_path):
            continue
        shutil.copy2(src_img_path, dst_img_path)

        ann_ids = coco.getAnnIds(imgIds=img_id)
        anns = coco.loadAnns(ann_ids)
        label_path = os.path.join(output_dir, "labels", img_filename.rsplit('.', 1)[0] + ".txt")
        with open(label_path, "w") as f:
            for ann in anns:
                bbox = ann['bbox']
                x_center = (bbox[0] + bbox[2] / 2) / w
                y_center = (bbox[1] + bbox[3] / 2) / h
                width = bbox[2] / w
                height = bbox[3] / h
                yolo_cat_id = cat2id[ann['category_id']]
                f.write(f"{yolo_cat_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")
