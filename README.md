## 1. Getting Started

Clone the repo:

  ```bash
  git clone https://github.com/bigmb/Unet-Segmentation-Pytorch-Nest-of-Unets.git
  ```

## 2. Requirements

```
python>=3.6
torch>=0.4.0
torchvision
torchsummary
tensorboardx
natsort
numpy
pillow
scipy
scikit-image
sklearn
```
Install all dependent libraries:
  ```bash
  pip install -r requirements.txt
  ```
## 3. Run the file

Add all your folders to this line 106-113
```
t_data = '' # Input data
l_data = '' #Input Label
test_image = '' #Image to be predicted while training
test_label = '' #Label of the prediction Image
test_folderP = '' #Test folder Image
test_folderL = '' #Test folder Label for calculating the Dice score
 ```