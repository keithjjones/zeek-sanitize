import sys
import csv
import hashlib

if len(sys.argv) != 3:
    print("\nUsage:\n\t{0} <salt value> <field list, comma delimited>".format(sys.argv[0]))
    print("\nExample:\n\tcat conn.log | zeek-cut | python {0} mysalt 2,4\n".format(sys.argv[0]))
    exit(-1)

salt = sys.argv[1]
fields = sys.argv[2].split(',')

rd = csv.reader(sys.stdin, delimiter="\t", quotechar='"')
wt = csv.writer(sys.stdout, delimiter="\t", quotechar='"', quoting=csv.QUOTE_MINIMAL)
for row in rd:
    for field in fields:
        tmpstr = "{0}{1}".format(salt, row[int(field)])
        row[int(field)] = hashlib.md5(tmpstr.encode('utf-8')).hexdigest()
        row[int(field)] = "REDACTED-{0}".format(row[int(field)][-10:])
    wt.writerow(row)