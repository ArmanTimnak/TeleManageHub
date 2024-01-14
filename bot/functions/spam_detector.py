import json
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

def spam_detector(message):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    spam_file_path = os.path.join(dir_path, '..', 'data', 'spam.json')
    with open(spam_file_path, 'r') as f:
        data = json.load(f)

    data = data['messages']

    messages = [str(item['Message']) for item in data]
    labels = [item['Category'] for item in data]

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(messages)

    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

    clf = MultinomialNB()
    clf.fit(X_train, y_train)

    return clf.predict(vectorizer.transform([message]))[0]