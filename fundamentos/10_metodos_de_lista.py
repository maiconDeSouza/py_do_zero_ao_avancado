films_list = ["Inception", "The Shawshank Redemption",
              "The Dark Kgnith", "Pulp Fiction", "Interstellar"]


print(len(films_list))
print(films_list.index("Interstellar"))
films_list.append("The Lord of the Rings")
print(films_list)

films_list.sort()
print(films_list)

films_copy = films_list.copy()
films_copy.remove("Pulp Fiction")
print(films_list)
print(films_copy)
films_copy.clear()
print(films_copy)
