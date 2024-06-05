import pandas as pd
import pytest
from functions.clean_names import clean_names

def test_clean_names():
    df = pd.DataFrame({'Column 1': [1, 2, 3], 'Column 2': [4, 5, 6]})

    cleaned_df = clean_names(df)

    assert cleaned_df.columns.tolist() == ['column_1', 'column_2']

if __name__ == "__main__":
    # Run the test using pytest
    pytest.main()