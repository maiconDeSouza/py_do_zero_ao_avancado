films_set = {"Inception", "The Shawshank Redemption",
             "The Dark Kgnith", "Pulp Fiction", "Interstellar"}

# True e 1 são considerados o mesmo valor
example_set = {"Inception", True, 1, 8.7}
print(example_set)

films_set.update(example_set)
print(films_set)

films_set.remove(8.7)
print(films_set)
