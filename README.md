# Object Detection with MMDetection for KITTI Dataset

## Introduction

Welcome to this repository, which focuses on:

- Training a 2D object detector for the KITTI dataset.
- Utilizing the powerful "MMDetection" framework for 2D object detection.  

<div style="max-width: 100%;">
    <img src="kitti.png" alt="KITTI Dataset" style="max-width: 100%; height: auto;">
</div>


For more detailed information, please refer to the official MMDetection documentation:
[https://mmdetection.readthedocs.io/en/latest/](https://mmdetection.readthedocs.io/en/latest/)

<div style="max-width: 80%;">
    <img src="mmdet-logo.png" alt="MMdetection-logo" style="max-width: 80%; height: auto;">
</div>


## 1. Getting Started

Clone the repo:

  ```bash
  git clone https://github.com/mingkyun/kitti_mmdetection
  ```

  
Download Kitti Dateset from following link  
https://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=2d  

**Download left color images of object data set (12 GB)**   
**Download training labels of object data set (5 MB)** 

Then put both both files at ./KITTI_MMDETECTION/data/

```
└── KITTI_MMDETECTION
    └── data
        ├── data_object_image_2.zip
        └── data_object_label_2.zip
```

## 2. Requirements

```
python>=3.7
PyTorch>=1.8
CUDA >=9.2
mmengine>=0.7.0
mmcv >= 2.0.0
```
Install all dependent libraries:  

  ```bash
  install/install_packages.sh
  ```
or
  ```bash
  python install/install_mmdetection.py
  ```
for users who do not have administrator privileges


## 3. Preprocessing

Execute following command for all preprocessing procedure at once 

  ```bash
  preprocessing/preprocess.sh
  ```

or execute following commands at /kitti_mmdetection/ 

(1) unzip files

  ```bash
  python preprocessing/unzip.py   
  ```

(2) split to train/val sets (default split rate 0.8)

  ```bash
  python preprocessing/split.py --split 0.9 
  ```

(3) transfer kitti annotation to COCO format

  ```bash
  python preprocessing/toCOCO.py
  ```

After all process done, your directory should look like this

```
KITTI_MMDETECTION
├── data
│   ├── data_object_image_2.zip
│   ├── data_object_label_2.zip
│   ├── image
│   │   ├── image_file_1.png
│   │   ├── image_file_2.png
│   │   └── ...
│   ├── label
│   │   ├── label_file_1.txt
│   │   ├── label_file_2.txt
│   │   └── ...
│   ├── train
│   │   ├── image
│   │   │   ├── image_file_1.png
│   │   │   ├── image_file_2.png
│   │   │   └── ...
│   │   ├── label
│   │   │   ├── label_file_1.txt
│   │   │   ├── label_file_2.txt
│   │   │   └── ...
│   │   └── coco
│   │       └── kitti_coco_format_train.json
│   └── val
│       ├── image
│       │   ├── image_file_3.png
│       │   ├── image_file_8.png
│       │   └── ...
│       ├── label
│       │   ├── label_file_3.txt
│       │   ├── label_file_8.txt
│       │   └── ...
│       └── coco
│           └── kitti_coco_format_val.json
├── mmdetection
├── install
├── preprocessing
└── train

```

## 4. Training

(Recommended)
Follow procedure at train/build_config.ipynb

After making config file, train model by following command (Modify your path)

  ```bash
  python mmdetection/tools/train.py mmdetection/configs/efficientnet/retinanet_effb3_fpn_8xb4-crop896-1x_kitti.py

  ```

  ## 5. Test  
    
You can visualize your model's output at train/test.ipynb


## Citation

```
@article{mmdetection,
  title   = {{MMDetection}: Open MMLab Detection Toolbox and Benchmark},
  author  = {Chen, Kai and Wang, Jiaqi and Pang, Jiangmiao and Cao, Yuhang and
             Xiong, Yu and Li, Xiaoxiao and Sun, Shuyang and Feng, Wansen and
             Liu, Ziwei and Xu, Jiarui and Zhang, Zheng and Cheng, Dazhi and
             Zhu, Chenchen and Cheng, Tianheng and Zhao, Qijie and Li, Buyu and
             Lu, Xin and Zhu, Rui and Wu, Yue and Dai, Jifeng and Wang, Jingdong
             and Shi, Jianping and Ouyang, Wanli and Loy, Chen Change and Lin, Dahua},
  journal= {arXiv preprint arXiv:1906.07155},
  year={2019}
}
```

## License

This project is released under the [Apache 2.0 license](LICENSE).
