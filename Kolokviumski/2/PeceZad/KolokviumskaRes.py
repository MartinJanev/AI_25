import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

from dataset_script import dataset  # this will import the dataset on coderunner at courses
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler


def modify_dataset(dataset):
    dataset = [[row[0] + row[10]] + [el for ind, el in enumerate(row) if ind not in [0, 10]] for row in dataset]
    return dataset


def split_dataset(dataset, C, P):
    dataset_good = [row for row in dataset if row[-1] == "good"]
    dataset_bad = [row for row in dataset if row[-1] == "bad"]

    if C == 0:
        train_set = dataset_good[:int(P / 100 * len(dataset_good))] + dataset_bad[:int(P / 100 * len(dataset_bad))]
        test_set = dataset_good[int(P / 100 * len(dataset_good)):] + dataset_bad[int(P / 100 * len(dataset_bad)):]

        train_X, test_X = [el[:-1] for el in train_set], [el[:-1] for el in test_set]
        train_y, test_y = [el[-1] for el in train_set], [el[-1] for el in test_set]
    else:
        train_set = dataset_good[int((100 - P) / 100 * len(dataset_good)):] + dataset_bad[
                                                                              int((100 - P) / 100 * len(dataset_bad)):]
        test_set = dataset_good[:int((100 - P) / 100 * len(dataset_good))] + dataset_bad[
                                                                             :int((100 - P) / 100 * len(dataset_bad))]

        train_X, test_X = [el[:-1] for el in train_set], [el[:-1] for el in test_set]
        train_y, test_y = [el[-1] for el in train_set], [el[-1] for el in test_set]

    return train_X, test_X, train_y, test_y


def scale(train_X, test_X):
    scaler = MinMaxScaler(feature_range=(-1, 1))
    train_X_scaled = scaler.fit_transform(train_X)
    test_X_scaled = scaler.transform(test_X)

    return train_X_scaled, test_X_scaled


def main():
    global dataset

    C = int(input())
    P = int(input())

    new_dataset = modify_dataset(dataset)

    train_X, test_X, train_y, test_y = split_dataset(new_dataset, C, P)

    train_X_scaled, test_X_scaled = scale(train_X, test_X)

    bayes1 = GaussianNB()
    bayes1.fit(train_X, train_y)

    bayes2 = GaussianNB()
    bayes2.fit(train_X_scaled, train_y)

    print(f"Tochnost: {bayes1.score(test_X, test_y) * 100:.2f}%")
    print(f"Tochnost: {bayes2.score(test_X_scaled, test_y) * 100:.2f}%")


main()
