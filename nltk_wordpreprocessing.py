from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk

nltk.download('wordnet')
nltk.download('stopwords')


# Tokenization and Stemming
stemmer = PorterStemmer()
phrase = "reading the books"
words = word_tokenize(phrase)

stemmed_words = []
for word in words:
  stemmed_words.append(stemmer.stem(word))
  
stemmed_phrase = " ".join(stemmed_words)
print(stemmed_phrase)

# Lemmatization

from nltk.stem import WordNetLemmatizer
lemmatized_words = []
lemmatizer = WordNetLemmatizer()
for word in words:
  lemmatized_words.append(lemmatizer.lemmatize(word))
  
lemmatized_phrase = " ".join(lemmatized_words)
print(lemmatized_phrase)

## Stopword removal

from nltk.corpus import stopwords

stop_words = stopwords.words("english")

phrase = "Here is an example of a sentence where we will use stopwords"

words = word_tokenize(phrase)

stripped_phrase = []
for word in words:
  if word not in stop_words:
    stripped_phrase.append(word)
    
stripped = " ".join(stripped_phrase)
print(stripped)