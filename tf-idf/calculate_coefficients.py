#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import sys
import math
import os
from operator import itemgetter
sys.path.append('helpers')
from helpers import *
# from helpers.helpers import *


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
    amount_matching = sum(
        map(
            lambda ngrams: ngrams.freq_uniques.get(ngram) is not None,
            texts_ngrams
            )
        )
    return math.log(len(texts_ngrams) / amount_matching, 10)


if len(sys.argv) < 3:
    print "Invalid amount of arguments."
    print "Expect a output file and directory for input files."
    exit(1)

output_file = sys.argv[1]
input_dir = sys.argv[2]

if not os.path.isdir(input_dir):
    print "Provided path '%s' is not directory."
    exit(1)

input_files = [
    os.path.join("", input_dir, fname)
    for fname in os.listdir(input_dir)
    ]
print "Will handle next files " + str(input_files)
texts = map(lambda in_file: Text(read_all_in_lowercase(in_file)), input_files)
texts_unigrams = map(lambda text: text.get_ngrams(TypeNGram.UNIGRAMS), texts)


tf_idfs = {}

for index in xrange(len(texts)):
    print "Calculate tf-idf for '{0}'...".format(input_files[index]),
    tf_idfs_text = {}
    ngrams = texts_unigrams[index]
    unigrams = ngrams.freq_uniques.keys()
    for unigram in unigrams:
        tf = calc_tf(unigram, ngrams)
        idf = calc_idf(unigram, texts_unigrams)
        tf_idfs_text[unigram] = tf * idf

    tf_idfs[input_files[index]] = tf_idfs_text
    print "   OK"

# first element for filenames
strs_output = ['']
processed_texts = 0

for filename, coefs in tf_idfs.items():
    print "Create report for '{0}'...".format(filename),
    pairs = sorted(coefs.items(), key=itemgetter(1), reverse=True)
    tf_idfs[filename] = pairs
    strs_output[0] += filename + ";;"

    for index in xrange(len(pairs)):
        new_pease = ";".join(map(str, pairs[index])) + ";"
        try:
            strs_output[index + 1] += new_pease
        except IndexError:
            strs_output.append(processed_texts * ";;" + new_pease)

    processed_texts += 1
    print "   OK"

with open(output_file, 'w') as f:
    for row in strs_output:
        f.write(row + os.linesep)
