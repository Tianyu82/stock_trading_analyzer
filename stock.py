# import pandas lib as pd
import pandas as pd
 
# read by default 1st sheet of an excel file
def readData():
    dataframe1 = pd.read_excel('123.xlsx')
    print(dataframe1)
    return dataframe1
    
# find out all stocks that are not closed (with >0 quantity)
def findOpenStock(origin_df):
    open_stock = origin_df.groupby('Symbol')['Quantity'].sum().reset_index()
    print(open_stock)
    return open_stock

def groupData(origin_df):
    net_gain_per_stock = df.groupby('Symbol')['Net Amount'].sum().reset_index()
    # print(net_gain_per_stock)

if __name__ == "__main__":
    origin_df=readData()
    findOpenStock(origin_df)
    # groupData(df1)