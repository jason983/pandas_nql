import pandas as pd
from pandas_nql import SchemaStringBuilderBase

class SqlSchemaStringBuilder(SchemaStringBuilderBase):
    def build_schema_string(self, dtypes: pd.Series) -> str:
        """
        Builds a string based off the schema of a Pandas DataFrame.

        :return: Formatted string representing the schema of the Pandas Dataframe. 
                    Format: "column_1 sql_type, column_2 sql_type, column_n sql_type..."
        :rtype: str
        """
        sql_types = {'int32': 'int',
                        'int64': 'bigint',
                        'float32': 'decimal(10,2)',
                        'float64': 'decimal(10,2)',
                        'object': 'varchar(255)',
                        'datetime64[ns]': 'timestamp',
                        'bool': 'bool'}
                 
        column_declarations = []
        for c, dtype in dtypes.items():
            sql_type = sql_types.get(str(dtype), 'varchar(255)') 
            column_declarations.append(f"{c} {sql_type}")
            
        sql_str = ', '.join(column_declarations)
        
        return sql_str