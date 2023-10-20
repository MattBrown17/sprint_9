'''List of Functions to Help with DataFrame Applications'''

import pandas as pd
import numpy as np

def random_phrase():
    adj = ['large', 'round', 'dirty', 'purple', 'strange']
    noun = ['tree', 'dragon', 'table', 'plane', 'ball']

    return adj[np.random.randint(0, len(adj) - 1)] + ' ' + noun[np.random.randint(0, len(noun) - 1)]

def random_float(min_val, max_val):
    return np.random.uniform(min_val, max_val)

def random_bowling_score():
    return np.random.randint(301)

def silly_tuple():
    return (random_phrase(), round(random_float(1, 5), 1), random_bowling_score())

def silly_tuple_list(num_tuples):
    result = []
    for _ in range(num_tuples):
        result.append(silly_tuple())
    return result


def null_count(df):
    return df.isnull().sum().sum()

def train_test_split(df, frac):
    train = df.sample(frac= frac)
    test = df.drop(train.index).sample(frac= 1.0)
    return train, test

def randomize(df, seed):
    return df.sample(frac= 1.0, random_state= seed)

def addy_split(addy_series):
    df = pd.DataFrame()
    city_list = []
    state_list = []
    zip_list = []
    for addy in addy_series:
        # Find Value in String
        second_half = addy.split('\n')[1]
        city = second_half.split(',')[0]
        state = second_half.split()[-2]
        zip = second_half.split()[-1]
        # Add the Strings to the List
        city_list.append(city)
        state_list.append(state)
        zip_list.append(zip)
    
    # Add the lists to the dataframe
    df['city'] = city_list
    df['state'] = state_list
    df['zip'] = zip_list

    return df

def abbr_2_st(state_series, abbr_2_st=True):
    state_dict = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
    }

    def abbrev_replace(abbrev):
        return state_dict[abbrev]
    
    def state_replace(state_name):
        reverse_state_dict = dict((v, k) for k, v in state_dict.items())
        return reverse_state_dict[state_name]
    
    if abbr_2_st:
        return state_series.apply(abbrev_replace)
    else:
        return state_series.apply(state_replace)

def list_2_series(list_2_series, df):
    new_column = pd.Series(list_2_series)
    return pd.concat([df, new_column], axis= 1)

def rm_outlier(df):
    cleaned_df = pd.DataFrame()

    for (columnName, columnData) in df.iteritems():
        Q1 = columnData.quantile(0.25)
        Q3 = columnData.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5*IQR
        upper_bound = Q3 + 1.5*IQR

        mask = columnData.between(lower_bound, upper_bound, inclusive= 'both')
        cleaned = columnData.loc[mask]

        cleaned_df[columnName] = cleaned

    return cleaned_df

def split_dates(date_series):
    # MM/DD/YYYY
    df = pd.DataFrame()

    month_list = []
    day_list = []
    year_list = []

    for date in date_series:
        month_list.append(date.split('/')[0])
        day_list.append(date.split('/')[1])
        year_list.append(date.split('/')[2])
    
    df['month'] = month_list
    df['day'] = day_list
    df['year'] = year_list

    return df

# if __name__ == '__main__':
#     print(random_phrase())
