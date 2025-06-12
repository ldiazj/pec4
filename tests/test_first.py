import pandas as pd
from src.exercise import first

def test_run():

    df = first.run()

    assert not df.empty