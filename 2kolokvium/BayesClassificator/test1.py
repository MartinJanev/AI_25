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
    Y = [row[-1] for row in data]
    X = [row[:-1] for row in data]
    # with fit, we learn the mapping of the categories to numbers
    encoder.fit(X)

    # with transform, we apply the mapping to the data
    X_encoded = encoder.transform(X)

    # split data into train and test

    # 0.7 train, 0.3 test - ima situacija so delenje dali vo 70 ili celoto vrz 100

    threshold = int(0.7 * len(data))
    train_X = X_encoded[:threshold]
    test_X = X_encoded[threshold:]

    train_Y = Y[:threshold]
    test_Y = Y[threshold:]

    # fit the classifier

    classifier = CategoricalNB()

    # fit function takes two arguments: the data and the labels
    # essentially, we are training the classifier to learn the mapping between the data and the labels
    classifier.fit(train_X, train_Y)

    # predict the test data

    # predY = classifier.predict(test_X)

    # prediction_0 is the value from predict function for the first element of test_X
    prediction_0 = classifier.predict([test_X[0]])[0]
    #predY is prediction for all test_X
    predY = classifier.predict(test_X)

    # calculate accuracy
    suma = sum(1 for pred, true in zip(predY, test_Y) if pred == true)
    print(suma / len(test_Y))

    # work with input




main()
