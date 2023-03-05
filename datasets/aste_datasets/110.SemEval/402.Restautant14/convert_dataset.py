# -*- coding: utf-8 -*-
# file: convert_dataset.py
# time: 05/03/2023
# author: yangheng <hy345@exeter.ac.uk>
# github: https://github.com/yangheng95
# huggingface: https://huggingface.co/yangheng
# google scholar: https://scholar.google.com/citations?user=NPq5a_0AAAAJ&hl=en
# Copyright (C) 2021. All Rights Reserved.

import re
import spacy
nlp = spacy.load('en_core_web_sm')


def convert_annotation_format(sentence, annotation):
    # Extract aspect and opinion terms from annotation
    aspect_spans = [(aspect_span[0], aspect_span[-1]) for (aspect_span, _, _) in annotation]
    opinion_spans = [(opinion_span[0], opinion_span[-1]) for (_, opinion_span, _) in annotation]
    sentiment = [sentiment_label for (_, _, sentiment_label) in annotation]

    # Tokenize sentence
    tokens = re.findall(r'\w+|[^\w\s]', sentence)
    postags, heads, deprels = get_dependencies(tokens)

    # Generate triples
    triples = []
    for i, aspect_span in enumerate(aspect_spans):
        for j, opinion_span in enumerate(opinion_spans):
            if aspect_span == opinion_span:
                continue
            aspect_start, aspect_end = aspect_span
            opinion_start, opinion_end = opinion_span
            if aspect_start > opinion_start:
                aspect_start, opinion_start = opinion_start, aspect_start
                aspect_end, opinion_end = opinion_end, aspect_end
            if aspect_end >= opinion_start:
                continue
            uid = f"{i}-{j}"
            target_tags = generate_tags(tokens, aspect_start, opinion_end, "BIO")
            opinion_tags = generate_tags(tokens, opinion_start, opinion_end, "BIO")
            triples.append({
                "uid": uid,
                "target_tags": target_tags,
                "opinion_tags": opinion_tags,
                "sentiment": sentiment
            })

    # Generate output dictionary
    output = {
        "id": "",
        "sentence": sentence,
        "postag": postags,
        "head": heads,
        "deprel": deprels,
        "triples": triples
    }

    return output

def generate_tags(tokens, start, end, scheme):
    if scheme == "BIO":
        tags = ["O"] * len(tokens)
        tags[start] = "B"
        for i in range(start+1, end+1):
            tags[i] = "I"
        return " ".join([f"{token}\\{tag}" for token, tag in zip(tokens, tags)])
    elif scheme == "IOB2":
        tags = ["O"] * len(tokens)
        tags[start] = "B"
        for i in range(start+1, end+1):
            tags[i] = "I"
        if end < len(tokens)-1 and tags[end+1] == "I":
            tags[end] = "B"
        return " ".join([f"{token}\\{tag}" for token, tag in zip(tokens, tags)])
    else:
        raise ValueError(f"Invalid tagging scheme '{scheme}'.")

def get_dependencies(tokens):
    # Replace special characters in tokens with placeholders
    placeholder_tokens = []
    for token in tokens:
        if re.search(r'[^\w\s]', token):
            placeholder = f"__{token}__"
            placeholder_tokens.append(placeholder)
        else:
            placeholder_tokens.append(token)

    # Get part-of-speech tags and dependencies using spaCy
    doc = nlp(" ".join(placeholder_tokens))
    postags = [token.pos_ for token in doc]
    heads = [token.head.i for token in doc]
    deprels = [token.dep_ for token in doc]

    # Replace placeholders in tokens with original special characters
    for i in range(len(tokens)):
        if re.search(r'[^\w\s]', tokens[i]):
            placeholder = f"__{tokens[i]}__"
            tokens[i] = tokens[i].replace(placeholder, tokens[i])

    return postags, heads, deprels


if __name__ == "__main__":
    # Read dataset
    with open("dev.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    # Sample sentence and annotation
    sentence = "The pizza is the best if you like thin crusted pizza."
    annotation = [([2], [8], 'POS')]

    # Convert annotation format
    output = convert_annotation_format(sentence, annotation)

    # Print output
    print(output)