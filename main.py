a = float(input("Введите первое число (a): "))
b = float(input("Введите второе число (b): "))

sum_result = a + b
subtract_result = a - b
multiply_result = a * b
average_result = (a + b) / 2
difference_abs_result = max(abs(a), abs(b)) - min(abs(a), abs(b))
quotient_result = a / b

print(f"Сумма чисел {a} и {b} = {sum_result}")
print(f"Разность чисел {a} и {b} = {subtract_result}")
print(f"Произведение чисел {a} и {b} = {multiply_result}")
print(f"Среднее арифметическое чисел {a} и {b} = {average_result}")
print(f"Разность максимального и минимального по модулю = {difference_abs_result}")
print(f"Частное чисел: {quotient_result:.2f}")