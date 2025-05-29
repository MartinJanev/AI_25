from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

dataset = []

if __name__ == '__main__':
    X = int(input())

    dataset_0, dataset_1 = [row for row in dataset if row[-1] == 0], [row for row in dataset if row[-1] == 1]

    train_set_0, test_set_0 = dataset_0[:int(X / 100 * len(dataset_0))], dataset_0[int(X / 100 * len(dataset_0)):]
    train_set_1, test_set_1 = dataset_1[:int(X / 100 * len(dataset_1))], dataset_1[int(X / 100 * len(dataset_1)):]

    model1 = GaussianNB()
    model2 = DecisionTreeClassifier(random_state=0, criterion="entropy")
    model3 = RandomForestClassifier(random_state=0, criterion="entropy", n_estimators=4)
    model4 = MLPClassifier(hidden_layer_sizes=(10,), activation='relu', learning_rate_init=0.001, random_state=0)

    train_set = train_set_0 + train_set_1
    test_set = test_set_0 + test_set_1

    train_X, test_X = [row[:-1] for row in train_set], [row[:-1] for row in test_set]
    train_y, test_y = [row[-1] for row in train_set], [row[-1] for row in test_set]

    models = [model1, model2, model3, model4]
    names = ["Naive Bayes", "Decision Tree", "Random Forest", "MLP"]
    acc = []
    for model in models:
        model.fit(train_X, train_y)
        accuracy = model.score(test_X, test_y)
        acc.append(accuracy)

    index = acc.index(max(acc))

    print(f"Najgolema tochnost ima modelot: {names[index]}")

    TP = 0
    FN = 0

    for row_x, class_ in zip(test_X, test_y):
        votes_0 = 0
        votes_1 = 0

        for i, model in enumerate(models):
            pred = model.predict([row_x])[0]
            if pred == 0:
                votes_0 += 2 if i == index else 1
            else:
                votes_1 += 2 if i == index else 1
        final_pred = 0 if votes_0 > votes_1 else 1

        if final_pred == 1 and final_pred == class_:
            TP += 1
        elif final_pred == 0 and final_pred != class_:
            FN += 1
    print(f"Obukvata tochnost e: {TP / (TP + FN) * 100:.2f}%")

