def task1():
    path = "text.txt"
    with open(path, "r", encoding="utf_8") as file:
        text = list(file.read().split(" "))
        print(text)
        sequence = input("Enter sequence to search ")
        text = [word for word in text if sequence not in word]
        text = " ".join(text)
        print(text)


def task2():
    from random import randint as rnd
    amount_of_candy = 150
    player = rnd(0, 2)
    win_condition = lambda amount_of_candy: amount_of_candy == 0
    announcement = lambda amount: print("{} candy left in the pile".format(amount))
    while not win_condition(amount_of_candy):
        announcement(amount_of_candy)
        if player == 0:
            player = 1
            amount_of_candy -= human_grab()
            if amount_of_candy < 0:
                amount_of_candy = 0
        else:
            player = 0
            print("CPU took {} candies".format(cpu_grab(amount_of_candy)))
            amount_of_candy -= cpu_grab(amount_of_candy)
    print("No candy left in the pile, {} takes all!".format("Human" if player == 1 else "CPU"))


# Define maximal amount of candy to grab from pile
maximal_grab = 28


def cpu_grab(candy_left):
    calculate = lambda x: (candy_left - 29) % 28
    if candy_left == 150:
        return 9
    elif candy_left <= maximal_grab:
        return candy_left
    elif calculate(candy_left) > 1:
        return calculate(candy_left)
    else:
        return 27


def human_grab():
    grab = int(input("Enter amount of candy to extract, your limit is {} : ".format(maximal_grab)))
    if grab < 0 or grab > maximal_grab:
        print("Invalid amount, try again")
        grab = human_grab()
    return grab


def task3():
    # Wanted to clear console each time field is updated, but it didn't work
    # import os
    # clear_console = lambda: os.system("cls")
    field = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]
    player = 1
    turn_counter = 0
    tie_condition = lambda turn_counter: turn_counter > 8
    win_condition = lambda box: (box[0] == box[1] == box[2] or
                                 box[3] == box[4] == box[5] or
                                 box[6] == box[7] == box[8] or
                                 box[0] == box[4] == box[8] or
                                 box[2] == box[4] == box[6] or
                                 box[0] == box[3] == box[6] or
                                 box[1] == box[4] == box[7] or
                                 box[2] == box[5] == box[8])
    while not tie_condition(turn_counter) and not win_condition(field):
        print(display_field(field))
        print("It's {} turn".format("X" if player == 1 else "O"))
        box = get_box(field)
        field = list(map(lambda item: item.replace(box, "X" if player == 1 else "O"), field))
        if player == 1:
            player = 0
        else:
            player = 1
        turn_counter += 1
        # clear_console()
        # This method of clearing the console doesn't work either:
        # print("\033[H\033[J", end="")
    print(display_field(field))
    print("Game over!{}".format("\nIt's a tie!" if tie_condition(turn_counter) else("")))


def display_field(field):
    string = "\n"
    j = 0
    for i in range(9):
        string += field[i] + "\t"
        if j % 3 == 2 and i != 8:
            string += "\n\n"
            j = -1
        j += 1
    string += "\n"
    return string


def get_box(field):
    box = input("Choose a box ")
    if (box not in [item for row in field for item in row]) or box == "X" or box == "O":
        box = get_box(field)
    return box


def task4():
    string = input("Enter string to compress ")
    path = "zipped.txt"
    with open(path, "w+") as file:
        string = compressor(string)
        file.write(string)
        file.seek(0)
        string = file.read()
        print("Zipped string is {}".format(string))
    path = "unzipped.txt"
    with open(path, "w+") as file:
        string = decompressor(string)
        file.write(string)
        file.seek(0)
        print("Unzipped string is {}".format(file.read()))


def compressor(string):
    string_list = []
    string_list.extend(string)
    compressed = []
    counter = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            counter += 1
        elif i == 1:
            compressed.append(str(counter) + string[0])
        else:
            compressed.append(str(counter) + string[i-1])
            counter = 1
        if i == len(string) - 1:
            compressed.append(str(counter) + string[i])
    return "".join(compressed)


def decompressor(string):
    string_list = []
    string_list.extend(string)
    decompressed = []
    buffer = ""
    for char in string:
        if not char.isdigit():
            decompressed.append(char * int(buffer))
            buffer = ""
        else:
            buffer += char
    return "".join(decompressed)


task_number = input('Choose a task 1..4 or enter anything to quit ')
if task_number == '1':
    task1()
elif task_number == '2':
    task2()
elif task_number == '3':
    task3()
elif task_number == '4':
    task4()
else:
    print('See you')
