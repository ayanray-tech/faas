import logging

from flask import request
from flask_restplus import Resource
from api.score.business import fetch_model_score_using_factory
from api.score.business import fetch_model_score_using_strategy
from api.score.serializers import model_score
from api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('model/score', description='Scoring by different ML Models')


@ns.route('/usingfactory')
class PostsCollectionFactory(Resource):

    @api.expect(model_score)
    def post(self):
        """
        Calculates score of a Model using Factory Design Pattern.
        """
        score = fetch_model_score_using_factory(request.json)
        print('SCORE', score)
        return score, 200


@ns.route('/usingstrategy')
class PostsCollectionStrategy(Resource):

    @api.expect(model_score)
    def post(self):
        """
        Calculates score of a Model using Strategy Design Pattern.
        """
        score = fetch_model_score_using_strategy(request.json)
        print('SCORE', score)
        return score, 200
