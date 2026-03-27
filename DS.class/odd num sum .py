def sum_odd_digits(n):
   
    if n == 0:
        return 0

    
    last_digit = n % 10

    if last_digit % 2 != 0:
        return last_digit + sum_odd_digits(n // 10)
    else: 
        return sum_odd_digits(n // 10)


num = int(input("Enter a number: "))
result = sum_odd_digits(num)
print("Sum of odd digits:", result)
