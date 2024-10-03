def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)

        return f"The result of the division is {num/denom}"
    except ValueError("Error: Please enter numeric values only.") as e:
        return e
    except ZeroDivisionError("Error: Cannot divide by Zero.") as e:
        return e