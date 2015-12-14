import io
import sys

if len(sys.argv) != 3:
    print "Invalid amount of arguments. Expect two filename."
    exit(1)

filename_input = sys.argv[1]
filename_output = sys.argv[2]

with io.open(filename_input, 'r', encoding='utf8') as f_in:
    with io.open(filename_output, 'w', encoding='utf8') as f_out:
        f_out.write(f_in.read())
