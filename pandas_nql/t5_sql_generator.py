import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
from pandas_nql import SqlGeneratorBase

TEMP_VIEW_NAME = "data_view"
DEFAULT_T5_TOKENIZER_MODEL = "t5-small"
DEFAULT_T5_GENERATION_MODEL = "cssupport/t5-small-awesome-text-to-sql"

class T5SqlGenerator(SqlGeneratorBase):
    
    def __init__(self, 
                 t5_tokenizer_model: str = DEFAULT_T5_TOKENIZER_MODEL, 
                 t5_generation_model: str = DEFAULT_T5_GENERATION_MODEL):
        
        super().__init__()

        # Initialize the tokenizer from Hugging Face Transformers library
        self.tokenizer = T5Tokenizer.from_pretrained(t5_tokenizer_model)

        # Load the model
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = T5ForConditionalGeneration.from_pretrained(t5_generation_model)
        self.model = self.model.to(self.device)
        self.model.eval()

    def generate_sql(self, query: str, schema: str, dataset_name: str = TEMP_VIEW_NAME) -> str:
        """
        Generate a sql statement using a natural language query and the schema of the data.

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

        def clean_sql(sql):
            return sql.replace("\"", "'")

        prompt = f"tables:\nCREATE TABLE {dataset_name}({schema})\nquery for: {query}"

        # Tokenize the input prompt
        inputs = self.tokenizer(prompt, padding=True, truncation=False, return_tensors="pt").to(self.device)
        
        # Forward pass
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_length=512)
        
        # Decode the output IDs to a string (SQL query in this case)
        generated_sql = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        cleaned_generated_sql = clean_sql(generated_sql)
    
        return cleaned_generated_sql