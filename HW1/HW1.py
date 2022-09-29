def task1():
    var = int(input('Is this day a day off? Enter day number '))
    if 0 < var < 6:
        print('Nope, business day')
    elif var == 6 or var == 7:
        print('Yes, day off')
    else:
        print('wut')


# Logical statement for Task2
def statement(x, y, z):
    return not (x or y or z) == (not x) and (not y) and (not z)


def task2():
    print("x\ty\tz\tf(x,y,z)")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print('{}\t{}\t{}\t{}'.format(x, y, z, statement(x, y, z)))


def task3():
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


def task4():
    # No switch-case in Python =(
    quarter = int(input('Limits of x and y coordinates in a quarter. Enter quarter number '))
    if quarter == 1:
        print('In quarter #{} x=(0,+inf), y=(0,+inf)'.format(quarter))
    elif quarter == 2:
        print('In quarter #{} x=(-inf,0), y=(0,+inf)'.format(quarter))
    elif quarter == 3:
        print('In quarter #{} x=(-inf,0), y=(-inf,0)'.format(quarter))
    elif quarter == 4:
        print('In quarter #{} x=(+inf,0), y=(-inf,0)'.format(quarter))
    else:
        print('there is no such thing as quarter #{}'.format(quarter))


def task5():
    print('Distance between two points')
    xA = int(input('Point A. Enter x '))
    yA = int(input('Point A. Enter y '))
    xB = int(input('Point B. Enter x '))
    yB = int(input('Point B. Enter y '))
    distanceAB = ((xB - xA) ** 2 + (yB - yA) ** 2) ** 0.5
    distanceAB = round(distanceAB, 2)
    print('A({},{}) B({},{}) |AB|={}'.format(xA, yA, xB, yB, distanceAB))


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