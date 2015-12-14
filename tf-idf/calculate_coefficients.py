#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
# sys.path.append('helpers')
from helpers.helpers import *

if len(sys.argv) < 4:
    print "Invalid amount of arguments."
    print "Expect a output file and two input files as minimum."
    exit(1)

output_file = sys.argv[1]
input_files = sys.argv[2:]

frequencies_unique_words_of_texts = []

for input_file in input_files:
    raw_text = read_all_in_lowercase(input_file)
    text = Text(raw_text)
    freq_words = text.get_frequencies_unique_words()
    frequencies_unique_words_of_texts.append(freq_words)
