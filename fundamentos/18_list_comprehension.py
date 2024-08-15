number_list = list(range(1, 51))

number_even = [i for i in number_list if i % 2 == 0]

print(number_even)


films_list = ["Inception", "The Shawshank Redemption",
              "The Dark Kgnith", "Pulp Fiction", "Interstellar"]

films_with_a = [film for film in films_list if "a" in film.lower()]
print(films_with_a)
