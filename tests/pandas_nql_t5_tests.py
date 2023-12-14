import unittest
import pandas as pd
from pandas_nql import PandasNQL, \
                        T5SqlGenerator, \
                        SqlSchemaStringBuilder

class PandasNQLT5SqlGeneratorTestCase(unittest.TestCase):

    def setUp(self):

        # Create test data for use in tests
        data = {
            'Name': ['John', 'Jane', 'Bob', 'Jason', 'Mike'],
            'Age': [25, 30, 22, 47, 46],
            'City': ['New York', 'San Francisco', 'Seattle', 'Denver', 'Denver']
        }

        df = pd.DataFrame(data)

        self.test_data_df = df
        self.sql_generator = T5SqlGenerator()
        self.schema_builder = SqlSchemaStringBuilder()

    def test_send_none_to_constructor(self):
        """Send None to constructor. """
        self.assertRaises(ValueError, PandasNQL, None)

    def test_send_empty_df_to_constructor(self):
        """Send no data to constructor. """
        df = pd.DataFrame()
        self.assertRaises(ValueError, PandasNQL, df)

    #def test_with_invalid_query(self):
    #    """Use an invalid query on the test dataframe."""
    #
    #    pandas_nql = PandasNQL(self.test_data_df, 
    #                           generator=self.sql_generator, 
    #                           schema_builder=self.schema_builder)
    #
    #    result = pandas_nql.query("this is an invalid query and should be ignored.")
    #    print(result)
    #    self.assertTrue(result[0].empty)

    def test_with_valid_query_1(self):
        """Use a valid query on the test dataframe."""

        # arrange
        expected_row_count = 2
        pandas_nql = PandasNQL(self.test_data_df, 
                               generator=self.sql_generator, 
                               schema_builder=self.schema_builder)

        # act
        result = pandas_nql.query("Select name for people in the city of Denver.")
        
        # assert
        actual_row_count = result[0].count()

        self.assertFalse(result[0].empty)
        self.assertTrue(result[0].any)
        self.assertTrue(actual_row_count.eq(expected_row_count).any())

    def test_with_valid_query_2(self):
        """Use a valid query on the test dataframe."""

        # arrange
        expected_row_count = 1
        expected_age = 47
        pandas_nql = PandasNQL(self.test_data_df, 
                               generator=self.sql_generator, 
                               schema_builder=self.schema_builder)

        # act
        result = pandas_nql.query("Select the name and age of the oldest person.")
        
        # assert
        actual_row_count = result[0].count()
        actual_age = result[0]["Age"]

        self.assertFalse(result[0].empty)
        self.assertTrue(result[0].any)
        self.assertTrue(actual_row_count.eq(expected_row_count).any())
        self.assertTrue(actual_age.eq(expected_age).any())

    def test_with_valid_query_3(self):
        """Use a valid query on the test dataframe."""

        # arrange
        expected_row_count = 4
        expected_people_count = 2
        pandas_nql = PandasNQL(self.test_data_df, 
                               generator=self.sql_generator, 
                               schema_builder=self.schema_builder)

        # act
        result = pandas_nql.query("Find the number of people in each City.")
        
        # assert
        actual_row_count = result[0].count()
        actual_people_count = result[0].iloc[:, 1]

        self.assertFalse(result[0].empty)
        self.assertTrue(result[0].any)
        self.assertTrue(actual_row_count.eq(expected_row_count).any())
        self.assertTrue(actual_people_count.eq(expected_people_count).any())

if __name__ == '__main__':
    unittest.main()