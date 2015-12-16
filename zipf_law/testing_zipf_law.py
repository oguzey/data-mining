#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from operator import itemgetter
sys.path.append('helpers')
from helpers import *
# from helpers.helpers import *

if len(sys.argv) != 3:
    print "Invalid amount of arguments. Expect two filename."
    exit(1)

input_text = sys.argv[1]
output_file = sys.argv[2]
print "Processing file '%s'" % input_text
raw_text = read_all_in_lowercase(input_text)
text = Text(raw_text)
freq = text.get_frequencies_unique_ngrams(TypeNGram.UNIGRAMS)
pairs = sorted(freq.items(), key=itemgetter(1), reverse=True)
write_pairs_to_file(output_file, pairs)
print "The file has %d words." % text.get_amount_ngrams(TypeNGram.UNIGRAMS)
# for pair in pairs:
#     print pair[0] + ": " + str(pair[1])
