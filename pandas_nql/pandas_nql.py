import pandas as pd
import duckdb
from pandas_nql import SqlGeneratorBase, \
                        OpenAISqlGenerator, \
                        SchemaStringBuilderBase, \
                        SqlSchemaStringBuilder

TEMP_VIEW_NAME = "data_view"
DEFAULT_MAX_RETRIES = 3

DEFAULT_GENERATOR = OpenAISqlGenerator()
DEFAULT_SCHEMA_BUILDER = SqlSchemaStringBuilder()

class PandasNQL:
    """
    Class used to query data using natural language queries
        
    :param df: The Pandas Dataframe containing the data to query
    :type df: Dataframe

    :param max_retries: The max number of tries to complete the query
    :type max_retries: int
    :default max_retries: 3

    :param generator: Used to generate sql statement
    :type generator: str
    :default generator: OpenAISqlGenerator
    """

    def __init__(self, 
                 df: pd.DataFrame, 
                 max_retries: int = DEFAULT_MAX_RETRIES, 
                 generator: SqlGeneratorBase = DEFAULT_GENERATOR,
                 schema_builder: SchemaStringBuilderBase = DEFAULT_SCHEMA_BUILDER):
        try:
            if (df.empty):
                raise ValueError("Pandas Dataframe is required.")
        except AttributeError:
            raise ValueError("Pandas Dataframe is required.")
        
        self.df = df
        self.max_retries = max_retries
        self.generator = generator
        self.schema_builder = schema_builder

    def query(self, query: str) -> (pd.DataFrame, str):
        """
        Select data from a Pandas's dataframe using natural language queries.

        :param query: The query in a natural language format.
        :type query: str

        :return: Query results in a Pandas Dataframe and the query that was generated.
        :rtype: (Dataframe, str)
        """    
        
        schema = self.schema_builder.build_schema_string(self.df.dtypes)

        # Connect to the DuckDB database
        con = duckdb.connect(database=':memory:')

        # Register the DataFrame as a temporary table without specifying a table name
        con.register(TEMP_VIEW_NAME, self.df)

        # Generate the sql statement based on the natural language query     
        sql_statement = self.generator.generate_sql(query=query, schema=schema)

        # Retry query execution up to max_retries
        for attempt in range(1, self.max_retries + 1):
            try:
                # Execute the query
                result = con.execute(sql_statement)

                # Fetch the result
                results_df = result.fetchdf()

                return results_df, sql_statement
            except Exception as e:
                if attempt == self.max_retries:
                    # If maximum retries reached, raise the error
                    raise ValueError(f"Query execution failed after {attempt} attempts. Reason: {str(e)}")

                # Append error details to the prompt and retry
                query += f"\n\n--- The last attempt to create the query failed. Please try again. ---\nQuery:{sql_statement}\nError: {str(e)}\n"

                sql_statement = self.generator.generate_sql(query=query, schema=schema)
