from textblob import TextBlob
import nltk

nltk.download('averaged_perceptron_tagger')

# spell correction
phrase = "thiis is an example"

tb_phrase = TextBlob(phrase)
corrected_phrase = tb_phrase.correct()
print(corrected_phrase)

# part of speech tagging
phrase2 = "I read the books"
tb_phrase2 = TextBlob(phrase2)
corrected_phrase2 = tb_phrase2.correct()
tags_phrase2 = tb_phrase2.tags

print(tags_phrase2)

# sentiment
# phrase3 = "The book was great"
phrase3 = "The book was horrible"
tb_phrase3 = TextBlob(phrase3)
sentiment_phrase3 = tb_phrase3.sentiment

print(sentiment_phrase3)