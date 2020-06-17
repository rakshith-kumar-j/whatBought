import pandas as pd 
import matplotlib.pyplot as plt 
from getProductList import getProductList
import numpy as np

def extract(x):
    x=x.replace("."," ")
    x=x.replace("+"," ")
    driver=getProductList()
    x=driver.preprocess(x)
    return x

df=pd.read_csv("customerRequest.csv",engine='python')
df["Products"]=df["Products"].apply(lambda x:extract(x))
df['Products'].replace('', np.nan, inplace=True)
df=df.dropna(how='any')
plt.title("Products Viewed by Customers")
plt.xlabel("Products")
plt.ylabel("Number of Customers")
plt.hist(df['Products'].values)
plt.show()