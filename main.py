import uniqueWordCounter as c

def main():
    url = "https://shakespeare.folger.edu/downloads/txt/romeo-and-juliet_TXT_FolgerShakespeare.txt"
    rAndJ = c.UniqueWordCounter(url)
    rAndJ.getUniqueWords()
    rAndJ.printNumberOfUniqueWords()
    rAndJ.printTopTenWords()
    rAndJ.saveFormattedText("test run\\formattedText.txt")
    rAndJ.saveUniqueWords("test run\\uniqueWords.json")

if __name__ == "__main__":
    main()