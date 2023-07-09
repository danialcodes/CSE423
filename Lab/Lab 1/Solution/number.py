from helper import draw_line

def draw_numbers(num, x):
    numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
    x = numbers[num](x, 250)
    return x + 20



def zero(x, y):
    draw_line(x, y+20, x, y+40)  # 1
    draw_line(x+20, y+40, x, y+40)  # 2
    draw_line(x+20, y+20, x+20, y+40)  # 3
    draw_line(x+20, y, x+20, y+20)  # 4
    draw_line(x, y, x + 20, y)  # 5
    draw_line(x, y, x, y + 20)  # 6
    # draw_line(x, y+20, x+20, y+20)  # 7
    # draw_line(x+10, y, x+10, y+40)  # 8
    return x+10


def one(x, y):
    # draw_line(x, y + 20, x, y + 40)  # 1
    # draw_line(x + 20, y + 40, x, y + 40)  # 2
    draw_line(x + 20, y, x + 20, y + 40)  # 3
    draw_line(x + 20, y, x + 20, y + 20)  # 4
    # draw_line(x, y, x + 20, y)  # 5
    # draw_line(x, y, x, y + 20)  # 6
    # draw_line(x, y + 20, x + 20, y + 20)  # 7
    # draw_line(x + 10, y, x + 10, y + 40)  # 8
    # draw_line(x+10, y+40, x, y+25)  # extra
    return x + 10


def two(x, y):
    # draw_line(x, y + 20, x, y + 40)  # 1
    draw_line(x + 20, y + 40, x, y + 40)  # 2
    draw_line(x + 20, y+20, x + 20, y + 40)  # 3
    # draw_line(x + 20, y, x + 20, y + 20)  # 4
    draw_line(x, y, x + 20, y)  # 5
    draw_line(x, y, x, y + 20)  # 6
    draw_line(x, y+20, x+20, y+20)  # 7
    # draw_line(x+10, y, x+10, y+40)  # 8
    return x + 10


def three(x, y):
    # draw_line(x, y + 20, x, y + 40)  # 1
    draw_line(x + 20, y + 40, x, y + 40)  # 2
    draw_line(x + 20, y + 20, x + 20, y + 40)  # 3
    draw_line(x + 20, y, x + 20, y + 20)  # 4
    draw_line(x, y, x + 20, y)  # 5
    # draw_line(x, y, x, y + 20)  # 6
    draw_line(x, y + 20, x + 20, y + 20)  # 7
    # draw_line(x+10, y, x+10, y+40)  # 8
    return x + 10


def four(x, y):
    draw_line(x, y + 20, x, y + 40)  # 1
    # draw_line(x + 20, y + 40, x, y + 40)  # 2
    draw_line(x + 20, y + 20, x + 20, y + 40)  # 3
    draw_line(x + 20, y, x + 20, y + 20)  # 4
    # draw_line(x, y, x + 20, y)  # 5
    # draw_line(x, y, x, y + 20)  # 6
    draw_line(x, y + 20, x + 20, y + 20)  # 7
    # draw_line(x+10, y, x+10, y+40)  # 8
    # draw_line(x + 10, y + 40, x, y + 20)  # extra
    return x + 10


def five(x, y):
    draw_line(x, y + 20, x, y + 40)  # 1
    draw_line(x + 20, y + 40, x, y + 40)  # 2
    # draw_line(x + 20, y + 20, x + 20, y + 40)  # 3
    draw_line(x + 20, y, x + 20, y + 20)  # 4
    draw_line(x, y, x + 20, y)  # 5
    # draw_line(x, y, x, y + 20)  # 6
    draw_line(x, y + 20, x + 20, y + 20)  # 7
    # draw_line(x+10, y, x+10, y+40)  # 8
    return x + 10


def six(x, y):
    draw_line(x, y + 20, x, y + 40)  # 1
    draw_line(x + 20, y + 40, x, y + 40)  # 2
    # draw_line(x + 20, y + 20, x + 20, y + 40)  # 3
    draw_line(x + 20, y, x + 20, y + 20)  # 4
    draw_line(x, y, x + 20, y)  # 5
    draw_line(x, y, x, y + 20)  # 6
    draw_line(x, y + 20, x + 20, y + 20)  # 7
    # draw_line(x+10, y, x+10, y+40)  # 8
    return x + 10


def seven(x, y):
    # draw_line(x, y + 20, x, y + 40)  # 1
    draw_line(x + 20, y + 40, x, y + 40)  # 2
    draw_line(x + 20, y + 20, x + 20, y + 40)  # 3
    draw_line(x + 20, y, x + 20, y + 20)  # 4
    # draw_line(x, y, x + 20, y)  # 5
    # draw_line(x, y, x, y + 20)  # 6
    # draw_line(x, y + 20, x + 20, y + 20)  # 7
    # draw_line(x + 10, y, x + 10, y + 40)  # 8
    # draw_line(x+20, y + 40, x, y)  # extra
    return x + 10


def eight(x, y):
    draw_line(x, y + 20, x, y + 40)  # 1
    draw_line(x + 20, y + 40, x, y + 40)  # 2
    draw_line(x + 20, y + 20, x + 20, y + 40)  # 3
    draw_line(x + 20, y, x + 20, y + 20)  # 4
    draw_line(x, y, x + 20, y)  # 5
    draw_line(x, y, x, y + 20)  # 6
    draw_line(x, y + 20, x + 20, y + 20)  # 7
    # draw_line(x+10, y, x+10, y+40)  # 8
    return x + 10


def nine(x, y):
    draw_line(x, y + 20, x, y + 40)  # 1
    draw_line(x + 20, y + 40, x, y + 40)  # 2
    draw_line(x + 20, y + 20, x + 20, y + 40)  # 3
    draw_line(x + 20, y, x + 20, y + 20)  # 4
    draw_line(x, y, x + 20, y)  # 5
    # draw_line(x, y, x, y + 20)  # 6
    draw_line(x, y + 20, x + 20, y + 20)  # 7
    # draw_line(x+10, y, x+10, y+40)  # 8
    return x + 10