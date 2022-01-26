import requests, re, string
from collections import Counter
import json

class UniqueWordCounter():
    """
    given a url with text in it, this class can find the total number of unique words by building off of the counter module from collections, and output data on the text such as:
    1.formatted text
    2.list of all unique words ordered alphabetically
    3.top ten most used unique words
    4.number of unique words
    """
    def __init__(self, url):
        self.url = url
        self.__getformattedText()
        self.__getEntireTextSplit()

    def __getURLData(self):
        """
        (self) -> (response object)

        gets data from url
        """
        return requests.get(self.url)

    def __getformattedText(self):
        """
        (self) -> (none)

        formats text using regular expressions, uses this mask '[!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~]' to remove punctuation
        """
        urlResponse = self.__getURLData()
        punctuationToRemove = '[0-9' + string.punctuation.replace("'", "") + ']'
        self.formattedText = re.sub(punctuationToRemove, ' ', urlResponse.text)

    def __getEntireTextSplit(self):
        """
        (self) -> (none)

        splits text into a list of all lowercase single words
        """
        self.EntireTextSplit = self.formattedText.lower().split()

    def getUniqueWords(self):
        """
        (self) -> (none)

        creates a counter object from the split text list which automatically counts the 
        unqiue items in the list
        """
        self.uniqueWords = Counter(self.EntireTextSplit)

    def getNumberOfUniqueWords(self):
        """
        (self) -> (str)

        returns a string with the total number of unique words
        """
        return "There are %d unqiue words in the provided text!\n" % (len(self.uniqueWords))

    def getTopTenWords(self):
        """
        (self) -> (str)

        using counter class, finds the top 10 most common words and # of occurances
        then adds them all to a string and returns it
        """
        topTenString = "#. | Word | # of Occurances\n"
        topTen = self.uniqueWords.most_common(10)
        count = 1
        for word in topTen:
            topTenString += "%d. | %s | %d\n" % (count, word[0], word[1])
            count += 1
        
        return topTenString

    def saveNumberOfUniquesAndTopTen(self, path):
        """
        (self, path) -> (none)

        saves data from getNumberOfUniqueWords and getTopTenWords to a .txt file at
        the given path destination
        """
        f = open(path, 'w')
        f.write(self.getNumberOfUniqueWords() + "\n")
        f.write(self.getTopTenWords())
        f.close()

    def saveFormattedText(self, path):
        """
        (self, path) -> (none)

        saves formatted text to a .txt file at the given path destination
        """
        f = open(path, 'w')
        f.write(self.formattedText)
        f.close()

    def __getSortedUniqueWords(self):
        """
        (self) -> ({str : int})

        sorts unique words into a dictionary in alphabetical order using sorted method
        then returns the sorted dictionary
        """
        sortedUniqueWords = {}
        for word in sorted(self.uniqueWords.keys()):
            sortedUniqueWords[word] = self.uniqueWords[word]
        return sortedUniqueWords

    def saveUniqueWords(self, path):
        """
        (self, path) -> (none)

        saves SortedUniqueWords dictionary to a .json file at the given path destination
        """
        f = open(path, 'w')
        json.dump(self.__getSortedUniqueWords(), f, indent = 4)
        f.close()