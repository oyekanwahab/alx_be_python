import datetime

def display_current_datetime ():
    current_date = datetime.datetime.now()
    return current_date

days = int(input("Enter a number of days: "))

def calculate_future_date (days, current_date):
    future_date = current_date + datetime.timedelta(days)
    formatted_date = future_date.strftime("%Y-%m-%d")

    print(formatted_date)

now = display_current_datetime()

calculate_future_date(days, now)