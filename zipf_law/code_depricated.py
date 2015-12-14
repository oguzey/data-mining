import re
import codecs
from operator import itemgetter
import sys

if len(sys.args) != 2:
    print "Invalid amount of arguments. Expect only filename."
    exit(1)

filename = sys.args[1]

text = None
with codecs.open(filename, 'r', 'utf8') as f:
    text = f.read().lower()


words = re.split("[\W\d_]+", text, flags=re.UNICODE)

freq = {}

for word in words:
    if freq.get(word) is None:
        freq[word] = 0
    freq[word] += 1


# for key, value in freq.items():
#     print key + ': ' + str(value)
pairs = sorted(freq.items(), key=itemgetter(1), reverse=True)
for pair in pairs:
    print pair[0] + ": " + str(pair[1])
with open('frequency.csv', 'w') as f:
    writer = codecs.getwriter('utf8')(f)
    for pair in pairs:
        writer.write(pair[0] + ';' + str(pair[1]) + '\n')
