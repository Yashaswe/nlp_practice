#Bag of Words model is used to preprocess the text by converting it into a bag of words, which keeps a count of the total occurrences of most frequently used words. It does not capture information about a word's meaning or context.
#BoW representation provides insights into the importance of different terms within the text. By counting the frequency of words, we can observe which words occur more frequently
#One hot coding allows words and phrases to be represented as numeric vectors. A unique index is assigned to each unique category (word or phrase), creating a binary vector of length equal to the total number of categories. This vector is called a “one hot” encoded vector because only one element is “hot” or active at a time.

class Category:
  BOOKS = "BOOKS"
  CLOTHING = "CLOTHING"

train_x = ["i love the books", "this is a great book", "the fit looks great", "i love the shoes"]
train_y = [Category.BOOKS, Category.BOOKS, Category.CLOTHING, Category.CLOTHING]

from sklearn.feature_extraction.text import CountVectorizer

# One Hot Encoding
# vectorizer = CountVectorizer(binary = True)

# Bag of Words
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

test_x = vectorizer.transform(['i like the book', "i love the story"])
predicted = clf_svm.predict(test_x)
print(predicted)

