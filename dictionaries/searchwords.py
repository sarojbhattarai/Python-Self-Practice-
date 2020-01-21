import sys
import string
words = {}

strip = string.whitespace + string.punctuation + string.digits + "\"'"
#strip is string for those characters we want to ignore 

#to run program: give "python searchwords.py filename" 
#In this case filename is filename

for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word)>2:
                words[word] = words.get(word,0)+1
for word in sorted(words):
    print("'{0}' occurs {1} times".format(word,words[word]))
