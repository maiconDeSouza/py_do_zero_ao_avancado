def sum_py(x, y):
    return x + y


def subtract_py(x, y):
    return x - y


def multiply_py(x, y):
    return x * y


def divide_py(x, y):
    try:
        if y == 0:
            raise ValueError("Valor não pode ser dividido por 0")
        return x / y
    except Exception as e:
        return e
