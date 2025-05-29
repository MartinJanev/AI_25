from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def read_dataset():
    data = []
    with open("winequality.csv") as f:
        _ = f.readline()
        while True:
            line = f.readline().strip()
            if line == '':
                break
            parts = line.split(";")
            data.append(list(map(float, parts[:-1])) + [parts[-1]])
    return data


if __name__ == '__main__':
    dataset = read_dataset()

    dataset_good = [row for row in dataset if row[-1] == "good"]
    dataset_bad = [row for row in dataset if row[-1] == "bad"]

    limit1 = int(0.7 * len(dataset_good))
    limit2 = int(0.7 * len(dataset_bad))

    limit3 = int(0.8 * len(dataset_good))
    limit4 = int(0.8 * len(dataset_bad))

    train_set = dataset_bad[:limit1] + dataset_good[:limit2]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]

    val_set = dataset_bad[limit1:limit3] + dataset_good[limit2:limit4]
    val_X = [row[:-1] for row in val_set]
    val_Y = [row[-1] for row in val_set]

    test_set = dataset_bad[limit3:] + dataset_good[limit4:]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    clf_1 = MLPClassifier(hidden_layer_sizes=5,
                          random_state=0,
                          activation="relu",
                          learning_rate_init=0.001,
                          max_iter=500)
    clf_2 = MLPClassifier(hidden_layer_sizes=10,
                          random_state=0,
                          activation="relu",
                          learning_rate_init=0.001,
                          max_iter=500)
    clf_3 = MLPClassifier(hidden_layer_sizes=100,
                          random_state=0,
                          activation="relu",
                          learning_rate_init=0.001,
                          max_iter=500)

    clf_1.fit(train_X, train_Y)
    clf_2.fit(train_X, train_Y)
    clf_3.fit(train_X, train_Y)

    # Validation, not test set
    predictions1 = clf_1.predict(val_X)
    predictions2 = clf_2.predict(val_X)
    predictions3 = clf_3.predict(val_X)

    acc_1 = accuracy_score(val_Y, predictions1)
    acc_2 = accuracy_score(val_Y, predictions2)
    acc_3 = accuracy_score(val_Y, predictions3)

    if acc_1 >= acc_2 and acc_1 >= acc_3:
        pred = clf_1.predict(test_x)
        acc = accuracy_score(test_y, pred)
        print(f'Tochnost so testirachko mnozestvo: {acc}')
    elif acc_2 >= acc_1 and acc_2 >= acc_3:
        pred = clf_2.predict(test_x)
        acc = accuracy_score(test_y, pred)
        print(f'Tochnost so testirachko mnozestvo: {acc}')
    else:
        pred = clf_3.predict(test_x)
        acc = accuracy_score(test_y, pred)
        print(f'Tochnost so testirachko mnozestvo: {acc}')

    standard_scaler = StandardScaler()
    standard_scaler.fit(train_X)

    classifier_scaled = MLPClassifier(hidden_layer_sizes=10,
                                      activation="relu",
                                      learning_rate_init=0.001,
                                      max_iter=500,
                                      random_state=0)

    classifier_scaled.fit(standard_scaler.transform(train_X), train_Y)
    predictions4 = classifier_scaled.predict(standard_scaler.transform(val_X))
    acc_4 = accuracy_score(val_Y, predictions4)
    print(f'Tochnost so normalizacii: {acc_4}')

    minmax_scaler = MinMaxScaler(feature_range=(-1, 1))
    minmax_scaler.fit(train_X)

    classifier_scaled = MLPClassifier(hidden_layer_sizes=10,
                                      activation="relu",
                                      learning_rate_init=0.001,
                                      max_iter=500,
                                      random_state=0)
    classifier_scaled.fit(minmax_scaler.transform(train_X), train_Y)
    predictions5 = classifier_scaled.predict(minmax_scaler.transform(val_X))
    acc_5 = accuracy_score(val_Y, predictions5)
    print(f'Tochnost so minmax normalizacii: {acc_5}')

    tp, tn, fp, fn = 0, 0, 0, 0

    for true, pred in zip(val_Y, predictions5):
        if true == "good" and pred == "good":
            tp += 1
        elif true == "bad" and pred == "bad":
            tn += 1
        elif true == "bad" and pred == "good":
            fp += 1
        elif true == "good" and pred == "bad":
            fn += 1

    acc_best = (tp + tn) / (tp + tn +   fp + fn)
    prec_best = tp / (tp + fp)
    rec_best = tp / (tp + fn)
