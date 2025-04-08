import pytest
from unittest.mock import patch, mock_open
import pandas as pd
from io import StringIO
from src.file_reader import read_csv_file, read_excel_file


@pytest.fixture
def mock_csv_data() -> str:
    return """date,amount,description
2023-01-01,100,Payment
2023-01-02,200,Transfer"""


@pytest.fixture
def mock_csv_df(mock_csv_data: str) -> pd.DataFrame:
    return pd.read_csv(StringIO(mock_csv_data))


def test_read_csv_file_success(mock_csv_df: pd.DataFrame):
    """Test CSV file reading with mock data."""
    # Mock file existence check
    with patch('pathlib.Path.exists', return_value=True):
        # Mock pandas.read_csv to return our test DataFrame
        with patch('pandas.read_csv', return_value=mock_csv_df):
            result = read_csv_file('test.csv')

            # Verify the results
            assert len(result) == 2
            assert result[0] == {
                'date': '2023-01-01',
                'amount': 100,
                'description': 'Payment'
            }
            assert result[1] == {
                'date': '2023-01-02',
                'amount': 200,
                'description': 'Transfer'
            }


def test_read_csv_file_not_found():
    """Test handling of missing CSV file."""
    with patch('pathlib.Path.exists', return_value=False):
        with pytest.raises(FileNotFoundError):
            read_csv_file('nonexistent.csv')


def test_read_csv_file_invalid_data():
    """Test handling of invalid CSV data."""
    with patch('pathlib.Path.exists', return_value=True):
        with patch('pandas.read_csv', side_effect=pd.errors.EmptyDataError):
            with pytest.raises(ValueError, match="Error reading CSV file"):
                read_csv_file('invalid.csv')
