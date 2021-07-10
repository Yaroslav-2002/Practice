import re
list=input("Enter a list:")
nums = re.findall(r'\d+', list)
letters = re.sub(r'\d', '', list)
letters_f = ' '.join(part[0].upper() + part[1:-1] + part[-1:].upper() for part in letters.split()) #змінюємо нульовий та -1 символи в кожній частині 
int_nums = [int(item) for item in nums]
to_the_power_of_two = [num**int_nums.index(num) for num in int_nums if num != max(int_nums)]
print(int_nums, letters, letters_f, to_the_power_of_two, int_nums)
print(letters)
print(letters_f)
print(to_the_power_of_two)
print(max(int_nums))
