import nltk
import numpy
from nltk.stem  import LancasterStemmer
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk import ngrams,ne_chunk,wordpunct_tokenize,pos_tag

with open('output.txt', 'r', encoding='utf-8') as f:
 raw=f.read()
#Tokenization
wtokens=nltk.word_tokenize(raw)
words=[word.lower() for word in wtokens if word.isalpha()]
print(words)
#Adding tag
print(nltk.pos_tag(words))
lStem = LancasterStemmer()
print("Lancaster Stemming :----------------------------------------------------- \n")
for tok in words:
    print(lStem.stem(str(tok)))
lemmatizer = WordNetLemmatizer()
print("Lemmatization ------------------------------------------------------------:\n")
for tok in words:
    print(lemmatizer.lemmatize(str(tok)))
print("Trigrams --------------------------------------------:\n")
trigram = []
x=0

trigram.append(list(ngrams(words, 3)))
print(trigram)
print("NER-------------------------------------\n")
print("NER : \n", ne_chunk(pos_tag(wordpunct_tokenize(str(words)))))
