
from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB
from ml_factory.helper import Helper


class GaussianNBService:
    def __init__(self, url, columns, scoring):
        self._url = url
        self._columns = columns
        self._scoring = scoring

    def predict(self):

        print('Preparing the data')
        s1 = Helper()
        self._X, self._Y = s1.fetch_data(self._url, self._columns)

        print('Predicting with Gaussian N B')
        kfold = model_selection.KFold(n_splits=10)
        cv_results = model_selection.cross_val_score(GaussianNB(), self._X, self._Y, cv=kfold, scoring=self._scoring)
        modelScore = {}
        modelScore['Algorithm'] = 'Gaussian N B'
        modelScore['Mean Accuracy'] = cv_results.mean()
        modelScore['Standard deviation Accuracy'] = cv_results.std()
        return modelScore


class GaussianNBServiceBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, source_url, names, scoring, **_ignored):
        if not self._instance:
            # url, columns = self.authorize(source_url, names)
            self._instance = GaussianNBService(source_url, names, scoring)
        return self._instance
