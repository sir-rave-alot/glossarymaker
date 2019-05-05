import sys
import subprocess
from subprocess import check_output
import csv
import re 

print ('Argument List:', str(sys.argv))

document = sys.argv[1]
wordlist = sys.argv[2]

outfile = "gloss-" + re.sub('\.csv$', '', wordlist) + ".txt"
delim = '..'

print "Generating glossary!"
print "Store in " + outfile

words = csv.reader(open(wordlist))

text_file = open(outfile, "w")

for row in words:
	for column in row:
		a = check_output(["./find.sh", document, column])
		a = a.replace('\n', delim)
		a = column + ', ' + a + '\n'
		print a
		text_file.write(a)

text_file.close()

print "end"