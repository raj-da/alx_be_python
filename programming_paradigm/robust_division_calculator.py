def safe_divide(numerator, denominator):
    pass

def main():
    try:
        numerator = float(input())
        denominator = float(input())
        safe_divide(numerator, denominator)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    main()