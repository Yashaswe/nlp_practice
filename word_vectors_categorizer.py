# Word vectors represent words as multidimensional continuous floating point numbers where semantically similar words are mapped to proximate points in geometric space. In simpler terms, a word vector is a row of real-valued numbers (as opposed to dummy numbers) where each point captures a dimension of the word's meaning and where semantically similar words have similar vectors.
import spacy
from sklearn import svm

nlp = spacy.load("en_core_web_md")

class Category:
  BOOKS = "BOOKS"
  CLOTHING = "CLOTHING"
  
train_x = ["i love the books", "this is a great book", "the fit looks great", "i love the shoes"]
train_y = [Category.BOOKS, Category.BOOKS, Category.CLOTHING, Category.CLOTHING]

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
train_x_vectors = vectorizer.fit_transform(train_x)

docs = [nlp(text) for text in train_x]
train_x_word_vectors = [x.vector for x in docs]
print(docs[0].vector)

clf_svm = svm.SVC(kernel = "linear")
clf_svm.fit(train_x_word_vectors, train_y)
test_x = ["i love the books", "i love the story", "i love the book"]
test_docs = [nlp(text) for text in test_x]
test_x_vectors = [x.vector for x in test_docs]
predicted = clf_svm.predict(test_x_vectors)
print(predicted)