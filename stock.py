# import pandas lib as pd
import pandas as pd
 
# read by default 1st sheet of an excel file
def readData():
    dataframe1 = pd.read_excel('123.xlsx')
    return dataframe1
    # print(dataframe1)

def groupData(df):
    net_gain_per_stock = df.groupby('Symbol')['Net Amount'].sum().reset_index()
    print(net_gain_per_stock)

if __name__ == "__main__":
    df1=readData()
    groupData(df1)