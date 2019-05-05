# Glossary Maker
This combination of a Python and Bash script is intended to create a glossary for an existing PDF.
Therefor one has to provide a word list with the expressions wanted.
The script then generates a text file with the corresponding page numbers within the PDF document.

## Usage
`python <document.pdf> <wordlist.csv>`

- The pattern match is **case insensitive**

### Example word list
```
wordlist.csv
------------

ISO 12757-2
Füllfederhaltertinten
Thermopapier
Eisengallustinte
```

### Example output
```
gloss-wordlist.txt
------------

ISO 12757-2 , 2..3..65
Füllfederhaltertinten , 2..3..4
Thermopapier, 34..35
Eisengallustinte, 4
```
## Dependencies
- python >= 2.7
- pdfgrep (`sudo apt install pdfgrep`)
- sed
- cut
- uniq
