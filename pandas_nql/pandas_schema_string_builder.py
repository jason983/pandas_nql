import pandas as pd
from pandas_nql import SchemaStringBuilderBase

class PandasSchemaStringBuilder(SchemaStringBuilderBase):
    def build_schema_string(self, dtypes: pd.Series) -> str:
        """
        Builds a string based off the schema of a Pandas DataFrame.

        :return: Formatted string representing the schema of the Pandas Dataframe. 
                    Format: "column_1: data_type, column_2: pandas_data_type, column_n: data_type..."
        :rtype: str
        """
        schema_string = ""
        for column_name, data_type in dtypes.items():
            schema_string += f"{column_name}: {data_type}, "

        # Remove the trailing comma and whitespace
        schema_string = schema_string[:-2]

        return schema_string