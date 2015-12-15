#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math
from __future__ import division
from operator import itemgetter
# sys.path.append('helpers')
from helpers.helpers import *


def calc_tf(ngram, ngrams):
    """
    Calculate term frequency (TF) of 'ngram' among other ngrams in text
        ngram   - [string] certain ngram
        ngrams  - [NGram] all ngrams with frequencies in text
    """
    return ngrams.freq_uniques[ngram] / ngrams.amount_ngrams


def calc_idf(ngram, texts_ngrams):
    """
    Calculate inverse document frequency (IDF) for ngram
        ngram           - [string] certain ngram
        texts_ngrams    - [list of NGram] all ngrams of all texts
    """
    def is_text_contain_ngram(ngrams): ngrams.get(ngram) is not None
    amount_matching = math.sum(map(is_text_contain_ngram, texts_ngrams))

    return amount_matching / len(texts_ngrams)

if len(sys.argv) < 4:
    print "Invalid amount of arguments."
    print "Expect a output file and two input files as minimum."
    exit(1)

output_file = sys.argv[1]
input_files = sys.argv[2:]

texts = map(lambda in_file: Text(read_all_in_lowercase(in_file)), input_files)
texts_unigrams = map(lambda text: text.get_ngrams(TypeNGram.UNIGRAMS), texts)


tf_idfs = {}

for index in xrange(len(texts)):
    tf_idfs_text = {}
    ngrams = texts_unigrams[index]
    unigrams = ngrams.freq_uniques.keys()
    for unigram in unigrams:
        tf = calc_tf(unigram, ngrams)
        idf = calc_idf(unigram, texts_unigrams)
        tf_idfs_text[unigram] = tf * idf

    tf_idfs[input_files[index]] = tf_idfs_text


for key, coefs in tf_idfs.items():
    tf_idfs[key] = sorted(coefs.items(), key=itemgetter(1), reverse=True)


