# import os
#
# os.environ['OPENBLAS_NUM_THREADS'] = '1'
#
# from submission_script import *
# from dataset_script import dataset
from zad1_dataset import dataset
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
import numpy as np

if __name__ == '__main__':
    # Одвојување на податоците во X и Y
    X = [row[:-1] for row in dataset]
    Y = [row[-1] for row in dataset]

    # Енкодирање на X
    encoder = OrdinalEncoder()
    encoder.fit(X)

    # Рачно делење на податоците 75% / 25%
    threshold1 = int(0.25 * len(dataset))
    threshold2 = int(0.5 * len(dataset))
    threshold3 = int(0.75 * len(dataset))

    train_X1 = X[:threshold1]
    train_Y1 = Y[:threshold1]

    train_X2 = X[threshold1:threshold2]
    train_Y2 = Y[threshold1:threshold2]

    train_X3 = X[threshold2:threshold3]
    train_Y3 = Y[threshold2:threshold3]

    test_X = X[threshold3:]
    test_Y = Y[threshold3:]

    # Тренирање на класификаторот
    classifier1 = CategoricalNB()
    classifier2 = CategoricalNB()
    classifier3 = CategoricalNB()

    train_X1 = encoder.transform(train_X1)
    train_X2 = encoder.transform(train_X2)
    train_X3 = encoder.transform(train_X3)

    test_X = encoder.transform(test_X)

    classifier1.fit(train_X1, train_Y1)
    classifier2.fit(train_X2, train_Y2)
    classifier3.fit(train_X3, train_Y3)

    cou = 0
    for i in range(len(test_X)):
        counter = 0
        preds1 = classifier1.predict([test_X[i]])[0]
        if preds1 == test_Y[i]:
            counter += 1
        preds2 = classifier2.predict([test_X[i]])[0]
        if preds2 == test_Y[i]:
            counter += 1
        preds3 = classifier3.predict([test_X[i]])[0]
        if preds3 == test_Y[i]:
            counter += 1
        if counter >= 2:
            cou += 1
    cou /= len(test_Y)

    print(cou)

    # Читање еден нов запис за предвидување

    input_record = input().strip().split(' ')
    input_encoded = encoder.transform([input_record])

    pred_class1 = classifier1.predict(input_encoded)[0]
    pred_class2 = classifier2.predict(input_encoded)[0]
    pred_class3 = classifier3.predict(input_encoded)[0]
    if pred_class1 == pred_class2 and pred_class2 == pred_class3:
        print(pred_class1)
    else:
        print("Klasata ne moze da bide odredena")
    # Печатење резултати
    # Submit функции
    # submit_train_data(train_X, train_Y)
    # submit_test_data(test_X, test_Y)
    # submit_classifier(classifier)
    # submit_encoder(encoder)
