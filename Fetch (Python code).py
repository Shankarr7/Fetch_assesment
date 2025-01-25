#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load CSV files into DataFrames
transactions = pd.read_csv('D:/Fetch/downloads/TRANSACTION_TAKEHOME.csv')
users = pd.read_csv('D:/Fetch/downloads/USER_TAKEHOME.csv')
products = pd.read_csv('D:/Fetch/downloads/PRODUCTS_TAKEHOME.csv')

# Display the first few rows of each dataset
print("Transactions Dataset:\n", transactions.head())
print("\nUsers Dataset:\n", users.head())
print("\nProducts Dataset:\n", products.head())


# In[3]:


# Check for missing values in each dataset
print("Missing values in Transactions:\n", transactions.isnull().sum())
print("\nMissing values in Users:\n", users.isnull().sum())
print("\nMissing values in Products:\n", products.isnull().sum())


# In[6]:


# Check for duplicate rows in each dataset
print("Duplicate rows in Transactions:", transactions.duplicated().sum())
print("Duplicate rows in Users:", users.duplicated().sum())
print("Duplicate rows in Products:", products.duplicated().sum())


# In[19]:


# Convert FINAL_SALE to numeric
if 'FINAL_SALE' in transactions.columns:
    transactions['FINAL_SALE'] = pd.to_numeric(transactions['FINAL_SALE'], errors='coerce')

    # Check for negative transaction amounts
    negative_transactions = transactions[transactions['FINAL_SALE'] < 0]
    print("Negative Transaction Amounts:")
    print(negative_transactions)

    # Check if any values could not be converted (e.g., invalid data)
    invalid_final_sales = transactions[transactions['FINAL_SALE'].isnull()]
    print("\nRows with Invalid FINAL_SALE values:")
    print(invalid_final_sales)
else:
    print("Column 'FINAL_SALE' not found in Transactions data.")


# In[17]:


# Display column names to verify
print("Transactions Columns:", transactions.columns)


# In[20]:


# Validate and format PURCHASE_DATE and SCAN_DATE
date_columns = ['PURCHASE_DATE', 'SCAN_DATE']  # Replace/add any other date columns if needed

for col in date_columns:
    if col in transactions.columns:
        # Convert the column to datetime, coercing invalid values to NaT (Not a Time)
        transactions[col] = pd.to_datetime(transactions[col], errors='coerce')

        # Find rows with invalid or missing dates
        invalid_dates = transactions[transactions[col].isnull()]
        print(f"\nInvalid Dates in {col}:")
        print(invalid_dates)
    else:
        print(f"Column '{col}' not found in Transactions data.")


# In[21]:


# Step 5: Generate Summary of Findings

# Initialize summary dictionary
summary = {}

# 1. Data Quality Issues
summary["Data Quality Issues"] = {
    "Missing Values": {
        "Transactions": transactions.isnull().sum().to_dict(),
        "Users": users.isnull().sum().to_dict(),
        "Products": products.isnull().sum().to_dict()
    },
    "Duplicate Rows": {
        "Transactions": transactions.duplicated().sum(),
        "Users": users.duplicated().sum(),
        "Products": products.duplicated().sum()
    },
    "Negative or Invalid Values": {
        "Negative FINAL_SALE Rows": len(negative_transactions),
        "Invalid FINAL_SALE Rows": len(invalid_final_sales),
        "Invalid Dates in PURCHASE_DATE": len(transactions[transactions['PURCHASE_DATE'].isnull()]),
        "Invalid Dates in SCAN_DATE": len(transactions[transactions['SCAN_DATE'].isnull()])
    }
}

# 2. Challenging Fields
summary["Challenging Fields"] = [
    "Column 'USER_ID' needs clarification: Is it anonymized or meaningful?",
    "Ambiguity in 'STORE_NAME': Are these unique identifiers or descriptive labels?",
    "Ensure 'BARCODE' is consistent across datasets (e.g., length, format)."
]

# Print summary
for key, value in summary.items():
    print(f"\n{key}:\n")
    print(value)


# In[ ]:




