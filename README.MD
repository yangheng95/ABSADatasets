# ABSA datasets processed for [PyABSA](https://github.com/yangheng95/PyABSA)
ATE, APC, Inference sets included

# Dataset contribution
We hope you can share your custom dataset or a availabel public dataset. If you want to, follow the contribution process:
- Format your APC dataset according to our dataset format. (**Recommended. Once you did this, we can help you to finish other steps**)
- Generate the inference dataset for APC / ATEPC task (**Optional**. The example is available at [here](https://github.com/yangheng95/PyABSA/blob/release/examples/aspect_polarity_classification/generate_inference_set.py))
- Convert the APC dataset to ATEPC dataset, and move the transformed ATEPC datasets from apc_dataset to corresponding atepc_datasets. (**Optional**. The example is available at [here](https://github.com/yangheng95/PyABSA/blob/release/examples/aspect_term_extraction/convert_apc_set_to_atepc_set.py) )
- Register your dataset in PyABSA. (**Optional**. Register at [here](https://github.com/yangheng95/PyABSA/blob/3238f319f6ee4938d728ed6ae61eb98b4753311a/pyabsa/functional/dataset/dataset_manager.py#L32))

## Additional note for ATEPC dataset
Each data item can have mutiple aspects, but it can only have one polarity label. If a review does have mutiple aspects, please duplicate the review coresponding to a target aspect and cancel the polarity labels of other aspects.

# Notice

All datasets provided are for research only, we do not hold any Copyright of any datasets.

## Datasets source:

MAMS https://github.com/siat-nlp/MAMS-for-ABSA

SemEval 2014: https://alt.qcri.org/semeval2014/task4/index.php?id=data-and-tools

SemEval 2015: https://alt.qcri.org/semeval2015/task12/index.php?id=data-and-tools

SemEval 2016: https://alt.qcri.org/semeval2016/task5/index.php?id=data-and-tools

Chinese: https://www.sciencedirect.com/science/article/abs/pii/S0950705118300972?via%3Dihub

Shampoo: brightgems@github

Twitter: https://dl.acm.org/doi/10.5555/2832415.2832437

Television & TShirt: https://github.com/rajdeep345/ABSA-Reproducibility
