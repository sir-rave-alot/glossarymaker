import subprocess
from subprocess import check_output
import csv 

document = "script.pdf"
wordlist = "wordlist.csv"
outfile = "gloss" + wordlist + ".csv"
delim = '..'



print "Generating glossary!"

words = csv.reader(open(wordlist))

for row in words:
	for column in row:
		a = check_output(["./find.sh", document, column])
		a = a.replace('\n', delim)
		a = column + ', ' + a
		print a

'''
csvData = [[a],[a]]

with open(outfile, 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()
'''
print "end"