import sys
import csv
import hashlib

i = 1
hash_values = dict()

if len(sys.argv) != 2:
    print("\nUsage:\n\t{0} <field list, comma delimited with no spaces>".format(sys.argv[0]))
    print("\nExample:\n\tcat conn.log | zeek-cut | python {0} 2,4\n".format(sys.argv[0]))
    exit(-1)

fields = sys.argv[1].split(',')

rd = csv.reader(sys.stdin, delimiter="\t", quotechar='"')
wt = csv.writer(sys.stdout, delimiter="\t", quotechar='"', quoting=csv.QUOTE_MINIMAL)
for row in rd:
    for field in fields:
        hash_val = hashlib.md5(row[int(field)].encode('utf-8')).hexdigest()
        if hash_val not in hash_values:
            hash_values[hash_val] = i
            row[int(field)] = "REDACTED-{0}".format(i)
            i += 1
        else:
            row[int(field)] = "REDACTED-{0}".format(hash_values[hash_val])
    wt.writerow(row)