import numpy as np
import pandas as pd
import xgboost as xgb
from xgboost.sklearn import XGBClassifier
# from lightgbm.sklearn import LGBMClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import roc_auc_score, accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer


pd.options.mode.chained_assignment = None

train_df = pd.read_csv('../input/train.csv')
test_df = pd.read_csv('../input/test.csv')

# Embarked deal with missing values
features = ['平均坡向', '平均高程', '地形粗糙度', '最小曲率', '水系距', '斷層距', '順向坡指標', 'f_60', 'f_85', 'f_5', 'f_20','崩塌']
train_df = train_df[features]
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
train_df = pd.DataFrame(imp.fit_transform(train_df),columns=features)
features.remove('崩塌')
test_df=test_df[features]
test_df = pd.DataFrame(imp.fit_transform(test_df),columns=features)


train_set = train_df
test_set = test_df

# prepare datasets
train_y = train_set['崩塌']
train_x = train_set[features]

train_x, test_x, train_y, test_y = train_test_split(train_x, train_y, test_size=0.25, random_state=42)
# test_x = train_x
# test_y = train_y

# train
params = {
    'n_estimators': 860,
    # 'learning_rate': 0.02,
    'eta': 0.02,
    'objective': 'binary:logistic',
    'subsample': 0.8,   #
    'colsample_bytree': 1,  #
    'min_child_weight': 1,  #
    'max_depth': 9, #
    'gamma': 0, #
    'reg_alpha': 0, #
    'reg_lambda': 1,    #
    'tree_method': 'exact',
    'scale_pos_weight': 16,  #
    'base_score': 0.5,
    # 'max_delta_step':4
    # 'missing': -999
}
model = XGBClassifier(**params)

# cross validation
scores = cross_val_score(model, train_x, train_y, cv=5)
print('Cross validation scores: ', scores)
print('Mean score: ', np.mean(scores))

model.fit(train_x, train_y)
pred_y = model.predict(test_x)
auc = roc_auc_score(test_y, pred_y)
print('AUC: {0:.3f}'.format(auc))
acc = accuracy_score(test_y, pred_y)
print('Accuracy: {0:.3f}'.format(acc))

# matrix = confusion_matrix(test_y, pred_y)
# print(matrix)
# report = classification_report(test_y, pred_y)
# print(report)

# predict
pred = pd.read_csv('../input/sample_submission.csv')
test_pred = model.predict(test_set)
pred['Collapse'] = test_pred
pred.to_csv('output.csv', index=None)