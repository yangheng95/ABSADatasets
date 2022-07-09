# -*- coding: utf-8 -*-
# file: test.py.py
# time: 29/01/2022
# author: yangheng <yangheng@m.scnu.edu.cn>
# github: https://github.com/yangheng95
# Copyright (C) 2021. All Rights Reserved.
import os

import findfile
from findfile import rm_files
from pyabsa.utils.file_utils import generate_inference_set_for_apc, convert_apc_set_to_atepc_set


# batch conversion for all ABSA datasets
generate_inference_set_for_apc('datasets')
convert_apc_set_to_atepc_set('datasets')

# default set ATEPC augmented datasets invisible
for f in findfile.find_cwd_files('.ignore.atepc'):
    os.rename(f, f.replace('.ignore.atepc', 'atepc.ignore'))

# remove train and valid inference set, as they are useless
rm_files(key=['train', 'inference'])
rm_files(key=['valid', 'inference'])
