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

texts = map(lambda in_file: Text(read_all_in_lowercase(in_file)), input_files)
