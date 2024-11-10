numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

numbers[4] = 5

sum_of_numbers = sum(numbers) - numbers[4]
quantity = len(numbers)
average = sum_of_numbers / quantity

numbers[4] = average
print("Измененный список:", numbers)
