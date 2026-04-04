def check_Even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter any number of your choice: "))
result = check_Even_odd(num)
print(result)
