import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

# from submission_script import *
# from dataset_script import dataset
from zad1_dataset import dataset

from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score
import numpy as np

if __name__ == '__main__':
    # Одвојување на податоците во X и Y
    X = [row[:-1] for row in dataset]
    Y = [row[-1] for row in dataset]

    # Енкодирање на X
    encoder = OrdinalEncoder()
    X_encoded = encoder.fit_transform(X)

    # Рачно делење на податоците 75% / 25%
    threshold = int(0.75 * len(dataset))
    train_X = X_encoded[:threshold]
    test_X = X_encoded[threshold:]
    train_Y = Y[:threshold]
    test_Y = Y[threshold:]

    # Тренирање на класификаторот
    classifier = CategoricalNB()
    classifier.fit(train_X, train_Y)

    # Предвидување на тест сет
    preds = classifier.predict(test_X)
    acc = sum(1 for true, pred in zip(test_Y, preds) if true == pred) / len(test_Y)

    # Читање еден нов запис за предвидување
    input_record = input().strip().split(' ')
    input_encoded = encoder.transform([input_record])
    pred_class = classifier.predict(input_encoded)[0]
    pred_probs = classifier.predict_proba(input_encoded)[0]

    # Печатење резултати
    print(acc)
    print(pred_class)
    print(np.array([pred_probs]))
    # Submit функции
    # submit_train_data(train_X, train_Y)
    # submit_test_data(test_X, test_Y)
    # submit_classifier(classifier)
    # submit_encoder(encoder)
