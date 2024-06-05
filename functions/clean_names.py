import pandas as pd
import re
from functions.helpers import normalize_string

def clean_names(df):
    df.columns = [normalize_string(col) for col in df.columns]
    return df