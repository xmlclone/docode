def handle_1():
    print(1)

def handle_2():
    print(2)

def handle_3():
    print(3)

def handle_4():
    print(4)

def handel_default():
    print(-1)


switch = {
    1: handle_1,
    2: handle_2,
    3: handle_3,
    4: handle_4
}


def main(case):
    result = switch.get(case, handel_default)()
    return result

if __name__ == '__main__':
    main(9)