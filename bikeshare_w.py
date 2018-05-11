import csv
import time
import pandas as pd
import matplotlib.pyplot as plt


#Search for tuples for pd.read csv
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

#List of available answers
cities = ["new york", "chicago", "washington"]
months = ["january", "febuary", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december" ]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

def get_city():
 #user input for cities with arguments
    while True:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     '\nWould you like to see data for Chicago (CH), New York (NY), or Washington (WA)?\n'
                     '\nPlease type: chicago, new york, washington\n').lower()
        #look at answer within cities list if wrong keep asking
        if city in cities:
            print("Great!")
            break
        else:
            print('Invalid Answer!')
    return(city)
def get_month():
    #user input for months with arguments
    while True:
        month = input('\nWhich month? (Ex. january, febuary, march...etc\n').lower()
        #Loop through months answer
        if month in months:
            print("Great! Lets look in the month of {}".format(month))
            break
        else:
            print("Sorry you typed: {}".format(month))
    return(month)
def get_day():
    #have user answer for days with correct argument
    while True:
        day = input('\n Which day?(Ex.monday, tuesday, wednesday....etc\n').lower()
    #loops answer for days in day list
        if day in days:
            print("Wonderful! {} it is".format(day))
            break
        else:
            print("Invalid Inputs!")
    return(day)
# from solutions of Udacity Lessons
def load_data(city, month, day):
    print("loading data filter {}, {}, {}.....please hold!!!".format(city, month, day))
    # load data file into a dataframe "Took from Udacity Website"
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime "Took from Udacity Website"
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, weekday, and hour
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    return df

def overall_stats(df):
    """Displays statistics on most common information"""
    print('\nCalculating Overall Information...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]

    # display the most common day of week
    popular_day_of_week = df['day'].mode()[0]

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]

    # display most commonly used start station amount of time it occures
    most_start_popular = df["Start Station"].value_counts().idxmax()

    # display most commonly used end station
    most_end_popular = df["End Station"].value_counts().idxmax()

    if all([item in df.columns for item in ['Birth Year']]):
        #display earliest
        earliest = df['Birth Year'].min()
        #display recent
        most = df['Birth Year'].max()
        #Display most common
        common = df['Birth Year'].mode()[0]
        print('\nEarliest Year: {}'
              '\nMost Recent: {}'
              '\nMost common: {}'.format(earliest,most, common))
    #print stats
    print('\nMost Popular Month: {}'
          '\nMost Popular Day: {}'
          '\nMost Popular Hour: {}'
          '\nMost Common Start Station: {}'
          '\nMost Common End Station: {}'.format(popular_month, popular_day_of_week, popular_hour, most_start_popular, most_end_popular))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Displays statistical analysis ( Means, std, max, mins, count....etc)
    total_tavel = df["Trip Duration"].describe()
    print('\n Total Statistics:\n',total_tavel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # IF all columns have user and type calculate crosstab of gender and user types
    if all([item in df.columns for item in ['User Type', 'Gender']]):
        subs = pd.crosstab(df['Gender'], df['User Type'], margins= True)
        print(subs)
    else:
        #Calculate most frequently occurring value
        print(df['User Type'].value_counts())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def graphs(df):
    """Displays graphs"""
    print('\nCalculating Graphs...\n')
    start_time = time.time()

    #Input: Create a hbar graph top 5 with title top 5 start stations
    df["Start Station"].value_counts().nlargest(5).plot(y='Start Station', title='top 5 start stations', kind='barh')

    #plot and reveal the graph. Block allows to continue with the program
    plt.show( block= False)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
def user(df):
    #input to see data set
    x = input('Would you like to see data?').lower()
    #set number rows to be shown
    y = 5
    #yes or no input to user to allow data to be shown
    while x =='yes':
        #Looks at data within y value which is given and columns 0-3
        data = df.iloc[0:int(y), 0:4]
        print(data)
        #user input
        z= input('\nWould you like to see more rows?\n').lower()
        #add 5 more rows as long as user says yes.
        if z == 'yes':
            y = y + 5
            data = df.iloc[0:y, 0:4]
            print(data)
        else:
            break

def main():
    while True:
        #Extract data from functions to load data necessary for dataframe
        city = get_city()
        month = get_month()
        day = get_day()
        df = load_data(city,month,day)
        #summarized data statistics for each .csv
        overall_stats(df)
        #interaction with user to allow data set to be shown 5 rows at a time
        user(df)
        #trip statistical anaylsis(std, mean, max, min..etc)
        trip_duration_stats(df)
        #Comparison Crosstab for users type / gender
        user_stats(df)
        #graphs top 5 most freq used stations
        graphs(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
