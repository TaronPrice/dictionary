from PyDictionary import PyDictionary
dictionary=PyDictionary()

""" a method to get all information on the word"""
def theWord(word):

    print("Meaning")
    print(dictionary.meaning(word))
    print("Synonyms")
    print(dictionary.synonym(word))
    print("Antonym")
    print(dictionary.antonym(word))
    print("Translation in spanish")
    print(dictionary.translate(word,'es'))
    print()

word=input("pick a word: ")
theWord(word)