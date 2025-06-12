import pandas as pd
import pytest
from src.exercise import third

@pytest.fixture
def dummy_dataframe():
    data = {
        'dia': ['01/08/2000', '01/08/2001', '01/08/2002', '01/08/2003'],
        'estacio': ['Embassament de name1 (name1)', 'Embassament de name2 (name2)', 'Embassament de name1 (name1)', 'Embassament de name3 (name3)'],
        'nivell_msnm': [899, 700, 650, 630],
        'nivell_perc': [59.2, 60, 63, 59.8]
    }
    return pd.DataFrame(data)

def test_run(dummy_dataframe):

    df_test = dummy_dataframe
    df_return = third.run(df_test)

    type_data_dia = df_return['dia'].dtype

    assert not df_return.empty
    assert type_data_dia == "datetime64[ns]", f"Expected type datetime64[ns], but got {type_data_dia}"
    assert "dia_decimal" in df_return.columns