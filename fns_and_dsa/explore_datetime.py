from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date

def calculate_future_date(days, current_date):
    future_date = current_date + timedelta(days=days)
    formatted_date = future_date.strftime("%Y-%m-%d %H:%M:%S")  # ✅ Required format
    print(formatted_date)

days = int(input("Enter the number of days to add to the current date:"))
now = display_current_datetime()
calculate_future_date(days, now)
