
import pandas as pd
import numpy as np
import os
path = os.path.dirname(__file__)
pd.options.mode.chained_assignment = None

class Ratio():
    def __init__(self) -> None:
        self.df = pd.read_csv(os.path.join(path, "..", 'data/processing/cleaner_output.csv'), index_col=0)

    def get_ratio(self, coint_df: pd.DataFrame =
                  pd.read_csv(
                      './data/processing/coint_output.csv'),

                  useful_df: pd.DataFrame =
                  pd.read_csv(
                      './data/processing/cleaner_output.csv')
                  
                  ) -> pd.DataFrame:

        rationed_df = self.__apply_ratio_calc(useful_df.median(numeric_only=True), coint_df)
        rationed_df.to_csv('./data/analyzed/final_output.csv', index=False)
        return rationed_df

    def __apply_ratio_calc(self, median, coint_df) -> pd.DataFrame:
        coint_df['Ratio'] = np.vectorize(
            lambda currency1, currency2: 
                   median[currency1] / median[currency2])(
                   coint_df['Currency1'], coint_df['Currency2'])
                   
        return coint_df.sort_values('Correlation', ascending=False)

