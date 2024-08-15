# 1. Dada uma lista de números, crie uma nova lista contendo o cubo de cada número.
list_number = list(range(1, 11))
numbers_cubed = [n ** 3 for n in list_number]
print(numbers_cubed)
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# 2. Transforme uma lista de palavras em uma lista contendo o comprimento de
# cada palavra.
random_names = [
    "Oliver", "Sophia", "Jackson", "Ava", "Liam",
    "Mia", "Noah", "Isabella", "Ethan", "Charlotte"
]

name_size = [{f"{name}": len(name)} for name in random_names]
print(name_size)
# [{'Oliver': 6}, {'Sophia': 6}, {'Jackson': 7}, {'Ava': 3}, {'Liam': 4},
# {'Mia': 3}, {'Noah': 4}, {'Isabella': 8}, {'Ethan': 5}, {'Charlotte': 9}]

# 3. Dada uma lista de preços, aplique um desconto de 10% a cada preço.
products_list = [
    {"product_name": "Cadeira", "price": 150.00},
    {"product_name": "Mesa", "price": 300.00},
    {"product_name": "Lâmpada", "price": 25.00},
    {"product_name": "Computador", "price": 2000.00},
    {"product_name": "Celular", "price": 1200.00},
    {"product_name": "Televisão", "price": 800.00},
    {"product_name": "Geladeira", "price": 2500.00},
    {"product_name": "Fogão", "price": 500.00},
    {"product_name": "Micro-ondas", "price": 300.00},
    {"product_name": "Ventilador", "price": 100.00}
]

discounted_products_list = [
    {**product, "price": product["price"] * 0.90} for product in products_list]
# [{'product_name': 'Cadeira', 'price': 135.0}, {'product_name': 'Mesa', 'price': 270.0},
# {'product_name': 'Lâmpada', 'price': 22.5}, {'product_name': 'Computador', 'price': 1800.0},
# {'product_name': 'Celular', 'price': 1080.0}, {'product_name': 'Televisão', 'price': 720.0},
# {'product_name': 'Geladeira', 'price': 2250.0}, {'product_name': 'Fogão', 'price': 450.0},
# {'product_name': 'Micro-ondas', 'price': 270.0}, {'product_name': 'Ventilador', 'price': 90.0}]

print(discounted_products_list)


# 4. Dada uma lista de números de 1 a 20, crie uma nova lista com cada número multiplicado por 5.
raised_to_five = [n * 5 for n in range(1, 21)]
print(raised_to_five)
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

# 5. Transforme uma lista de nomes próprios em uma lista com os nomes em minúsculas.
names_list = [
    "Alice", "Bob", "Charlie", "Diana", "Ethan",
    "Fiona", "George", "Hannah", "Ian", "Julia",
    "Kevin", "Laura", "Michael", "Nina", "Oscar",
    "Paul", "Quinn", "Rachel", "Steve", "Tina",
    "Ursula", "Victor", "Wendy", "Xander", "Yara",
    "Zane"
]

names_lower = [name.lower() for name in names_list]
print(names_lower)
# ['alice', 'bob', 'charlie', 'diana', 'ethan', 'fiona', 'george', 'hannah',
# 'ian', 'julia', 'kevin', 'laura', 'michael', 'nina', 'oscar', 'paul', 'quinn',
# 'rachel', 'steve', 'tina', 'ursula', 'victor', 'wendy', 'xander', 'yara', 'zane']
