FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR

    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR

    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
    return fahrenheit

def main():
    try:
        temperature = float(input('Enter the temperature to convert: '))
        type = input('Is this temperature in Celsius or Fahrenheit? (C/F): ')
        match type:
            case 'F' | 'f':
                print(f'{temperature} F is {convert_to_celsius(temperature)} C')
            case 'C' | 'c':
                print(f'{temperature} C is {convert_to_fahrenheit(temperature)} F')
            case _:
                print('Invalid Temprature type.')
    except ValueError:
        print('Invalid temperature. Please enter a numeric value.')


if __name__ == "__main__":
    main()