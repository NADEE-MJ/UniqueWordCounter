# UniqueWordCounter
Python class to find the unique words from a text file from a url

There is a basic example of usage in the main.py file and example of output in the run folder

## Initializing the class
The class takes a url in the form of a string to initialize, when initializing the class automatically gets data from the url and formats the text, removing punctuation.

After you have options of what you can do with the data.

## Different Methods
1. class.getUniqueWords() - creates counter object, must be preformed to do the following methods
    1. class.getNumberOfUniqueWords() - returns string with number of unique words
    2. class.getTopTenWords() - returns string with top ten unique words and the number of occurances in the text
    3. class.saveNumberOfUniquesAndTopTen(path) - saves output of methods a and b to a .txt file based on path given
    4. class.saveUniqueWords(path) - saves sorted dictionary of all unique words and number of occurances to a .json file based on the given path
2. class.saveFormattedText(path) - saves the formatted text to a .txt file based on the path given
