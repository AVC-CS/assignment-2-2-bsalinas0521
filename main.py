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

"""
    ########################################
    # Do not delete the return statement
    ########################################
"""

print((f'Fahrenheit:\t{fahrenheit:.2f}'))


if __name__ == '__main__':
    main()
