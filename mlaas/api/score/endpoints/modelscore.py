import logging

from flask import request
from flask_restplus import Resource
from api.score.business import fetch_model_score
from api.score.serializers import model_score
from api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('model/score', description='Scoring by different ML Models')


@ns.route('/')
class PostsCollection(Resource):

    @api.expect(model_score)
    def post(self):
        """
        Calculates score of a Model.
        """
        score = fetch_model_score(request.json)
        print('SCORE', score)
        return score, 200
