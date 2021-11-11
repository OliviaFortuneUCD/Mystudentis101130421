import pandas as pd
# loading in the dataset
# skip first 11 rows of the file because there is unwanted information
units_sold = pd.read_csv('Car Units sold by month 2018-2021.csv')
df_adspend = pd.read_csv('Car Adspend 2018-2021.csv', skiprows=11)

# removing the first and last few rows between data because it does not contain relevant information
# saving it to a new object so it does not overwrite the original dataframe

df_adspend_del = df_adspend.drop([0, 22, 23, 24, 25, 26, 27, 28, 29])

# renaming the first column from "Unnamed: 0 to Brands so it makes sense

df_adspend_del = df_adspend_del.rename(columns = {'Unnamed: 0':'Brands'})
# in order to calculate the share of voice we need the total of the entire month
# we need to remove the categorical variable so we take columns 1 to 40
# then the money spent by each brand is divided by this total money spent by using the sum() function
# then multiply by 100 hundred to get the percentage

df_adspend_sov = (df_adspend_del[df_adspend_del.columns[1:40]]/ df_adspend_del[df_adspend_del.columns[1:40]].sum())*100


list_brands = []
for i in df_adspend_del["Brands"]:
    brand_name = i.split()[0].upper()
    list_brands.append(brand_name)


# double checking if everything is there and lengths match

if __name__ == "__main__":
    print(list_brands)
    len(list_brands)
# length of the list which corresponds to the number of rows in the dataframe
    print()