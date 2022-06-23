# -*- coding: utf-8 -*-
# file: test.py.py
# time: 29/01/2022
# author: yangheng <yangheng@m.scnu.edu.cn>
# github: https://github.com/yangheng95
# Copyright (C) 2021. All Rights Reserved.
import findfile
from findfile import rm_files
from pyabsa.utils.file_utils import generate_inference_set_for_apc, convert_apc_set_to_atepc_set

# generate_inference_set_for_apc('121')
# convert_apc_set_to_atepc_set('121')
rm_files(key=['train','inference'])