# -*- coding: utf-8 -*-
# file: pre_segment_non_enlish_data.py
# time: 2022/8/4
# author: yangheng <hy345@exeter.ac.uk>
# github: https://github.com/yangheng95
# huggingface: https://huggingface.co/yangheng
# google scholar: https://scholar.google.com/citations?user=NPq5a_0AAAAJ&hl=en
# Copyright (C) 2021. All Rights Reserved.

def pre_word_segment(file=None, seg_fn=None):

    with open(file, mode='r', encoding='utf8') as fin:
        with open(file+'.seg', mode='w', encoding='utf8') as fout:
            for line in fin:
                line = line.strip()
                if line:
                    fout.write(' '.join(seg_fn(line)) + '\n')
                else:
                    fout.write('\n')

    print('segmentation done!')


if __name__ == '__main__':
    # Before annotating non-blank segmented text, you need to segment the data.
    # You can try other word segmentation tools here and PR to this repo.

    # 1. jieba segmentation
    import jieba
    seg_fn = jieba.cut

    # # 2. pkuseg segmentation
    # import pkuseg
    # seg_fn = pkuseg.pkuseg.cut

    # # 3. THULAC segmentation
    # import thulac
    # seg_fn = thulac.thulac(seg_only=True).cut

    # # 4. wordsegment segmentation
    # import wordsegment
    # from wordsegment import load, segment
    # seg_fn = segment

    pre_word_segment(file='sampleData.csv', seg_fn=seg_fn)
