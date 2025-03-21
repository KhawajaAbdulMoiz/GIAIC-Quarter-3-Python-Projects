def sum(number):
    digits=str(number)
    total=0 
    for digit in digits:  
        total += int(digit) 
    return total  
number = input("Enter Number For Sum : ")
result = sum(number)
print(f"Sum of digits in {number}: {result}")  