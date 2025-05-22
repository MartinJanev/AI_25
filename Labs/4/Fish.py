import os

from sklearn.ensemble import RandomForestClassifier

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset

# from zad2_dataset import *

if __name__ == '__main__':
    col_index = int(input())
    num_of_trees = int(input())
    criterion = input()
    arr = input().split()

    deleted_dataset_col = list()
    for row in dataset:
        deleted_dataset_col.append([row[i] for i in range(0, len(row)) if i != col_index])
    dataset_updated = deleted_dataset_col

    limit = int(0.85 * len(dataset_updated))

    train_set = dataset_updated[:limit]
    test_set = dataset_updated[limit:]

    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]

    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    classifier = RandomForestClassifier(n_estimators=num_of_trees, criterion=criterion, random_state=0)
    classifier.fit(train_X, train_Y)

    acc = 0
    for i in range(len(test_set)):
        predicted = classifier.predict([test_X[i]])[0]
        true = test_Y[i]
        if predicted == true:
            acc += 1
    print(f"Accuracy: {acc / len(test_X)}")

    array = [arr[i] for i in range(len(arr)) if i != col_index]
    print(classifier.predict([array])[0])
    print(classifier.predict_proba([array])[0])
    # Vashiot kod tuka

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo
    # i klasifikatorot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    submit_classifier(classifier)
