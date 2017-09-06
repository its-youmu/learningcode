# a simple loop that outputs a value if there is a listed item in the string it receives, otherwise it's ignored
# feel free to use and lemme know if it was helpful
# https://github.com/its-youmu
# requires nltk from http://www.nltk.org/install.html
# might want to replace the tokens with other values

from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize

# regex to remove punctuation
tokenizer = RegexpTokenizer(r'\w+')

itsList = ["true", "same", "item3"]

# list compare
def i_true(text):
    valueList = [] # need to define empty list to append later
    q = 0
    y = tokenizer.tokenize(text) # break the string into a list broken apart by spaces, and remove any punctuation
    y = [w.lower() for w in y] # make everything lowercase

# this will loop for every item in itsList (three words), it will compare to each item in the text you send it, and 
    for z in itsList:
        if z in y:
            valueList.append("CHECK")
            q += 1
        else:
            valueList.append("UNCHECK")
            q += 1
    if "CHECK" in valueList: # dont forget to update this string if you change the other
        print(*(map('{} {}'.format, valueList, itsList)))
    else:
        return

sentence = "This is a great sentence. TRuE same. same same"
i_true(sentence)

# CHECK true CHECK same UNCHECK item3

sentence2 = "No words listed are put here."
i_true(sentence2)

# this will output nothing, the 'else' just returns with no value

sentence3 = "True same item3!!!! item34!"
i_true(sentence3)

# CHECK true CHECK same CHECK item3
