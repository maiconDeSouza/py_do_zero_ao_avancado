def full_name(first_name, last_name):
    return f"O nome é {first_name} {last_name}"


def sum_number(a, b):
    return f"a soma de {a} + {b} = {a + b}"


def address(country="Brasil"):
    return f"Eu moro {country}"


def rate_movie(movie_name: str, num_ratings: list):
    average = (sum(num_ratings)) / len(num_ratings)
    return f"A média de notas do filme {movie_name} é de {average:.2f}"


print(full_name("Dante", "Parrudo Kiko III"))
print(sum_number(7, 8))
print(address())
print(address("Portugal"))
print(rate_movie("Top Gun", [10, 9.8]))
