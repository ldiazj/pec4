import pandas as pd
import pytest
from src.exercise import second

@pytest.fixture
def dummy_dataframe():
    data = {
        'Dia': ['2000/08/01', '2001/08/01', '2002/08/01', '2003/08/01'],
        'Estació': ['Embassament de name1 (name1)', 'Embassament de name2 (name2)', 'Embassament de name1 (name1)', 'Embassament de name3 (name3)'],
        'Nivell absolut (msnm)': [899, 700, 650, 630]
    }
    return pd.DataFrame(data)

def test_rename_columns(dummy_dataframe):

    df_test = dummy_dataframe
    expected_columns = ['dia', 'estacio', 'nivell_msnm']
    df_return = second.rename_columns(df_test)

    assert not df_return.empty
    assert list(df_return.columns) == expected_columns, f"Expected columns {expected_columns}, but got {list(df_return.columns)}"

def test_get_unique_names(dummy_dataframe):

    df_test = dummy_dataframe
    expected_names = ['Embassament de name1 (name1)', 'Embassament de name2 (name2)', 'Embassament de name3 (name3)']
    array_names = second.get_unique_names(second.rename_columns(df_test))

    assert array_names == expected_names, f"Expected names {expected_names}, but got {array_names}"

def test_rename_names(dummy_dataframe):

    df_test = dummy_dataframe
    expected_names = ['name1', 'name2', 'name3']
    df_rename_name = second.rename_names(second.rename_columns(df_test))

    array_names = df_rename_name['estacio'].unique().tolist()

    assert array_names == expected_names, f"Expected names {expected_names}, but got {array_names}"

def test_run(dummy_dataframe):

    df_test = dummy_dataframe
    df_return = second.run(df_test)

    assert df_return.empty