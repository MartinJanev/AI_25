import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

# from submission_script import *
# from dataset_script import dataset
from zad2_dataset import dataset

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import numpy as np

if __name__ == '__main__':
    # Одвојување на податоците во X и Y - categorical и class
    X = [row[:-1] for row in dataset]
    Y = [int(row[-1]) for row in dataset]

    # Претвори X во флоат вредности
    X = [list(map(float, x)) for x in X]

    print(len(X))

    # Подели на тренинг и тест сет
    threshold = int((85 * len(X))/100)
    print(threshold)
    train_X = X[:threshold]
    test_X = X[threshold:]
    train_Y = Y[:threshold]
    test_Y = Y[threshold:]

    # Тренирање на GaussianNB
    classifier = GaussianNB()
    classifier.fit(train_X, train_Y)

    # Предвидување на тест сет
    preds = classifier.predict(test_X)
    acc = accuracy_score(test_Y, preds)

    # Читање еден нов запис за предвидување
    input_record = input().strip().split(' ')
    input_record = list(map(float, input_record))
    input_encoded = [input_record]

    pred_class = classifier.predict(input_encoded)[0]
    pred_probs = classifier.predict_proba(input_encoded)[0]

    # Печатење резултати
    print(f"{acc}")
    print(pred_class)
    print(np.array([pred_probs]))

    # Submit функции
#     submit_train_data(train_X, train_Y)
#     submit_test_data(test_X, test_Y)
#     submit_classifier(classifier)
#
# # povtoren import na kraj / ne ja otstranuvajte ovaa linija
# import submission_script
