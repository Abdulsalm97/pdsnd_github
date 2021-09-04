#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

VALID_CITIES = ['chicago', 'new york city', 'washington']
MONTHS =       ['all','january' , 'february', 'march', 'april', 'may', 'june']
DAYS =         ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
def get_filters():
    while True:
        city = input('Please choose a city from the following cities ( Chicago, New York City, Washington) ').lower()
        print('-'*40)
        

    
        if city not in VALID_CITIES :
            print("Sorry, the selected city must be in (  Chicago, New York City, Washington )")
            print('-'*40)

            continue
        else:

            break
            
    while True:
        month = input('Please choose a month from the following months (All , January , February, March, April, May, June) ').lower()
        print('-'*40)
        

    
        if month not in MONTHS :
            print("Sorry, the selected month must be in (All , January , February, March, April, May, June)")
            print('-'*40)

            continue
        else:

            break
    while True:
        day = input('Please choose a day from the following days (All,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday) ').lower()
        print('-'*40)
        

    
        if day not in DAYS :
            print("Sorry, the selected day must be in (All,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday)")
            print('-'*40)

            continue
        else:

            break
            
    
        print('-'*40)
    return city , month ,day

# city, month , day = get_filters()

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df
# df =load_data(city, month, day)
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    common_month=df['Start Time'].dt.month_name().mode()[0]
    print('Most Popular Start Month:', common_month)
    
    # display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print('Most Popular Start day:', common_day)

    # display the most common start hour
    common_start_hour=df['Start Time'].dt.hour.mode()[0]
    print('Most Popular start hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print('Most Popular start station:', common_start_station)

    # display most commonly used end station

    common_end_station=df['End Station'].mode()[0]
    print('Most Popular end_station:', common_end_station)
    # display most frequent combination of start station and end station trip
    frequent_combination_station = 'From ' + df['Start Station']+ ' To ' + df['End Station']
    frequent_combination_station = frequent_combination_station.mode()[0]
    print('Most Popular frequent_combination_stations:', frequent_combination_station)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['End Time']= pd.to_datetime(df['End Time'])
    df['Start Time']= pd.to_datetime(df['Start Time'])
    total_travel_time = df['End Time'] - df['Start Time']

    # display total travel time

    print('total travel time',  total_travel_time.sum())

    # display mean travel time
    print('mean travel time',  total_travel_time.mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print('\n counts of user types ' , user_types )

    # Display counts of gender
    if 'Gender' in df.columns:

        gender = df.groupby(['Gender'])['Gender'].count()
        print('\n counts of gender ' , gender )
    else :
        print('\nSorry, gender information is not available for this city')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        

        print('earliest year of birth' , min(df['Birth Year'])
         ,'\nrecent year of birth' , max(df['Birth Year'])
         ,'\ncommon year of birth' , df['Birth Year'].mode()[0])
    else :
        print('\nSorry, birth Year is not available for this city')
      

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

    
def Show_df(df):
    Count = 0

    while True :
        Choose = input('\n Do you want to see raw data?  Please Choose between (Yes or No)').lower()
        print('-'*40)
        
        if Choose in ['yes'] :
            
            Count += 5
            print(df.iloc[Count : Count + 5])
        elif Choose in ['no'] :
            break 
        else:
            print('Please enter yes or no to continue')
            
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        Show_df(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:




