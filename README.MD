# ABSA datasets for [PyABSA](https://github.com/yangheng95/PyABSA)

[![total views](https://raw.githubusercontent.com/yangheng95/ABSADatasets/traffic/total_views.svg)](https://github.com/yangheng95/ABSADatasets/tree/traffic#-total-traffic-data-badge)
[![total views per week](https://raw.githubusercontent.com/yangheng95/ABSADatasets/traffic/total_views_per_week.svg)](https://github.com/yangheng95/ABSADatasets/tree/traffic#-total-traffic-data-badge)
[![total clones](https://raw.githubusercontent.com/yangheng95/ABSADatasets/traffic/total_clones.svg)](https://github.com/yangheng95/ABSADatasets/tree/traffic#-total-traffic-data-badge)
[![total clones per week](https://raw.githubusercontent.com/yangheng95/ABSADatasets/traffic/total_clones_per_week.svg)](https://github.com/yangheng95/ABSADatasets/tree/traffic#-total-traffic-data-badge)

## Contribute (prepare) your dataset in using PyABSA
We hope you can share your custom dataset or an available public dataset. If you want to, follow these steps:
 
### Important: Rename your dataset filename before use it in PyABSA

Although the integrated datasets have no ids, it is recommended to assign an id for your dataset. 
While merge your datasets into ABSADatasets, please keep the id remained.

- APC dataset name should be {id}.{dataset name}, and the dataset files should be named in {dataset name}.{type}.dat.atepc e.g., 
```tree
datasets
├── 101.restaurant
│    ├── restaurant.train.dat  # train_dataset
│    ├── restaurant.test.dat  # test_dataset
│    └── restaurant.valid.dat  # valid_dataset, dev set are not recognized in PyASBA, please rename dev-set to valid-set
└── others
```

- ATEPC dataset files should be {id}.{dataset name}.{type}.dat.atepc,
e.g., 
```tree
datasets
├── 101.restaurant
│    ├── restaurant.train.dat.atepc  # train_dataset
│    ├── restaurant.test.dat.atepc  # test_dataset
│    └── restaurant.valid.dat.atepc  # valid_dataset, dev set are not recognized in PyASBA, please rename dev-set to valid-set
└── others
```

I prepare a demo custom APC/ATEPC dataset which is based on Yelp dataset, if you got problem in dataset rename, please feed your data into the prepared dataset folds.
Check [datasets/apc_datasets/100.CustomDataset](./datasets/apc_datasets/100.CustomDataset) and [datasets/atepc_datasets/100.CustomDataset](./datasets/apc_datasets/100.CustomDataset)to view or rewrite the custom dataset.

Then, use the {id}.{dataset name} to locate your dataset, e.g., 

```python3
from pyabsa.functional import APCConfigManager
from pyabsa.functional import Trainer
from autocuda import auto_cuda

config = APCConfigManager.get_apc_config_english() # APC task
dataset = '101.restaurant' 
# dataset = '100.CustomDataset'
Trainer(config=config,
        dataset=dataset,  # train set and test set will be automatically detected
        checkpoint_save_mode=1,
        auto_device=auto_cuda()  # automatic choose CUDA or CPU
        )
```

It will avoid some potential problem (e.g., duplicated dataset name) while PyABSA detects the dataset.

### Dataset Processing
- Format your APC dataset according to our dataset format. (**Recommended. Once you finished this step, we can help you to finish other steps**)
![image](https://user-images.githubusercontent.com/51735130/136219441-c3e9b4e2-6e31-4d32-b6c3-a66788b179f6.png)

- Generate the inference dataset for APC / ATEPC task (**Optional**. The example is available [here](https://github.com/yangheng95/PyABSA/blob/release/demos/aspect_polarity_classification/generate_inference_set.py))
- Convert the APC dataset to ATEPC dataset, and move the transformed ATEPC datasets from apc_dataset to corresponding atepc_datasets. (**Optional**. The example is available [here](https://github.com/yangheng95/PyABSA/blob/release/demos/aspect_term_extraction/convert_apc_set_to_atepc_set.py) )
- Register your dataset in PyABSA. (**Optional**. Register [here](https://github.com/yangheng95/PyABSA/blob/302da1e4b2292cdbc5b9c712862e623c427132b8/pyabsa/functional/dataset/dataset_manager.py#L37))

### Annotate Your Dataset
- A Stand-alone browser based tool to help process data for the training set. [here](https://github.com/yangheng95/ABSADatasets/tree/v1.2/DPT)
![image1](https://user-images.githubusercontent.com/4684417/139701633-d77a009b-1a12-4ef2-9663-37d2d36e1af1.JPG)

  Once data saved, 3 files will be created: 

  1. a CSV file training set for classic sentiment analysis 
  2. a TXT file training set for PyABSA
  3. a JSON file for saving unfinished work

## Notice

All datasets provided are for research only, we do not hold any Copyright of any datasets. These datasets follow their original licenses (if any).

## Datasets source:

MAMS https://github.com/siat-nlp/MAMS-for-ABSA

SemEval 2014: https://alt.qcri.org/semeval2014/task4/index.php?id=data-and-tools

SemEval 2015: https://alt.qcri.org/semeval2015/task12/index.php?id=data-and-tools

SemEval 2016: https://alt.qcri.org/semeval2016/task5/index.php?id=data-and-tools

Chinese: https://www.sciencedirect.com/science/article/abs/pii/S0950705118300972?via%3Dihub

Shampoo: [brightgems@github](https://github.com/brightgems/ABSADatasets)

MOOC: [jmc-123@github](https://github.com/jmc-123/ABSADatasets) with GPL License

Twitter: https://dl.acm.org/doi/10.5555/2832415.2832437

Television & TShirt: https://github.com/rajdeep345/ABSA-Reproducibility

Yelp: [WeiLi9811@github](https://github.com/WeiLi9811)
