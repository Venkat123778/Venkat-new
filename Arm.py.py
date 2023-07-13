python code to print armstrong number
def is_armstrong_number(number):
    # Convert the number to a string to get the number of digits
    num_str = str(number)
    num_digits = len(num_str)

    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the sum is equal to the original number
    if armstrong_sum == number:
        return True
    else:
        return False

def print_armstrong_numbers(max_num):
    for num in range(1, max_num + 1):
        if is_armstrong_number(num):
            print(num)
