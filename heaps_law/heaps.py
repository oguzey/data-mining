#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('helpers')
from helpers import *

if len(sys.argv) != 3:
    print "Invalid amount of arguments. Expect two filename."
    exit(1)

input_text = sys.argv[1]
output_file = sys.argv[2]

words = read_words_from_file(input_text)

step = 1000
pairs = []
unique_words = {}
amount_unique = 0
processed_words = 0

for word in words:
    if word:
        is_unique = unique_words.get(word, 1)
        amount_unique += is_unique
        unique_words[word] = 0
        processed_words += 1
        if processed_words % step == 0:
            pairs.append((amount_unique, processed_words))

pairs.append((amount_unique, processed_words))

for key, value in pairs:
    print str(key) + ': ' + str(value)

write_pairs_to_file(output_file, pairs)
