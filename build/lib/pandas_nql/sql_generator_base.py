from abc import ABC, abstractmethod

TEMP_VIEW_NAME = "data_view"

class SqlGeneratorBase(ABC):

    def __init__(self):
        super().__init__()        

    @abstractmethod
    def generate_sql(self, query: str, schema: str, dataset_name: str = TEMP_VIEW_NAME) -> str:
        pass

    @classmethod
    def get_generator_type(cls):
        return cls.__name__