import pandas as pd
import pytest
from src.exercise import fifth

@pytest.fixture
def dummy_dataframe():
    data = {
        'dia': ['01/08/2000', '01/08/2001', '01/08/2002', '01/08/2003'],
        'dia_decimal' : [2000.10, 2001.15, 2002.20, 2003.20],
        'estacio': ['Embassament de name1 (name1)', 'Embassament de name2 (name2)', 'Embassament de name1 (name1)', 'Embassament de name3 (name3)'],
        'nivell_msnm': [899, 700, 650, 630],
        'nivell_perc': [59.2, 60, 63, 59.8],
        'nivell_perc_smooth' : [59.2, 59.8, 60.1, 62]
    }
    return pd.DataFrame(data)

def test_calculate_periods(dummy_dataframe):

    df_test = dummy_dataframe
    periods = fifth.calculate_periods(df_test)

    expected_periods = [[2000.10, 2002.20]]

    assert periods == expected_periods, f"Expected periods {expected_periods}, but got {periods}"