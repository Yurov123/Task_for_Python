# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.

yeha = int(input())
print('Сумма цифр =', yeha//100 + (yeha % 100) // 10 + yeha%10)
print('Произведение цифр =', (yeha//100) * ((yeha % 100) // 10) * (yeha%10))