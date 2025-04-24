import csv

from sklearn.naive_bayes import CategoricalNB, GaussianNB
from sklearn.preprocessing import OrdinalEncoder


def readFile(path):
    with open(path) as file:
        reader = csv.reader(file)
        lines = list(reader)[1:]
    return lines


def main():
    # read data

    data = readFile('car.csv')

    # preprocessing

    encoder = OrdinalEncoder()
    X = [row[:-1] for row in data]
    encoder.fit(X)

    X_encoded = encoder.transform(X)

    # split data into train and test
    Y = [row[-1] for row in data]

    # 0.7 train, 0.3 test - ima situacija so delenje dali vo 70 ili celoto vrz 100

    threshold = int(0.7 * len(data))
    train_X = X_encoded[:threshold]
    test_X = X_encoded[threshold:]

    train_Y = Y[:threshold]
    test_Y = Y[threshold:]

    # fit the classifier

    classifier = CategoricalNB()

    classifier.fit(train_X, train_Y)

    # predict the test data

    # predY = classifier.predict(test_X)

    prediction_0 = classifier.predict([test_X[0]])[0]
    predY = classifier.predict(test_X)

    # calculate accuracy

    suma = sum(1 for pred, true in zip(predY, test_Y) if pred == true)
    print(suma / len(test_Y))

    # work with input




main()
