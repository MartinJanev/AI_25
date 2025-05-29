from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

if __name__ == '__main__':
    P = int(input())
    C = input()
    L = int(input())

    split = int(P * len(dataset) / 100)

    train_set = dataset[:split]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]
    test_set = dataset[split:]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    model_params = {
        'criterion': C,
        'max_leaf_nodes': L,
        'random_state': 0
    }

    model1 = DecisionTreeClassifier(**model_params)
    model1.fit(train_X, train_Y)

    acc1 = model1.score(test_X, test_Y)

    models = []
    # Train a separate model for each class - 'Perch', 'Roach', 'Bream'
    for class_ in ['Perch', 'Roach', 'Bream']:
        model = DecisionTreeClassifier(**model_params)
        model.fit(train_X, [1 if label == class_ else 0 for label in train_Y])
        models.append((class_, model))

    count2 = 0
    # It is correct if the apropriate model predicts 1 and the others predict 0
    for row_x, label in zip(test_X, test_Y):
        all_models_predict_correct = True
        for class_, model in models:
            pred = model.predict([row_x])[0]
            # Here is checked the model for the class of check
            if pred == label:
                if pred != 1:
                    all_models_predict_correct = False
                    break
            else:
                # Here are checked the other models
                if pred != 0:
                    all_models_predict_correct = False
                    break
        if all_models_predict_correct:
            count2 += 1

    acc2 = count2 / len(test_X)

    print(f"Tochnost so originalniot klasifikator: {acc1}")
    print(f"Tochnost so kolekcija od klasifikatori: {acc2}")
