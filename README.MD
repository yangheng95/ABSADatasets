# ABSA datasets for [PyABSA](https://github.com/yangheng95/PyABSA)

[![total views](https://raw.githubusercontent.com/yangheng95/ABSADatasets/traffic/total_views.svg)](https://github.com/yangheng95/ABSADatasets/tree/traffic#-total-traffic-data-badge)
[![total views per week](https://raw.githubusercontent.com/yangheng95/ABSADatasets/traffic/total_views_per_week.svg)](https://github.com/yangheng95/ABSADatasets/tree/traffic#-total-traffic-data-badge)
[![total clones](https://raw.githubusercontent.com/yangheng95/ABSADatasets/traffic/total_clones.svg)](https://github.com/yangheng95/ABSADatasets/tree/traffic#-total-traffic-data-badge)
[![total clones per week](https://raw.githubusercontent.com/yangheng95/ABSADatasets/traffic/total_clones_per_week.svg)](https://github.com/yangheng95/ABSADatasets/tree/traffic#-total-traffic-data-badge)

## Dataset contribution

We hope you can share your custom dataset or a available public dataset. If you want to, follow these steps:

- Format your APC dataset according to our dataset format. (**Recommended. Once you finished this step, we can help you to finish other steps**)
![image](https://user-images.githubusercontent.com/51735130/136219441-c3e9b4e2-6e31-4d32-b6c3-a66788b179f6.png)


- Generate the inference dataset for APC / ATEPC task (**Optional**. The example is available [here](https://github.com/yangheng95/PyABSA/blob/release/demos/aspect_polarity_classification/generate_inference_set.py))
- Convert the APC dataset to ATEPC dataset, and move the transformed ATEPC datasets from apc_dataset to corresponding atepc_datasets. (**Optional**. The example is available [here](https://github.com/yangheng95/PyABSA/blob/release/demos/aspect_term_extraction/convert_apc_set_to_atepc_set.py) )
- Register your dataset in PyABSA. (**Optional**. Register [here](https://github.com/yangheng95/PyABSA/blob/3238f319f6ee4938d728ed6ae61eb98b4753311a/pyabsa/functional/dataset/dataset_manager.py#L32))


## Notice

All datasets provided are for research only, we do not hold any Copyright of any datasets. These datasets follow their original licenses (if any).

## Datasets source:

MAMS https://github.com/siat-nlp/MAMS-for-ABSA

SemEval 2014: https://alt.qcri.org/semeval2014/task4/index.php?id=data-and-tools

SemEval 2015: https://alt.qcri.org/semeval2015/task12/index.php?id=data-and-tools

SemEval 2016: https://alt.qcri.org/semeval2016/task5/index.php?id=data-and-tools

Chinese: https://www.sciencedirect.com/science/article/abs/pii/S0950705118300972?via%3Dihub

Shampoo: [brightgems@github](https://github.com/brightgems/ABSADatasets)

MOOC: [jmc-123@github](https://github.com/jmc-123/ABSADatasets)

Twitter: https://dl.acm.org/doi/10.5555/2832415.2832437

Television & TShirt: https://github.com/rajdeep345/ABSA-Reproducibility
