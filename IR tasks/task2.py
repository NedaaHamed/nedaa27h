import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
doc=input("WRITE YOUR TEXT: ")
choice=int(input(" Choice number 1: Print tokenized words\n Choice number 2: Print tokenized sentences\n Choice number 3: Print original text\n CHOOSE THE ACTION YOU WANT: "))
if choice == 1:
    print(nltk.word_tokenize(doc))
elif choice == 2:
    print(nltk.sent_tokenize(doc))
else :
    print(doc)
    
    

