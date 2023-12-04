# Pandas Natural Language Query (NQL) Library
Pandas_nql is an open source Python library that enables natural language queries on Pandas Dataframes using the latest advances in generative AI. Inspired by OpenAI's groundbreaking language models, pandas_nql allows users to analyze data in a more intuitive way - by simply asking questions in plain English instead of writing complex code.

This library is perfect for data scientists, analysts, and developers looking to enhance their data analysis workflows. By leveraging the power of GPT and other language models behind the scenes, pandas_nql can understand complex data questions and automatically translate them into sql statements to extract insights from data.

Whether you're a Python expert looking to save time or someone new to data analysis, pandas_nql makes exploring datasets more accessible. It's as simple as pip installing the library and typing a query like "show me average monthly sales by region." You'll feel like you have a personal AI-powered data analyst at your fingertips!

Some key features:

- Query Dataframes in plain English without writing code
- Understands complex questions and data relationships
- Automatically translates questions to SQL statements
- Open source library for community involvement

Bring natural language queries to your data analysis today with the power of pandas_nql!

### Disclaimers
- PyPi is not accepting new registraions at this time so I can't upload the package for easy installation. Going to add to the test site for now.
- So you aware, your data is never sent to the language model for query creation, however, the schema of the data is sent and used. 
- Typical AI warning - AI can make mistakes. Consider checking important information.

### Installation
```
pip install pandas_nql
```

### Prerequisites
- OPENAI_API_KEY Environment variable must be set with a valid OpenAI Api Key
- Python3.9+

### Get started
How to select data from a Pandas dataframe using natural language:

```Python
import pandas as pd
from pands_nql import PandasNQL

# load Dataframe
data = {
    'Name': ['John', 'Jane', 'Bob', 'Jason', 'Mike'],
    'Age': [25, 30, 22, 47, 46],
    'City': ['New York', 'San Francisco', 'Seattle', 'Denver', 'Denver']
}

df = pd.DataFrame(data)

# Instantiate PandasNQL object passing in data to query
pandas_nql = PandasNQL(df)

# Call the query method to select data
results_df = pandas_nql.query("Show me the average age of people in Denver.")

print(results_df)

# ...

```

### Generators
Allows for custom sql statement generators. The default uses OpenAI.

#### Write custom generator

```Python
from generators import SqlStatementGeneratorBase

# define custom sql stement generator class
class CustomSqlGenerator(SqlGeneratorBase):
    
    def __init__(self, ...):
        super().__init__()        

    # override generate_sql method
    def generate_sql(self, query: str, schema: str, dataset_name: str = TEMP_VIEW_NAME) -> str:
        # generate sql statement
        # return sql statement
```

#### Use custom generator

```Python
import pandas as pd
from pands_nql import PandasNQL

# load Dataframe
df = ...

# instatiate custom generator
custom_generator = CustomSqlGenerator(...)

# Instantiate PandasNQL with data
pandas_nql = PandasNQL(df, generator=custom_generator)

# Call the query method to select data
results_df = pandas_nql.query("Show me the average age of people in Denver.")

print(results_df)
```