#Tokenization

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = [
  'I love my dog',
  'I love my cat',
  'You love my dog!',
  'Do you think my dog is amazing?'
]

tokenizer = Tokenizer(num_words = 100, oov_token = "<OOV>")

# go through all the texts
tokenizer.fit_on_texts(sentences)

# create tokens from words
word_index = tokenizer.word_index

# create sequences of sentences as tokens
sequences = tokenizer.texts_to_sequences(sentences)
print(word_index)
print(sequences)

# to pad sequences or create all sequences with the same length as the maximum sentence
# to add zeros at the end pass: padding = 'post'
# maxlen = N, to specify max length, truncating = 'post' to truncate words more than maxlength
padded_seq = pad_sequences(sequences)
print(padded_seq)

test_data = [
  'i really love my dog',
  'my dog loves my manatee'
]

# corpus used to build the token does't have all the words
# to solve this use oov_token while initializing tokenizer
text_seq = tokenizer.texts_to_sequences(test_data)
print(text_seq)

