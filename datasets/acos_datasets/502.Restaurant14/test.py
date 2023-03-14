# -*- coding: utf-8 -*-
# file: test.py
# time: 15:21 2023/3/13
# author: YANG, HENG <hy345@exeter.ac.uk> (杨恒)
# github: https://github.com/yangheng95
# huggingface: https://huggingface.co/yangheng
# google scholar: https://scholar.google.com/citations?user=NPq5a_0AAAAJ&hl=en
# Copyright (C) 2019-2023. All Rights Reserved.
import json

for file in ['rest16_quad_dev.tsv', 'rest16_quad_test.tsv', 'rest16_quad_train.tsv']:
    with open(file + '.jsonl', 'w', encoding='utf8') as fout:
        with open(file, 'r', encoding='utf8') as fin:
            lines = fin.readlines()
            for line in lines:
                text, labels = line.strip().split('\t')[0], line.strip().split('\t')[1:]
                data = {
                    'text': text,
                    'labels': []
                }
                for label in labels:
                    aspect, category, polarity, opinion = label.split()
                    tokens = text.split()
                    aspect_start, aspect_end = [int(x) for x in aspect.split(',')]
                    opinion_start, opinion_end = [int(x) for x in opinion.split(',')]
                    aspect = ' '.join(tokens[aspect_start:aspect_end])
                    opinion = ' '.join(tokens[opinion_start:opinion_end])
                    polarity = {'0': 'negative', '1': 'neutral', '2': 'positive'}[polarity]

                    data['labels'].append({
                        'aspect': aspect if aspect != '' else 'NULL',
                        'opinion': opinion if opinion != '' else 'NULL',
                        'polarity': polarity,
                        'category': category if category != '' else 'NULL',
                    })

                fout.write(
                    json.dumps(data, ensure_ascii=False, indent=None)
                    + '\n')
