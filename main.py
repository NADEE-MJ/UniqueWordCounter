import requests, re, string
from collections import Counter
import json

response = requests.get("https://shakespeare.folger.edu/downloads/txt/romeo-and-juliet_TXT_FolgerShakespeare.txt")

punctuationToRemove = '[' + re.escape(string.punctuation.replace("'", "")) + ']'
textNoPunctuation = re.sub(punctuationToRemove, '', response.text)

f = open('textNoPunction.txt', 'w')
f.write(textNoPunctuation)
f.close()

textList = textNoPunctuation.lower().split()

wordCounter = Counter(textList)

sorted_dict = {}
for word in sorted(wordCounter):
    sorted_dict[word] = wordCounter[word]
f = open('mostCommonWords.json', 'w')
json.dump(sorted_dict, f, indent = 4)
f.close()

print(len(wordCounter))
print(wordCounter.most_common(10))
