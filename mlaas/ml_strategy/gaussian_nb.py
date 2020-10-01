from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB
from ml_strategy.helper import Helper


def predictUsingNB(self):

    print('Preparing the data')
    s1 = Helper()
    self._X, self._Y = s1.fetch_data(self._url, self._columns)

    print('Predicting with Gaussian NB')
    kfold = model_selection.KFold(n_splits=10)
    cv_results = model_selection.cross_val_score(GaussianNB(), self._X, self._Y, cv=kfold, scoring=self._scoring)
    modelScore = {}
    modelScore['Algorithm'] = 'Gaussian NB'
    modelScore['Mean Accuracy'] = cv_results.mean()
    modelScore['Standard deviation Accuracy'] = cv_results.std()
    return modelScore
