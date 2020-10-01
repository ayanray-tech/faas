from ml_factory import  model as factory_model
from ml_strategy import model as strategy_model


def fetch_model_score_using_factory(data):

    config = {
        'source_url': data.get('source_url'),
        'names': list(data.get('field_names').split(",")),
        'scoring': 'accuracy'
    }
    algorithm = data.get('algorithm')
    modelService = factory_model.services.get(algorithm, **config)
    score = modelService.predict()
    return score


def fetch_model_score_using_strategy(data):

    url = data.get('source_url')
    columns = list(data.get('field_names').split(","))
    algorithm = data.get('algorithm')
    scoring = 'accuracy'

    strat = strategy_model.selectModel(algorithm, url, columns, scoring)

    isString = isinstance(strat, str)
    print('Type is : ', type)

    modelScore = {}

    if not isString:
        strat._url = url
        strat._columns = columns
        strat._scoring = scoring
        modelScore = strat.execute()

    else:
        modelScore['Algorithm'] = strat
        modelScore['Mean Accuracy'] = 0.0
        modelScore['Standard deviation Accuracy'] = 0.0

    return modelScore
