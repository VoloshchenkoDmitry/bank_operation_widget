from pathlib import Path
from typing import Any, Dict, List

import pandas as pd


def read_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """Read CSV file and return list of transactions."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        df = pd.read_csv(path)
        return df.to_dict("records")
    except Exception as e:
        raise ValueError(f"Error reading CSV file: {str(e)}")


def read_excel_file(file_path: str) -> List[Dict[str, Any]]:
    """Read Excel file and return list of transactions."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        df = pd.read_excel(path, engine="openpyxl")
        return df.to_dict("records")
    except Exception as e:
        raise ValueError(f"Error reading Excel file: {str(e)}")
