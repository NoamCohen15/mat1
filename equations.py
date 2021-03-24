
def exponent(x: float) -> float:
    i = 0
    ateret = 1
    cur_x = 1
    res = 1
    while i < 20:
        i += 1
        cur_x *= x
        ateret *= i
        res += cur_x / ateret

    return res


def abs(x: float) -> float:
    if x < 0:
        return -1
    else:
        return x


def Ln(x: float) -> float:
    if x <= 0:
        return 0
    y_cur = x - 1
    while True:
        y_next = y_cur + 2 * ((x - exponent(y_cur)) / (x + exponent(y_cur)))
        if abs(y_cur - y_next) <= 0.001:
            return y_next
        y_cur = y_next


def XtimesY(x: float, y: float) -> float:
    if x < 0:
        return 0
    return exponent(y * Ln(x))


def sqrt(x: float, y: float) -> float:
    if x == 0:
        return 0
    return XtimesY(y, 1 / x)


def calculate(x: float) -> float:
    return exponent(x) * XtimesY(7, x) * XtimesY(x, -1) * sqrt(x, x)


x = input("what the number to calculate with the formula? ")
x = float(x)
print(calculate(x))




