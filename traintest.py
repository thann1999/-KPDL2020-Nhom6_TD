# Chia tập train/test
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import os
import fasttext
import time
from cleandata import * 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
import numpy as np
MODEL_PATH = "models"
if not os.path.exists(MODEL_PATH):
    os.makedirs(MODEL_PATH)
# tỉ lệ tập test - train là 8 : 2
test_percent = 0.2
 
text = []
label = []
 
for line in open('data/topic_detection_prep.txt', "r", encoding="utf8"):
    words = line.strip().split()
    label.append(words[0])
    text.append(' '.join(words[1:]))
 
X_train, X_test, y_train, y_test = train_test_split(text, label, test_size=test_percent, random_state=42)
 
# Lưu train/test data
# Giữ nguyên train/test để về sau so sánh các mô hình cho công bằng
with open('data/train.txt', 'w', encoding="utf8") as fp:
    for x, y in zip(X_train, y_train):
        fp.write('{} {}\n'.format(y, x))
 
with open('data/test.txt', 'w', encoding="utf8") as fp:
    for x, y in zip(X_test, y_test):
        fp.write('{} {}\n'.format(y, x))
 
# encode label
label_encoder = LabelEncoder()
label_encoder.fit(y_train)
# print(list(label_encoder.classes_), '\n')
y_train = label_encoder.transform(y_train)
y_test = label_encoder.transform(y_test)
    
# start_time = time.time()
# text_clf = Pipeline([('vect', CountVectorizer(ngram_range=(1,1),
#                                              max_df=0.8,
#                                              max_features=None)), 
#                      ('tfidf', TfidfTransformer()),
#                      ('clf', LogisticRegression(solver='lbfgs', 
#                                                 multi_class='auto',
#                                                 max_iter=10000))
#                     ])
# text_clf = text_clf.fit(X_train, y_train)

# train_time = time.time() - start_time
# print('Done training Linear Classifier in', train_time, 'seconds.')

# # Save model
# pickle.dump(text_clf, open(os.path.join(MODEL_PATH, "linear_classifier.pkl"), 'wb'))


# Linear Classifier
model = pickle.load(open(os.path.join(MODEL_PATH,"linear_classifier.pkl"), 'rb'))
with open('data/result1.txt', 'w', encoding="utf8") as fp:
    for line in open('data/topic_detection_test_prep.txt', 'r', encoding="utf8"):
        label = model.predict([line])
        fp.write(str(label_encoder.inverse_transform(label)) + ' ' + line)

    

