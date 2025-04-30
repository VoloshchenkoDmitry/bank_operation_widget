from src.file_reader import read_csv_file, read_excel_file

try:
    csv_data = read_csv_file('transactions.csv')
    excel_data = read_excel_file('transactions_excel.xlsx')

    print("CSV Transactions:", csv_data)
    print("Excel Transactions:", excel_data)
except FileNotFoundError as e:
    print(f"Error: {e}")
