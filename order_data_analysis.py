!pip install kaggle

import kaggle
!kaggle datasets download ankitbansal06/retail-orders -f orders.csv

import zipfile
zip_ref = zipfile.ZipFile('orders.csv.zip')
zip_ref.extractall()
zip_ref.close()

#read data from the file and handle null values
import pandas as pd
orders_data = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
orders_data['Ship Mode'].unique()

orders_data.isnull()

#orders_data.rename(columns={'Order Id':'order_id','City':'city',}) #this is not a good practics
#orders_data.head(3)

orders_data.columns=orders_data.columns.str.lower().str.replace(' ','_')
orders_data.head()

orders_data.dtypes

orders_data['order_date']= pd.to_datetime(orders_data['order_date'])

orders_data.shape

#derive new columns: discount, sale price and profit
orders_data['discount']=orders_data['list_price']*orders_data['discount_percent']/100
orders_data

orders_data['sale_price']= orders_data['list_price']-orders_data['discount']

orders_data['profit']=orders_data['sale_price']-orders_data['cost_price']
orders_data

#convert order date from object data type to datetime
orders_data['order_date']=pd.to_datetime(orders_data['order_date'],format="%Y-%m-%d")

#drop cost, price, list price, and discount percent columns
orders_data.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)
