import pandas as pd
from abc import ABC, abstractmethod

class SchemaStringBuilderBase(ABC):

    def __init__(self):
        super().__init__()        

    @abstractmethod
    def build_schema_string(self, dtypes: pd.Series) -> str:
        pass

    @classmethod
    def get_generator_type(cls):
        return cls.__name__