from ml_strategy.strategy import Strategy
from ml_strategy.logistic_regression import predictUsingLR
from ml_strategy.knn import predictUsingKNN
from ml_strategy.decision_tree_classifier import predictUsingDT
from ml_strategy.gaussian_nb import predictUsingNB
from ml_strategy.lda import predictUsingLDA
from ml_strategy.svc import predictUsingSVM


def selectModel(algorithm, url, columns, scoring):

    switcher = {
                'LR': Strategy(predictUsingLR),
                'KNN': Strategy(predictUsingKNN),
                'CART': Strategy(predictUsingDT),
                'NB': Strategy(predictUsingNB),
                'SVM': Strategy(predictUsingSVM),
                'LDA': Strategy(predictUsingLDA)
             }

    strat = switcher.get(algorithm, "Not a valid model input")

    return strat
