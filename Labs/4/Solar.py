import os

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
from submission_script import *
from dataset_script import dataset

# from zad1_dataset import *


if __name__ == '__main__':
    encoder = OrdinalEncoder()
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

    print(f"Depth: {classifier.get_depth()}")
    print(f"Number of leaves: {classifier.get_n_leaves()}")

    acc = 0
    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_X[i]])
        true_class = test_Y[i]
        if predicted_class == true_class:
            acc += 1
    print(f"Accuracy: {acc / len(test_set)}")

    features_imp = list(classifier.feature_importances_)
    print(F"Most important feature: {features_imp.index(max(features_imp))}")
    print(f"Least important feature: {features_imp.index(min(features_imp))}")

    # Vashiot kod tuka

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    submit_classifier(classifier)

    # submit na encoderot
    submit_encoder(encoder)
