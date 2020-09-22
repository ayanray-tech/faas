from ml_factory.object_factory import ObjectFactory
from ml_factory.logistic_regression import LogisticRegressionServiceBuilder
from ml_factory.decisiontreeclassifier import DecisionTreeClassifierServiceBuilder
from ml_factory.lda import LDAServiceBuilder
from ml_factory.knn import KNNServiceBuilder
from ml_factory.gaussianb import GaussianNBServiceBuilder
from ml_factory.svc import SVCServiceBuilder


class ModelServiceProvider(ObjectFactory):
    def get(self, service_id, **kwargs):
        return self.create(service_id, **kwargs)


services = ModelServiceProvider()
services.register_builder('LR', LogisticRegressionServiceBuilder())
services.register_builder('CART', DecisionTreeClassifierServiceBuilder())
services.register_builder('LDA', LDAServiceBuilder())
services.register_builder('KNN', KNNServiceBuilder())
services.register_builder('NB', GaussianNBServiceBuilder())
services.register_builder('SVM', SVCServiceBuilder())
