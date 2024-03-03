import pandas as pd
import os

class DataOpr():
    def _operations_logic(self, df1, df2):
        """
        This functions performs salary related calculation and return final DF
        """
        try:
            master_df = pd.concat([df1, df2])

            ##calculating salary
            master_df['gross_salary'] = master_df['basic_salary'] + master_df['allowances']
            average_salary = master_df['gross_salary'].mean()
            master_df = master_df.sort_values(by= 'gross_salary', ascending= False)
            second_high_sal = master_df['gross_salary'].iloc[1]

            master_df = master_df.drop_duplicates()

            ##adding footer
            footer = pd.DataFrame(
                {
                    'id': [f"Second Highest salary = {second_high_sal}"],
                    "first_name": [f"average_salary = {average_salary}"]
                }
            )
            master_df = pd.concat([master_df, footer])

            return master_df
        except Exception as e:
            print(f"!!! Calculation logic exception: {e}")


    def _write_file(self, master_df):
        """
        This function write files into desired location
        """
        try:
            path = os.path.expanduser("~/Documents/result.csv")
            master_df.to_csv(path, index= False)
            return True
        except Exception as e:
            print(f"!!! File write Exception: {e}")
            return False

    def _read_data(self):
        """
        This function reads the .dat file from specific location and return
        """
        try:
            df1 = pd.read_csv(os.path.expanduser("DATA (3).dat"), delimiter= "\t")
            df2 = pd.read_csv(os.path.expanduser("DATA1 (3).dat"), delimiter= "\t")

            return df1, df2
        except Exception as e:
            print(f"!!! File read exception: {e}")

    def operation_handler(self):
        """
        This function is main handler which calls other services
        """
        df1, df2 = self._read_data()
        master_df = self._operations_logic(df1, df2)
        res = self._write_file(master_df)

        if res:
            print("Operation has been successfully finished")
        else:
            print("Error while performing operations")



### calling main handler
obj = DataOpr()
obj.operation_handler()

