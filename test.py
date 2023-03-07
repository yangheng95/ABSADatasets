# -*- coding: utf-8 -*-
# file: test.py
# time: 29/01/2022
# author: yangheng <yangheng@m.scnu.edu.cn>
# github: https://github.com/yangheng95
# Copyright (C) 2021. All Rights Reserved.
import os

import findfile
from findfile import rm_files

from pyabsa import check_package_version, generate_inference_set_for_apc, convert_apc_set_to_atepc_set

check_package_version(min_version='v2.0.0')

# from pyabsa import APCCheckpointManager
# classifier = APCCheckpointManager.get_sentiment_classifier('fast')
# label_map = {0: 'Negative', 1: 'Neutral', 2: 'Positive', '0': 'Negative', '1': 'Neutral', '2': 'Positive'}
# def read_csv_by_pandas(path):
#     import pandas as pd
#     df = pd.read_csv(path)
#     with open(path+'.dat', 'w', encoding='utf-8') as f:
#         for index, row in df.iterrows():
#             if row['aspect'].strip() and row['text'].strip() and row['aspect'] in row['text']:
#                 text = row['text'].replace('\r', '').replace('\n', '').strip()
#                 aspect = row['aspect'].replace('\r', '').replace('\n', '').strip()
#                 res = classifier.infer(text.replace(aspect, '[ASP]{}[ASP]'.format(aspect)))
#                 f.write(text.replace(aspect, '$T$')+'\n')
#                 f.write(aspect+'\n')
#                 f.write(label_map[res['sentiment'][0]]+'\n')
#                 # f.write(label_map[row['label']]+'\n')
#     return df
# read_csv_by_pandas('datasets/apc_datasets/129.Kaggle/test.csv')



findfile.rm_files(os.getcwd(), '.ignore.atepc')
findfile.rm_files(os.getcwd(), '.atepc.ignore')

# batch conversion for all ABSA datasets
generate_inference_set_for_apc('apc_datasets')
convert_apc_set_to_atepc_set('apc_datasets')

# default set ATEPC augmented datasets invisible
for f in findfile.find_cwd_files('.ignore.atepc'):
    os.rename(f, f.replace('.ignore.atepc', '.atepc.ignore'))

# remove train and valid inference set, as they are useless
rm_files(key=['train', 'inference'])
rm_files(key=['valid', 'inference'])
