import csv

from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OrdinalEncoder


def readFile(path):
    with open(path) as file:
        reader = csv.reader(file)
        lines = list(reader)[1:]
    return lines


def main():
    # read data

    data = readFile('medical_data.csv')

    # preprocessing

    encoder = OrdinalEncoder()
    X = [row[:-1] for row in data]
    # Convert all elements in X to integers for proper encoding
    X = [[int(a) for a in row] for row in X]

    # Learn the mapping of categories to numerical values
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

    classifier = GaussianNB()
    # fit function takes two arguments: the data and the labels
    # essentially, we are training the classifier to learn the mapping between the data and the labels
    classifier.fit(train_X, train_Y)

    # predict the test data

    # predY = classifier.predict(test_X)

    prediction_0 = classifier.predict([test_X[0]])[0]
    predY = classifier.predict(test_X)

    # calculate accuracy

    suma = sum(1 for pred, true in zip(predY, test_Y) if pred == true)
    print(suma / len(test_Y))

    # work with input

    data_read = "100,80"
    data_read = data_read.split(',')
    print(data_read)

    data_read = [int(value) for value in data_read]  # Convert to numeric values
    pred_read = classifier.predict([data_read])[0]
    print(pred_read)


main()
