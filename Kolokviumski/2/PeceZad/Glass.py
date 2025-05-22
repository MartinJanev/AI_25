from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler


def most_imprtant_feature(train_X, train_Y, L):
    model = RandomForestClassifier(random_state=0, max_leaf_nodes=L)
    model.fit(train_X, train_Y)
    feat_imps = list(model.feature_importances_)  # list of importances of each feature in the model

    # feat_imps = enumerate(feat_imps)
    # sorted_feat_imps = sorted(feat_imps, key=lambda x: x[1], reverse=True)
    #
    # index = sorted_feat_imps[0][0]

    index = feat_imps.index(max(feat_imps))
    return index


def f(train_X, test_X, index):
    train_X_modified = [row[:index] + row[index + 1:] for row in train_X]
    # train_X_modified = [[el for ind, el in enumerate(row) if ind != index]for row in train_X]
    test_X_modified = [row[:index] + row[index + 1:] for row in test_X]

    scaler = StandardScaler()
    scaler.fit(train_X_modified)
    train_X_scaled = scaler.transform(train_X_modified)
    test_X_scaled = scaler.transform(test_X_modified)

    # sample = [1, 2, 3, 14, 3]
    # scaled_sample = scaler.transform([sample])[0]  # returns a 2D array [[-0.5, 0.5, 0.5, 0.5]]

    return train_X_scaled, test_X_scaled


dataset = []
if __name__ == '__main__':
    N = int(input())
    D = int(input())
    L = int(input())

    train_set = dataset[N:]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]
    test_set = dataset[:N]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    index = most_imprtant_feature(train_X, test_X, L)

    train_X_scaled, test_X_scaled = f(train_X, test_X, index)

    model = RandomForestClassifier(random_state=0, n_estimators=D, criterion='gini')
    model.fit(train_X, train_Y)
    acc1 = model.score(test_X, test_Y)

    model.fit(train_X_scaled, train_Y)
    acc2 = model.score(test_X_scaled, test_Y)

    if acc2>acc1:
        print("YES")
    else:
        print("NO")
