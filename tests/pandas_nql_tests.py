import unittest
import pandas as pd
from pandas_nql import PandasNQL

class PandasNQLTestCase(unittest.TestCase):

    def setUp(self):

        # Create test data for use in tests
        data = {
            'Name': ['John', 'Jane', 'Bob', 'Jason', 'Mike'],
            'Age': [25, 30, 22, 47, 46],
            'City': ['New York', 'San Francisco', 'Seattle', 'Denver', 'Denver']
        }

        df = pd.DataFrame(data)

        self.test_data_df = df

    def test_send_none_to_constructor(self):
        """Send None to constructor. """
        self.assertRaises(ValueError, PandasNQL, None)

    def test_send_empty_df_to_constructor(self):
        """Send no data to constructor. """
        df = pd.DataFrame()
        self.assertRaises(ValueError, PandasNQL, df)

    def test_with_invalid_query(self):
        """Use an invalid query on the test dataframe."""

        pandas_nql = PandasNQL(self.test_data_df)

        result = pandas_nql.query("this is an invalid query and should be ignored.")
        
        self.assertTrue(result[0].empty)

    def test_with_valid_query(self):
        """Use a valid query on the test dataframe."""

        pandas_nql = PandasNQL(self.test_data_df)

        result = pandas_nql.query("show me all users from the city of Denver.")
        
        self.assertTrue(result[0].any)

if __name__ == '__main__':
    unittest.main()