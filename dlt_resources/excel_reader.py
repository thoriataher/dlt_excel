import pandas as pd
import dlt

@dlt.resource
def excel_rows(filepath: str):
    df = pd.read_excel(filepath)
    
    for _, row in df.iterrows():
        yield row.to_dict()