from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date

def calculate_future_date(days, current_date):
    future_date = current_date + timedelta(days=days)
    formatted_date = future_date.strftime("%Y-%m-%d")
    print(formatted_date)

days = int(input("Enter a number of days: "))
now = display_current_datetime()
calculate_future_date(days, now)