def sum_two_numbers(number_1 : int, number_2: int) -> int:
   return number_1 + number_2

# Call function and store the returned value
result = sum_two_numbers(7, 8)
print(result)

def sum_two_numbersx(number_1 : int=3, number_2: int=2) -> int:
 return number_1 + number_2

result = sum_two_numbersx()
print(result)
