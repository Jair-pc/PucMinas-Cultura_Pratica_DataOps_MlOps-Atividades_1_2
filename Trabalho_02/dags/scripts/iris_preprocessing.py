from pandas_schema import Column, Schema
from pandas_schema.validation import InRangeValidation, InListValidation


class IrisPreprocessing:
    def __init__(self, dados):
        self.dados = dados
        self.schema = self._create_schema()
        self.errors = self._validate_schema()


    def _create_schema(self):
        return Schema([
            Column('sepal_length', [InRangeValidation(4.3, 7.901)]),
            Column('sepal_width', [InRangeValidation(2.0, 4.401)]),
            Column('petal_length', [InRangeValidation(1.0, 6.901)]),
            Column('petal_width', [InRangeValidation(0.1, 2.501)]),
            Column('classEncoder', [InRangeValidation(0, 2.01)]),
            Column('class', [InListValidation(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])])
        ])


    def _validate_schema(self):
        return self.schema.validate(self.dados)


    def _get_errors(self):
        return self.errors

