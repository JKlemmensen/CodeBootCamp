import pandas as pd
import numpy as np


    # Read data from file
df = pd.read_csv('adult.data.csv')


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
races = df['race'].drop_duplicates().to_numpy()
race_count = pd.Series(np.zeros(len(races)),index = races)
#print(races)
for race in races:
    race_count[race] = sum(df['race'] == race)
    x=race_count

#print(race_count)



    # What is the average age of men?
men = (df['sex'] == 'Male')
average_age_men = df['age'][men].mean()
#print(average_age_men)

    # What is the percentage of people who have a Bachelor's degree?
#print((df['education'] == 'Bachelors').sum()/(df['education'] != 'cow').sum())
#percentage_bachelors = None

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
HighEd = ((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))

#print((df['salary'][HighEd] == ">50K").sum()/(df['salary'][HighEd] != None).sum())
#print((df['salary'][~HighEd] == ">50K").sum()/(df['salary'][~HighEd] != None).sum())


higher_education = None
lower_education = None

    # percentage with salary >50K
higher_education_rich = None
lower_education_rich = None

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours = df['hours-per-week'].min()
#print(min_work_hours)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
#num_min_workers = ((df['hours-per-week'] == min_work_hours) & (df['salary'] == ">50K")).sum()/(df['hours-per-week'] == min_work_hours).sum()
#print(num_min_workers)

#rich_percentage = ((df['hours-per-week'] == min_work_hours) & (df['salary'] == ">50K")).sum()/(df['hours-per-week'] == min_work_hours).sum()

    # What country has the highest percentage of people that earn >50K?
countries = df['native-country'].drop_duplicates().to_list()
#print(countries)
CountryEarning = pd.Series(np.zeros(len(countries)), index = countries)

for country in countries:
    CountryEarning[country] = (df['salary'][df['native-country'] == country] == ">50K").sum()/(df['salary'][df['native-country'] == country] != None).sum()


#print(CountryEarning.index[CountryEarning.argmax()], CountryEarning.max())


highest_earning_country = None
highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
Occupations = df['occupation'][df['native-country'] == 'India'].drop_duplicates().to_list()
india_occ_df = pd.Series(index = Occupations)

for occupation in Occupations:
    india_occ_df[occupation] = (df['occupation'][df['native-country'] == 'India'] == occupation).sum()

print(india_occ_df.index[india_occ_df.argmax()], max(india_occ_df))
top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE