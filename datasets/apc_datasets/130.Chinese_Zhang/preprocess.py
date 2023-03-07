# -*- coding: utf-8 -*-
# file: preprocess.py
# time: 14:20 2023/1/23
# author: yangheng <hy345@exeter.ac.uk>
# github: https://github.com/yangheng95
# huggingface: https://huggingface.co/yangheng
# google scholar: https://scholar.google.com/citations?user=NPq5a_0AAAAJ&hl=en
# Copyright (C) 2021. All Rights Reserved.

import os

import findfile

sentiment_map = {
    'NEU': 'Neutral',
    'NEG': 'Negative',
    'POS': 'Positive'
}

for f in findfile.find_cwd_files('.txt', '.apc'):
    print(f)
    with open(f, 'r', encoding='utf-8') as fin:
        lines = fin.readlines()
    with open(f.replace('.ignore', '') + '.dat.apc', 'w', encoding='utf-8') as fout:
        for line in lines:
            text, tuples = line.split('####')
            text = text.strip()
            tuples = eval(tuples.strip())

            tokens = text.split()
            _temp = []
            for t in tuples:
                if ' '.join(tokens[t[0][0]: t[0][1] + 1]).strip() == '':
                    continue
                if ' '.join(tokens[t[0][0]: t[0][1] + 1]).strip() in _temp:
                    continue
                _temp.append(' '.join(tokens[t[0][0]: t[0][1] + 1]).strip())
                fout.write(' '.join(tokens[:t[0][0]] + ['$T$'] + tokens[t[0][1] + 1:]) + '\n')
                fout.write(' '.join(tokens[t[0][0]: t[0][1] + 1]) + '\n')
                fout.write(sentiment_map[t[2]] + '\n')
