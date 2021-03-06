#!/usr/bin/python
import sys
import csv
if len(sys.argv)<2:
    print >>sys.stderr, "need bom file, optional quantity"
    exit( 1)
bom_file = sys.argv[1]
if len(sys.argv) == 3:
    quantity = int(sys.argv[2])
else:
    quantity = 1

rows = 0
bad_rows = 0

with open(bom_file,'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        #check for errors
        rows += 1
        if rows == 1:
            continue
        if not 'ERROR' in row[0]:
            #check row length, should be 10
            if len(row) != 10:
                print >> sys.stderr, "bad row length: ", row
                bad_rows+=1
            else:
                comment = row[4].replace(',','')[0:30-13]
                print ', '.join([row[3],str(int(row[5])*quantity),comment])
        else:
            bad_rows += 1
print >>sys.stderr ,"processed %d rows with %d missing rows" % (rows,bad_rows)

