def task1():
    d = float(input('Enter accuracy to calculate Pi '))
    n, s1, s2 = 0.0, 0.0, 0.0
    rank = extract_rank(d)
    finish = False
    diff = lambda s1, s2: round(s1 - s2, rank)
    # very convoluted vay to round for anomaly elimination
    pi = lambda s1, s2: (s1 + s2)/2
    pi_cut = lambda s1, s2: (pi(s1, s2) * (10 ** rank) // 1) * 10 ** (-rank)
    pi_rounded = lambda s1, s2: round(pi_cut(s1, s2), rank)
    while not finish:
        n += 1
        s1 = s2 + 4/(2 * n - 1)
        n += 1
        s2 = s1 - 4/(2 * n - 1)
        if diff(s1, s2) <= d:
            finish = True
    # get number of iterations
    # print(round(n/2))
    # get rounded Pi
    print(round(pi(s1, s2), rank))
    # get better rounded Pi
    print(pi_rounded(s1, s2))


def extract_rank(d):
    rank = 0
    while d < 1:
        d *= 10
        rank += 1
    return rank


def task2():
    n = int(input("Enter a number to get list of its' prime denominators "))
    list_of_primes = list(prime_series(n))
    list_of_denominators = [item for item in list_of_primes if n % item == 0]
    print("List of prime numbers 1..N is %s" % list_of_primes)
    print("Your list of prime denominators of N is %s" % list_of_denominators)


def prime_series(n):
    list = []
    is_prime = lambda number: all(number % i != 0 for i in range(2, number))
    for j in range(2, n+1):
        if is_prime(j):
            list.append(j)
    return list


def task3():
    sequence = input(str("Enter sequence of digits to sort out unique figures "))
    list_of_digits = []
    list_of_doubles = []
    for digit in sequence:
        if digit not in list_of_digits:
            list_of_digits.append(digit)
        else:
            list_of_doubles.append(digit)
    list_of_digits = list(filter(lambda digit: digit not in list_of_doubles, list_of_digits))
    print(list_of_digits)


def task4():
    from random import randint as rnd
    rank = int(input("Enter top rank of equation "))
    equation = ""
    for i in range(rank, -1, -1):
        k = rnd(-100, 100)
        if k != 0:
            if i != rank and k > 0:
                equation += "+"
            equation += str(k) + "x^" + str(i) + " "
    equation += "= 0"
    path = "equation_1.txt"
    file = open(path, "w")
    file.write(equation)
    file.close()
    file = open(path, "r")
    print(file.read())
    file.close()


def task5():
    path = "equation_1.txt"
    equation_1 = equation_extractor(path)
    path = "equation_2.txt"
    equation_2 = equation_extractor(path)
    while len(equation_1) != len(equation_2):
        if len(equation_1) > len(equation_2):
            equation_2.append([0, 0])
        else:
            equation_1.append([0, 0])
    sum_of_equations = [equation_1[i][0] + equation_2[i][0] for i in range(max(len(equation_1), len(equation_2)))]
    print(sum_of_equations)
    equation_3 = ""
    for i in range(len(sum_of_equations)-1, -1, -1):
        if sum_of_equations[i] != 0:
            if i != len(sum_of_equations) and sum_of_equations[i] > 0:
                equation_3 += "+"
            equation_3 += str(sum_of_equations[i]) + "x^" + str(i) + " "
    equation_3 += "= 0"
    path = "equation_3.txt"
    file = open(path, "w")
    file.write(equation_3)
    file.close()
    file = open(path, "r")
    print(file.read())
    file.close()


# actually proud of this method
def equation_extractor(path):
    file = open(path, "r")
    equation = file.read()
    file.close()
    equation = list(equation.split())
    equation.reverse()
    # remove "0" and "=" entries
    for _ in range(2):
        del equation[0]
    equation = [list(item.split("x^")) for item in equation]
    equation = [[int(item[0]), int(item[1])] for item in equation]
    # add zero entries for missing polynomial terms
    while equation[len(equation) - 1][1] != len(equation) - 1:
        for i in range(0, len(equation)):
            if equation[i][1] != i:
                equation.insert(i, [0, i])
                break
    return equation


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
else:
    print('See you')