def main():
    """
          ##################################################
          # Comlete your code here
          Use the same variables: celsius fahrenheit
          ##################################################
    """
    fahrenheit = 0.0
    celsius = float(input("Enter the degrees in celsius."))
    fahrenheit = (celsius*(9/5)) +32   
    print((f'Fahrenheit:\t{fahrenheit:.2f}'))
    return celsius, fahrenheit

if __name__ == '__main__':
    main()
