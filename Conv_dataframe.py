from typing import List
import pandas as pd
def get_dataframe_column(list_col: List[str], df: pd.DataFrame):
    """
    Return a dataframe subset with specific columns.
    Input: 
         list_col: list type [] with name of columns to be extract and returned as a new dataframe.
                   Example: list_col = ['L1', 'L2','L5'] returns only phase observables.  
         df: dataframe that contains the rinex observation data
    Output:
         new_df: dataframe with subset of columns from input dataframe (df)

    Author: Claudinei Rodrigues de Aguiar
    """
    list_col = [col for col in list_col if col in df.columns]
    
    if all(elem in df.columns  for elem in list_col):
        return df[list_col], list_col
    else:
        list_col = [col for col in list_col if col in df.columns]
        print('Some subset columns from list ',list_col,' is not in dataframe columns: ',df.columns)
        return df[list_col], list_col

