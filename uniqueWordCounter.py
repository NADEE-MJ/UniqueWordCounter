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

    def getNumberOfUniqueWords(self):
        return "There are %d unqiue words in the provided text!\n" % (len(self.uniqueWords))

    def getTopTenWords(self):
        topTenString = "#. | Word | # of Occurances\n"
        topTen = self.uniqueWords.most_common(10)
        count = 1
        for word in topTen:
            topTenString += "%d. | %s | %d\n" % (count, word[0], word[1])
            count += 1
        
        return topTenString

    def saveNumberOfUniquesAndTopTen(self, path):
        f = open(path, 'w')
        f.write(self.getNumberOfUniqueWords() + "\n")
        f.write(self.getTopTenWords())
        f.close()

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