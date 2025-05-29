import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

from sklearn.tree import DecisionTreeClassifier

from dataset_script import dataset


def split_(data):
    return (
        [row[:-1] for row in data],
        [row[-1] for row in data]
    )


if __name__ == '__main__':
    P = int(input())
    C = input()
    L = int(input())

    limit = int(P/100 * len(dataset))

    train_set = dataset[:limit]
    train_X, train_y = split_(train_set)
    test_set = dataset[limit:]
    test_X, test_y = split_(test_set)

    model_params = {
        'criterion': C,
        'max_leaf_nodes': L,
        'random_state': 0
    }
    tree = DecisionTreeClassifier(**model_params)
    tree.fit(train_X, train_y)

    acc1 = tree.score(test_X, test_y)

    models = []

    for class_ in ["Perch", "Roach", "Bream"]:
        model = DecisionTreeClassifier(**model_params)
        trainY = [1 if label == class_ else 0 for label in train_y]
        model.fit(train_X, trainY)
        models.append((class_, model))

    count2 = 0
    for row_x, label in zip(test_X, test_y):
        all_correct = True
        for class_, model in models:
            pred = model.predict([row_x])[0]
            # ako e soodvetniot model
            if label == class_:
                # ako e taj classifier, ama ne predviduva tocno
                if pred != 1:
                    all_correct = False
                    break
            else:
                # ako ne e taj classifier, a tocno go predviduva
                if pred != 0:
                    all_correct = False
                    break
        if all_correct:
            count2 += 1

    acc2 = count2 / len(test_X)

    print(f"Tochnost so originalniot klasifikator: {acc1}")
    print(f"Tochnost so kolekcija od klasifikatori: {acc2}")
