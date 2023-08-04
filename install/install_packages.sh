#!/bin/bash

# Move back to the previous directory
cd ..

# Install specific PyTorch and torchvision versions
conda install -n myenv -c pytorch pytorch==2.0.1 torchvision==0.15.2

# Install openmim, mmengine, and mmcv
pip install openmim "mmengine>=0.7.0" "mmcv>=2.0.0rc4"

# Clone mmdetection repository and install it in editable mode
rm -rf mmdetection
git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection
pip install -e .

# Move back to the previous directory
cd ..
