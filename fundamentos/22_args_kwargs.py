def sum_number(*num):
    sum_total = sum(num)
    return sum_total


print(sum_number(2, 8, 15, 9))


def presentation(**data):
    return data


print(presentation(name="Python", category="Backend", level="init"))
