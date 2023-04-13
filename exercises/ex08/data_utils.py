
import csv

def read_csv_rows(data_file_path: str) -> list[dict[str, str]]:
    """Reads a CSV file from the provided path and returns a list of dictionaries, where each dictionary represents a row from the CSV file."""
    rows = []
    with open(data_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)
    return rows

def column_values(rows: list[dict[str, str]], column: str) -> list[str]:
    """Given a list of rows representing a table and the name of a column, returns a list of the values in that column."""
    values = []
    for row in rows:
        if column in row:
            values.append(row[column])
    return values

def columnar(data_rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Given a list of rows representing a table, returns a dictionary of columns where each key is the name of a column and each value is a list of values in that column."""
    columns = {}
    for row in data_rows:
        for key, value in row.items():
            if key not in columns:
                columns[key] = []
            columns[key].append(value)
    return columns

def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Given a column-based table of data and an integer n, returns a new table that includes the first n rows of the input table"""
    if n >= len(table):
        return table
    else:
        return {key: table[key][:n] for key in table}
    
def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Given a column-based table of data and a list of column names, returns a new table that includes only the specified columns"""
    return {key: table[key] for key in columns}

def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Two tables, returns a new table with both tables combined."""
    result = {}
    # Loop through each column in the first table
    for column in table1.keys():
        result[column] = table1[column].copy()
    # Loop through each column in the second table
    for column in table2.keys():
        if column in result:
            result[column].extend(table2[column])
        else:
            result[column] = table2[column].copy()
    return result

def count(lst: list[str]) -> dict[str, int]:
    """Given a list of values, returns a dictionary with the count of each value."""
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts