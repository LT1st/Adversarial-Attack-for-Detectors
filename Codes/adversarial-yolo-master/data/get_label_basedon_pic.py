import os
import shutil

# 获取pos文件夹下所有文件的文件名
pos_folder = "pos"
pic_list = os.listdir(pos_folder)

# 将所有元素的文件名后缀.png换成.txt为后缀
pic_list = [os.path.splitext(pic)[0] + ".txt" for pic in pic_list]

# 创建新的文件夹yolo-labels
labels_folder = os.path.join(pos_folder, "yolo-labels")
if not os.path.exists(labels_folder):
    os.mkdir(labels_folder)

# 从annotations文件夹中获取对应文件，并统一复制到yolo-labels中
ann_folder = "annotations"
for pic in pic_list:
    ann_file = os.path.join(ann_folder, pic)
    if os.path.exists(ann_file):
        label_file = os.path.join(labels_folder, pic)
        shutil.copy(ann_file, label_file)
    else:
        print(f"File {ann_file} not found.")
