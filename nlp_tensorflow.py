#Tokenization

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
  'I love my dog',
  'I love my cat',
  'You love my dog!',
  'Do you think my dog is amazing?'
]

tokenizer = Tokenizer(num_words = 100)

# go through all the texts
tokenizer.fit_on_texts(sentences)

# create tokens from words
word_index = tokenizer.word_index

# create sequences of sentences as tokens
sentences = tokenizer.texts_to_sequences(sentences)
print(word_index)
print(sentences)
