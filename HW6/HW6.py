# Homework 1 Task 2
def statement_old(x, y, z):
    return not (x or y or z) == (not x) and (not y) and (not z)


def task1_2_old():
    print("x\ty\tz\tf(x,y,z)")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print('{}\t{}\t{}\t{}'.format(x, y, z, statement_old(x, y, z)))


def task1_2():
    print("Truth table for statement ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z, Homework 1 Task 2")
    statement = lambda x, y, z: not (x or y or z) == (not x) and (not y) and (not z)
    print("x\ty\tz\tf(x,y,z)")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print('{}\t{}\t{}\t{}'.format(x, y, z, statement(x, y, z)))


# Homework 1 task 3
def task1_3_old():
    print('Locate coordinate quarter of a point (x,y)')
    x = int(input('Enter x '))
    y = int(input('Enter y '))
    if x != 0 and y != 0:
        if x > 0:
            if y > 0:
                quarter = 1
            else:
                quarter = 4
        else:
            if y > 0:
                quarter = 2
            else:
                quarter = 3
        print('Point ({},{}) is located in {} quarter'.format(x, y, quarter))
    else:
        print('Point ({},{}) is located on an axis'.format(x, y))


def task1_3():
    print('Locate coordinate quarter of a point (x,y), Homework 1 task 3')
    x = int(input('Enter x '))
    y = int(input('Enter y '))
    quarters = [[True, True], [False, True], [False, False], [True, False]]
    location = lambda x, y: [x > 0, y > 0]
    if x != 0 and y != 0:
        for quarter, condition in enumerate(quarters, 1):
            if location(x, y) == condition:
                print('Point ({},{}) is located in {} quarter'.format(x, y, quarter))
    else:
        print('Point ({},{}) is located on an axis'.format(x, y))


# Homework 3 task 5
def fibonacci(k):
    if k < 2:
        return 1
    else:
        return fibonacci(k - 1) + fibonacci(k - 2)


def task3_5_old():
    k = int(input("Input number for creating Negafibonacci sequence "))
    negafibonacci = [0]
    for i in range(0, k):
        negafibonacci.append(fibonacci(i))
        negafibonacci.append(-fibonacci(i))
    negafibonacci.sort()
    print(negafibonacci)


def task3_5():
    print("Negafibonacci, Homework 3 task 5")
    k = int(input("Input number for creating negafibonacci "))
    negafibonacci = [0]
    fibonacci = lambda k: fibonacci(k-1) + fibonacci(k-2) if k > 2 else 1
    for i in range(1, k+1):
        negafibonacci.append(fibonacci(i))
        negafibonacci.insert(0, -fibonacci(i) if i % 2 == 0 else fibonacci(i))
    print(negafibonacci)


task_number = input('Choose a task 1..3 or enter anything to quit ')
if task_number == '1':
    task1_2()
elif task_number == '2':
    task1_3()
elif task_number == '3':
    task3_5()
else:
    print('See you')