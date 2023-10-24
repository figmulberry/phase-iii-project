# Creating the functions
"""
The function to remove the unnecessary columns for our model in the data.
"""
# ***************************************************************************************************
def unnecessaryCols(data, columns):           
    cleanDF = data.drop(columns, axis=1)
    return cleanDF

# ***************************************************************************************************
"""
The function checks for the cardniality.
"""
def assessHighCardinality(data):
    cat_cols = [i for i in data.columns if data[i].dtype in ['O']]
    hCardinality_cols = [col for col in cat_cols if len(data[col].value_counts().index) > 1000]
    return hCardinality_cols

# ***************************************************************************************************
"""
This function checks for placeholders in the dataframe
We shall only print a few records since there are so many if printed all
"""
def assessPlaceholders(data, num_records=2): # if you want to see all the records, you can assume the num_records part
    tables = []
    for column in data.columns:
        table = data[column].value_counts(normalize=True).reset_index().head(num_records)
        tables.append(tabulate(table, headers=['Value', 'Count'], tablefmt='simple_outline'))

    if len(tables) <= 5:
        print("\n".join("\t\t".join(t) for t in zip(*[table.splitlines() for table in tables])))
    else:
        mid = len(tables) // 2
        tables1 = tables[:mid]
        tables2 = tables[mid:]

        print("cont.")
        print("\n".join("\t\t".join(t) for t in zip(*[table.splitlines() for table in tables1])))
        
        print("\ncont.")
        print("\n".join("\t\t".join(t) for t in zip(*[table.splitlines() for table in tables2])))

# ***************************************************************************************************
"""
The function will be used to downscale the high cardinality for the columns (funder & installer)
"""
def downscaleCardinality(data):
    data[['funder']]= data[['funder']].where(data[['funder']].apply(lambda x: x.map(x.value_counts()))>= 1374, 'other')
    data[['installer']] = data[['installer']].where(data[['installer']].apply(lambda x: x.map(x.value_counts()))>=1060, 'other')
    return data

# ***************************************************************************************************
""" 
This function returns any column with missing values
"""
def valsMissing(data):
    return {column:data[column].isnull().sum() for column in data.columns if data[column].isnull().sum()}

# ***************************************************************************************************
from modules import * # This function utilizes the random module which is called from the modules.py file
"""
This function loops over columns with missing values and fills those missing values with random 
non-missing values from the same column.
"""
def fill_missing_with_random(data):
    # Looping over the columns with missing values
    # Fill missing values with a random choice from non-missing values
    col_missing = [column for column in data.columns if data[column].isnull().sum()]
    data[col_missing[0]] = data[col_missing[0]].fillna(random.choice(data[col_missing[0]][data[col_missing[0]].notna()]))
    data[col_missing[1]] = data[col_missing[1]].fillna(random.choice(data[col_missing[1]][data[col_missing[1]].notna()]))
    return data

# ***************************************************************************************************
def valReplacer(data):
    """ 
    Function to replace similar values in particular columns with a common phrase.
    """
    data['management'] = data['management'].replace({'unknown': 'other', 'other - school':'school'})

    data['payment_type'] = data['payment_type'].replace({'unknown': 'other', 'per bucket':'pay(annual/per_bucket/on_failure/monthly)', 
                                                         'monthly': 'pay(annual/per_bucket/on_failure/monthly)', 
                                                         'on failure':'pay(annual/per_bucket/on_failure/monthly)', 
                                                         'annually':'pay(annual/per_bucket/on_failure/monthly)'})

    data['waterpoint_type_group'] = data['waterpoint_type_group'].replace(['improved spring', 'cattle trough','dam'], 'other')
    data['water_quality'] = data['water_quality'].replace({'salty abandoned': 'salty', 'fluoride abandoned':'fluoride'})
    return data

# ***************************************************************************************************
"""
The age function takes in a parameter data(df).
Inside the loop, we attempt to parse the date string using the datetime.strptime() function. 
It expects the date to be in the format 'mm/dd/yyyy', and it extracts the year from the date.
If parsing the date is successful (no ValueError is raised), assign the extracted year to the variable 'year'. 
Otherwise, assign a default value of None (or any other appropriate default value) to handle the ValueError.
Then, we will convert the 'date_recorded' column into a pandas DateTime series, enabling us to perform datetime operations.
We will extract the year component from the df series.
To calculate the age of each record, we will subtract the 'construction_year' column from the 'year recorded' column 
and assign the result to a new column named 'age' in the df.
Finally, our function returns the modified df data with the added 'year recorded' and 'age' columns.
"""
from datetime import datetime

def age(data):
    year_recorded = []
    for date in data['date_recorded']:
        try:
            year = datetime.strptime(date, '%m/%d/%Y').year
        except ValueError:
            # Handle the ValueError by assigning a default value
            year = None  # You can use any other appropriate default value
        year_recorded.append(year)
    year_recorded = pd.DataFrame(year_recorded, columns=['year_recorded'], index=data.index)
    data['year recorded'] = year_recorded.astype('float64')
    return data

# ***************************************************************************************************

import matplotlib.ticker as mtick

def vizOutliers(data):
    cont_cols = data.select_dtypes(include=['float64', 'int64']).\
        columns.drop(['id', 'permit', 'region_code', 'district_code', 'public_meeting'], errors='ignore')

    fig, axes = plt.subplots(ncols=3, nrows=2, figsize=(22, 10))
    for col, ax in zip(cont_cols, axes.flatten()):
        col_label = col.replace('_', ' ').title()  # format x-axis column label to look nicer and readable
        sns.histplot(data[col], bins=10, kde=True, ax=ax)
        ax.set_xlabel(col_label)
        ax.set_ylabel("N0. of H20 pumps")
        ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, pos: '{:.0f}'.format(x/1000) + 'k'))

    plt.tight_layout()
    plt.show()