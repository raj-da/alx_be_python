import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    return current_date

# print(display_current_datetime())

def calculate_future_date(number_of_days):
    t_delta = datetime.timedelta(days=number_of_days)
    future_date = datetime.date.today() + t_delta

    return future_date

def main():
    print(f'Current date and time: {display_current_datetime()}')

    number_of_days = int(input('Enter the number of days to add to the current date: '))
    print(f'Future date: {calculate_future_date(number_of_days)}')


if __name__ == '__main__':
    main()