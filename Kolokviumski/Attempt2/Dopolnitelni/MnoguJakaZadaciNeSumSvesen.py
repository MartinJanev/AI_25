import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

from dataset_script import dataset  # this will import the dataset on coderunner at courses
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler


def modifyDataset(dataset):
    dataset = [[row[0] + row[10]] + [el for ind, el in enumerate(row) if ind not in [0, 10]] for row in dataset]
    return dataset


def train_test_splitter(dataset, C, P):
    dataset_good = [row for row in dataset if row[-1] == 'good']
    dataset_bad = [row for row in dataset if row[-1] == 'bad']

    train_set, test_set = [], []
    if C == 0:
        limit_g = int(len(dataset_good) * P / 100)
        limit_b = int(len(dataset_bad) * P / 100)

        train_set = dataset_good[:limit_g] + dataset_bad[:limit_b]
        test_set = dataset_good[limit_g:] + dataset_bad[limit_b:]
    elif C == 1:
        limit_g = int(len(dataset_good) * (100 - P) / 100)
        limit_b = int(len(dataset_bad) * (100 - P) / 100)

        train_set = dataset_good[limit_g:] + dataset_bad[limit_b:]
        test_set = dataset_good[:limit_g] + dataset_bad[:limit_b]

    return ([row[:-1] for row in train_set],
            [row[-1] for row in train_set],
            [row[:-1] for row in test_set],
            [row[-1] for row in test_set],
            )


def scale(train_X, test_X):
    scaler = MinMaxScaler(feature_range=(-1, 1))
    train_X = scaler.fit_transform(train_X)
    test_X = scaler.transform(test_X)

    return train_X, test_X


def main():
    global dataset

    newDataset = modifyDataset(dataset)
    C = int(input())
    P = int(input())

    train_X, train_y, test_X, test_y = train_test_splitter(newDataset, C, P)

    scaled_train_X, scaled_test_X = scale(train_X, test_X)

    clf1 = GaussianNB()
    clf1.fit(train_X, train_y)

    clf2 = GaussianNB()
    clf2.fit(scaled_train_X, train_y)

    predY1 = clf1.predict(test_X)
    predY2 = clf2.predict(scaled_test_X)

    acc1 = sum(1 for true, pred in zip(test_y, predY1) if true == pred) / len(test_y)
    acc2 = sum(1 for true, pred in zip(test_y, predY2) if true == pred) / len(test_y)

    print("Broj na podatoci vo train se: " + str(len(train_X)))
    print("Broj na podatoci vo test se: " + str(len(test_X)))
    # print("Tochnost so zbir na koloni:", acc1)
    # print("Tochnost so zbir na koloni i skaliranje:", acc2)


main()
