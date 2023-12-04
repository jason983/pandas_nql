from pandas_nql import SqlGeneratorBase
from pandas_nql import OpenAIApiClient

TEMP_VIEW_NAME = "data_view"
BASE_PROMPT = "Generate a duckdb library compatable SQL statement to query the data based on the schema and natural language query provided by the user. \
                 If the natural language query does not relate to the data return a query that will return zero results."

class OpenAISqlGenerator(SqlGeneratorBase):
    
    def __init__(self):
        super().__init__()
        self.openai_api_client = OpenAIApiClient()

    def generate_sql(self, query: str, schema: str, dataset_name: str = TEMP_VIEW_NAME) -> str:
        """
        Generate a sql statement using a natural language query and the shape of the data.

        :param query: The natural language query
        :type gpt_model: str

        :param schema: The schema of the Pandas Dataframe
        :type schema: str

        :param dataset_name: The name of the dataset
        :type dataset_name: str
        :default dataset_name: data_view

        :return: Generated sql statement
        :rtype: str
        """
        prompt = "name of the dataset: " + dataset_name + ", data schema: " + schema + ", natural language query: " + query

        messages = [{"role": "system", "content": BASE_PROMPT},
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": f"Query:"}]
        
        response = self.openai_api_client.chat_completion(messages)

        return response