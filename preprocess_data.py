import pandas as pd
import numpy as np
#loading dataset
data = pd.read_csv("clean_data.csv")

data['ProdID'] = data['ProdID'].replace('-2147483648', np.nan)
data["User's ID"] = data["User's ID"].replace('-2147483648', np.nan)

#remove rows where user id is Nan
data = data.dropna(subset=["User's ID"])

#removes duplicates
data = data.drop_duplicates()
#Drop unwanted columns (like 'Unnamed: 0') if they exist
if 'Unnamed: 0' in data.columns:
        data.drop(columns=['Unnamed: 0'], inplace=True)

#integer conversion
data["User's ID"] = data["User's ID"].astype('int64')

#innteger conversion for ProdID
data = data.dropna(subset=['ProdID'])
data['ProdID'] = data['ProdID'].astype('int64')

#integer conversion for Rating
data['Review Count'] = data['Review Count'].astype('int64')

#filling with empty strings
data['Category'] = data['Category'].fillna('')
data['Brand'] = data['Brand'].fillna('')
data['Description'] = data['Description'].fillna('')
data['Tags'] = data['Tags'].fillna('')

# Remove 0 values
data = data[(data["User's ID"] != 0) & (data["ProdID"] != 0)]

# Clean ImageURL
if "ImageURL" in data.columns:
    data["ImageURL"] = data["ImageURL"].str.replace("|", "", regex=False)

# Reset the index and return the cleaned dataframe
    data.reset_index(drop=True, inplace=True)
# User item matrix
    user_item_matrix = df.pivot_table(index="User's ID", 
                                     columns="ProdID", 
                                     values="Review Count", 
                                     fill_value=0)
    
    return user_item_matrix
return cleaned_data
