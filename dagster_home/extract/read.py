from msilib import schema
from operator import index
import pandas as pd
from loads.loads import load_data



def get_data():
  try:
    read_excel = '../Matriz_de_adyacencia_data_team.xlsx'
    xl = pd.ExcelFile(read_excel)
    sheets = xl.sheet_names
    for item in sheets:
      dataframe = pd.read_excel(read_excel, sheet_name= item)
      number_columns = len(dataframe.columns)
      if number_columns > 5:
        data_range = [item for item in range(number_columns)]
        data_columns = dataframe.iloc[:,data_range[2:]]
        data_drop_nan = data_columns.dropna()
        data_all = data_drop_nan.drop(index=0)
        print(type(data_all))
        name_table = "stg_habi_data"
        load_and_create_table_data = load_data(data_all, name_table)
      else:
        data_range = [item for item in range(number_columns)]
        data_columns = dataframe.iloc[:,data_range]
        data_columns.columns =['id', 'ids', 'name']
        data_ = data_columns.dropna()
        name_table = "stg_habi_user"
        load_and_create_table_user = load_data(data_, name_table)
  except Exception as e:
    print("No puede extrar datos {}".format(e))
      
      
    

    


