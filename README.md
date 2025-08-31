# Inventory Optimization

This project focuses on **optimizing grocery inventory management**.  
Currently, it is applied to a **specific product: chocolaty coffee sachet boxes (4×4×4, each having 100 sachets)**.  
However, the same approach can be **extended to other products** in the inventory by using their stock, expiry, and sales data.  

The goal is to **maximize profit, minimize wastage**, and provide insights for better decision-making.  

---

## 🔍 Project Overview
- **Problem**: Grocery products have expiry dates. If stock is not allocated smartly, businesses lose money due to expired items or inefficient distribution.  
- **Solution**: This project analyzes inventory data, calculates expiry timelines, and recommends **what to do with each batch of stock**:
  - Dispose expired items  
  - Gift soon-to-expire stock to employees  
  - Use for marketing campaigns  
  - Send to franchise (high-margin)  
  - Sell at discount to retailers  
  - Sell normally to retailers  

The logic is **generic**, so even though this project demonstrates it for **coffee sachet boxes**, it can be used for **any other product in the dataset**.  

---

## ✨ Features
- **Data Cleaning**: Extracts useful columns (`Product_ID`, `Supplier_ID`, `Stock_Quantity`, `Date_Received`, `Expiration_Date`).  
- **Stock Scaling**: Adjusts stock quantity (here assumed: each product box = 100 sachets).  
- **Expiry Calculation**: Finds number of days left before expiry.  
- **Categorization Rules**:
  - **Expired → Dispose**  
  - **0–10 days → Gift to employees**  
  - **10–20 days → Marketing campaign**  
  - **20–45 days → Franchise**  
  - **45–60 days → Retailers (discounted)**  
  - **>60 days → Retailers**  
- **Worth Estimation**: Calculates financial worth of stock across categories.  
- **Monthly Insights**: Tracks stock received per month and its average shelf life.  
- **Profit Estimation**: Estimates annual profit potential across all categories.  

---
