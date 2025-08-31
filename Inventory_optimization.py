#Inventory optimization

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

#Accessing the dataset
dataset = pd.read_csv("/Users/harshsrivastava/Downloads/Grocery_Inventory_and_Sales_Dataset.csv")

# Taking out the required inforamtion for our assignment : Making a table from an inventory assuming every product is the chocolaty coffee sachet boxes 4*4*4(each having 100 Sachets) recieved from the factories.
inventory = dataset[["Product_ID", "Supplier_ID",  "Stock_Quantity", "Date_Received", "Expiration_Date"]].copy()
inventory["Stock_Quantity"] = inventory["Stock_Quantity"] * 100

# Finding the current value of the sachets with respect to the no. of days left before expiry and status(expired or not)
Sachets_selling_price = 10 # In INR
inventory["Stock_selling_cost"] = inventory["Stock_Quantity"] * Sachets_selling_price

#as the data set has old values so using todays date all the stock will be declared expired so picking a random date
"""todays_date = date.today()
formatted_date_mdy = todays_date.strftime("%m-%d-%Y")"""
inventory["Expiration_Date"] = pd.to_datetime(inventory["Expiration_Date"])
inventory["Date_Received"] = pd.to_datetime(inventory["Date_Received"])
todays_date = pd.to_datetime('2024-03-06')
inventory["N0._of_days_left_before_expiry"] = (inventory["Expiration_Date"] - todays_date).dt.days

# Categorizing the data and adding neccessary columns
for i in range(0,len(inventory["N0._of_days_left_before_expiry"])):
    if inventory.loc[i,"N0._of_days_left_before_expiry"] <= 0 :
        inventory.loc[i,"Status"] = "Expired"
        inventory.loc[i,"Stock_selling_cost"] = 0
        inventory.loc[i,"Send it to"] = "Disposed it of"
    else : 
        inventory.loc[i,"Status"] = "Not Expired"
        if 0 < inventory.loc[i,"N0._of_days_left_before_expiry"] <= 10 :
            inventory.loc[i,"Send it to"] = "Gifting it to employees"
        elif  10 < inventory.loc[i,"N0._of_days_left_before_expiry"] <= 20 :
            inventory.loc[i,"Send it to"] = "Marketing Campaign"
        elif  20 < inventory.loc[i,"N0._of_days_left_before_expiry"] <= 45 :
            inventory.loc[i,"Send it to"] = "Franchise"
        elif 45< inventory.loc[i,"N0._of_days_left_before_expiry"] <= 60 :
            inventory.loc[i,"Send it to"] = "Offering discount of INR 2 to retailers"
        elif 60< inventory.loc[i,"N0._of_days_left_before_expiry"] :
            inventory.loc[i,"Send it to"] = "Retailers"
        
print(inventory)

"""
We can predict the demand from the retailers as it is the subscriptions based model 
we know the quantities + for the franchise we can forcast the demand from the 
Sales_&_quantity_to_be_sold_forecasting

The division of stock are as follows : 
"""
cost = 5
selling_directly_to_customer = 10
retailer_selling_price = 7.5
for r in range(0,len(inventory["N0._of_days_left_before_expiry"])):
    if inventory.loc[r,"Send it to"] == "Gifting it to employees" :
        selling_price = -cost
        inventory.loc[r,'Worth_of_stock'] = inventory.loc[r,"Stock_Quantity"] * selling_price
    elif  inventory.loc[r,"Send it to"] == "Franchise" :
        selling_price = cost
        inventory.loc[r,'Worth_of_stock'] = inventory.loc[r,"Stock_Quantity"] * selling_price
    elif  inventory.loc[r,"Send it to"] == "Marketing Campaign" :
        selling_price = -5
        inventory.loc[r,'Worth_of_stock'] = inventory.loc[r,"Stock_Quantity"] * selling_price
    elif  inventory.loc[r,"Send it to"] == "Offering discount of INR 2 to retailers":
        selling_price = retailer_selling_price - 2
        inventory.loc[r,'Worth_of_stock'] = inventory.loc[r,"Stock_Quantity"] * selling_price
    elif  inventory.loc[r,"Send it to"] == "Retailers":
        selling_price = retailer_selling_price
        inventory.loc[r,'Worth_of_stock'] = inventory.loc[r,"Stock_Quantity"] * selling_price
    elif  inventory.loc[r,"Send it to"] == "Disposed it of" :
        selling_price = -cost
        inventory.loc[r,'Worth_of_stock'] = inventory.loc[r,"Stock_Quantity"] * selling_price



#Total monthly stocking and days before expiry insights
monthly_stocking = inventory.groupby(inventory['Date_Received'].dt.month)['Stock_Quantity'].sum().reset_index()
print(monthly_stocking.describe())
monthly_stocking_days_before_expiry = inventory.groupby(inventory['Date_Received'].dt.month)['N0._of_days_left_before_expiry'].median()
print(monthly_stocking_days_before_expiry.describe())

#Estimating maximum total potential of worth of the stocks of chocolaty cold coffee in inventory
grouping = inventory.groupby(inventory['Send it to'])[['Stock_Quantity', 'Worth_of_stock']].sum().reset_index()
print("Category_wise_sales")
print(grouping)
print(f"Annual profit :  {sum(grouping['Worth_of_stock'])}")

# For any dataset the categorizing rules will be same. Only things is that the decision makers have to focus on franchise to create more sales out of the stock in the inventory.
# In marketing campaign and gifting the sachet to the employee will boost mouth of word publicity which can increase the sales from franchise or retail. Money from retailer is fixed so the only area that is left and which can actually increase the revenue is via franchise.
# Franchise the goods will be goes to make chocolaty cold coffee(high profit margin) and direct selling to cuistmoer(without middleman)  


