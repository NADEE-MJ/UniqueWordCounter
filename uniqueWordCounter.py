import requests, re, string
from collections import Counter
import json

class UniqueWordCounter():
    """

    """
    def __init__(self, url):
        self.url = url
        self.__getformattedText()
        self.__getEntireTextSplit()

    def __getURLData(self):
        return requests.get(self.url)

    def __getformattedText(self):
        urlResponse = self.__getURLData()
        punctuationToRemove = '[' + string.punctuation.replace("'", "") + ']'
        self.formattedText = re.sub(punctuationToRemove, ' ', urlResponse.text)

    def __getEntireTextSplit(self):
        self.EntireTextSplit = self.formattedText.lower().split()

    def getUniqueWords(self):
        self.uniqueWords = Counter(self.EntireTextSplit)

    def printNumberOfUniqueWords(self):
        print("There are %d words in the provided text!" % (len(self.uniqueWords))) 

    def printTopTenWords(self):
        topTen = self.uniqueWords.most_common(10)
        print("Word:  # of Occurances")
        for word in topTen:
            print("%s:  %d" % (word[0], word[1]))

    def saveFormattedText(self, path):
        f = open(path, 'w')
        f.write(self.formattedText)
        f.close()

    def __getSortedUniqueWords(self):
        sortedUniqueWords = {}
        for word in sorted(self.uniqueWords):
            sortedUniqueWords[word] = self.uniqueWords[word]
        return sortedUniqueWords

    def saveUniqueWords(self, path):
        f = open(path, 'w')
        json.dump(self.__getSortedUniqueWords(), f, indent = 4)
        f.close()