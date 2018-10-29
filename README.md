# Geosr - A Computer Vision Package for Remote Sensing Image Super Resolution
High Resolution: PSNR            |  Low Resolution: 33.32 |  Super Resolution: 36.26
:-------------------------:|:-------------------------:|:-------------------------:
![hr_img2](/uploads/78c541a647afdb8820cfa0b682a96820/hr_img2.png)  |  ![lr_img2](/uploads/ddb75a8f6e9c7e498c89ac02deeb69e0/lr_img2.png)  |  ![sr_img2](/uploads/55831ea1829bcb47b65d6911ef60d783/sr_img2.png)

## Structure of directories
### sub directories
```
Geosr
├── src
│   └── data_dir
├── dataset
│   └── save_dir
│       ├── all.csv
│       ├── train.csv
│       ├── test.csv
│       ├── val.csv
│       ├── statistic.csv
│       └── image
│           ├── train
│           ├── test
│           └── val
├── logs
│   ├── curve
│   ├── raw
│   └── statistic
│       ├── model_info.csv
│       ├── train.csv
│       ├── test.csv
│       └── val.csv
├── model_zoo
│   └── trained_model
├── archs
│   ├── blockunits.py
│   ├── drcn.py
│   ├── espcn.py
│   ├── fsrnn.py
│   ├── rednet.py
│   ├── srcnn.py
│   ├── srdensenet.py
│   └── vdsr.py
├── utils
│   ├── extractor.py
│   ├── metrics.py
│   ├── preprocessor.py
│   ├── runner.py
│   └── vision.py
...
```
#### directories
* `./src/data_dir`: original images
* `./dataset/save_dir`: croped images and related information
* `./model_zoo`: pretrained and trained models with related information
* `./archs`: model architectures
* `./utils`: utilities

#### scripts
* `extractor.py`: extract crops from big images saved in `./data/data_dir` with different methods, save crops and related information in `./dataset/save_dir`
* `preprocess.py`: data augmentation
* `loader.py`: load images from `./data/data_dir` with data augmentation
* `metrics.py`: evaluation metrics such as PSNR, SSIM, NRMSE, VIFP
* `runner.py`: training, testing, log saving

#### files
* `./dataset/save_dir/all.csv trian.csv test.csv val.csv`: image names(id)
* `./dataset/save_dir/statistic.csv`: the way of obtaining data
* `./logs/statistic/model_info.csv`: model argument information
* `./logs/statistic/trian.csv test.csv val.csv` final statistic result and parameter information for related model

## Model Architectures
[Here](https://gitlab.com/Chokurei/geosr/tree/master/archs)

## Get Started
### Reference
If you use our code or any of the ideas from our paper please cite:
```
@article{wu2018geoseg,
  title={Geosr: A Computer Vision Package for Remote Sensing Image Super Resolution},
  author={Guo, Zhiling and Wu, Guangming},
  journal={arXiv preprint arXiv:1809.03175},
  year={2018}
}
```
### Requirements
* [Python 3.5.2+](https://www.python.org/)
* [torch 0.4.1+](https://pytorch.org/tutorials/)
* [torchvision 0.2.1+](https://pytorch.org/docs/stable/torchvision/index.html)

### Data
```
$ python ./utils/extractor.py --data_dir DATA_DIR --mode 'slide-rand'
```
or  
save existing training, valiation, and testing dataset in `./dataset/save_dir` respectively

### Preprocessing
__Band choose__  
```python
parser.add_argument('--band_mode', type=str, default='Y', choices=['Y', 'YCbCr', 'RGB'], help="band mode")
```
__Data augmentation__  
Choose data augmentation method in `./main.py`, detailed information in `./utils/preprocessor.py`
```python
parser.add_argument('--aug', type=lambda x: (str(x).lower() == 'true'), default=True, help='data augmentation or not')
parser.add_argument('--aug_mode', type=str, default='c', choices=['a', 'b', 'c', 'd', 'e'],
                        help='data augmentation mode: a, b, c, d, e')
```

## Visualization
### Epoch difference
| Epoch  | 5                                                                                                               | 10                                                                                                              | 15                                                                                                              | 20                                                                                                              | 25                                                                                                              |
|--------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Image  | ![bridge_030_1_epoch_5_iter_65](/uploads/d4dd084d4a9e9157bac84d1c6f030820/bridge_030_1_epoch_5_iter_65.png)     | ![bridge_030_1_epoch_10_iter_130](/uploads/4f99eb3cd0befcef02d3670bd98b7b20/bridge_030_1_epoch_10_iter_130.png) | ![bridge_030_1_epoch_15_iter_195](/uploads/7050131287c32d34df593253378c728f/bridge_030_1_epoch_15_iter_195.png) | ![bridge_030_1_epoch_20_iter_260](/uploads/fe9e382257dcbb06f0fc37359fec584a/bridge_030_1_epoch_20_iter_260.png) | ![bridge_030_1_epoch_25_iter_325](/uploads/704a47215586986fb40d25b0c21c5d5a/bridge_030_1_epoch_25_iter_325.png) |
| Epoch  | 30                                                                                                              | 35                                                                                                              | 40                                                                                                              | 45                                                                                                              | 50                                                                                                              |
| Imgage | ![bridge_030_1_epoch_30_iter_390](/uploads/52491ea724fde4e0a1ada7f11414931b/bridge_030_1_epoch_30_iter_390.png) | ![bridge_030_1_epoch_35_iter_455](/uploads/630e83e6ab67415a78f18ba21c8ba325/bridge_030_1_epoch_35_iter_455.png) | ![bridge_030_1_epoch_40_iter_520](/uploads/bce9950ad3b89017974fce9562b4694d/bridge_030_1_epoch_40_iter_520.png) | ![bridge_030_1_epoch_50_iter_650](/uploads/df5950368112d0d71e41d11be29d005c/bridge_030_1_epoch_50_iter_650.png) | ![bridge_030_1_epoch_45_iter_585](/uploads/41d929498dec44b5dfb738e7ec92fa06/bridge_030_1_epoch_45_iter_585.png) |

