# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Get the temperature from the user
        temperature = float(input('Enter the temperature to convert: '))

        # Ask whether the temperature is in Celsius or Fahrenheit
        temp_type = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').upper()

        # Match the input and perform the respective conversion
        match temp_type:
            case 'F':
                print(f'{temperature}°F is {convert_to_celsius(temperature)}°C')
            case 'C':
                print(f'{temperature}°C is {convert_to_fahrenheit(temperature)}°F')
            case _:
                print('Invalid temperature type. Please enter C for Celsius or F for Fahrenheit.')
    except ValueError:
        print('Invalid temperature. Please enter a numeric value.')

# Call the main function
if __name__ == "__main__":
    main()
