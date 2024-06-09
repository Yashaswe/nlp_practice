class Category:
  BOOKS = "BOOKS"
  CLOTHING = "CLOTHING"

train_x = ["i love the books", "this is a great book", "the fit looks great", "i love the shoes"]
train_y = [Category.BOOKS, Category.BOOKS, Category.CLOTHING, Category.CLOTHING]

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
train_x_vectors = vectorizer.fit_transform(train_x)

# get unique names
# print(vectorizer.get_feature_names_out())

# get data in vector format
# print(vectors.toarray())

# CLASSIFIER 

from sklearn import svm

clf_svm = svm.SVC(kernel = "linear")
clf_svm.fit(train_x_vectors, train_y)

test_x = vectorizer.transform(['i like the book'])
predicted = clf_svm.predict(test_x)
print(predicted)

