import pytest
from CompareExcel import *  # Replace 'compare' with the actual module name

def test_compare_excel_files():
    file1 = r"F:\Class\Ninzarin Project Plan v1.0 draft.xlsx"
    file2 = r"F:\Class\Ninzarin Project Plan v1.0 draft.xlsx"

    match, result = compare_excel_files(file1, file2)
    if not match:
        if isinstance(result, str):
            print(f"Error: {result}")
        else:
            print("Differences found:")
            for diff in result:
                print(f"Row {diff['row']} Col {diff['col']}: {diff['df1_value']} != {diff['df2_value']}")
        assert False, f"Excel files do not match. Differences: {result}"

if __name__ == "__main__":
    pytest.main()
