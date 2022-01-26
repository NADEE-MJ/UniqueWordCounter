import uniqueWordCounter as c

def main():
    """
    This file runs the logic in the UnqiueWordCounter Class, change the url variable to any url link that contains text data and it will run the class to determine all unique words in the text.

    The following example uses the passage Romeo and Juliet, prints the number of unique words and 10 top ten occurances to the console and saves the entire formatted text and list of unique words and the number of times they each occur 
    """
    url = "https://shakespeare.folger.edu/downloads/txt/romeo-and-juliet_TXT_FolgerShakespeare.txt"
    rAndJ = c.UniqueWordCounter(url)
    rAndJ.getUniqueWords()
    rAndJ.printNumberOfUniqueWords()
    rAndJ.printTopTenWords()

    #the following two lines are for testing purposes
    rAndJ.saveFormattedText("run//formattedText.txt")
    rAndJ.saveUniqueWords("run//uniqueWords.json")

if __name__ == "__main__":
    main()