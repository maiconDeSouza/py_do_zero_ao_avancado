import os
print("Digite o nome do filme:")
name = input()
year_launch = int(input("Digite o ano de lançamento:\n"))
review = float(input("Digite a nota do filme:\n"))
plan_included_pr = input(
    "está disponível no catalogo? (digite apenas 'sim' ou 'não'\n").lower()
plan_included = None

if plan_included_pr == "sim":
    plan_included = True
elif plan_included_pr == 'não':
    plan_included = False
else:
    plan_included = None

os.system("clear")

print(f"{name} = {type(name)}")
print(f"{year_launch} = {type(year_launch)}")
print(f"{review} = {type(review)}")
print(f"{plan_included} = {type(plan_included)}")
