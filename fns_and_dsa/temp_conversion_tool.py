FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temperature = float(input('Enter the temperature to convert: '))
        temp_type = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').upper()

        match temp_type:
            case 'F':
                print(f'{temperature}°F is {convert_to_celsius(temperature)}°C')
            case 'C':
                print(f'{temperature}°C is {convert_to_fahrenheit(temperature)}°F')
            case _:
                print('Invalid temperature type. Please enter C for Celsius or F for Fahrenheit.')
    except ValueError:
        print('Invalid temperature. Please enter a numeric value.')


if __name__ == "__main__":
    main()
