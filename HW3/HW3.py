def task1():
    print("Let's get sum of list elements with odd positions!")
    finish_input = False
    list_of_numbers = []
    while not finish_input:
        var = input('Enter a number or nothing to finish list ')
        if var != "":
            list_of_numbers.append(int(var))
        else:
            finish_input = True
    print("Your list of numbers is %s" % list_of_numbers)
    sum_of_odd = 0
    for i in range(1, len(list_of_numbers), 2):
        sum_of_odd += list_of_numbers[i]
    print("Sum of odd elements is %s" % sum_of_odd)


def task2():
    print("Let's make a list of multiplied pairs ([i] * [-1-i]) from list of numbers!")
    string_of_numbers = input("Enter list of numbers divided by spaces ")
    list_of_numbers = string_of_numbers.split()
    list_of_numbers = list(map(int, list_of_numbers))
    print("Your list of numbers is %s" % list_of_numbers)
    list_of_pairs = []
    for i in range(0, len(list_of_numbers)//2):
        list_of_pairs.append(list_of_numbers[i] * list_of_numbers[-1-i])
    if len(list_of_numbers) % 2 != 0:
        list_of_pairs.append(list_of_numbers[len(list_of_numbers)//2]**2)
    print("Your list of pairs is %s" % list_of_pairs)


def task3_2():
    print("Let's find difference between maximal and minimal fractional parts from list of floats!")
    string_of_floats = input("Enter list of float numbers divided by spaces ")
    list_of_floats = string_of_floats.split()
    list_of_floats = list(map(float, list_of_floats))
    print("Your list of floats is %s" % list_of_floats)
    list_of_fractions = [round(abs(x % 1), 8) for x in list_of_floats if x % 1 != 0]
    list_of_fractions.sort()
    print("Your list of fractions is %s" % list_of_fractions)
    print("Answer is %s" % (list_of_fractions[-1]-list_of_fractions[0]))


def task3():
    print("Let's find difference between maximal and minimal fractional parts from list of floats!")
    string_of_floats = input("Enter list of float numbers divided by spaces ")
    list_of_floats = string_of_floats.split()
    list_of_floats = list(map(float, list_of_floats))
    print("Your list of floats is %s" % list_of_floats)
    list_of_floats = list(filter(lambda x: x % 1 != 0, list_of_floats))
    list_of_floats = list(map(lambda x: round(x % 1, 8), list_of_floats))
    list_of_floats.sort()
    print("Your list of fractions is %s" % list_of_floats)
    print("Answer is %s" % (list_of_floats[-1]-list_of_floats[0]))


def task4():
    decimal = int(input("Input decimal number to turn it into binary "))
    list_of_binary = []
    while decimal > 0:
        list_of_binary.insert(0, str(decimal % 2))
        decimal //= 2
    print("".join(list_of_binary))


def fibonacci(k):
    if k < 2:
        return 1
    else:
        return fibonacci(k - 1) + fibonacci(k - 2)


def task5():
    k = int(input("Input number for creating negafibonacci "))
    negafibonacci = [0]
    for i in range(0, k):
        negafibonacci.append(fibonacci(i))
        negafibonacci.append(-fibonacci(i))
    negafibonacci.sort()
    print(negafibonacci)


def task6():
    prime_number_10 = 29
    prime_number_1000 = 7919
    import time
    random = lambda x: (x * prime_number_10) ** 3 % prime_number_1000 / prime_number_1000
    for _ in range(0, 10):
        sec = time.localtime().tm_sec
        time.sleep(1)
        print(random(sec))


task_number = input('Choose a task 1..6 or enter anything to quit ')
if task_number == '1':
    task1()
elif task_number == '2':
    task2()
elif task_number == '3':
    task3()
elif task_number == '4':
    task4()
elif task_number == '5':
    task5()
elif task_number == '6':
    task6()
else:
    print('See you')