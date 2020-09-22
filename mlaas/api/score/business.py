from ml_factory import model


def fetch_model_score(data):

    config = {
        'source_url': data.get('source_url'),
        'names': list(data.get('field_names').split(",")),
        'scoring': 'accuracy'
    }
    algorithm = data.get('algorithm')
    modelService = model.services.get(algorithm, **config)
    score = modelService.predict()
    return score
