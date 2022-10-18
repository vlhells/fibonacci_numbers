N = int(input("Введите N для генерации чисел Фибоначчи\n"))


def fibonacci_numbers_generator(N):
    prev_previous_f_number = 0
    previous_f_number = 1
    i = 0
    while i < N:
        current_fibonacci_number = prev_previous_f_number + previous_f_number
        yield current_fibonacci_number
        prev_previous_f_number = previous_f_number
        previous_f_number = current_fibonacci_number
        i += 1


for number in fibonacci_numbers_generator(N):
    print(number)
