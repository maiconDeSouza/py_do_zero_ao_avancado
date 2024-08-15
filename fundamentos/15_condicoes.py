# name = input("Digite o nome do filme:\n")
# year_release = int(input("Digite o ano do lançamento do filme:\n"))
# rating = float(input("Digite a nota do filme:\n"))

# if rating > 8.0 and year_release > 2015:
#     print(f"O filme {name} é muito bom e é recente. Recomendo assisti-lo.")
# else:
#     print(f"O filme {name} ainda não atingiu uma boa nota e nem é recente.")


num_1 = float(input("Digite o primeiro número:\n"))
num_2 = float(input("Digite o segundo número:\n"))
operation = input("Digite a operação a ser realizada: (+, -, *, /)\n")

if operation == "+":
    result = num_1 + num_2
elif operation == "-":
    result = num_1 - num_2
elif operation == "*":
    result = num_1 * num_2
elif operation == "/":
    result = num_1 / num_2
else:
    result = "Final não encontrado"

print(f"{result:.2}")
