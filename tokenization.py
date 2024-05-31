#Corpus - Paragraph
#Documents - sentences
#Vocabulary - Unique word
#Words
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize, TreebankWordTokenizer


corpus = "Hello! This is Yashaswe Amatya. I am a student at Gettysburg College. It's a beautiful day."

# Paragraphs -> Sentence

sentences = sent_tokenize(corpus)
print(sentences)

# Paragraph -> Words
# Sentence -> Words

words = word_tokenize(corpus)
print(words)

# Treat punctuation as seperate words
punc_words = wordpunct_tokenize(corpus)
print(punc_words)

# Include fullstop with the word except the last fullstop
tokenizer = TreebankWordTokenizer()
treebank_words = tokenizer.tokenize(corpus)
print(treebank_words)






