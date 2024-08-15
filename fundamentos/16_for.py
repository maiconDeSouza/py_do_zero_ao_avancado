# films_list = ["Inception", "The Shawshank Redemption",
#               "The Dark Kgnith", "Pulp Fiction", "Interstellar"]

# for film in films_list:
#     print(film)

number_list = list(range(1, 51))

# for number in number_list:
#     if number != 26:
#         print(number)
#     else:
#         break

for number in number_list:
    if number % 2 != 0:
        continue
    print(number)
