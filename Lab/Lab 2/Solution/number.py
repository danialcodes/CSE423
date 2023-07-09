from helper import midpoint
def draw_numbers(num, x):
    numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
    x = numbers[num](x, 300)
    return x + 20
    
def zero(x, y):
    midpoint(x, y + 20, x, y + 40)  # 1
    midpoint(x + 20, y + 40, x, y + 40)  # 2
    midpoint(x + 20, y + 20, x + 20, y + 40)  # 3
    midpoint(x + 20, y, x + 20, y + 20)  # 4
    midpoint(x, y, x + 20, y)  # 5
    midpoint(x, y, x, y + 20)  # 6
    return x + 15


def one(x, y):
    midpoint(x + 20, y + 20, x + 20, y + 40)  # 3
    midpoint(x + 20, y, x + 20, y + 20)  # 4
    return x + 15


def two(x, y):
    midpoint(x + 20, y + 40, x, y + 40)  # 2
    midpoint(x + 20, y + 20, x + 20, y + 40)  # 3
    midpoint(x, y, x + 20, y)  # 5
    midpoint(x, y, x, y + 20)  # 6
    midpoint(x, y + 20, x + 20, y + 20)  # 7
    return x + 15


def three(x, y):
    midpoint(x + 20, y + 40, x, y + 40)  # 2
    midpoint(x + 20, y + 20, x + 20, y + 40)  # 3
    midpoint(x + 20, y, x + 20, y + 20)  # 4
    midpoint(x, y, x + 20, y)  # 5
    midpoint(x, y + 20, x + 20, y + 20)  # 7
    return x + 15


def four(x, y):
    midpoint(x, y + 20, x, y + 40)  # 1
    midpoint(x + 20, y + 20, x + 20, y + 40)  # 3
    midpoint(x + 20, y, x + 20, y + 20)  # 4
    midpoint(x, y + 20, x + 20, y + 20)  # 7
    return x + 15


def five(x, y):
    midpoint(x, y + 20, x, y + 40)  # 1
    midpoint(x + 20, y + 40, x, y + 40)  # 2
    midpoint(x + 20, y, x + 20, y + 20)  # 4
    midpoint(x, y, x + 20, y)  # 5
    midpoint(x, y + 20, x + 20, y + 20)  # 7
    return x + 15


def six(x, y):
    midpoint(x, y + 20, x, y + 40)  # 1
    midpoint(x + 20, y + 40, x, y + 40)  # 2
    midpoint(x + 20, y, x + 20, y + 20)  # 4
    midpoint(x, y, x + 20, y)  # 5
    midpoint(x, y, x, y + 20)  # 6
    midpoint(x, y + 20, x + 20, y + 20)  # 7
    return x + 15


def seven(x, y):
    midpoint(x + 20, y + 40, x, y + 40)  # 2
    midpoint(x + 20, y + 20, x + 20, y + 40)  # 3
    midpoint(x + 20, y, x + 20, y + 20)  # 4
    return x + 15


def eight(x, y):
    midpoint(x, y + 20, x, y + 40)  # 1
    midpoint(x + 20, y + 40, x, y + 40)  # 2
    midpoint(x + 20, y + 20, x + 20, y + 40)  # 3
    midpoint(x + 20, y, x + 20, y + 20)  # 4
    midpoint(x, y, x + 20, y)  # 5
    midpoint(x, y, x, y + 20)  # 6
    midpoint(x, y + 20, x + 20, y + 20)  # 7
    return x + 15


def nine(x, y):
    midpoint(x, y + 20, x, y + 40)  # 1
    midpoint(x + 20, y + 40, x, y + 40)  # 2
    midpoint(x + 20, y + 20, x + 20, y + 40)  # 3
    midpoint(x + 20, y, x + 20, y + 20)  # 4
    midpoint(x, y, x + 20, y)  # 5
    midpoint(x, y + 20, x + 20, y + 20)  # 7
    return x + 15