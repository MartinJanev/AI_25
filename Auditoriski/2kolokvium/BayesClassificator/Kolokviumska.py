import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

from dataset_script import dataset
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler


def main():
    global dataset
    C = int(input())
    P = int(input())

    dataset_new = []
    for row in dataset:
        new_row = []
        new_row.append(row[0] + row[-2])  # Збир на првата и последната хемиска карактеристика
        new_row.extend(row[1:-2])  # Средните карактеристики
        new_row.append(row[-1])  # Класата
        dataset_new.append(new_row)

    dataset = dataset_new

    dataset_good = [row for row in dataset if row[-1] == "good"]
    dataset_bad = [row for row in dataset if row[-1] == "bad"]

    if C == 0:
        threshold_good = int(P * len(dataset_good) / 100)
        threshold_bad = int(P * len(dataset_bad) / 100)

        train_good = dataset_good[:threshold_good]
        test_good = dataset_good[threshold_good:]

        train_bad = dataset_bad[:threshold_bad]
        test_bad = dataset_bad[threshold_bad:]
    else:
        threshold_good = int((100 - P) * len(dataset_good) / 100)
        threshold_bad = int((100 - P) * len(dataset_bad) / 100)

        train_good = dataset_good[threshold_good:]
        test_good = dataset_good[:threshold_good]

        train_bad = dataset_bad[threshold_bad:]
        test_bad = dataset_bad[:threshold_bad]

    train = train_good + train_bad
    test = test_good + test_bad

    train_X = [row[:-1] for row in train]
    train_Y = [row[-1] for row in train]

    test_X = [row[:-1] for row in test]
    test_Y = [row[-1] for row in test]

    # Скалирање во [-1, 1]
    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaler.fit(train_X)

    train_x_scaled = scaler.transform(train_X)
    test_x_scaled = scaler.transform(test_X)

    # Наивни баесови класификатори
    classificator1 = GaussianNB()
    classificator2 = GaussianNB()

    classificator1.fit(train_X, train_Y)
    classificator2.fit(train_x_scaled, train_Y)

    predY1 = classificator1.predict(test_X)
    predY2 = classificator2.predict(test_x_scaled)

    acc1 = sum(1 for true, pred in zip(test_Y, predY1) if true == pred) / len(test_Y)
    acc2 = sum(1 for true, pred in zip(test_Y, predY2) if true == pred) / len(test_Y)

    print("Broj na podatoci vo train se: " + str(len(train)))
    print("Broj na podatoci vo test se: " + str(len(test)))
    print("Tochnost so zbir na koloni:", acc1)
    print("Tochnost so zbir na koloni i skaliranje:", acc2)


main()
