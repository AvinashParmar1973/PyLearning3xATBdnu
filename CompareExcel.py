import pandas as pd


def compare_excel_files(file1, file2):
    try:
        df1 = pd.read_excel(file1, dtype=str)
        df2 = pd.read_excel(file2, dtype=str)
    except Exception as e:
        return False, f"Error reading files: {e}"

    if df1.shape != df2.shape:
        return False, f"Shape mismatch: {df1.shape} vs {df2.shape}"

    differences = []
    for row in range(df1.shape[0]):
        for col in range(df1.shape[1]):
            value1 = df1.iat[row, col]
            value2 = df2.iat[row, col]
            if value1 != value2:
                differences.append({
                    'row': row + 1,  # Excel rows are 1-indexed
                    'col': col + 1,  # Excel columns are 1-indexed
                    'df1_value': value1,
                    'df2_value': value2
                })

    if differences:
        return False, differences
    else:
        return True, "Excel files match exactly."
