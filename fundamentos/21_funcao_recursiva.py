def fatorial(number):
    if number == 1:
        return 1
    return (number * fatorial(number - 1))


res = fatorial(9)
print(res)
