# 1. Crie uma lista contendo apenas os números ímpares de 1 a 100.
list_odd = [n for n in range(1, 101) if n % 2 != 0]
print(list_odd)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41,
# 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81,
# 83, 85, 87, 89, 91, 93, 95, 97, 99]


# 2. Filtre todos os filmes que têm mais de 15 caracteres no título.
films = [
    "The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction",
    "Forrest Gump", "Inception", "Fight Club", "The Matrix", "Goodfellas",
    "The Silence of the Lambs", "Se7en", "The Usual Suspects", "The Lion King",
    "Schindler's List", "Saving Private Ryan", "Gladiator", "Jurassic Park",
    "Back to the Future", "Titanic", "Star Wars: A New Hope"
]
films_15_char = [film for film in films if len(film) > 15]
print(films_15_char)
# ['The Shawshank Redemption', 'The Silence of the Lambs', 'The Usual Suspects',
# "Schindler's List", 'Saving Private Ryan', 'Back to the Future',
# 'Star Wars: A New Hope']

# 3. Crie uma lista contendo apenas as palavras que têm mais de 4 letras em uma frase dada.
phrase = "Crie uma lista contendo apenas as palavras que têm mais de 4 letras em uma frase dada"
more_than_four_letters = [word for word in phrase.split(" ") if len(word) > 4]
print(more_than_four_letters)
# ['lista', 'contendo', 'apenas', 'palavras', 'letras', 'frase']

# 4. Filtre os números que são divisíveis por 3 em uma lista de 1 a 50.
divisible_by_three = [n for n in range(1, 51) if n % 3 == 0]
print(divisible_by_three)
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]

# 5. Dada uma lista de nomes, crie uma nova lista com apenas os nomes que começam
# com a letra "J".
random_names = [
    "Alice", "Zebra", "Brazil", "California", "Tokyo",
    "Mars", "Python", "Lion", "Greece", "New York",
    "Himalayas", "Saturn", "Eagle", "Shakespeare", "Berlin",
    "Amazon", "Venus", "Elephant", "Rome", "Paris",
    "Kangaroo", "Mozart", "Australia", "Chicago", "Jupiter",
    "Picasso", "Whale", "Norway", "Texas", "Mumbai",
    "Dolphin", "Leonardo", "Canada", "Buenos Aires", "Milky Way",
    "Giraffe", "India", "Washington", "Machu Picchu", "Einstein",
    "Tiger", "Portugal", "Los Angeles", "Neptune", "Barcelona",
    "Wolf", "Mona Lisa", "France", "Alaska", "Hawaii",
    "Penguin", "Newton", "Peru", "Mexico City", "Pluto",
    "Orion", "Cheetah", "Einstein", "Florence", "Sydney",
    "Aspen", "Gorilla", "Chile", "Tokyo Tower", "Comet",
    "Galaxy", "Gandhi", "Llama", "Argentina", "Rio de Janeiro",
    "Hercules", "Cairo", "Sphinx", "Kilimanjaro", "Venice",
    "Spacex", "Jaguar", "Nepal", "Toronto", "Arctic",
    "Yosemite", "Da Vinci", "Copenhagen", "Everest", "Amazon Rainforest",
    "Edison", "Bermuda", "Antarctica", "Milan", "Louvre",
    "Atlantis", "Ostrich", "Scotland", "Dubai", "Apollo",
    "Phoenix", "Tesla", "Galapagos", "Buenos Aires", "Vatican City"
]

names_starting_with_j = [
    name for name in random_names if name[0].upper() == "J"]
print(names_starting_with_j)
# ['Jupiter', 'Jaguar']
