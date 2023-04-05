
import pandas as pd
import numpy as np
import os
path = os.path.dirname(__file__)


class Correlation():
    def __init__(self) -> None:
        self.df = pd.read_csv(os.path.join(path, "..", 'data/processing/cleaner_output.csv'), index_col=0)
        
    def get_log_correlation(self, min_correlation: float = 0.7) -> pd.DataFrame:
        
        self.df = pd.DataFrame(self.__get_highest_df(self.__get_unstacked_df(self.__get_corr_df(self.__get_log_df(self.df))), min_correlation)).reset_index()
        self.df.columns = ['Currency1', 'Currency2', 'Correlation']
        self.df.to_csv('./data/processing/corr_output.csv', index=False)
        return self.df
    
    def __get_log_df(self, df:pd.DataFrame) -> pd.DataFrame:
        return np.log(df.pct_change() + 1)

    def __get_corr_df(self, df:pd.DataFrame) -> pd.DataFrame:
        return df.corr()
    
    def __get_unstacked_df(self, df:pd.DataFrame) -> pd.DataFrame:
        return df.unstack().drop_duplicates()

    def __get_highest_df(self, df:pd.DataFrame, min_correlation:float) -> pd.DataFrame:
        return df[(df < 1) & (df >= min_correlation)]