from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time, and format it as "YYYY-MM-DD HH:MM:SS"
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_date

def calculate_future_date(number_of_days):
    t_delta = timedelta(days=number_of_days)
    future_date = datetime.today().date() + t_delta
    return future_date

def main():
    print(f'Current date and time: {display_current_datetime()}')

    number_of_days = int(input('Enter the number of days to calculate future date: '))
    print(f'Future date: {calculate_future_date(number_of_days)}')

main()
