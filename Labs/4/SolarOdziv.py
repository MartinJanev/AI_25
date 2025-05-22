import os

from sklearn.metrics import recall_score
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

# Дадено ни е податочно множество за соларен одблесок. Сите атрибути кои ги содржи се од категориски тип. Ваша задача е да истренирате класификатор - дрво на одлука кој ќе предвидува класи на соларен одблесок користејќи ги последните X% од даденото податочно множество. Треба да ја пресметате точноста која ја добивате над останатите (100 - X)% од податочното множество.
#
# Во почетниот код имате дадено податочно множество. На влез се прима вредност за процентот на поделба X. На пример, ако вредноста е 80 значи дека ги користите последните 80% од множеството за тренирање, а првите 20% за тестирање. Дополнително во променливата criterion се вчитува вредност за критериумот за избор на најдобар атрибут.
#
# На излез треба да се испечати точност, длабочина и број на листови на изграденото дрво, како и карактеристиките со најголема и најмала важност.
#
# За да ги добиете истите резултати како и во тест примерите, при креирање на класификаторот поставете random_state=0


os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
# from dataset_script import dataset

from zad1_dataset import *

if __name__ == '__main__':
    encoder = OrdinalEncoder()
    dataset = [row for row in dataset if row[-1] == '0' or row[-1] == '1']

    X = [row[:-1] for row in dataset]
    encoder.fit(X)

    splitt = int(input()) / 100

    limit = int((1 - splitt) * len(dataset))
    train_set = dataset[limit:]
    test_set = dataset[:limit]

    train_X = [row[:-1] for row in train_set]
    train_X = encoder.transform(train_X)
    train_Y = [row[-1] for row in train_set]

    test_X = [row[:-1] for row in test_set]
    test_X = encoder.transform(test_X)
    test_Y = [row[-1] for row in test_set]

    criterion = input()
    classifier = DecisionTreeClassifier(criterion=criterion, random_state=0)
    classifier.fit(train_X, train_Y)

    tp = 0
    fn = 0
    predictions = classifier.predict(test_X)
    for true, pred in zip(test_Y, predictions):
        if true == pred == '1':
            tp += 1
        if true == '1' and pred == '0':
            fn += 1
    print("Odziv: ", tp / (tp + fn))

    col_delete = int(input())

    temp = []
    for row in train_X:
        redica = [row[i] for i in range(len(row)) if i != col_delete]
        temp.append(redica)
    train_X_2 = temp

    temp = []
    for row in test_X:
        redica = [row[i] for i in range(len(row)) if i != col_delete]
        temp.append(redica)
    test_X_2 = temp

    classifier2 = DecisionTreeClassifier(criterion=criterion, random_state=0)
    classifier2.fit(train_X_2, train_Y)

    # print(recall_score(test_Y, classifier2.predict(test_X_2), pos_label='1'))

    tp = 0
    fn = 0
    predictions = classifier2.predict(test_X_2)
    for true, pred in zip(test_Y, predictions):
        if true == pred == '1':
            tp += 1
        if true == '1' and pred == '0':
            fn += 1
    print("Odziv: ", tp / (tp + fn))
