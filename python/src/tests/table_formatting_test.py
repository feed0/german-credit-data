from utils.data_utils import map_column_inplace
import pandas as pd

class TableFormattingTest:
    '''Ensures column statistics are unchanged after processing'''
    
    def test_column_statistics(self, original: pd.DataFrame, processed: pd.DataFrame):
        # 1. Prepare
        original = original.copy()
        processed = processed.copy()
        
        ## 1.1 Flatten MultiIndex columns for comparison
        original.columns = processed.columns

        # 2. Reverse the boolean columns mapping in processed
        inverse_boolean_map = {
            'A19 - Telephone'        : {True: 'A192', False: 'A191'},
            'A20 - Foreign worker'   : {True: 'A201', False: 'A202'},
            'T1 - Is good credit'    : {True: 1, False: 2}
        }

        boolean_columns = list(inverse_boolean_map.keys())
        
        for column in boolean_columns:
            map_column_inplace(
                df = processed,
                column = column,
                value_map = inverse_boolean_map[column]
            )
            
        # Reverse int64 to catgegory mapping
        processed['A8 - Installment rate in percentage of disposable income'] = processed['A8 - Installment rate in percentage of disposable income'].astype('int64')

        # 3. Compare statistics for each column ---------------------------------------------------------------------------------------------------------
        for col in original.columns:

                orig_stats = original[col].describe(include='all')
                proc_stats = processed[col].describe(include='all')
                
                for stat in orig_stats.index:
                    assert orig_stats[stat] == proc_stats[stat], f"Statistic '{stat}' for column '{col}' changed: {orig_stats[stat]} != {proc_stats[stat]}"

        print("All column statistics are unchanged after processing.")