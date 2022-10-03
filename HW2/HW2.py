def task1():
    var = float(input('Enter float to calculate sum of its digits '))
    if var < 0:
        var *= -1
    result = int(0)
    while var % 1 > 0:
        var *= 10
    var = round(var)
    while var > 0:
        result += var % 10
        var //= 10
    print('Sum of digits in {} is {}'.format(var, result))


def task2_multiplication(n):
    if n < 2:
        return 1
    else:
        return task2_multiplication(n - 1) * n


def task2():
    var = int(input('Enter a number to get list of multiplications of numbers 1..N '))
    list_of_multiplications = []
    for i in range(1, var + 1):
        list_of_multiplications.append(task2_multiplication(i))
    print('Multiplication list of numbers between 1 and N: {}'
          .format(list_of_multiplications))


def task3():
    var = int(input('Enter a number to get sum of n sequence elements (1+1/n)^n '))
    list_of_sequence = []
    sum_of_sequence = 0
    for n in range(1, var + 1):
        list_of_sequence.append((1 + 1 / n) ** n)
        sum_of_sequence += list_of_sequence[n - 1]
    print('List of n elements of sequence (1+1/n)^n: {}'
          .format(list_of_sequence))
    print('Sum of elements is {}'.format(sum_of_sequence))


def task4():
    n = int(input('Enter length of list to get multiplication of elements given in file.txt '))
    list_of_elements = []
    import random
    for i in range(0, n):
        list_of_elements.append(random.randint(-n, n))
    print('Your list is {}'.format(list_of_elements))
    list_of_positions = []
    path = "file.txt"
    data = open(path, "r")
    for line in data:
        list_of_positions.append(int(line))
    data.close()
    print('Positions to multiply are {}'.format(list_of_positions))
    multiplication = 1
    for i in range(0, len(list_of_positions)):
        if 0 < list_of_positions[i] < n:  # We don't want out of range experience for our list
            multiplication *= list_of_elements[list_of_positions[i]]
    print("Answer is %d" % multiplication)  # Wow, I can do it instead of .format()


def task5():
    list_of_elements = []
    path = "file.txt"
    data = open(path, "r")
    for line in data:
        list_of_elements.append(int(line))
    data.close()
    print("We got original list form file.txt, here it is: %s" % list_of_elements)
    import random
    for i in range(0, len(list_of_elements)-1):
        new_position = random.randint(i, len(list_of_elements)-1)
        buffer = list_of_elements[new_position]
        list_of_elements[new_position] = list_of_elements[i]
        list_of_elements[i] = buffer
    print("New arrangement of list is: %s" % list_of_elements)


task_number = input('Choose a task 1..5 or enter anything to quit ')
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
else:
    print('See you')
