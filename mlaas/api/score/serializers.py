from flask_restplus import fields
from api.restplus import api


model_score = api.model('Model Score', {
    'algorithm': fields.String(required=True, description='Model name'),
    'source_url': fields.String(required=True, description='Source URL'),
    'field_names': fields.String(required=True, description='Field Names'),
})
