import sys
import csv
import hashlib

i = 1
field_values = dict()
redaction_phrase = "REDACTED-{0}"

if len(sys.argv) != 2:
    print("\nUsage:\n\t{0} <field list, comma delimited with no spaces>".format(sys.argv[0]))
    print("\nExample:\n\tcat conn.log | zeek-cut | python {0} 2,4\n".format(sys.argv[0]))
    exit(-1)

fields = sys.argv[1].split(',')

rd = csv.reader(sys.stdin, delimiter="\t", quotechar='"')
wt = csv.writer(sys.stdout, delimiter="\t", quotechar='"', quoting=csv.QUOTE_MINIMAL)
for row in rd:
    for field in fields:
        field_val = row[int(field)]
        if field_val not in field_values:
            field_values[field_val] = i
            row[int(field)] = redaction_phrase.format(i)
            i += 1
        else:
            row[int(field)] = redaction_phrase.format(field_values[field_val])
    wt.writerow(row)