def welcome():
    return "Seja bem vindo a mundo pythonico!"


res_1 = welcome()
print(res_1)


def calculate_average():
    num_ratings = int(
        input("Digite quantas avaliações deseja inserir para este filme\n"))
    total = 0

    for i in range(1, num_ratings + 1):
        note = float(input(f"Digite a {i}° nota:\n"))
        total += note

    response = f"{(total/num_ratings):.2f}"
    return response


print(calculate_average())
